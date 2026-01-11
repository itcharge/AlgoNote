# [0469. 凸多边形](https://leetcode.cn/problems/convex-polygon/)

- 标签：几何、数组、数学
- 难度：中等

## 题目链接

- [0469. 凸多边形 - 力扣](https://leetcode.cn/problems/convex-polygon/)

## 题目大意

**描述**：

给定 X-Y 平面上的一顶点坐标 $points$，其中 $points[i] = [x_i, y_i]$。这些点按顺序连成一个多边形。

**要求**：

判断该多边形是否为凸多边形。如果是凸多边形，则返回 true，否则返回 false。

**说明**：

- 假设由给定点构成的多边形总是一个 简单的多边形（简单多边形的定义）。换句话说，我们要保证每个顶点处恰好是两条边的汇合点，并且这些边「互不相交」。
- $3 \le points.length \le 10^4$。
- $points[i].length = 2$。
- $-10^4 \le points[i][0], points[i][1] \le 10^4$。
- 所有点都是唯一的。

**示例**：

- 示例 1：

```python
输入：points = [[0,0],[0,5],[5,5],[5,0]]
输出：true
```

- 示例 2：

```python
输入：points = [[0,0],[0,10],[10,10],[10,0],[5,5]]
输出：false
解释：这是一个凹多边形。
```

## 解题思路

### 思路 1：叉积判断凸多边形

判断一个多边形是否为凸多边形。凸多边形的特点是：所有内角都小于 180 度，或者说所有顶点的转向方向一致。

**核心思路**：

- 使用向量叉积判断转向方向。
- 对于三个连续的点 $A$、$B$、$C$，计算向量 $\vec{AB}$ 和 $\vec{BC}$ 的叉积。
- 叉积的符号表示转向方向：正数表示左转，负数表示右转。
- 如果所有转向方向一致（都是左转或都是右转），则为凸多边形。

**解题步骤**：

1. 遍历所有连续的三个点（包括首尾相连）。
2. 计算叉积：$cross = (x_2 - x_1) \times (y_3 - y_2) - (y_2 - y_1) \times (x_3 - x_2)$。
3. 记录叉积的符号，如果出现不同符号的叉积，说明不是凸多边形。
4. 注意：叉积为 0 表示三点共线，可以忽略。

### 思路 1：代码

```python
class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        n = len(points)
        prev_cross = 0  # 记录上一个叉积的符号
        
        for i in range(n):
            # 三个连续的点
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            x3, y3 = points[(i + 2) % n]
            
            # 计算叉积
            cross = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
            
            # 如果叉积不为 0，检查符号是否一致
            if cross != 0:
                if cross * prev_cross < 0:
                    return False
                prev_cross = cross
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是多边形的顶点数。需要遍历所有顶点。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
