# [0378. 有序矩阵中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/)

- 标签：数组、二分查找、矩阵、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0378. 有序矩阵中第 K 小的元素 - 力扣](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/)

## 题目大意

给定一个 `n * n` 矩阵 `matrix`，其中每行和每列元素均按升序排序。

要求：找到矩阵中第 `k` 小的元素。

注意：它是排序后的第 `k` 小元素，而不是第 `k` 个 不同的元素。

## 解题思路

已知二维矩阵 `matrix` 每行每列是按照升序排序的。那么二维矩阵的下界就是左上角元素 `matrix[0][0]`，上界就是右下角元素 `matrix[rows - 1][cols - 1]`。那么我们可以使用二分查找的方法在上界、下界之间搜索所有值，找到第 `k` 小的元素。

我们可以通过判断矩阵中比 `mid` 小的元素个数是否等于 `k` 来确定是否找到第 `k` 小的元素。

- 如果比 `mid` 小的元素个数大于等于 `k`，说明最终答案 `ans` 小于等于 `mid`。
- 如果比 `mid` 小的元素个数小于 `k`，说明最终答案 `ans` 大于 `k`。

## 代码

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[rows - 1][cols - 1] + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.counterKthSmallest(mid, matrix) >= k:
                right = mid
            else:
                left = mid + 1
        return left

    def counterKthSmallest(self, mid, matrix):
        rows, cols = len(matrix), len(matrix[0])
        count = 0
        j = cols - 1
        for i in range(rows):
            while j >= 0 and mid < matrix[i][j]:
                j -= 1
            count += j + 1
        return count
```

