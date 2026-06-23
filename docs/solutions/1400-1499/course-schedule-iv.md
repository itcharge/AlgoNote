# [1462. 课程表 IV](https://leetcode.cn/problems/course-schedule-iv/)

- 标签：深度优先搜索、广度优先搜索、图、拓扑排序
- 难度：中等

## 题目链接

- [1462. 课程表 IV - 力扣](https://leetcode.cn/problems/course-schedule-iv/)

## 题目大意

**描述**：给定 $n$ 门课程（编号 $0 \sim n-1$）和一个先修关系数组 $prerequisites$，其中 $prerequisites[i] = [a, b]$ 表示学习 $b$ 之前必须先学 $a$（即 $a$ 是 $b$ 的先修课，$a \to b$）。

再给定一个 $queries$ 数组，每个查询 $queries[j] = [u, v]$ 询问 $u$ 是否是 $v$ 的先修课（直接或间接）。

**要求**：返回布尔数组，表示每个查询的结果。

**说明**：
- $2 \le n \le 100$。
- $0 \le prerequisites.length \le n \times (n-1)/2$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg)

```python
输入：numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
输出：[false,true]
解释：[1, 0] 数对表示在你上课程 0 之前必须先上课程 1。
课程 0 不是课程 1 的先修课程，但课程 1 是课程 0 的先修课程。
```

- 示例 2：

```python
输入：numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
输出：[false,false]
解释：没有先修课程对，所以每门课程之间是独立的。
```

## 解题思路

### 思路 1：Floyd 全源可达判断

#### 1. 核心思想

$n \le 100$，用 Floyd-Warshall 算法（三重循环）预处理所有点对之间的可达性。

#### 2. 具体步骤

**第 1 步**：初始化 $reachable[n][n]$，对角线为 $False$，根据 $prerequisites$ 设置直接先修关系。

**第 2 步**：三重循环 Floyd：
$$reachable[i][j] = reachable[i][j] \lor (reachable[i][k] \land reachable[k][j])$$

**第 3 步**：遍历 $queries$，返回 $reachable[u][v]$。

#### 3. 举例说明

以 $n=4, prerequisites=[[0,1],[1,2],[0,3]], queries=[[0,2],[1,3],[2,0]]$ 为例：

直接关系：$0 \to 1, 1 \to 2, 0 \to 3$

Floyd 后得到：$0 \to 1 \to 2$ 传递为 $0 \to 2$。

结果：$[True, False, False]$。

### 思路 1：代码

```python
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Floyd 求传递闭包
        reachable = [[False] * n for _ in range(n)]

        for a, b in prerequisites:
            reachable[a][b] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True

        return [reachable[u][v] for u, v in queries]
```

### 思路 1：复杂度分析

- **时间复杂度**：预处理 Floyd $O(n^3)$，回答查询 $O(1)$ 每个。$n \le 100$，$n^3 = 10^6$ 可行。
- **空间复杂度**：$O(n^2)$。

---

### 思路 2：BFS 每个点

也可以对每个点 BFS 找出所有能到达的节点：

```python
from collections import deque

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for a, b in prerequisites:
            graph[a].append(b)

        # 预处理每个点能到达的所有点
        reachable = [[False] * n for _ in range(n)]

        def bfs(start):
            q = deque([start])
            visited = [False] * n
            visited[start] = True
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        reachable[start][v] = True
                        q.append(v)

        for i in range(n):
            bfs(i)

        return [reachable[u][v] for u, v in queries]
```

BFS 每个点 $O(n \times (n + m))$，$n=100$ 同样可行。
