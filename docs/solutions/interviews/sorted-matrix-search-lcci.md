# [面试题 10.09. 排序矩阵查找](https://leetcode.cn/problems/sorted-matrix-search-lcci/)

- 标签：数组、二分查找、分治、矩阵
- 难度：中等

## 题目链接

- [面试题 10.09. 排序矩阵查找 - 力扣](https://leetcode.cn/problems/sorted-matrix-search-lcci/)

## 题目大意

给定一个 `m * n` 大小的有序整数矩阵。每一行、每一列都按升序排列。再给定一个目标值 `target`。

要求：判断矩阵中是否可以找到 `target`，如果找到 `target`，返回 `True`，否则返回 `False`。

## 解题思路

矩阵是有序的，可以考虑使用二分搜索来进行查找。

迭代对角线元素，假设对角线元素的坐标为 `(row, col)`。把数组元素按对角线分为右上角部分和左下角部分。

则对于当前对角线元素右侧第 `row` 行、对角线元素下侧第 `col` 列进行二分查找。

- 如果找到目标，直接返回 `True`。
- 如果找不到目标，则缩小范围，继续查找。
- 直到所有对角线元素都遍历完，依旧没找到，则返回 `False`。

## 代码

```python
class Solution:
    def diagonalBinarySearch(self, matrix, diagonal, target):
        left = 0
        right = diagonal
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid][mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def rowBinarySearch(self, matrix, begin, cols, target):
        left = begin
        right = cols
        while left < right:
            mid = left + (right - left) // 2
            if matrix[begin][mid] < target:
                left = mid + 1
            elif matrix[begin][mid] > target:
                right = mid - 1
            else:
                left = mid
                break
        return begin <= left <= cols and matrix[begin][left] == target

    def colBinarySearch(self, matrix, begin, rows, target):
        left = begin + 1
        right = rows
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid][begin] < target:
                left = mid + 1
            elif matrix[mid][begin] > target:
                right = mid - 1
            else:
                left = mid
                break
        return begin <= left <= rows and matrix[left][begin] == target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False

        min_val = min(rows, cols)
        index = self.diagonalBinarySearch(matrix, min_val - 1, target)
        if matrix[index][index] == target:
            return True
        for i in range(index + 1):
            row_search = self.rowBinarySearch(matrix, i, cols - 1, target)
            col_search = self.colBinarySearch(matrix, i, rows - 1, target)
            if row_search or col_search:
                return True
        return False
```

