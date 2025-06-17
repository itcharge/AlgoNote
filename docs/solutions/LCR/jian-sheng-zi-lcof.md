# [LCR 131. 砍竹子 I](https://leetcode.cn/problems/jian-sheng-zi-lcof/)

- 标签：数学、动态规划
- 难度：中等

## 题目链接

- [LCR 131. 砍竹子 I - 力扣](https://leetcode.cn/problems/jian-sheng-zi-lcof/)

## 题目大意

给定一根长度为 `n` 的绳子，将绳子剪成整数长度的 `m` 段，每段绳子长度即为 `k[0]`、`k[1]`、...、`k[m - 1]`。

要求：计算出 `k[0] * k[1] * ... * k[m - 1]` 可能的最大乘积。

## 解题思路

可以使用动态规划求解。

定义状态 `dp[i]` 为：拆分长度为 `i` 的绳子，可以获得的最大乘积为 `dp[i]`。

将 `j` 从 `1` 遍历到 `i - 1`，通过两种方式得到 `dp[i]`：

- `(i - j) * j` ，直接将长度为 `i` 的绳子分割为 `i - j` 和 `j`，获取两者乘积。
- `dp[i - j] * j`，将长度为 `i`的绳子 中的 `i - j` 部分拆分，得到 `dp[i - j]`，和 `j` ，获取乘积。

则 `dp[i]` 取两者中的最大值。遍历 `j`，得到 `dp[i]` 的最大值。

则状态转移方程为：`dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)`。

最终输出 `dp[n]`。

## 代码

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
        return dp[n]
```

