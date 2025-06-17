# [LCR 068. 搜索插入位置](https://leetcode.cn/problems/N6YdxV/)

- 标签：数组、二分查找
- 难度：简单

## 题目链接

- [LCR 068. 搜索插入位置 - 力扣](https://leetcode.cn/problems/N6YdxV/)

## 题目大意

给定一个排好序的数组 `nums`，以及一个目标值 `target`。

要求：在数组中找到目标值，并返回下标。如果找不到，则返回目标值按顺序插入数组的位置。

## 解题思路

二分查找法。利用两个指针 `left` 和 `right`，分别指向数组首尾位置。每次用 `left` 和 `right` 中间位置上的元素值与目标值做比较，如果等于目标值，则返回当前位置。如果小于目标值，则更新 `left` 位置为 `mid + 1`，继续查找。如果大于目标值，则更新 `right` 位置为 `mid - 1`，继续查找。直到查找到目标值，或者 `left > right` 值时停止查找。然后返回 `left` 所在位置，即是代插入数组的位置。

## 代码

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

