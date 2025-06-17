# [LCR 146. 螺旋遍历二维数组](https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

- 标签：数组、矩阵、模拟
- 难度：简单

## 题目链接

- [LCR 146. 螺旋遍历二维数组 - 力扣](https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

## 题目大意

给定一个 `m * n` 大小的二维矩阵 `matrix`。

要求：按照顺时针旋转的顺序，返回矩阵中的所有元素。

## 解题思路

按照题意进行模拟。可以实现定义一下上、下、左、右的边界，然后按照逆时针的顺序从边界上依次访问元素。

当访问完当前边界之后，要更新一下边界位置，缩小范围，方便下一轮进行访问。

## 代码

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        size_m = len(matrix)
        if size_m == 0:
            return []
        size_n = len(matrix[0])
        if size_n == 0:
            return []

        up, down, left, right = 0, size_m - 1, 0, size_n - 1
        ans = []
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
            if down < up:
                break
            for i in range(down, up - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans
```

