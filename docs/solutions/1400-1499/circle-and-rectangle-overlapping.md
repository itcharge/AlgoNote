# [1401. 圆和矩形是否有重叠](https://leetcode.cn/problems/circle-and-rectangle-overlapping/)

- 标签：几何、数学
- 难度：中等

## 题目链接

- [1401. 圆和矩形是否有重叠 - 力扣](https://leetcode.cn/problems/circle-and-rectangle-overlapping/)

## 题目大意

**描述**：给定圆 $(x\_center, y\_center, radius)$ 和一个轴对齐矩形 $(x1, y1, x2, y2)$，其中 $(x1, y1)$ 是左下角，$(x2, y2)$ 是右上角。

**要求**：判断圆和矩形是否有重叠区域（包括边界）。

**说明**：
- $-10^4 \le x\_center, y\_center, x1, x2, y1, y2 \le 10^4$。
- $x1 < x2, y1 < y2$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png)

```python
输入：radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
输出：true
解释：圆和矩形存在公共点 (1,0) 。
```

- 示例 2：

```python
输入：radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
输出：false
```

- 示例 3：

![](https://assets.leetcode.com/uploads/2020/02/20/sample_2_1728.png)

```python
输入：radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
输出：true
```

## 解题思路

### 思路 1：几何分析

#### 1. 核心思想

圆和矩形有重叠，等价于圆心到矩形的最短距离 $\le radius$。

矩形区域为 $[x1, x2] \times [y1, y2]$。圆心 $(cx, cy)$ 到矩形的最短距离为：

$$dist = \max(0, \max(x1 - cx, 0, cx - x2))^2 + \max(0, \max(y1 - cy, 0, cy - y2))^2$$

即：如果圆心在矩形内部（水平方向和垂直方向都在范围内），距离为 $0$。否则，取水平和垂直方向上到矩形边界的最近距离。

#### 2. 具体步骤

**第 1 步**：计算水平方向最近距离：
- 如果 $cx < x1$，最近距离为 $x1 - cx$。
- 如果 $cx > x2$，最近距离为 $cx - x2$。
- 否则最近距离为 $0$。

**第 2 步**：垂直方向同理。

**第 3 步**：计算 $dist^2 = h^2 + v^2$。返回 $dist^2 \le radius^2$。

#### 3. 举例说明

以 $(cx, cy) = (3, 3), radius = 2$，矩形 $(x1=1, y1=1, x2=5, y2=5)$ 为例：

圆心在矩形内部 → $dist = 0 \le 2$ → 重叠。

以 $(cx, cy) = (6, 3), radius = 2$，矩形 $(1,1,5,5)$ 为例：

水平最近距离：$cx - x2 = 6 - 5 = 1$
垂直最近距离：$cy$ 在 $[1,5]$ 内 → $0$
$dist^2 = 1^2 + 0^2 = 1 \le 4$ → 重叠。

### 思路 1：代码

```python
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int,
                      x1: int, y1: int, x2: int, y2: int) -> bool:
        # 水平方向最近距离
        if x_center < x1:
            h = x1 - x_center
        elif x_center > x2:
            h = x_center - x2
        else:
            h = 0

        # 垂直方向最近距离
        if y_center < y1:
            v = y1 - y_center
        elif y_center > y2:
            v = y_center - y2
        else:
            v = 0

        return h * h + v * v <= radius * radius
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。
