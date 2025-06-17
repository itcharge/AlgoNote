# [1605. 给定行和列的和求可行矩阵](https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/)

- 标签：贪心、数组、矩阵
- 难度：中等

## 题目链接

- [1605. 给定行和列的和求可行矩阵 - 力扣](https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/)

## 题目大意

**描述**：给你两个非负整数数组 `rowSum` 和 `colSum` ，其中 `rowSum[i]` 是二维矩阵中第 `i` 行元素的和，`colSum[j]` 是第 `j` 列元素的和。换句话说，我们不知道矩阵里的每个元素，只知道每一行的和，以及每一列的和。

**要求**：找到并返回一个大小为 `rowSum.length * colSum.length` 的任意非负整数矩阵，且该矩阵满足 `rowSum` 和 `colSum` 的要求。

**说明**：

- 返回任意一个满足题目要求的二维矩阵即可，题目保证存在至少一个可行矩阵。
- $1 \le rowSum.length, colSum.length \le 500$。
- $0 \le rowSum[i], colSum[i] \le 10^8$。
- $sum(rows) == sum(columns)$。

**示例**：

- 示例 1：

```python
输入：rowSum = [3,8], colSum = [4,7]
输出：[[3,0],
        [1,7]]

解释
第 0 行：3 + 0 = 3 == rowSum[0]
第 1 行：1 + 7 = 8 == rowSum[1]
第 0 列：3 + 1 = 4 == colSum[0]
第 1 列：0 + 7 = 7 == colSum[1]
行和列的和都满足题目要求，且所有矩阵元素都是非负的。
另一个可行的矩阵为   [[1,2],
                   [3,5]]
```

## 解题思路

### 思路 1：贪心算法

题目要求找出一个满足要求的非负整数矩阵，矩阵中元素值可以为 `0`。所以我们可以尽可能将大的值填入前面的行和列中，然后剩余位置用 `0` 补齐即可。具体做法如下：

1. 使用二维数组 `board` 来保存答案，初始情况下，`board` 中元素全部赋值为 `0`。
2. 遍历二维数组的每一行，每一列。当前位置下的值为当前行的和与当前列的和的较小值，即 `board[row][col] = min(rowSum[row], colSum[col])`。
3. 更新当前行的和，将当前行的和减去 `board[row][col]`。
4. 更新当前列的和，将当前列的和减去 `board[row][col]`。
5. 遍历完返回二维数组 `board`。

### 思路 1：贪心算法代码

```python
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        board = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                board[row][col] = min(rowSum[row], colSum[col])
                rowSum[row] -= board[row][col]
                colSum[col] -= board[row][col]
        return board
```
