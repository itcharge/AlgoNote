# [LCR 166. 珠宝的最高价值](https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/)

- 标签：数组、动态规划、矩阵
- 难度：中等

## 题目链接

- [LCR 166. 珠宝的最高价值 - 力扣](https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/)

## 题目大意

给定一个 `m * n` 大小的二维矩阵 `grid` 代表棋盘，棋盘的每一格都放有一个礼物，每个礼物有一定的价值（价值大于 `0`）。`grid[i][j]` 表示棋盘第 `i` 行第 `j` 列的礼物价值。我们可以从左上角的格子开始拿礼物，每次只能向右或者向下移动一格，直到到达棋盘的右下角。

要求：计算出最多能拿多少价值的礼物。 

## 解题思路

可以用动态规划求解，设 `dp[i][j]` 是从 `(0, 0)` 到 `(i - 1, j - 1)` 能得礼物的最大价值。

显然 `dp[i][j] = max(dp[i - 1][j] + dp[i][j - 1]) + grid[i][j]`。

因为是自上而下递推 `dp[i-1][j]` 可以用 `dp[j]` 来表示，所以也可以将二维改为一位。状态转移公式为： `dp[j] = max(dp[j], dp[j - 1]) + grid[i][j]`。

## 代码

```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        size_m = len(grid)
        size_n = len(grid[0])
        dp = [0 for _ in range(size_n + 1)]
        for i in range(size_m):
            for j in range(size_n):
                dp[j + 1] = max(dp[j], dp[j + 1]) + grid[i][j]
        return dp[size_n]
```

