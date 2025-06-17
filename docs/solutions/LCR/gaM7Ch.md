# [LCR 103. 零钱兑换](https://leetcode.cn/problems/gaM7Ch/)

- 标签：广度优先搜索、数组、动态规划
- 难度：中等

## 题目链接

- [LCR 103. 零钱兑换 - 力扣](https://leetcode.cn/problems/gaM7Ch/)

## 题目大意

给定不同面额的硬币 `coins` 和一个总金额 `amount`。

乔秋：计算出凑成总金额所需的最少的硬币个数。如果无法凑出，则返回 `-1`。

## 解题思路

完全背包问题。

可以转换为有 `n` 枚不同的硬币，每种硬币可以无限次使用。凑成总金额为 `amount` 的背包，最少需要多少硬币。

动态规划的状态 `dp[i]` 可以表示为：凑成总金额为 `i` 的组合中，至少有 `dp[i]` 枚硬币。

动态规划的状态转移方程为：`dp[i] = min(dp[i], + dp[i-coin] + 1`，意思为凑成总金额为 `i` 最少硬币数量 = 「不使用当前 `coin`，只使用之前硬币凑成金额 `i` 的最少硬币数量」和「凑成金额 `i - num` 的最少硬币数量，再加上当前硬币」两者的较小值。

## 代码

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
```

