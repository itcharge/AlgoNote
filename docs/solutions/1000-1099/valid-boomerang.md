# [1037. 有效的回旋镖](https://leetcode.cn/problems/valid-boomerang/)

- 标签：几何、数组、数学
- 难度：简单

## 题目链接

- [1037. 有效的回旋镖 - 力扣](https://leetcode.cn/problems/valid-boomerang/)

## 题目大意

**描述**：给定一个数组 $points$，其中 $points[i] = [xi, yi]$ 表示平面上的一个点。

**要求**：如果这些点构成一个回旋镖，则返回 `True`，否则，则返回 `False`。

**说明**：

- **回旋镖**：定义为一组三个点，这些点各不相同且不在一条直线上。
- $points.length == 3$。
- $points[i].length == 2$。
- $0 \le xi, yi \le 100$。

**示例**：

- 示例 1：

```python
输入：points = [[1,1],[2,3],[3,2]]
输出：True
```

- 示例 2：

```python
输入：points = [[1,1],[2,2],[3,3]]
输出：False
```

## 解题思路

### 思路 1：

设三点坐标为 $A = (x1, y1)$，$B = (x2, y2)$，$C = (x3, y3)$，则向量 $\overrightarrow{AB} = (x2 - x1, y2 - y1)$，$\overrightarrow{BC} = (x3 - x2, y3 - y2)$。

如果三点共线，则应满足：$\overrightarrow{AB} \times \overrightarrow{BC} = (x2 − x1) \times (y3 − y2) - (x3 − x2) \times (y2 − y1) = 0$。

如果三点不共线，则应满足：$\overrightarrow{AB} \times \overrightarrow{BC} = (x2 − x1) \times (y3 − y2) - (x3 − x2) \times (y2 − y1) \ne 0$。

### 思路 1：代码

```python
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        cross1 = (x2 - x1) * (y3 - y2)
        cross2 = (x3 - x2) * (y2 - y1)
        return cross1 - cross2 != 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。
