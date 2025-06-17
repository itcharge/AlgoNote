# [LCR 098. 不同路径](https://leetcode.cn/problems/2AoeFn/)

- 标签：数学、动态规划、组合数学
- 难度：中等

## 题目链接

- [LCR 098. 不同路径 - 力扣](https://leetcode.cn/problems/2AoeFn/)

## 题目大意

给定一个 `m * n` 的棋盘， 机器人在左上角的位置，机器人每次只能向右、或者向下移动一步。

要求：求出到达棋盘右下角共有多少条不同的路径。

## 解题思路

可以用动态规划求解，设 `dp[i][j]` 是从 `(0, 0)`到 `(i, j)` 的不同路径数。显然 `dp[i][j] = dp[i-1][j] + dp[i][j-1]`。对于第一行、第一列，因为只能超一个方向走，所以 `dp[i][0] = 1`，`dp[0][j] = 1`。

## 代码

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
```

