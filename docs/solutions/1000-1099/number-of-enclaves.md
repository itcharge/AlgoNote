# [1020. 飞地的数量](https://leetcode.cn/problems/number-of-enclaves/)

- 标签：深度优先搜索、广度优先搜索、并查集、数组、矩阵
- 难度：中等

## 题目链接

- [1020. 飞地的数量 - 力扣](https://leetcode.cn/problems/number-of-enclaves/)

## 题目大意

**描述**：给定一个二维数组 `grid`，每个单元格为 `0`（代表海）或 `1`（代表陆地）。我们可以从一个陆地走到另一个陆地上（朝四个方向之一），然后从边界上的陆地离开网络的边界。

**要求**：返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。

**说明**：

- $m == grid.length$。
- $n == grid[i].length$。
- $1 \le m, n \le 500$。
- $grid[i][j]$ 的值为 $0$ 或 $1$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg)

```python
输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg)

```python
输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。
```

## 解题思路

### 思路 1：深度优先搜索

与四条边界相连的陆地单元是肯定能离开网络边界的。

我们可以先通过深度优先搜索将与四条边界相关的陆地全部变为海（赋值为 `0`）。

然后统计网格中 `1` 的数量，即为答案。

### 思路 1：代码

```python
class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            return
        grid[i][j] = 0

        for direct in self.directs:
            new_i = i + direct[0]
            new_j = j + direct[1]
            self.dfs(grid, new_i, new_j)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            if grid[i][0] == 1:
                self.dfs(grid, i, 0)
            if grid[i][cols - 1] == 1:
                self.dfs(grid, i, cols - 1)

        for j in range(cols):
            if grid[0][j] == 1:
                self.dfs(grid, 0, j)
            if grid[rows - 1][j] == 1:
                self.dfs(grid, rows - 1, j)

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$。其中 $m$ 和 $n$ 分别为行数和列数。
- **空间复杂度**：$O(m \times n)$。