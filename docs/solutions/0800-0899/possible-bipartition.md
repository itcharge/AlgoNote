# [0886. 可能的二分法](https://leetcode.cn/problems/possible-bipartition/)

- 标签：深度优先搜索、广度优先搜索、并查集、图
- 难度：中等

## 题目链接

- [0886. 可能的二分法 - 力扣](https://leetcode.cn/problems/possible-bipartition/)

## 题目大意

把 n 个人（编号为 1, 2, ... , n）分为任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。

给定表示不喜欢关系的数组 `dislikes`，其中 `dislikes[i] = [a, b]` 表示 `a` 和 `b` 互相不喜欢，不允许将编号 `a` 和 `b` 的人归入同一组。

要求：如果可以以这种方式将所有人分为两组，则返回 `True`；如果不能则返回 `False`。

## 解题思路

先构建图，对于 `dislikes[i] = [a, b]`，在节点 `a` 和 `b` 之间建立一条无向边，然后判断该图是否为二分图。具体做法如下：

- 找到一个没有染色的节点 `u`，将其染成红色。
- 然后遍历该节点直接相连的节点 `v`，如果该节点没有被染色，则将该节点直接相连的节点染成蓝色，表示两个节点不是同一集合。如果该节点已经被染色并且颜色跟 `u` 一样，则说明该图不是二分图，直接返回 `False`。
- 从上面染成蓝色的节点 `v` 出发，遍历该节点直接相连的节点。。。依次类推的递归下去。
- 如果所有节点都顺利染上色，则说明该图为二分图，可以将所有人分为两组，返回 `True`。否则，如果在途中不能顺利染色，不能将所有人分为两组，则返回 `False`。

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

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        colors = [0 for _ in range(n + 1)]

        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        for i in range(1, n + 1):
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1):
                return False
        return True
```

