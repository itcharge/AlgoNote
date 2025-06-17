# [0518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [0518. 零钱兑换 II - 力扣](https://leetcode.cn/problems/coin-change-ii/)

## 题目大意

**描述**：给定一个整数数组 $coins$ 表示不同面额的硬币，另给一个整数 $amount$ 表示总金额。

**要求**：计算并返回可以凑成总金额的硬币方案数。如果无法凑出总金额，则返回 $0$。

**说明**：

- 每一种面额的硬币枚数为无限个。
- $1 \le coins.length \le 300$。
- $1 \le coins[i] \le 5000$。
- $coins$ 中的所有值互不相同。
- $0 \le amount \le 5000$。

**示例**：

- 示例 1：

```python
输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

- 示例 2：

```python
输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3。
```

## 解题思路

### 思路 1：动态规划

这道题可以转换为：有 $n$ 种不同的硬币，$coins[i]$ 表示第 $i$ 种硬币的面额，每种硬币可以无限次使用。请问凑成总金额为 $amount$ 的背包，一共有多少种方案？

这就变成了完全背包问题。「[322. 零钱兑换](https://leetcode.cn/problems/coin-change/)」中计算的是凑成总金额的最少硬币个数，而这道题计算的是凑成总金额的方案数。

###### 1. 划分阶段

按照当前背包的载重上限进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i]$ 表示为：凑成总金额为 $i$ 的方案总数。

###### 3. 状态转移方程

凑成总金额为 $i$ 的方案数 = 「不使用当前 $coin$，只使用之前硬币凑成金额 $i$ 的方案数」+「使用当前 $coin$ 凑成金额 $i - coin$ 的方案数」。即状态转移方程为：$dp[i] = dp[i] + dp[i - coin]$。

###### 4. 初始条件

- 凑成总金额为 $0$ 的方案数为 $1$，即 $dp[0] = 1$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i]$ 表示为：凑成总金额为 $i$ 的方案总数。 所以最终结果为 $dp[amount]$。

### 思路 1：代码

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times amount)$，其中 $n$ 为数组 $coins$ 的元素个数，$amount$ 为总金额。
- **空间复杂度**：$O(amount)$。

