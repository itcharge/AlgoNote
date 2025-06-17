# [LCR 102. 目标和](https://leetcode.cn/problems/YaVDxD/)

- 标签：数组、动态规划、回溯
- 难度：中等

## 题目链接

- [LCR 102. 目标和 - 力扣](https://leetcode.cn/problems/YaVDxD/)

## 题目大意

给定一个整数数组 `nums` 和一个整数 `target`。数组长度不超过 `20`。向数组中每个整数前加 `+` 或 `-`。然后串联起来构造成一个表达式。

要求：返回通过上述方法构造的、运算结果等于 `target` 的不同表达式数目。

## 解题思路

暴力方法就是使用深度优先搜索对每位数字遍历 `+`、`-`，并统计符合要求的表达式数目。但是实际发现超时了。所以采用动态规划的方法来做。

假设数组中所有元素和为 `sum`，数组中所有符号为 `+` 的元素为 `sum_x`，符号为 `-` 的元素和为 `sum_y`。则 `target = sum_x - sum_y`。

而 `sum_x + sum_y = sum`。根据两个式子可以求出 `2 * sum_x = target + sum `，即 `sum_x = (target + sum) / 2`。

那么这道题就变成了，如何在数组中找到一个集合，使集合中元素和为 `(target + sum) / 2`。这就变为了求容量为 `(target + sum) / 2` 的 `01` 背包问题。

动态规划的状态 `dp[i]` 表示为：填满容量为 `i` 的背包，有 `dp[i]` 种方法。

动态规划的状态转移方程为：`dp[i] = dp[i] + dp[i-num]`，意思为填满容量为 `i` 的背包的方法数 = 不使用当前 `num`，只使用之前元素填满容量为 `i` 的背包的方法数 + 填满容量 `i - num` 的包的方法数，再填入 `num` 的方法数。

## 代码

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if target > sum_nums or (target + sum_nums) % 2 == 1:
            return 0
        size = (target + sum_nums) // 2
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1
        for num in nums:
            for i in range(size, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
        return dp[size]
```

