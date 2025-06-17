# [LCR 161. 连续天数的最高销售额](https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

- 标签：数组、分治、动态规划
- 难度：简单

## 题目链接

- [LCR 161. 连续天数的最高销售额 - 力扣](https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

## 题目大意

给定一个整数数组 `nums` 。

要求：找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和，要求时间复杂度为 `O(n)`。

## 解题思路

动态规划的方法，关键点是要找到状态转移方程。

假设 f(i) 表示第 i 个数结尾的「连续子数组的最大和」，那么 $max_{0 < i \le n-1} {f(i)} = max(f(i-1) + nums[i], nums[i])$

即将之前累加和加上当前值与当前值做比较。

- 如果将之前累加和加上当前值 > 当前值，那么加上当前值。
- 如果将之前累加和加上当前值 < 当前值，那么 $f(i) = nums[i]$。

## 代码

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ans = nums[0]
        ans = 0
        for num in nums:
            ans = max(ans + num, num)
            max_ans = max(max_ans, ans)
        return max_ans
```

