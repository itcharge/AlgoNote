# [LCR 172. 统计目标成绩的出现次数](https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

- 标签：数组、二分查找
- 难度：简单

## 题目链接

- [LCR 172. 统计目标成绩的出现次数 - 力扣](https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

## 题目大意

给定一个排序数组 `nums`，以及一个整数 `target`。

要求：统计 `target` 在排序数组 `nums` 中出现的次数。

## 解题思路

两次二分查找。

- 先查找 `target` 第一次出现的位置（下标）：`left`。
- 再查找 `target` 最后一次出现的位置（下标）：`right`。
- 最终答案为 `right - left + 1`。

## 代码

```python
class Solution:
    def searchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1

    def searchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        return left

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)

        if left == -1:
            return 0

        return right - left + 1
```

