# [1391. 检查网格中是否存在有效路径](https://leetcode.cn/problems/check-if-there-is-a-valid-path-in-a-grid/)

- 标签：深度优先搜索、广度优先搜索、并查集、数组、矩阵
- 难度：中等

## 题目链接

- [1391. 检查网格中是否存在有效路径 - 力扣](https://leetcode.cn/problems/check-if-there-is-a-valid-path-in-a-grid/)

## 题目大意

**描述**：给定一个 $m \times n$ 的网格 $grid$。每个格子代表一种街道，街道可以连接相邻格子的中心。街道有 $6$ 种类型：
- $1$：左+右
- $2$：上+下
- $3$：左+下
- $4$：右+下
- $5$：左+上
- $6$：右+上

**要求**：判断是否存在一条从 $(0,0)$ 到 $(m-1,n-1)$ 的有效路径（街道相连）。

**说明**：
- $1 \le m, n \le 300$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/e1.png)

```python
输入：grid = [[2,4,3],[6,5,2]]
输出：true
解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/e2.png)

```python
输入：grid = [[1,2,1],[1,2,1]]
输出：false
解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
```


## 解题思路

### 思路 1：DFS/BFS 模拟

#### 1. 核心思想

模拟街道的连接关系。从 $(0,0)$ 出发，每次检查当前街道类型的出口是否与相邻格子的入口匹配。

关键是要为每种街道类型定义"入口"和"出口"方向。可以从四个方向进入格子（上、下、左、右，分别编号 $0,1,2,3$），然后根据街道类型确定可以从哪个方向出来。

#### 2. 建图、遍历、标记、收集

- 建图：每种街道类型定义了入口→出口的映射。
- 遍历：BFS/DFS 从起点出发。
- 标记：visited 数组防止重复。
- 收集：到达终点时返回 True。

#### 3. 具体步骤

**第 1 步**：定义方向：$0$ 左，$1$ 右，$2$ 上，$3$ 下。

**第 2 步**：定义每种街道的"出口方向"：
- 类型 1（左右）：左→右，右→左
- 类型 2（上下）：上→下，下→上
- 类型 3（左下）：左→下，下→左
- 类型 4（右下）：右→下，下→右
- 类型 5（左上）：左→上，上→左
- 类型 6（右上）：右→上，上→右

**第 3 步**：BFS 遍历。对当前格子的每个出口方向，计算相邻格子坐标。检查相邻格子是否能从反方向接收。

### 思路 1：代码

```python
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        # 方向：左0, 右1, 上2, 下3
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # 每种街道类型：从方向d进入后，可以从哪些方向出去
        # pipe[type][d] = [out_dir1, out_dir2]
        pipe = {
            1: [[1], [0], [], []],         # 左右：左↔右
            2: [[], [], [3], [2]],          # 上下：上↔下
            3: [[3], [], [], [0]],          # 左下：左↔下
            4: [[], [3], [], [1]],          # 右下：右↔下
            5: [[2], [], [0], []],          # 左上：左↔上
            6: [[], [2], [1], []]           # 右上：右↔上
        }

        # 从起点开始 BFS，将起点视为从任何方向进入都可以
        q = deque()
        visited = set()
        # 从起点出发，尝试从各个方向进入
        for d in range(4):
            q.append((0, 0, d))
            visited.add((0, 0, d))

        while q:
            r, c, in_dir = q.popleft()
            if r == m - 1 and c == n - 1:
                return True
            street = grid[r][c]
            for out_dir in pipe[street][in_dir]:
                dr, dc = dirs[out_dir]
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # 相邻格子的进入方向与当前出口方向相反
                    in_next = out_dir ^ 1  # 0↔1, 2↔3
                    if (nr, nc, in_next) not in visited:
                        # 检查相邻格子是否能从这个方向进入
                        if pipe[grid[nr][nc]][in_next]:
                            visited.add((nr, nc, in_next))
                            q.append((nr, nc, in_next))
        return False
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(mn)$。
- **空间复杂度**：$O(mn)$。
