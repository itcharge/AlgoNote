# [1041. 困于环中的机器人](https://leetcode.cn/problems/robot-bounded-in-circle/)

- 标签：数学、字符串、模拟
- 难度：中等

## 题目链接

- [1041. 困于环中的机器人 - 力扣](https://leetcode.cn/problems/robot-bounded-in-circle/)

## 题目大意

**描述**：在无限的平面上，机器人最初位于 $(0, 0)$ 处，面朝北方。注意:

- 北方向 是 $y$ 轴的正方向。
- 南方向 是 $y$ 轴的负方向。
- 东方向 是 $x$ 轴的正方向。
- 西方向 是 $x$ 轴的负方向。

机器人可以接受下列三条指令之一：

- `"G"`：直走 $1$ 个单位
- `"L"`：左转 $90$ 度
- `"R"`：右转 $90$ 度

给定一个字符串 $instructions$，机器人按顺序执行指令 $instructions$，并一直重复它们。

**要求**：只有在平面中存在环使得机器人永远无法离开时，返回 $True$。否则，返回 $False$。

**说明**：

- $1 \le instructions.length \le 100$。
- $instructions[i]$ 仅包含 `'G'`，`'L'`，`'R'`。

**示例**：

- 示例 1：

```python
输入：instructions = "GGLLGG"
输出：True
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
“L”:逆时针旋转90度。位置:(0,2).方向:西。
“L”:逆时针旋转90度。位置:(0,2)方向:南。
“G”:移动一步。位置:(0,1)方向:南。
“G”:移动一步。位置:(0,0)方向:南。
重复指令，机器人进入循环:(0,0)——>(0,1)——>(0,2)——>(0,1)——>(0,0)。
在此基础上，我们返回 True。
```

- 示例 2：

```python
输入：instructions = "GG"
输出：False
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
重复这些指示，继续朝北前进，不会进入循环。
在此基础上，返回 False。
```

## 解题思路

### 思路 1：模拟

设定初始位置为 $(0, 0)$，初始方向 $direction = 0$，假设按照给定字符串 $instructions$ 执行一遍之后，位于 $(x, y)$ 处，且方向为 $direction$，则可能出现的所有情况为：

1. 方向不变（$direction == 0$），且 $(x, y) == (0, 0)$，则会一直在原点，无法走出去。
2. 方向不变（$direction == 0$），且 $(x, y) \ne (0, 0)$，则可以走出去。
3. 方向相反（$direction == 2$），无论是否产生位移，则再执行 $1$ 遍将会回到原点。
4. 方向逆时针 / 顺时针改变 $90°$（$direction == 1 \text{ or } 3$），无论是否产生位移，则再执行 $3$ 遍将会回到原点。

综上所述，最多模拟 $4$ 次即可知道能否回到原点。

从上面也可以等出结论：如果不产生位移，则一定会回到原点。如果改变方向，同样一定会回到原点。

我们只需要根据以上结论，按照 $instructions$ 执行一遍之后，通过判断是否产生位移和改变方向，即可判断是否一定会回到原点。

### 思路 1：代码

```Python
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 分别代表北、东、南、西
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y = 0, 0
        # 初始方向为北
        direction = 0
        for step in instructions:
            if step == 'G':
                x += directions[direction][0]
                y += directions[direction][1]
            elif step == 'L':
                direction = (direction + 1) % 4
            else:
                direction = (direction + 3) % 4
        
        return (x == 0 and y == 0) or direction != 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为字符串 $instructions$ 的长度。
- **空间复杂度**：$O(1)$。
