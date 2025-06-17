# [0264. 丑数 II](https://leetcode.cn/problems/ugly-number-ii/)

- 标签：哈希表、数学、动态规划、堆（优先队列）
- 难度：中等

## 题目链接

- [0264. 丑数 II - 力扣](https://leetcode.cn/problems/ugly-number-ii/)

## 题目大意

给定一个整数 `n`。

要求：找出并返回第 `n` 个丑数。

- 丑数：只包含质因数 `2`、`3`、`5` 的正整数。

## 解题思路

动态规划求解。

定义状态 `dp[i]` 表示第 `i` 个丑数。

状态转移方程为：`dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)` ，其中 `p2`、`p3`、`p5` 分别表示当前 `i` 中  `2`、`3`、`5` 的质因子数量。

## 代码

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[n - 1]
```

