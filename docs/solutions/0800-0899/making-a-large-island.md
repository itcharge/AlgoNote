# [0827. 最大人工岛](https://leetcode.cn/problems/making-a-large-island/)

- 标签：深度优先搜索、广度优先搜索、并查集、数组、矩阵
- 难度：困难

## 题目链接

- [0827. 最大人工岛 - 力扣](https://leetcode.cn/problems/making-a-large-island/)

## 题目大意

**描述**：

给定一个大小为 $n \times n$ 二进制矩阵 $grid$。最多 只能将一格 0 变成 1 。

**要求**：

返回执行此操作后，$grid$ 中最大的岛屿面积是多少？

**说明**：

- 「岛屿」由一组上、下、左、右四个方向相连的 1 形成。
- $n == grid.length$。
- $n == grid[i].length$。
- $1 \le n \le 500$。
- grid[i][j] 为 0 或 1。

**示例**：

- 示例 1：

```python
输入: grid = [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
```

- 示例 2：

```python
输入: grid = [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。
```

## 解题思路

### 思路 1：DFS（深度优先搜索）+ 并查集

这道题要求在最多将一个 $0$ 变成 $1$ 的情况下，计算最大的岛屿面积。

算法步骤：

1. 使用 DFS 标记每个岛屿，并计算每个岛屿的面积。
2. 为每个岛屿分配一个唯一的 ID。
3. 遍历所有的 $0$，尝试将其变成 $1$：
   - 统计该位置四周相邻的不同岛屿。
   - 计算将该 $0$ 变成 $1$ 后的总面积（$1$ + 相邻岛屿面积之和）。
4. 返回最大面积。
5. 特殊情况：如果没有 $0$，返回整个网格的面积。

### 思路 1：代码

```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # 四个方向
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # DFS 标记岛屿并计算面积
        def dfs(i, j, island_id):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            
            grid[i][j] = island_id  # 标记为岛屿 ID
            area = 1
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                area += dfs(ni, nj, island_id)
            
            return area
        
        # 标记所有岛屿并记录面积
        island_id = 2  # 从 2 开始，因为 0 和 1 已被使用
        area_map = {}  # 记录每个岛屿的面积
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, island_id)
                    area_map[island_id] = area
                    island_id += 1
        
        # 如果没有 0，返回整个网格的面积
        max_area = max(area_map.values()) if area_map else 0
        
        # 尝试将每个 0 变成 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # 统计相邻的不同岛屿
                    adjacent_islands = set()
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            adjacent_islands.add(grid[ni][nj])
                    
                    # 计算总面积
                    total_area = 1 + sum(area_map[island] for island in adjacent_islands)
                    max_area = max(max_area, total_area)
        
        return max_area
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是网格的边长。需要遍历网格两次，一次标记岛屿，一次尝试填充 $0$。
- **空间复杂度**：$O(n^2)$，递归调用栈的深度最多为 $O(n^2)$。
