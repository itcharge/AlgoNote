# [LCR 104. 组合总和 Ⅳ](https://leetcode.cn/problems/D0F0SV/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [LCR 104. 组合总和 Ⅳ - 力扣](https://leetcode.cn/problems/D0F0SV/)

## 题目大意

给定一个由不同整数组成的数组 `nums` 和一个目标整数 `target`。

要求：从 `nums` 中找出并返回总和为 `target` 的元素组合个数。

## 解题思路

完全背包问题。题目求解的是组合数。

动态规划的状态 `dp[i]` 可以表示为：凑成总和 `i` 的组合数。

动态规划的状态转移方程为：`dp[i] = dp[i] + dp[i - nums[j]]`，意思为凑成总和为 `i` 的组合数 = 「不使用当前 `nums[j]`，只使用之前整数凑成和为 `i` 的组合数」+「使用当前 `nums[j]` 凑成金额 `i - nums[j]` 的方案数」。

最终输出 `dp[target]`。

## 代码

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        size = len(nums)
        for i in range(target + 1):
            for j in range(size):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]
        return dp[target]
```

