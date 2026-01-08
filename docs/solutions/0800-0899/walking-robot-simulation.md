# [0874. 模拟行走机器人](https://leetcode.cn/problems/walking-robot-simulation/)

- 标签：数组、哈希表、模拟
- 难度：中等

## 题目链接

- [0874. 模拟行走机器人 - 力扣](https://leetcode.cn/problems/walking-robot-simulation/)

## 题目大意

**描述**：

机器人在一个无限大小的 XY 网格平面上行走，从点 $(0, 0)$ 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 $commands$：

- $-2$：向左转 90 度
- $-1$：向右转 90 度
- $1 \le x \le 9$：向前移动 $x$ 个单位长度

在网格上有一些格子被视为障碍物 $obstacles$。第 $i$ 个障碍物位于网格点 $obstacles[i] = (xi, yi)$。

机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，并继续执行下一个命令。



**要求**：

返回机器人距离原点的「最大欧式距离」的「平方」。（即，如果距离为 5 ，则返回 25 ）

**说明**：

- 注意：
   - 北方表示 +Y 方向。
   - 东方表示 +X 方向。
   - 南方表示 -Y 方向。
   - 西方表示 -X 方向。
   - 原点 $[0,0]$ 可能会有障碍物。
- $1 \le commands.length \le 10^{4}$。
- $commands[i]$ 的值可以取 -2、-1 或者是范围 $[1, 9]$ 内的一个整数。
- $0 \le obstacles.length \le 10^{4}$。
- $-3 \times 10^{4} \le xi, yi \le 3 \times 10^{4}$。
- 答案保证小于 $2^{31}$。

**示例**：

- 示例 1：

```python
输入：commands = [4,-1,3], obstacles = []
输出：25
解释：
机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 3 个单位，到达 (3, 4)
距离原点最远的是 (3, 4) ，距离为 32 + 42 = 25
```

- 示例 2：

```python
输入：commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出：65
解释：机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4)
4. 左转
5. 向北走 4 个单位，到达 (1, 8)
距离原点最远的是 (1, 8) ，距离为 12 + 82 = 65
```

## 解题思路

### 思路 1:模拟 + 哈希表

模拟机器人的行走过程:

1. 用方向数组表示四个方向:北(0, 1)、东(1, 0)、南(0, -1)、西(-1, 0)。
2. 用变量 $direction$ 表示当前方向的索引。
3. 将障碍物坐标存入哈希集合,方便快速查询。
4. 遍历命令:
   - 如果是 -2(左转),方向索引减 1
   - 如果是 -1(右转),方向索引加 1
   - 如果是移动命令,逐步移动,每次移动一格并检查是否有障碍物
5. 记录过程中距离原点的最大欧式距离的平方。

### 思路 1:代码

```python
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 方向数组:北、东、南、西
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0  # 初始方向为北
        
        # 将障碍物转换为集合,方便查询
        obstacle_set = set(map(tuple, obstacles))
        
        x, y = 0, 0  # 初始位置
        max_dist = 0  # 最大距离的平方
        
        for cmd in commands:
            if cmd == -2:
                # 左转
                direction = (direction - 1) % 4
            elif cmd == -1:
                # 右转
                direction = (direction + 1) % 4
            else:
                # 前进 cmd 步
                dx, dy = directions[direction]
                for _ in range(cmd):
                    # 尝试移动一步
                    next_x, next_y = x + dx, y + dy
                    # 检查是否有障碍物
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        # 更新最大距离
                        max_dist = max(max_dist, x * x + y * y)
                    else:
                        # 遇到障碍物,停止移动
                        break
        
        return max_dist
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(N + K)$,其中 $N$ 是命令数组的长度,$K$ 是所有移动命令的步数之和。将障碍物加入集合需要 $O(M)$,其中 $M$ 是障碍物数量。
- **空间复杂度**:$O(M)$,需要存储障碍物的哈希集合。
