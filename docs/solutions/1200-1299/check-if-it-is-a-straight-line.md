# [1232. 缀点成线](https://leetcode.cn/problems/check-if-it-is-a-straight-line/)

- 标签：几何、数组、数学
- 难度：简单

## 题目链接

- [1232. 缀点成线 - 力扣](https://leetcode.cn/problems/check-if-it-is-a-straight-line/)

## 题目大意

给定一系列的二维坐标点的坐标 `(xi, yi)`，判断这些点是否属于同一条直线。如果属于同一条直线，则返回 True，否则返回 False。

## 解题思路

如果根据斜率来判断点是否处于同一条直线，需要处理斜率不存在（无穷大）的情况。我们可以使用叉乘来判断三个点构成的两个向量是否处于同一条直线上。

叉乘原理：

设向量 P 为 `(x1, y1)` 向量，Q 为 `(x2, y2)`，则向量 P、Q 的叉积定义为：$P × Q = x_1y_2 - x_2y_1$，其几何意义表示为如果以向量 P 和向量 Q 为边构成一个平行四边形，那么这两个向量叉乘的模长与这个平行四边形的正面积相等。

![向量叉积](https://img.geek-docs.com/mathematical-basis/linear-algebra/220px-Cross_product_parallelogram.png)

- 如果 `P × Q = 0`，则 P 与 Q 共线，有可能同向，也有可能反向。
- 如果 `P × Q > 0`，则 P 在 Q 的顺时针方向。
- 如果 `P × Q < 0`，则 P 在 Q 的逆时针方向。

具体求解方法：

- 先求出第一个坐标与第二个坐标构成的向量 P。
- 遍历所有坐标，求出所有坐标与第一个坐标构成的向量 Q。
  - 如果 `P × Q ≠ 0`，则返回 False。
- 如果遍历完仍没有发现 `P × Q ≠ 0`，则返回 True。

## 代码

```python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1 = coordinates[1][0] - coordinates[0][0]
        y1 = coordinates[1][1] - coordinates[0][1]

        for i in range(len(coordinates)):
            x2 = coordinates[i][0] - coordinates[0][0]
            y2 = coordinates[i][1] - coordinates[0][1]
            if x1 * y2 != x2 * y1:
                return False
        return True
```

