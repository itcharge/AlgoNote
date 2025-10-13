# [0836. 矩形重叠](https://leetcode.cn/problems/rectangle-overlap/)

- 标签：几何、数学
- 难度：简单

## 题目链接

- [0836. 矩形重叠 - 力扣](https://leetcode.cn/problems/rectangle-overlap/)

## 题目大意

给定两个矩形的左下角、右上角坐标：[x1, y1, x2, y2]。[x1, y1] 表示左下角坐标，[x2, y2] 表示右上角坐标。如果两个矩形相交面积大于 0，则称两矩形重叠。

要求：根据给定的矩形 rec1 和 rec2 的左下角、右上角坐标，如果重叠，则返回 True，否则返回 False。

## 解题思路

如果两个矩形重叠，则两个矩形的水平边投影到 x 轴上的线段会有交集，同理竖直边投影到 y 轴上的线段也会有交集。因此我们可以把问题看做是：判断两条线段是否有交集。

矩形 rec1 和 rec2 水平边投影到 x 轴上的线段为 `(rec1[0], rec1[2])` 和 `(rec2[0], rec2[2])`。如果两条线段有交集，则 `min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])`。

矩形 rec1 和 rec2 竖直边投影到 y 轴上的线段为 `(rec1[1], rec1[3])` 和 `(rec2[1], rec2[3])`。如果两条线段有交集，则 `min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])`。

判断是否满足上述条件，如果满足则说明两个矩形重叠，返回 True，如果不满足则返回 False。

## 代码

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
         return min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) and min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])
```

