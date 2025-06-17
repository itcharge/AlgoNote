# [LCR 088. 使用最小花费爬楼梯](https://leetcode.cn/problems/GzCJIP/)

- 标签：数组、动态规划
- 难度：简单

## 题目链接

- [LCR 088. 使用最小花费爬楼梯 - 力扣](https://leetcode.cn/problems/GzCJIP/)

## 题目大意

给定一个数组 `cost` 代表一段楼梯，`cost[i]` 代表爬上第 `i` 阶楼梯醒酒药花费的体力值（下标从 `0` 开始）。

每爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

要求：找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 `0` 或 `1` 的元素作为初始阶梯。

## 解题思路

使用动态规划方法。

状态 `dp[i]` 表示为：到达第 `i` 个台阶所花费的最少体⼒。

则状态转移方程为： `dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]`。

表示为：到达第 `i` 个台阶所花费的最少体⼒ = 到达第 `i - 1` 个台阶所花费的最小体力 与 到达第 `i - 2` 个台阶所花费的最小体力中的最小值 + 到达第 `i` 个台阶所需要花费的体力值。

## 代码

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [0 for _ in range(size + 1)]
        for i in range(2, size + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[size]
```

