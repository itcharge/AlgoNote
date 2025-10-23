# [0332. 重新安排行程](https://leetcode.cn/problems/reconstruct-itinerary/)

- 标签：深度优先搜索、图、欧拉回路
- 难度：困难

## 题目链接

- [0332. 重新安排行程 - 力扣](https://leetcode.cn/problems/reconstruct-itinerary/)

## 题目大意

**描述**：

给定一份航线列表 $tickets$ ，其中 $tickets[i] = [from_i, to_i]$ 表示飞机出发和降落的机场地点。

**要求**：

请你对该行程进行重新规划排序。

所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。

- 例如，行程 `["JFK", "LGA"]` 与 `["JFK", "LGB"]` 相比就更小，排序更靠前。

假定所有机票至少存在一种合理的行程。且所有的机票「必须都用一次」且「只能用一次」。

**说明**：

- $1 \le tickets.length \le 300$。
- $tickets[i].length == 2$。
- $from_i.length == 3$。
- $to_i.length == 3$。
- $from_i$ 和 $to_i$ 由大写英文字母组成。
- $from_i \ne to_i$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg)

```python
输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
输出：["JFK","MUC","LHR","SFO","SJC"]
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg)

```python
输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
```

## 解题思路

### 思路 1：深度优先搜索 + 欧拉回路

这道题本质上是寻找欧拉回路的问题。给定一个有向图，要求找到一条从 JFK 开始的路径，使得每条边都被恰好访问一次。

**1. 问题分析**

- 将每个机场看作图中的节点，每张机票看作图中的有向边。
- 需要找到一条欧拉路径（从 JFK 开始，经过所有边恰好一次）。
- 当存在多条路径时，选择字典序最小的路径。

**2. 算法思路**

使用深度优先搜索（DFS）来构建欧拉路径：

- 构建邻接表 $graph$，其中 $graph[from]$ 存储从 $from$ 出发可以到达的所有机场。
- 对每个机场的邻接列表进行排序，确保优先选择字典序较小的机场。
- 使用 DFS 遍历图，每次选择字典序最小的未访问边。
- 使用栈来记录访问路径，当无法继续前进时，将当前节点加入结果路径。

**3. 关键步骤**

1. 构建邻接表：$graph[from_i] = [to_1, to_2, ..., to_k]$，并按字典序排序。
2. 从 JFK 开始 DFS 遍历。
3. 对于当前节点 $current$，依次访问其邻接节点中字典序最小的未访问节点。
4. 当无法继续前进时，将 $current$ 加入结果路径。
5. 最终将结果路径反转得到正确的行程。

### 思路 1：代码

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 构建邻接表
        graph = {}
        for from_airport, to_airport in tickets:
            if from_airport not in graph:
                graph[from_airport] = []
            graph[from_airport].append(to_airport)
        
        # 对每个机场的邻接列表进行排序，确保字典序最小
        for airport in graph:
            graph[airport].sort()
        
        # 使用栈进行 DFS 遍历
        stack = ["JFK"]  # 从 JFK 开始
        result = []      # 存储最终结果
        
        while stack:
            current = stack[-1]
            # 如果当前机场还有未访问的邻接机场
            if current in graph and graph[current]:
                # 选择字典序最小的邻接机场
                next_airport = graph[current].pop(0)
                stack.append(next_airport)
            else:
                # 当前机场没有未访问的邻接机场，将其加入结果
                result.append(stack.pop())
        
        # 反转结果得到正确的行程顺序
        return result[::-1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(E \log E)$，其中 $E$ 为机票数量。构建邻接表需要 $O(E)$ 时间，对每个机场的邻接列表排序需要 $O(E \log E)$ 时间，DFS 遍历需要 $O(E)$ 时间。
- **空间复杂度**：$O(E)$，用于存储邻接表和递归栈空间。
