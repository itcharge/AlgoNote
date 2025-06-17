# [0797. 所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)

- 标签：深度优先搜索、广度优先搜索、图、回溯
- 难度：中等

## 题目链接

- [0797. 所有可能的路径 - 力扣](https://leetcode.cn/problems/all-paths-from-source-to-target/)

## 题目大意

给定一个有 `n` 个节点的有向无环图（DAG），用二维数组 `graph` 表示。

要求：找出所有从节点 `0` 到节点 `n - 1` 的路径并输出（不要求按特定顺序）。

二维数组 `graph` 的第 `i` 个数组 `graph[i]` 中的单元都表示有向图中 `i` 号节点所能到达的下一个节点，如果为空就是没有下一个结点了。

## 解题思路

从第 `0` 个节点开始进行深度优先搜索遍历。在遍历的同时，通过回溯来寻找所有路径。具体做法如下：

- 使用 `ans` 数组存放所有答案路径，使用 `path` 数组记录当前路径。
- 从第 `0` 个节点开始进行深度优先搜索遍历。
  - 如果当前开始节点 `start` 等于目标节点 `target`。则将当前路径 `path` 添加到答案数组 `ans` 中，并返回。
  - 然后遍历当前节点 `start` 所能达到的下一个节点。
    - 将下一个节点加入到当前路径中。
    - 从该节点出发进行深度优先搜索遍历。
    - 然后将下一个节点从当前路径中移出，进行回退操作。
- 最后返回答案数组 `ans`。

## 代码

```python
class Solution:
    def dfs(self, graph, start, target, path, ans):
        if start == target:
            ans.append(path[:])
            return
        for end in graph[start]:
            path.append(end)
            self.dfs(graph, end, target, path, ans)
            path.remove(end)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        ans = []
        self.dfs(graph, 0, len(graph) - 1, path, ans)
        return ans
```

