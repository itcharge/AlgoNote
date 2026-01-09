# [0939. 最小面积矩形](https://leetcode.cn/problems/minimum-area-rectangle/)

- 标签：几何、数组、哈希表、数学、排序
- 难度：中等

## 题目链接

- [0939. 最小面积矩形 - 力扣](https://leetcode.cn/problems/minimum-area-rectangle/)

## 题目大意

**描述**：

给定一个 X-Y 平面上的点数组 $points$，其中 $points[i] = [x_i, y_i]$。

**要求**：

返回由这些点形成的矩形的最小面积，矩形的边与 X 轴和 Y 轴平行。如果不存在这样的矩形，则返回 0。


**说明**：

- $1 \le points.length \le 500$。
- $points[i].length == 2$。
- $0 \le x_i, y_i \le 4 \times 10^{4}$。
- 所有给定的点都是「唯一」的。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG)

```python
输入： points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
输出： 4
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG)

```python
输入： points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
输出： 2
```

## 解题思路

### 思路 1：哈希表

要找到边平行于坐标轴的最小面积矩形，我们需要找到四个点构成的矩形。

1. **枚举对角线**：矩形可以由对角线上的两个点确定。对于边平行于坐标轴的矩形，对角线的两个点 $(x_1, y_1)$ 和 $(x_2, y_2)$ 满足 $x_1 \ne x_2$ 且 $y_1 \ne y_2$。
2. **验证矩形**：对于每对对角线点，检查另外两个点 $(x_1, y_2)$ 和 $(x_2, y_1)$ 是否存在。
3. **计算面积**：如果四个点都存在，计算面积 $|x_2 - x_1| \times |y_2 - y_1|$，更新最小值。
4. **优化**：使用哈希集合存储所有点，快速判断点是否存在。

### 思路 1：代码

```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple, points))
        min_area = float('inf')
        
        # 枚举所有点对作为对角线
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                
                # 必须是对角线（不在同一行或同一列）
                if x1 != x2 and y1 != y2:
                    # 检查另外两个点是否存在
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        min_area = min(min_area, area)
        
        return min_area if min_area != float('inf') else 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是点的数量，需要枚举所有点对。
- **空间复杂度**：$O(n)$，需要使用哈希集合存储所有点。
