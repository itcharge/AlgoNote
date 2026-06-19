# [1129. 颜色交替的最短路径](https://leetcode.cn/problems/shortest-path-with-alternating-colors/)

- 标签：广度优先搜索、图
- 难度：中等

## 题目链接

- [1129. 颜色交替的最短路径 - 力扣](https://leetcode.cn/problems/shortest-path-with-alternating-colors/)

## 题目大意

**描述**：给定一个整数 $n$，表示有向图中的节点数（从 $0$ 到 $n-1$）。图中的边有两种颜色：红色或蓝色，每种颜色的边分别用两个数组给出：
- $redEdges[i] = [a_i, b_i]$：从 $a_i$ 到 $b_i$ 的红色有向边
- $blueEdges[j] = [u_j, v_j]$：从 $u_j$ 到 $v_j$ 的蓝色有向边

**要求**：返回长度为 $n$ 的数组 $answer$，其中 $answer[X]$ 是从节点 $0$ 到节点 $X$ 的 **红蓝交替** 的最短路径长度。如果不存在这样的路径，则 $answer[X] = -1$。

**说明**：

- $1 \le n \le 10^3$。
- $0 \le redEdges.length, blueEdges.length \le 400$。
- 图中可能存在自环和平行边。

**示例**：

- 示例 1：

```python
输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]
```

- 示例 2：

```python
输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]
```

## 解题思路

### 思路 1：广度优先搜索（BFS）

**为什么颜色交替很重要？** 同一个节点可以通过红色边到达，也可以通过蓝色边到达，这两种情况下的下一步选择是不同的。所以我们需要区分这两种状态，分别记录是否访问过。

**拆解步骤**：

1. **建图**：分别构建红色边和蓝色边的邻接表（从每个节点出发能到达哪些节点）。

2. **初始化**：
   - 结果数组 $answer$ 全部初始化为 $-1$，$answer[0] = 0$。
   - BFS 队列初始放入两个起点：$(0, \text{红色})$ 和 $(0, \text{蓝色})$，表示出发时可以选择红色或蓝色作为第一步。
   - 用二维数组 $visited[color][node]$ 记录是否访问过，避免重复。

3. **BFS 循环**：
   - 从队列中取出一个状态 $(node, prev\_color, dist)$
   - 下一步必须走颜色 $next\_color = 1 - prev\_color$
   - 遍历 $next\_color$ 邻接表中从 $node$ 出发的所有边
   - 如果目标节点未以 $next\_color$ 颜色访问过，标记并加入队列
   - 如果 $answer[next\_node]$ 还是 $-1$，更新为 $dist + 1$

4. **返回 $answer$ 数组**。

### 思路 1：代码

```python
from collections import deque, defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 邻接表：graph[0] 红色边，graph[1] 蓝色边
        graph = [defaultdict(list), defaultdict(list)]
        for u, v in redEdges:
            graph[0][u].append(v)
        for u, v in blueEdges:
            graph[1][u].append(v)

        # 结果数组，全部初始化为 -1
        answer = [-1] * n
        answer[0] = 0

        # BFS 队列：(当前节点, 上一条边的颜色, 距离)
        queue = deque([(0, 0, 0), (0, 1, 0)])

        # visited[color][node] 表示通过 color 颜色的边到达 node 是否访问过
        visited = [[False] * n for _ in range(2)]
        visited[0][0] = visited[1][0] = True

        while queue:
            node, prev_color, dist = queue.popleft()

            # 下一步必须走另一种颜色的边
            next_color = 1 - prev_color

            for next_node in graph[next_color][node]:
                if not visited[next_color][next_node]:
                    visited[next_color][next_node] = True
                    queue.append((next_node, next_color, dist + 1))
                    # 第一次到达时记录最短距离
                    if answer[next_node] == -1:
                        answer[next_node] = dist + 1

        return answer
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$。用人话说就是：每个节点最多以红色和蓝色各访问一次，每条边也最多被检查两次，时间和图的规模成正比。
- **空间复杂度**：$O(n + m)$。需要存储两种颜色的邻接表和访问状态。
