# [LCR 111. 除法求值](https://leetcode.cn/problems/vlzXQL/)

- 标签：深度优先搜索、广度优先搜索、并查集、图、数组、最短路
- 难度：中等

## 题目链接

- [LCR 111. 除法求值 - 力扣](https://leetcode.cn/problems/vlzXQL/)

## 题目大意

给定一个变量对数组 `equations` 和一个实数数组 `values` 作为已知条件，其中 `equations[i] = [Ai, Bi]`  和 `values[i]` 共同表示 `Ai / Bi = values[i]`。每个 `Ai` 或 `Bi` 是一个表示单个变量的字符串。

再给定一个表示多个问题的数组 `queries`，其中 `queries[j] = [Cj, Dj]` 表示第 `j` 个问题，要求：根据已知条件找出 `Cj / Dj = ?` 的结果作为答案。返回所有问题的答案。如果某个答案无法确定，则用 `-1.0` 代替，如果问题中出现了给定的已知条件中没有出现的表示变量的字符串，则也用 `-1.0` 代替这个答案。

## 解题思路

在「[等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations)」的基础上增加了倍数关系。在「[等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations)」中我们处理传递关系使用了并查集，这道题也是一样，不过在使用并查集的同时还要维护倍数关系。

举例说明：

- `a / b = 2.0`：说明 `a = 2b`，`a` 和 `b` 在同一个集合。
- `b / c = 3.0`：说明 `b = 3c`，`b`  和 `c`  在同一个集合。

根据上述两式可得：`a`、`b`、`c` 都在一个集合中，且 `a = 2b = 6c`。

我们可以将同一集合中的变量倍数关系都转换为与根节点变量的倍数关系，比如上述例子中都转变为与 `a` 的倍数关系。

具体操作如下：

- 定义并查集结构，并在并查集中定义一个表示倍数关系的 `multiples` 数组。
- 遍历 `equations` 数组、`values` 数组，将每个变量按顺序编号，并使用 `union` 将其并入相同集合。
- 遍历 `queries` 数组，判断两个变量是否在并查集中，并且是否在同一集合。如果找到对应关系，则将计算后的倍数关系存入答案数组，否则则将 `-1` 存入答案数组。
- 最终输出答案数组。

并查集中维护倍数相关方法说明：

- `find` 方法： 
    - 递推寻找根节点，并将倍数累乘，然后进行路径压缩，并且更新当前节点的倍数关系。
- `union` 方法：
    - 如果两个节点属于同一集合，则直接返回。
    - 如果两个节点不属于同一个集合，合并之前当前节点的倍数关系更新，然后再进行更新。
- `is_connect` 方法：
    - 如果两个节点不属于同一集合，返回 `-1`。
    - 如果两个节点属于同一集合，则返回倍数关系。

## 代码

```python
class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.multiples = [1 for _ in range(n)]

    def find(self, x):
        multiple = 1.0
        origin = x
        while x != self.parent[x]:
            multiple *= self.multiples[x]
            x = self.parent[x]
        self.parent[origin] = x
        self.multiples[origin] = multiple
        return x

    def union(self, x, y, multiple):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        self.multiples[root_x] = multiple * self.multiples[y] / self.multiples[x]
        return

    def is_connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            return -1.0

        return self.multiples[x] / self.multiples[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equations_size = len(equations)
        hash_map = dict()
        union_find = UnionFind(2 * equations_size)

        id = 0
        for i in range(equations_size):
            equation = equations[i]
            var1, var2 = equation[0], equation[1]
            if var1 not in hash_map:
                hash_map[var1] = id
                id += 1
            if var2 not in hash_map:
                hash_map[var2] = id
                id += 1
            union_find.union(hash_map[var1], hash_map[var2], values[i])

        queries_size = len(queries)
        res = []
        for i in range(queries_size):
            query = queries[i]
            var1, var2 = query[0], query[1]
            if var1 not in hash_map or var2 not in hash_map:
                res.append(-1.0)
            else:
                id1 = hash_map[var1]
                id2 = hash_map[var2]
                res.append(union_find.is_connected(id1, id2))

        return res
```

