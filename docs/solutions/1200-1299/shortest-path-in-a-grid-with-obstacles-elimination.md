# [1293. 网格中的最短路径](https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

- 标签：广度优先搜索、数组、矩阵
- 难度：困难

## 题目链接

- [1293. 网格中的最短路径 - 力扣](https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

## 题目大意

**描述**：给定一个 $m \times n$ 的网格 $grid$，其中 $0$ 表示空地，$1$ 表示障碍物。你最多可以消除 $k$ 个障碍物（即将 $1$ 变为 $0$）。

**要求**：返回从左上角 $(0,0)$ 到右下角 $(m-1,n-1)$ 的最短路径长度（步数）。如果无法到达，返回 $-1$。

**说明**：

- $1 \le m, n \le 40$。
- $1 \le k \le m \times n$。

**示例**：

- 示例 1：

```python
输入：grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
输出：6
解释：最短路径长度为 6，需要消除 1 个障碍物。
```

- 示例 2：

```python
输入：grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
输出：-1
```

## 解题思路

### 思路 1：BFS + 三维状态

#### 1. 核心思想

这道题的关键在于状态的定义。普通 BFS 中，每个格子 $(i,j)$ 是一个状态，访问过的格子不再重复访问。但在这个问题中，消除障碍物会改变"可通行性"，所以同一个格子可以通过不同的"剩余消除次数"来再次到达。

因此状态需要引入第三个维度：$(i, j, remaining\_k)$ 表示在位置 $(i,j)$ 时还剩余 $remaining\_k$ 次消除机会。

BFS 逐层扩展，第一次到达 $(m-1, n-1)$ 时的步数就是最短路径。

#### 2. 建图、遍历、标记、收集

- **建图**：网格是图，每个格子 $(i,j)$ 是一个节点，状态扩展为 $(i,j,remaining\_k)$。
- **遍历**：BFS 逐层搜索。
- **标记**：用 $visited[i][j][remaining\_k]$ 标记状态是否访问过。
- **收集**：当第一次到达 $(m-1, n-1)$ 时返回步数。

#### 3. 具体步骤

**第 1 步**：初始化队列，将 $(0, 0, k)$ 入队，$visited[0][0][k] = True$。

**第 2 步**：BFS 循环：
- 从队列取出 $(i, j, rem, steps)$。
- 如果 $(i,j)$ 是终点 $(m-1, n-1)$，返回 $steps$。
- 尝试向四个方向扩展：
  - 如果超出边界，跳过。
  - 如果是障碍物（$grid[ni][nj] == 1$）且 $rem > 0$，可以消除障碍物，新状态 $(ni, nj, rem-1)$。
  - 如果是空地（$grid[ni][nj] == 0$），新状态 $(ni, nj, rem)$。
  - 如果新状态未访问，入队并标记。

**第 3 步**：队列为空返回 $-1$。

#### 4. 结合示例走一遍

$grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k=1$

BFS 过程（简化）：

```
(0,0,k=1,steps=0)
  → (0,1,k=1,1), (1,0,k=1,1)
(0,1,k=1,1)
  → (0,2,k=1,2), (1,1,k=0,2) [消除障碍，k=0]
(1,0,k=1,1)
  → (2,0,k=1,2), (1,1,k=0,2) [已访问]
...
```

沿着路径 $(0,0)→(0,1)→(0,2)→(1,2)→(2,2)→(3,2)→(4,2)→(4,3)$ 会需要清除 2 个障碍，但 $k=1$ 不够。

另一条路径 $(0,0)→(1,0)→(2,0)→(2,1)→(2,2)→(3,2)→(4,2)→(4,3)$ 也在第 1 行有个障碍...

实际上最短路径 $6$ 步会利用 $k=1$ 消除一个障碍。从 $(0,0)→(0,1)→(0,2)→(1,2)→(2,0)→...$ 这是 BFS 的具体细节，这里不展开全部。

### 思路 1：代码

```python
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # 如果 k 足够大，可以直接走曼哈顿距离
        if k >= m + n - 3:
            return m + n - 2

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # visited[i][j][rem] 表示在 (i,j) 剩余 rem 次消除机会时是否访问过
        visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
        q = deque()
        q.append((0, 0, k, 0))
        visited[0][0][k] = True

        while q:
            i, j, rem, steps = q.popleft()

            if i == m - 1 and j == n - 1:
                return steps

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        if rem > 0 and not visited[ni][nj][rem - 1]:
                            visited[ni][nj][rem - 1] = True
                            q.append((ni, nj, rem - 1, steps + 1))
                    else:
                        if not visited[ni][nj][rem]:
                            visited[ni][nj][rem] = True
                            q.append((ni, nj, rem, steps + 1))

        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n \times k)$，每个格子最多有 $k+1$ 种剩余消除状态，总共 $O(mnk)$ 个状态。
- **空间复杂度**：$O(m \times n \times k)$，$visited$ 数组的大小。

$m, n \le 40$，$k \le m \times n = 1600$，最坏 $40 \times 40 \times 1600 = 256$ 万，在可接受范围内。

### 优化小技巧

当 $k \ge m + n - 3$ 时，可以直接返回 $m + n - 2$（曼哈顿距离）。因为即使网格中全是障碍物，足够的消除机会也能让你沿着直线路径走到终点。
