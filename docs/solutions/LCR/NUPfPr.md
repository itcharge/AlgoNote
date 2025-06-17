# [LCR 101. 分割等和子集](https://leetcode.cn/problems/NUPfPr/)

- 标签：数学、字符串、模拟
- 难度：简单

## 题目链接

- [LCR 101. 分割等和子集 - 力扣](https://leetcode.cn/problems/NUPfPr/)

## 题目大意

给定一个只包含正整数的非空数组 `nums`。

要求：判断是否可以将这个数组分成两个子集，使得两个子集的元素和相等。

## 解题思路

动态规划求解。

如果两个子集和相等，则两个子集元素和刚好等于整个数组元素和的一半。这就相当于 `0-1` 背包问题。

定义 `dp[i][j]` 表示从 `[0, i]` 个数中任意选取一些数，放进容量为 j 的背包中，价值总和最大为多少。则 `dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])`。

转换为一维 dp 就是：`dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])`。

然后进行递归求解。最后判断 `dp[target]` 和 `target` 是否相等即可。

## 代码

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = 100010
        dp = [0 for _ in range(size)]
        sum_nums = sum(nums)
        if sum_nums & 1:
            return False
        target = sum_nums // 2
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        if dp[target] == target:
            return True
        return False
```

