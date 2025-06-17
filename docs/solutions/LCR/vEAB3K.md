# [LCR 106. 判断二分图](https://leetcode.cn/problems/vEAB3K/)

- 标签：深度优先搜索、广度优先搜索、并查集、图
- 难度：中等

## 题目链接

- [LCR 106. 判断二分图 - 力扣](https://leetcode.cn/problems/vEAB3K/)

## 题目大意

给定一个代表 n 个节点的无向图的二维数组 `graph`，其中 `graph[u]` 是一个节点数组，由节点 `u` 的邻接节点组成。对于 `graph[u]` 中的每个 `v`，都存在一条位于节点 `u` 和节点 `v` 之间的无向边。

该无向图具有以下属性：

- 不存在自环（`graph[u]` 不包含 `u`）。
- 不存在平行边（`graph[u]` 不包含重复值）。
- 如果 `v` 在 `graph[u]` 内，那么 `u` 也应该在 `graph[v]` 内（该图是无向图）。
- 这个图可能不是连通图，也就是说两个节点 `u` 和 `v` 之间可能不存在一条连通彼此的路径。

要求：判断该图是否是二分图，如果是二分图，则返回 `True`；否则返回 `False`。

- 二分图：如果能将一个图的节点集合分割成两个独立的子集 `A` 和 `B`，并使图中的每一条边的两个节点一个来自 `A` 集合，一个来自 `B` 集合，就将这个图称为 二分图 。

## 解题思路

对于图中的任意节点 `u` 和 `v`，如果 `u` 和 `v` 之间有一条无向边，那么 `u` 和 `v` 必然属于不同的集合。

我们可以通过在深度优先搜索中对邻接点染色标记的方式，来识别该图是否是二分图。具体做法如下：

- 找到一个没有染色的节点 `u`，将其染成红色。
- 然后遍历该节点直接相连的节点 `v`，如果该节点没有被染色，则将该节点直接相连的节点染成蓝色，表示两个节点不是同一集合。如果该节点已经被染色并且颜色跟 `u` 一样，则说明该图不是二分图，直接返回 `False`。
- 从上面染成蓝色的节点 `v` 出发，遍历该节点直接相连的节点。。。依次类推的递归下去。
- 如果所有节点都顺利染上色，则说明该图为二分图，返回 `True`。否则，如果在途中不能顺利染色，则返回 `False`。

## 代码

```python
class Solution:
    def dfs(self, graph, colors, i, color):
        colors[i] = color
        for j in graph[i]:
            if colors[j] == colors[i]:
                return False
            if colors[j] == 0 and not self.dfs(graph, colors, j, -color):
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        colors = [0 for _ in range(size)]
        for i in range(size):
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1):
                return False
        return True
```

