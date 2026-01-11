# [0499. 迷宫 III](https://leetcode.cn/problems/the-maze-iii/)

- 标签：深度优先搜索、广度优先搜索、图、数组、字符串、矩阵、最短路、堆（优先队列）
- 难度：困难

## 题目链接

- [0499. 迷宫 III - 力扣](https://leetcode.cn/problems/the-maze-iii/)

## 题目大意

**描述**：

给定一个迷宫（二维数组）$maze$，其中 $0$ 表示空地，$1$ 表示墙壁。球可以向上、下、左、右四个方向滚动，但在碰到墙壁或洞前不会停止滚动。当球停下时，可以选择下一个方向。

迷宫中有一个洞 $hole$，球一旦滚到洞的位置就会掉进洞里。

给定球的起始位置 $ball$ 和洞的位置 $hole$。

**要求**：

返回球到达洞的最短路径的「字典序最小」的指令序列。指令用 `'u'`（上）、`'d'`（下）、`'l'`（左）、`'r'`（右）表示。如果球无法到达洞，返回 `"impossible"`。

**说明**：

- $m == maze.length$。
- $n == maze[i].length$。
- $1 \le m, n \le 100$。
- $maze[i][j]$ 是 $0$ 或 $1$。
- $ball.length = 2$。
- $hole.length = 2$。

**示例**：

- 示例 1：

```python
输入 1: 迷宫由以下二维数组表示

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

输入 2: 球的初始位置 (rowBall, colBall) = (4, 3)
输入 3: 洞的位置 (rowHole, colHole) = (0, 1)

输出: "lul"

解析: 有两条让球进洞的最短路径。
第一条路径是 左 -> 上 -> 左, 记为 "lul".
第二条路径是 上 -> 左, 记为 'ul'.
两条路径都具有最短距离6, 但'l' < 'u'，故第一条路径字典序更小。因此输出"lul"。
```

![](https://assets.leetcode.com/uploads/2018/10/13/maze_2_example_1.png)

- 示例 2：

```python
输入 1: 迷宫由以下二维数组表示

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

输入 2: 球的初始位置 (rowBall, colBall) = (4, 3)
输入 3: 洞的位置 (rowHole, colHole) = (3, 0)

输出: "impossible"

示例: 球无法到达洞。
```

![](https://assets.leetcode.com/uploads/2018/10/13/maze_2_example_2.png)

## 解题思路

### 思路 1：Dijkstra + 优先队列

这是迷宫问题的升级版，不仅要找到终点，还要找到字典序最小的路径。

**核心思路**：

- 球会沿着一个方向一直滚动，直到遇到墙壁、边界或洞。
- 使用 Dijkstra 算法找最短路径，同时记录路径字符串。
- 优先队列按照 (距离, 路径字符串) 排序，保证找到字典序最小的最短路径。

**解题步骤**：

1. 使用优先队列，存储 (距离, 路径, x, y)。
2. 四个方向分别对应字符 `'d'`（下）、`'l'`（左）、`'r'`（右）、`'u'`（上）。
3. 对于每个位置，尝试四个方向滚动：
   - 如果遇到洞，记录距离和路径。
   - 否则滚动到停止位置，更新距离和路径。
4. 使用字典记录每个位置的最短距离和路径，避免重复访问。
5. 返回到达洞的最短路径，如果无法到达返回 `"impossible"`。

### 思路 1：代码

```python
import heapq

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        # 方向：下、左、右、上（字典序）
        directions = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
        
        # 优先队列：(距离, 路径, x, y)
        heap = [(0, '', ball[0], ball[1])]
        # 记录每个位置的最短距离和路径
        visited = {(ball[0], ball[1]): (0, '')}
        
        while heap:
            dist, path, x, y = heapq.heappop(heap)
            
            # 如果到达洞
            if [x, y] == hole:
                return path
            
            # 如果当前状态不是最优，跳过
            if (x, y) in visited and (dist, path) > visited[(x, y)]:
                continue
            
            # 尝试四个方向
            for dx, dy, direction in directions:
                nx, ny = x, y
                steps = 0
                
                # 沿着当前方向滚动
                while (0 <= nx + dx < m and 0 <= ny + dy < n and 
                       maze[nx + dx][ny + dy] == 0):
                    nx += dx
                    ny += dy
                    steps += 1
                    
                    # 如果遇到洞，停止
                    if [nx, ny] == hole:
                        break
                
                new_dist = dist + steps
                new_path = path + direction
                
                # 如果找到更短的路径或字典序更小的路径
                if ((nx, ny) not in visited or 
                    (new_dist, new_path) < visited[(nx, ny)]):
                    visited[(nx, ny)] = (new_dist, new_path)
                    heapq.heappush(heap, (new_dist, new_path, nx, ny))
        
        return "impossible"
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n \times \max(m, n) \times \log(m \times n))$，每个位置最多访问一次，每次滚动需要 $O(\max(m, n))$，堆操作需要 $O(\log(m \times n))$。
- **空间复杂度**：$O(m \times n)$，存储访问状态和优先队列。
