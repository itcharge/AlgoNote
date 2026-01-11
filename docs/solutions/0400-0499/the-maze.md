# [0490. 迷宫](https://leetcode.cn/problems/the-maze/)

- 标签：深度优先搜索、广度优先搜索、数组、矩阵
- 难度：中等

## 题目链接

- [0490. 迷宫 - 力扣](https://leetcode.cn/problems/the-maze/)

## 题目大意

**描述**：

给定一个迷宫（二维数组）$maze$，其中 $0$ 表示空地，$1$ 表示墙壁。球可以向上、下、左、右四个方向滚动，但在碰到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。

给定球的起始位置 $start$ 和目的地 $destination$。

**要求**：

判断球能否在目的地停下。

**说明**：

- $m == maze.length$。
- $n == maze[i].length$。
- $1 \le m, n \le 100$。
- $maze[i][j]$ 是 $0$ 或 $1$。
- $start.length = 2$。
- $destination.length = 2$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/31/maze1-1-grid.jpg)

```python
输入：maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
输出：true
解释：一种可能的路径是 : 左 -> 下 -> 左 -> 下 -> 右 -> 下 -> 右。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/03/31/maze1-2-grid.jpg)

```python
输入：maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
输出：false
解释：不存在能够使球停在目的地的路径。注意，球可以经过目的地，但无法在那里停驻。
```

## 解题思路

### 思路 1：BFS + 模拟

球在迷宫中滚动，遇到墙壁或边界才会停下。需要判断球能否从起点滚到终点。

**核心思路**：

- 球会沿着一个方向一直滚动，直到遇到墙壁或边界。
- 使用 BFS 搜索所有可能的停止位置。
- 每次从一个位置出发，尝试四个方向，滚动到停止位置。

**解题步骤**：

1. 使用 BFS，初始位置为 $start$。
2. 对于每个位置，尝试四个方向（上、下、左、右）。
3. 沿着每个方向一直滚动，直到遇到墙壁或边界，记录停止位置。
4. 如果停止位置是终点，返回 `True`。
5. 如果停止位置未访问过，加入队列继续搜索。
6. 使用 $visited$ 集合避免重复访问。

### 思路 1：代码

```python
from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 右、左、下、上
        
        queue = deque([tuple(start)])
        visited = {tuple(start)}
        
        while queue:
            x, y = queue.popleft()
            
            # 如果到达终点
            if [x, y] == destination:
                return True
            
            # 尝试四个方向
            for dx, dy in directions:
                nx, ny = x, y
                
                # 沿着当前方向一直滚动
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                
                # 如果停止位置未访问过
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n \times \max(m, n))$，其中 $m$ 和 $n$ 是迷宫的行数和列数。每个位置最多访问一次，每次滚动最多需要 $O(\max(m, n))$ 时间。
- **空间复杂度**：$O(m \times n)$，$visited$ 集合和队列的空间开销。
