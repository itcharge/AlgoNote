# [0994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/)

- 标签：广度优先搜索、数组、矩阵
- 难度：中等

## 题目链接

- [0994. 腐烂的橘子 - 力扣](https://leetcode.cn/problems/rotting-oranges/)

## 题目大意

**描述**：

$m \times n$ 网格 $grid$ 中，每个单元格可以有以下三个值之一：

- 值 0 代表空单元格；
- 值 1 代表新鲜橘子；
- 值 2 代表腐烂的橘子。

每分钟，腐烂的橘子「周围 4 个方向上相邻」的新鲜橘子都会腐烂。

**要求**：

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

**说明**：

- $m == grid.length$。
- $n == grid[i].length$。
- $1 \le m, n \le 10$。
- $grid[i][j]$ 仅为 0、1 或 2。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/oranges.png)

```python
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
```

- 示例 2：

```python
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
```

## 解题思路

### 思路 1：广度优先搜索

这是一个多源 BFS 问题，所有腐烂的橘子同时开始扩散。

1. **初始化**：
   - 遍历矩阵，统计新鲜橘子的数量
   - 将所有腐烂橘子的位置加入队列
2. **BFS 扩展**：
   - 每一轮 BFS 代表一分钟
   - 从队列中取出所有腐烂橘子，向四个方向扩散
   - 如果相邻位置是新鲜橘子，将其变为腐烂，加入队列，新鲜橘子数量减 $1$
3. **判断结果**：
   - 如果最后还有新鲜橘子，返回 $-1$
   - 否则返回经过的分钟数

### 思路 1：代码

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        fresh_count = 0
        
        # 统计新鲜橘子数量，收集腐烂橘子位置
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        # 如果没有新鲜橘子，直接返回 0
        if fresh_count == 0:
            return 0
        
        # BFS 扩散
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # 如果相邻位置是新鲜橘子
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # 变为腐烂
                        fresh_count -= 1
                        queue.append((nx, ny))
            
            # 如果队列不为空，说明这一轮有橘子腐烂
            if queue:
                minutes += 1
        
        # 如果还有新鲜橘子，返回 -1
        return minutes if fresh_count == 0 else -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$，其中 $m$ 和 $n$ 是矩阵的行数和列数，每个格子最多访问一次。
- **空间复杂度**：$O(m \times n)$，队列中最多存储所有格子。
