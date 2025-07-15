# [面试题 01.08. 零矩阵](https://leetcode.cn/problems/zero-matrix-lcci/)

- 标签：数组、哈希表、矩阵
- 难度：中等

## 题目链接

- [面试题 01.08. 零矩阵 - 力扣](https://leetcode.cn/problems/zero-matrix-lcci/)

## 题目大意

给定一个 `m * n` 大小的二维矩阵 `matrix`。

要求：编写一种算法，如果矩阵中某个元素为 `0`，增将其所在行与列清零。

## 解题思路

直观上可以使用两个数组或者集合来标记行和列出现 `0` 的情况，但更好的做法是不用开辟新的数组或集合，直接原本二维矩阵 `matrix` 的空间。使用数组原本的元素进行记录出现 0 的情况。

设定两个变量 `flag_row0`、`flag_col0` 来标记第一行、第一列是否出现了 `0`。

接下来我们使用数组第一行、第一列来标记 `0` 的情况。

对数组除第一行、第一列之外的每个元素进行遍历，如果某个元素出现 `0` 了，则使用数组的第一行、第一列对应位置来存储 `0` 的标记。

再对数组除第一行、第一列之外的每个元素进行遍历，通过对第一行、第一列的标记 0 情况，进行置为 `0` 的操作。

最后再根据 `flag_row0`、`flag_col0` 的标记情况，对第一行、第一列进行置为 `0` 的操作。

## 代码

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        flag_col0 = False
        flag_row0 = False
        for i in range(rows):
            if matrix[i][0] == 0:
                flag_col0 = True
                break

        for j in range(cols):
            if matrix[0][j] == 0:
                flag_row0 = True
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(rows):
                matrix[i][0] = 0

        if flag_row0:
            for j in range(cols):
                matrix[0][j] = 0
```

