# [0489. 扫地机器人](https://leetcode.cn/problems/robot-room-cleaner/)

- 标签：回溯、交互
- 难度：困难

## 题目链接

- [0489. 扫地机器人 - 力扣](https://leetcode.cn/problems/robot-room-cleaner/)

## 题目大意

**描述**：

给定一个房间（二维网格），其中 $0$ 表示空地，$1$ 表示障碍物。有一个扫地机器人，初始位置和朝向未知。

机器人可以通过以下 API 与环境交互：

- `move()`：向前移动一格，如果前方是障碍物或边界则返回 $false$，否则返回 $true$。
- `turnLeft()`：原地左转 90 度。
- `turnRight()`：原地右转 90 度。
- `clean()`：清扫当前格子。

**要求**：

使用机器人清扫所有可达的空地。

**说明**：

- 房间的大小未知。
- 机器人的初始位置和朝向未知。
- 机器人不能穿过障碍物。
- 所有空单元格都可以从起始位置出发访问到。
- $m == room.length$。
- $n == room[i].length$。
- $1 \le m \le 100$。
- $1 \le n \le 200$。
- $room[i][j]$ 为 0 或 1。
- $0 \le row < m$。
- $0 \le col < n$。
- $room[row][col] == 1$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/07/17/lc-grid.jpg)

```python
输入：room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
输出：Robot cleaned all rooms.
解释：
房间内的所有单元格用 0 或 1 填充。
0 表示障碍物，1 表示可以通过。 
机器人从 row=1, col=3 的初始位置出发。
在左上角的一行以下，三列以右。
```

- 示例 2：

```python
输入：room = [[1]], row = 0, col = 0
输出：Robot cleaned all rooms.
```

## 解题思路

### 思路 1：DFS + 回溯

扫地机器人需要清扫所有可达的格子。使用 DFS 遍历所有可达位置。

**核心思路**：

- 机器人只能通过 API 与环境交互，不知道房间的布局。
- 使用 DFS 遍历，记录已访问的位置。
- 关键是在回溯时恢复机器人的方向和位置。

**解题步骤**：

1. 定义四个方向：上、右、下、左（顺时针）。
2. 使用 DFS 遍历：
   - 清扫当前格子。
   - 尝试四个方向，如果可以移动且未访问，递归访问。
   - 回溯：转向相反方向，移动回原位置。
3. 使用集合记录已访问的位置，避免重复访问。

**关键点**：

- 机器人的方向需要维护，使用 `turnRight()` 和 `turnLeft()` 调整方向。
- 回溯时需要让机器人回到原位置和原方向。

### 思路 1：代码

```python
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # 四个方向：上、右、下、左（顺时针）
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        
        def go_back():
            # 回到上一个位置
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(x, y, direction):
            # 清扫当前格子
            robot.clean()
            visited.add((x, y))
            
            # 尝试四个方向
            for i in range(4):
                new_direction = (direction + i) % 4
                dx, dy = directions[new_direction]
                nx, ny = x + dx, y + dy
                
                # 如果未访问且可以移动
                if (nx, ny) not in visited and robot.move():
                    dfs(nx, ny, new_direction)
                    go_back()
                
                # 转向下一个方向
                robot.turnRight()
        
        dfs(0, 0, 0)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n - m)$，其中 $n$ 是房间中的格子总数，$m$ 是障碍物数量。每个可达格子访问一次。
- **空间复杂度**：$O(n - m)$，递归栈和 $visited$ 集合的空间开销。
