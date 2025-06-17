# [0463. 岛屿的周长](https://leetcode.cn/problems/island-perimeter/)

- 标签：深度优先搜索、广度优先搜索、数组、矩阵
- 难度：简单

## 题目链接

- [0463. 岛屿的周长 - 力扣](https://leetcode.cn/problems/island-perimeter/)

## 题目大意

**描述**：给定一个 `row * col` 大小的二维网格地图 `grid` ，其中：`grid[i][j] = 1` 表示陆地，`grid[i][j] = 0` 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（多个表示陆地的格子相连组成）。

岛屿内部中没有「湖」（指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。

**要求**：计算这个岛屿的周长。

**说明**：

- $row == grid.length$。
- $col == grid[i].length$。
- $1 <= row, col <= 100$。
- $grid[i][j]$ 为 $0$ 或 $1$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/island.png)

```python
输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
输出：16
解释：它的周长是上面图片中的 16 个黄色的边
```

- 示例 2：

```python
输入：grid = [[1]]
输出：4
```

## 解题思路

### 思路 1：广度优先搜索

1. 使用整形变量 `count` 存储周长，使用队列 `queue` 用于进行广度优先搜索。
2. 遍历一遍二维数组 `grid`，对 `grid[row][col] == 1` 的区域进行广度优先搜索。
3. 先将起始点 `(row, col)` 加入队列。
4. 如果队列不为空，则取出队头坐标 `(row, col)`。先将 `(row, col)` 标记为 `2`，避免重复统计。
5. 然后遍历上、下、左、右四个方向的相邻区域，如果遇到边界或者水域，则周长加 1。
6. 如果相邻区域 `grid[new_row][new_col] == 1`，则将其赋值为 `2`，并将坐标加入队列。
7. 继续执行 4 ~ 6 步，直到队列为空时返回 `count`。

### 思路 1：代码

```python
class Solution:
    def bfs(self, grid, rows, cols, row, col):
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = collections.deque([(row, col)])

        count = 0
        while queue:
            row, col = queue.popleft()
            # 避免重复统计
            grid[row][col] = 2
            for direct in directs:
                new_row = row + direct[0]
                new_col = col + direct[1]
                # 遇到边界或者水域，则周长加 1
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid[new_row][new_col] == 0:
                    count += 1
                # 相邻区域为陆地，则将其标记为 2，加入队列
                elif grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col))
                # 相邻区域为 2 的情况不做处理
        return count

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return self.bfs(grid, rows, cols, row, col)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $m$ 和 $n$ 分别为行数和列数。
- **空间复杂度**：$O(n \times m)$。

## 参考资料

- 【题解】[Golang BFS 实现，性能比dfs要高 - 岛屿的周长 - 力扣](https://leetcode.cn/problems/island-perimeter/solution/golang-bfs-shi-xian-xing-neng-bi-dfsyao-nln2g/) 
