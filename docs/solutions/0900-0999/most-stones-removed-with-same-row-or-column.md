# [0947. 移除最多的同行或同列石头](https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/)

- 标签：深度优先搜索、并查集、图
- 难度：中等

## 题目链接

- [0947. 移除最多的同行或同列石头 - 力扣](https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/)

## 题目大意

**描述**：二维平面中有 $n$ 块石头，每块石头都在整数坐标点上，且每个坐标点上最多只能有一块石头。如果一块石头的同行或者同列上有其他石头存在，那么就可以移除这块石头。

给你一个长度为 $n$ 的数组 $stones$ ，其中 $stones[i] = [xi, yi]$ 表示第 $i$ 块石头的位置。

**要求**：返回可以移除的石子的最大数量。

**说明**：

- $1 \le stones.length \le 1000$。
- $0 \le xi, yi \le 10^4$。
- 不会有两块石头放在同一个坐标点上。

**示例**：

- 示例 1：

```python
输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
```

- 示例 2：

```python
输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
解释：一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
```

## 解题思路

### 思路 1：并查集

题目「求最多可以移走的石头数目」也可以换一种思路：「求最少留下的石头数目」。

- 如果两个石头 $A$、$B$ 处于同一行或者同一列，我们就可以删除石头 $A$  或 $B$，最少留下 $1$ 个石头。
- 如果三个石头 $A$、$B$、$C$，其中 $A$、$B$ 处于同一行，$B$、$C$ 处于同一列，则我们可以先删除石头 $A$，再删除石头 $C$，最少留下 $1$ 个石头。
- 如果有 $n$ 个石头，其中每个石头都有一个同行或者同列的石头，则我们可以将 $n - 1$ 个石头都删除，最少留下 $1$ 个石头。

通过上面的分析，我们可以利用并查集，将同行、同列的石头都加入到一个集合中。这样「最少可以留下的石头」就是并查集中集合的个数。

则答案为：**最多可以移走的石头数目 = 所有石头个数 - 最少可以留下的石头（并查集的集合个数）**。

因为石子坐标是二维的，在使用并查集的时候要区分横纵坐标，因为 $0 <= xi, yi <= 10^4$，可以取 $n = 10010$，将纵坐标映射到 $[n, n + 10000]$ 的范围内，这样就可以得到所有节点的标号。

最后计算集合个数，可以使用 set 集合去重，然后统计数量。

整体步骤如下：

1. 定义一个 $10010 \times 2$ 大小的并查集。
2. 遍历每块石头的横纵坐标：
   1. 将纵坐标映射到 $[10010, 10010 + 10000]$ 的范围内。
   2. 然后将当前石头的横纵坐标相连接（加入到并查集中）。
3. 建立一个 set 集合，查找每块石头横坐标所在集合对应的并查集编号，将编号加入到 set 集合中。
4. 最后，返回「所有石头个数 - 并查集集合个数」即为答案。

### 思路 1：代码

```python
class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        size = len(stones)
        n = 10010
        union_find = UnionFind(n * 2)
        for i in range(size):
            union_find.union(stones[i][0], stones[i][1] + n)

        stones_set = set()
        for i in range(size):
            stones_set.add(union_find.find(stones[i][0]))

        return size - len(stones_set)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \alpha(n))$。其中 $n$ 是石子个数。$\alpha$ 是反 Ackerman 函数。
- **空间复杂度**：$O(n)$。