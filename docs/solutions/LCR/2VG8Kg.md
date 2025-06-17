# [LCR 008. 长度最小的子数组](https://leetcode.cn/problems/2VG8Kg/)

- 标签：数组、二分查找、前缀和、滑动窗口
- 难度：中等

## 题目链接

- [LCR 008. 长度最小的子数组 - 力扣](https://leetcode.cn/problems/2VG8Kg/)

## 题目大意

给定一个只包含正整数的数组 `nums` 和一个正整数 `target`。

要求：找出数组中满足和大于等于 `target` 的长度最小的「连续子数组」，并返回其长度。

## 解题思路

最直接的做法是暴力枚举，时间复杂度为 $O(n^2)$。但是我们可以利用滑动窗口的方法，在时间复杂度为 $O(n)$ 的范围内解决问题。

定义两个指针 `start` 和 `end`。`start` 代表滑动窗口开始位置，`end` 代表滑动窗口结束位置。再定义一个变量 `sum` 用来存储滑动窗口中的元素和，一个变量 `ans` 来存储满足提议的最小长度。

先不断移动 `end`，直到 `sum ≥ target`，则更新最小长度值 `ans`。然后再将滑动窗口的起始位置从滑动窗口中移出去，直到 `sum ≤ target`，在移出的期间，同样要更新最小长度值 `ans`。

然后等满足 `sum ≤ target` 时，再移动 `end`，重复上一步，直到遍历到数组末尾。

## 代码

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        start = 0
        end = 0
        sum = 0
        ans = n + 1
        while end < n:
            sum += nums[end]
            while sum >= target:
                ans = min(ans, end - start + 1)
                sum -= nums[start]
                start += 1
            end += 1
        if ans == n + 1:
            return 0
        else:
            return ans
```

