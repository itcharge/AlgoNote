# [LCR 179. 查找总价格为目标值的两个商品](https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/)

- 标签：数组、双指针、二分查找
- 难度：简单

## 题目链接

- [LCR 179. 查找总价格为目标值的两个商品 - 力扣](https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/)

## 题目大意

给定一个升序数组 `nums`，以及一个目标整数 `target`。

要求：在数组中查找两个数，使它们的和刚好等于 `target`。

## 解题思路

因为数组是升序的，可以使用双指针。`left`、`right` 分别指向数组首尾位置。

- 计算 `sum = nums[left] + nums[right]`。
- 如果 `sum > target`，则 `right` 进行左移。
- 如果 `sum < target`，则 `left` 进行右移。
- 如果 `sum == target`，则返回 `[nums[left], nums[right]]`。

## 代码

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return nums[left], nums[right]
        return []
```

