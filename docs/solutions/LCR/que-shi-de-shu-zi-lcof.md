# [LCR 173. 点名](https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/)

- 标签：位运算、数组、哈希表、数学、二分查找
- 难度：简单

## 题目链接

- [LCR 173. 点名 - 力扣](https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/)

## 题目大意

给定一个 `n - 1` 个数的升序数组，数组中元素值都在 `0 ~ n - 1` 之间。 `nums` 中有且只有一个数字不在该数组中。

要求：找出这个缺失的数字。

## 解题思路

可以用二分查找解决。

对于中间值，判断元素值与索引值是否一致，如果一致，则说明缺失数字在索引的右侧。如果不一致，则可能为当前索引或者索引的左侧。

## 代码

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid == nums[mid]:
                left = mid + 1
            else:
                right = mid
        if left == nums[left]:
            return left + 1
        else:
            return left
```

