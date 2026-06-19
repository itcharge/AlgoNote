# [1368. 使网格图至少有一条有效路径的最小代价](https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

- 标签：广度优先搜索、图、数组、矩阵、最短路、堆（优先队列）
- 难度：困难

## 题目链接

- [1368. 使网格图至少有一条有效路径的最小代价 - 力扣](https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

## 题目大意

**描述**：给定一个 $m \times n$ 的网格，每个格子有一个箭头（$1$ 左、$2$ 右、$3$ 上、$4$ 下）。从 $(0,0)$ 出发，沿箭头方向移动不需要代价，修改箭头方向需要 $1$ 代价。

**要求**：返回从左上角到右下角的最小修改次数。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/29/grid1.png)

```python
输入：grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
输出：3
解释：你将从点 (0, 0) 出发。
到达 (3, 3) 的路径为： (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) 花费代价 cost = 1 使方向向下 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 花费代价 cost = 1 使方向向下 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) 花费代价 cost = 1 使方向向下 --> (3, 3)
总花费为 cost = 3.
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/29/grid2.png)

```python
输入：grid = [[1,1,3],[3,2,2],[1,1,4]]
输出：0
解释：不修改任何数字你就可以从 (0, 0) 到达 (2, 2) 。
```


## 解题思路

### 思路 1：0-1 BFS

#### 1. 核心思想

如果沿箭头方向移动，边权为 $0$；否则为 $1$。这是标准的 0-1 BFS（双端队列）：权 $0$ 入队头，权 $1$ 入队尾。

#### 2. 代码

```python
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 1右,2左,3下,4上
        dq = deque([(0, 0, 0)])
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0

        while dq:
            r, c, cost = dq.popleft()
            if r == m - 1 and c == n - 1:
                return cost
            for i, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + (0 if grid[r][c] == i + 1 else 1)
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        if grid[r][c] == i + 1:
                            dq.appendleft((nr, nc, new_cost))
                        else:
                            dq.append((nr, nc, new_cost))
        return dist[m - 1][n - 1]
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(mn)$。
- **空间复杂度**：$O(mn)$。
