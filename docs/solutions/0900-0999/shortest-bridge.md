# [0934. 最短的桥](https://leetcode.cn/problems/shortest-bridge/)

- 标签：深度优先搜索、广度优先搜索、数组、矩阵
- 难度：中等

## 题目链接

- [0934. 最短的桥 - 力扣](https://leetcode.cn/problems/shortest-bridge/)

## 题目大意

**描述**：

给定一个大小为 $n \times n$ 的二元矩阵 $grid$，其中 1 表示陆地，0 表示水域。

「岛」是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。$grid$ 中 恰好存在两座岛 。

你可以将任意数量的 0 变为 1，以使两座岛连接起来，变成「一座岛」。

**要求**：

返回必须翻转的 0 的最小数目。

**说明**：

- $n == grid.length == grid[i].length$。
- $2 \le n \le 10^{3}$。
- $grid[i][j]$ 为 0 或 1。
- $grid$ 中恰有两个岛。

**示例**：

- 示例 1：

```python
输入：grid = [[0,1],[1,0]]
输出：1
```

- 示例 2：

```python
输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
输出：2
```

## 解题思路

### 思路 1：广度优先搜索

这道题需要找到连接两个岛屿的最短桥，可以分为两步：

1. **找到第一个岛屿**：使用 DFS 找到第一个岛屿的所有格子，并将它们加入队列。
2. **BFS 扩展**：从第一个岛屿的所有格子开始，使用 BFS 向外扩展，直到遇到第二个岛屿。

**具体步骤**：

- 遍历矩阵，找到第一个值为 $1$ 的格子，从这里开始 DFS
- DFS 标记第一个岛屿的所有格子（改为 $2$），并将它们加入队列
- BFS 从队列中的所有格子开始扩展，每次将水域（$0$）改为 $2$，直到遇到第二个岛屿（$1$）

### 思路 1：代码

```python
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # DFS 找到第一个岛屿
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2  # 标记为第一个岛屿
            queue.append((i, j))
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        # 找到第一个岛屿并标记
        queue = collections.deque()
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        
        # BFS 扩展，寻找第二个岛屿
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:  # 找到第二个岛屿
                            return steps
                        elif grid[nx][ny] == 0:  # 水域，继续扩展
                            grid[nx][ny] = 2
                            queue.append((nx, ny))
            steps += 1
        
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是矩阵的边长。DFS 和 BFS 都最多访问每个格子一次。
- **空间复杂度**：$O(n^2)$，队列和递归栈的空间。
