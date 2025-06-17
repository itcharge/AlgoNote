# [0990. 等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/)

- 标签：并查集、图、数组、字符串
- 难度：中等

## 题目链接

- [0990. 等式方程的可满足性 - 力扣](https://leetcode.cn/problems/satisfiability-of-equality-equations/)

## 题目大意

**描述**：给定一个由字符串方程组成的数组 `equations`，每个字符串方程 `equations[i]` 的长度为 `4`，有以下两种形式组成：`a==b` 或 `a!=b`。`a` 和 `b` 是小写字母，表示单字母变量名。

**要求**：判断所有的字符串方程是否能同时满足，如果能同时满足，返回 `True`，否则返回 `False`。

**说明**：

- $1 \le equations.length \le 500$。
- $equations[i].length == 4$。
- $equations[i][0]$ 和 $equations[i][3]$ 是小写字母。
- $equations[i][1]$ 要么是 `'='`，要么是 `'!'`。
- `equations[i][2]` 是 `'='`。

**示例**：

- 示例 1：

```python
输入：["a==b","b!=a"]
输出：False
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
```

## 解题思路

### 思路 1：并查集

字符串方程只有 `==` 或者 `!=`，可以考虑将相等的遍历划分到相同集合中，然后再遍历所有不等式方程，看方程的两个变量是否在之前划分的相同集合中，如果在则说明不满足。

这就需要用到并查集，具体操作如下：

- 遍历所有等式方程，将等式两边的单字母变量顶点进行合并。
- 遍历所有不等式方程，检查不等式两边的单字母遍历是不是在一个连通分量中，如果在则返回 `False`，否则继续扫描。如果所有不等式检查都没有矛盾，则返回 `True`。

### 思路 1：并查集代码

```python
class UnionFind:
    def __init__(self, n):                          # 初始化
        self.fa = [i for i in range(n)]             # 每个元素的集合编号初始化为数组 fa 的下标索引
    
    def __find(self, x):                            # 查找元素根节点的集合编号内部实现方法
        while self.fa[x] != x:                      # 递归查找元素的父节点，直到根节点
            self.fa[x] = self.fa[self.fa[x]]        # 隔代压缩优化
            x = self.fa[x]
        return x                                    # 返回元素根节点的集合编号

    def union(self, x, y):                          # 合并操作：令其中一个集合的树根节点指向另一个集合的树根节点
        root_x = self.__find(x)
        root_y = self.__find(y)
        if root_x == root_y:                        # x 和 y 的根节点集合编号相同，说明 x 和 y 已经同属于一个集合
            return False
        
        self.fa[root_x] = root_y                    # x 的根节点连接到 y 的根节点上，成为 y 的根节点的子节点
        return True

    def is_connected(self, x, y):                   # 查询操作：判断 x 和 y 是否同属于一个集合
        return self.__find(x) == self.__find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_find = UnionFind(26)
        for eqation in equations:
            if eqation[1] == "=":
                index1 = ord(eqation[0]) - 97
                index2 = ord(eqation[3]) - 97
                union_find.union(index1, index2)

        for eqation in equations:
            if eqation[1] == "!":
                index1 = ord(eqation[0]) - 97
                index2 = ord(eqation[3]) - 97
                if union_find.is_connected(index1, index2):
                    return False
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + C \times \log C)$。其中 $n$ 是方程组 $equations$ 中的等式数量。$C$ 是字母变量的数量。本题中变量都是小写字母，即 $C \le 26$。
- **空间复杂度**：$O(C)$。