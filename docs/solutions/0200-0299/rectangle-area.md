# [0223. 矩形面积](https://leetcode.cn/problems/rectangle-area/)

- 标签：几何、数学
- 难度：中等

## 题目链接

- [0223. 矩形面积 - 力扣](https://leetcode.cn/problems/rectangle-area/)

## 题目大意

给定两个矩形的左下角坐标、右上角坐标 `(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)`。其中 `(ax1, ay1)` 表示第一个矩形左下角坐标，`(ax2, ay2)` 表示第一个矩形右上角坐标，`(bx1, by1)` 表示第二个矩形左下角坐标，`(bx2, by2)` 表示第二个矩形右上角坐标。

要求：计算出两个矩形覆盖的总面积。

## 解题思路

两个矩形覆盖的总面积 = 第一个矩形面积 + 第二个矩形面积 - 重叠部分面积。

需要分别计算出两个矩形面积，还有求出相交部分的长、宽，并计算出对应重叠部分的面积。

## 代码

```python
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        area_overlap = overlap_width * overlap_height

        return area_a + area_b - area_overlap
```

