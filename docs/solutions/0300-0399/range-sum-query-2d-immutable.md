# [0304. 二维区域和检索 - 矩阵不可变](https://leetcode.cn/problems/range-sum-query-2d-immutable/)

- 标签：设计、数组、矩阵、前缀和
- 难度：中等

## 题目链接

- [0304. 二维区域和检索 - 矩阵不可变 - 力扣](https://leetcode.cn/problems/range-sum-query-2d-immutable/)

## 题目大意

给定一个二维矩阵 `matrix`。

要求：满足以下多个请求：

- ` def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:`计算以 `(row1, col1)` 为左上角、`(row2, col2)` 为右下角的子矩阵中各个元素的和。
- `def __init__(self, matrix: List[List[int]]):` 对二维矩阵 `matrix` 进行初始化操作。

## 解题思路

在进行初始化的时候做预处理，这样在多次查询时可以减少重复计算，也可以减少时间复杂度。

在进行初始化的时候，使用一个二维数组 `pre_sum` 记录下以 `(0, 0)` 为左上角，以当前 `(row, col)` 为右下角的子数组各个元素和，即 `pre_sum[row + 1][col + 1]`。

则在查询时，以 `(row1, col1)` 为左上角、`(row2, col2)` 为右下角的子矩阵中各个元素的和就等于以 `(0, 0)` 到 `(row2, col2)` 的大子矩阵减去左边 `(0, 0)` 到 `(row2, col1 - 1)`的子矩阵，再减去上边 `(0, 0)` 到 `(row1 - 1, col2)` 的子矩阵，再加上左上角 `(0, 0)` 到 `(row1 - 1, col1 - 1)` 的子矩阵（因为之前重复减了）。即 `pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] - self.pre_sum[row1][col2 + 1] + self.pre_sum[row1][col1]`。

## 代码

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.pre_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                self.pre_sum[row + 1][col + 1] = self.pre_sum[row + 1][col] + self.pre_sum[row][col + 1] - self.pre_sum[row][col] + matrix[row][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] - self.pre_sum[row1][col2 + 1] + self.pre_sum[row1][col1]
```

