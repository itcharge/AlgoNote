# [1263. 推箱子](https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/)

- 标签：广度优先搜索、图、数组、矩阵、堆（优先队列）
- 难度：困难

## 题目链接

- [1263. 推箱子 - 力扣](https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/)

## 题目大意

**描述**：给定一个 $m \times n$ 的网格 $grid$，其中包含：
- `'#'` 表示墙壁。
- `'.'` 表示空地。
- `'S'` 表示玩家的初始位置。
- `'B'` 表示箱子的初始位置。
- `'T'` 表示目标位置。

玩家可以按上下左右方向移动，但不能穿墙。当玩家走到箱子相邻的位置时，可以向箱子所在方向推箱子（即箱子向同方向移动一格）。箱子不能穿墙，也不能被推到墙里。

**要求**：返回将箱子推到目标位置的最少推动次数。如果无法推到目标位置，返回 $-1$。

**说明**：

- $1 \le m, n \le 20$。
- 网格中有且仅有一个 `'S'`、一个 `'B'`、一个 `'T'`。

**示例**：

- 示例 1：

```python
输入：grid = [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#","#","#","#","#","#"]]
输出：3
```

- 示例 2：

```python
输入：grid = [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#",".",".",".",".","#"],
             ["#","#","#","#","#","#"]]
输出：-1
```

## 解题思路

### 思路 1：BFS + 优先队列

#### 1. 核心思想

推箱子是一个经典的状态搜索问题。关键是要理解"人推箱子"这个过程可以分成两层：

1. **人的移动**：人需要在箱子周围移动，以便走到箱子的四个相邻位置（上、下、左、右），然后朝目标方向推动箱子。
2. **箱子的移动**：只有当人站在箱子某一侧的相邻格子时，才能将箱子推向相反方向。

状态的维度：$(box\_r, box\_c, player\_r, player\_c)$ 表示箱子的位置和玩家的位置。但更高效的是将状态定义为**箱子的位置**，因为箱子的总可能位置是 $m \times n$，而玩家位置可以由箱子位置推导（在推箱子场景中，我们关心的是"人能否走到箱子的某个相邻格子来推箱子"）。

常用的做法是使用 **BFS + 优先队列（Dijkstra 风格）**：
- 每个状态为 $(box\_r, box\_c, pushes)$，表示箱子在 $(box\_r, box\_c)$，已经推动了 $pushes$ 次。
- 对于每个状态，尝试从四个方向推动箱子。推箱子的前提是：玩家能走到箱子被推方向的相反方向的格子，且推后的新位置是空地。
- 对"推的次数"使用优先队列（最小堆），每次取出推动次数最小的状态进行扩展。
- 同时需要记录箱子位置和玩家的可达性：用 BFS 检查玩家能否从当前位置走到箱子的指定相邻位置。

#### 2. 建图、遍历、标记、收集

四步法拆解：

- **建图**：网格本身就是图，空地是可以走的节点，墙是不可走的。
- **遍历**：用 BFS 遍历玩家的可达位置，确定玩家能否从当前位置到达箱子某个方向的相邻格子。
- **标记**：用 $visited[box\_r][box\_c][dir]$ 标记箱子在 $(box\_r, box\_c)$ 时，是否已经处理过从某个方向被推过来的情况（每个方向最多处理一次）。
- **收集**：当箱子位置等于目标位置时，返回推动次数。

#### 3. 具体步骤

**第 1 步**：找到初始位置 $S$、箱子位置 $B$ 和目标位置 $T$。

**第 2 步**：初始化优先队列，将初始状态 $(B\_r, B\_c, pushes=0)$ 入队，同时记录玩家的初始位置。

