# [0861. 翻转矩阵后的得分](https://leetcode.cn/problems/score-after-flipping-matrix/)

- 标签：贪心、位运算、数组、矩阵
- 难度：中等

## 题目链接

- [0861. 翻转矩阵后的得分 - 力扣](https://leetcode.cn/problems/score-after-flipping-matrix/)

## 题目大意

**描述**：给定一个二维矩阵 `A`，其中每个元素的值为 `0` 或 `1`。

我们可以选择任一行或列，并转换该行或列中的每一个值：将所有 `0` 都更改为 `1`，将所有 `1` 都更改为 `0`。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

**要求**：返回尽可能高的分数。

**说明**：

- $1 \le A.length \le 20$。
- $1 \le A[0].length \le 20$。
- `A[i][j]` 值为 `0` 或 `1`。

**示例**：

- 示例 1：

```python
输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为  [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
```

## 解题思路

### 思路 1：贪心算法

对于一个二进制数来说，应该优先保证高位（靠前的列）尽可能的大，也就是保证高位尽可能值为 `1`。

- 我们先来看矩阵的第一列数，只要第一列的某一行为 `0`，则将这一行的值进行翻转。这样就保证了最高位一定为 `1`。
- 接下来，我们再来关注除了第一列的其他列，这里因为有最高位限制，所以我们不能随意再将某一行的值进行翻转，只能选择某一列进行翻转。
- 为了保证当前位上有尽可能多的 `1`。我们可以用两个变量 `one_cnt`、`zeo_cnt` 来记录当前列上 `1` 的个数和 `0` 的个数。如果 `0` 的个数多于 `1` 的个数，那么我们就将当前列进行翻转。从而保证当前位上有尽可能多的 `1`。
- 当所有列都遍历完成后，我们会得到加和最大的情况。

### 思路 1：贪心算法代码

```python
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        zero_cnt, one_cnt = 0, 0
        res = 0
        rows, cols = len(grid), len(grid[0])

        for col in range(cols):
            for row in range(rows):
                if col == 0 and grid[row][col] == 0:
                    for j in range(cols):
                        grid[row][j] = 1 - grid[row][j]
                else:
                    if grid[row][col] == 1:
                        one_cnt += 1
                    else:
                        zero_cnt += 1
            if zero_cnt > one_cnt:
                for row in range(rows):
                    grid[row][col] = 1 - grid[row][col]

            for row in range(rows):
                if grid[row][col] == 1:
                    res += pow(2, cols - col - 1)
            zero_cnt = 0
            one_cnt = 0
        return res
```
