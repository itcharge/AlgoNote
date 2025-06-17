# [LCR 116. 省份数量](https://leetcode.cn/problems/bLyHh0/)

- 标签：深度优先搜索、广度优先搜索、并查集、图
- 难度：中等

## 题目链接

- [LCR 116. 省份数量 - 力扣](https://leetcode.cn/problems/bLyHh0/)

## 题目大意

一个班上有 `n` 个同学，其中一些彼此是朋友，另一些不是。如果 `a` 与 `b` 是直接朋友，且 `b` 与 `c` 也是直接朋友，那么 `a` 与 `c` 是间接朋友。

现在定义「朋友圈」是由一组直接或间接朋友组成的集合。

现在给定一个 `n * n` 的矩阵 `isConnected` 表示班上的朋友关系。其中 `isConnected[i][j] = 1` 表示第 `i` 个同学和第 `j` 个同学是直接朋友，`isConnected[i][j] = 0` 表示第 `i` 个同学和第 `j` 个同学不是直接朋友。

要求：根据给定的同学关系，返回「朋友圈」的数量。

## 解题思路

可以利用并查集来做。具体做法如下：

遍历矩阵 `isConnected`。如果 `isConnected[i][j] = 1`，将 `i` 节点和 `j` 节点相连。然后判断每个同学节点的根节点，然后统计不重复的根节点有多少个，即为「朋友圈」的数量。

## 代码

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        union_find = UnionFind(size)
        for i in range(size):
            for j in range(i + 1, size):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)

        return union_find.count
```