**第 3 步**：BFS 循环：
- 从优先队列中取出 $(box\_r, box\_c, pushes)$。
- 如果 $(box\_r, box\_c) == T$，返回 $pushes$。
- 尝试四个方向推箱子：
  - 推方向 $d$：新箱子位置 $(nbr, nbc) = (box\_r + dr[d], box\_c + dc[d])$。
  - 玩家的目标位置（推之前人需要站的位置）：$(pr, pc) = (box\_r - dr[d], box\_c - dc[d])$。
  - 检查新箱子位置和玩家目标位置是否都是空地（不是墙且在网格内）。
  - 用 BFS 检查玩家能否从当前位置走到 $(pr, pc)$（注意箱子当前所在格子是障碍物，玩家不能穿过箱子）。
  - 如果能走到，将新状态 $(nbr, nbc, pushes+1)$ 入队（如果该方向未被访问过）。

**第 4 步**：队列为空时，返回 $-1$。

#### 4. 结合示例走一遍

对于示例 1 的网格：

```
# # # # # #
# T . . # #
# . # B . #
# . . . . #
# # # # # #
```

初始位置 $S = (3,1)$，箱子 $B = (2,3)$，目标 $T = (1,1)$。

1. 玩家从 $(3,1)$ 可以走到 $(2,1)$（箱子左侧的下方）吗？检查路径：$(3,1)→(2,1)$ 是空地 → 可以。将箱子从 $(2,3)$ 向左推到 $(2,2)$，$pushes=1$。
2. 玩家现在在 $(2,3)$（推完后的位置），继续... 实际上这个过程需要仔细 BFS 扩展多次。

最终最少推动次数为 $3$。

### 思路 1：代码

```python
from heapq import heappush, heappop
from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右

        # 找到初始位置
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        # BFS 检查玩家能否从 start 走到 end（箱子位置是障碍）
        def can_reach(start, end, box_pos):
            if start == end:
                return True
            q = deque([start])
            visited = set([start])
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != '#':
                        if (nr, nc) == box_pos:
                            continue
                        if (nr, nc) == end:
                            return True
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return False

        # 优先队列：每个元素为 (pushes, box_r, box_c, player_r, player_c)
        heap = [(0, box[0], box[1], player[0], player[1])]
        # visited[box_r][box_c][dir] 标记箱子在某位置时，已被从 dir 方向推过
        visited = [[[False] * 4 for _ in range(n)] for _ in range(m)]

        while heap:
            pushes, br, bc, pr, pc = heappop(heap)

            # 箱子到达目标
            if (br, bc) == target:
                return pushes

            # 尝试四个方向推箱子
            for d, (dr, dc) in enumerate(dirs):
                # 箱子被推向新位置
                nbr, nbc = br + dr, bc + dc
                # 玩家需要站的位置（推之前）
                stand_r, stand_c = br - dr, bc - dc

                # 检查新位置和玩家位置是否合法
                if not (0 <= nbr < m and 0 <= nbc < n and grid[nbr][nbc] != '#'):
                    continue
                if not (0 <= stand_r < m and 0 <= stand_c < n and grid[stand_r][stand_c] != '#'):
                    continue
                if visited[br][bc][d]:
                    continue

                # 检查玩家能否走到箱子对面去推
                if can_reach((pr, pc), (stand_r, stand_c), (br, bc)):
                    visited[br][bc][d] = True
                    heappush(heap, (pushes + 1, nbr, nbc, br, bc))

        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O((m \times n)^2)$，每个箱子位置有 4 个方向需要检查，每次检查需要 BFS 判断玩家可达性（$O(m \times n)$）。
- **空间复杂度**：$O((m \times n)^2)$，需要记录每个箱子位置每个方向是否访问过。

网格大小 $m, n \le 20$，$m \times n \le 400$，$400^2 = 160000$，完全可行。

### 思路 1：要点总结

推箱子问题的核心是处理**人和箱子两个实体的联动**：
- 人要先走到箱子对面的位置（"推的位置"），然后箱子才能移动。
- BFS 判断人的可达性时，要把箱子当前位置视为障碍物。
- 使用优先队列（按推动次数排序）保证每次扩展的是"最少推动次数"的状态。也可以用普通的 BFS（每推动一次算一步），但优先队列更直观地体现了"推动次数"是代价。
