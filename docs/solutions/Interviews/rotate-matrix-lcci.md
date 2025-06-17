# [面试题 01.07. 旋转矩阵](https://leetcode.cn/problems/rotate-matrix-lcci/)

- 标签：数组、数学、矩阵
- 难度：中等

## 题目链接

- [面试题 01.07. 旋转矩阵 - 力扣](https://leetcode.cn/problems/rotate-matrix-lcci/)

## 题目大意

给定一个 `n * n` 大小的二维矩阵用来表示图像，其中每个像素的大小为 4 字节。

要求：设计一种算法，将图像旋转 90 度。并且要不占用额外内存空间。

## 解题思路

题目要求不占用额外内存空间，就是要在原二维矩阵上直接进行旋转操作。我们可以用翻转操作代替旋转操作。具体可以分为两步：

1. 上下翻转。

2. 主对角线翻转。

举个例子：

```
 1  2  3  4
 5  6  7  8
 9 10 11 12              
13 14 15 16              
```

上下翻转后变为：

```
13 14 15 16
 9 10 11 12
 5  6  7  8
 1  2  3  4 
```

在经过主对角线翻转后变为：

```
13  9  5  1
14 10  6  2
15 11  7  3
16 12  8  4
```

## 代码

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size // 2):
            for j in range(size):
                matrix[i][j], matrix[size - i - 1][j] = matrix[size - i - 1][j], matrix[i][j]
        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

