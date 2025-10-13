# [LCR 006. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/kLl5u1/)

- 标签：数组、双指针、二分查找
- 难度：简单

## 题目链接

- [LCR 006. 两数之和 II - 输入有序数组 - 力扣](https://leetcode.cn/problems/kLl5u1/)

## 题目大意

给定一个升序数组：`numbers` 和一个目标值 `target`。

要求：从数组中找出满足相加之和等于 `target` 的两个数，并返回两个数在数组中下的标值。

## 解题思路

因为数组是有序的，所以我们可以使用两个指针 low，high。low 指向数组开始较小元素位置，high 指向数组较大元素位置。判断两个位置上的元素和，如果和等于目标值，则返回两个元素位置。如果和大于目标值，则 high 左移，继续检测。如果和小于目标值，则 low 右移，继续检测。直到 low 和 high 移动到相同位置停止检测。如果最终仍没找到，则返回 [0, 0]。

## 代码

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low, high]
            elif total < target:
                low += 1
            else:
                high -= 1
        return [0, 0]
```

