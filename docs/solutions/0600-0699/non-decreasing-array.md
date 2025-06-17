# [0665. 非递减数列](https://leetcode.cn/problems/non-decreasing-array/)

- 标签：数组
- 难度：中等

## 题目链接

- [0665. 非递减数列 - 力扣](https://leetcode.cn/problems/non-decreasing-array/)

## 题目大意

给定一个整数数组 nums，问能否在最多改变 1 个元素的条件下，使数组变为非递减序列。若能，返回 True，不能则返回 False。

## 解题思路

循环遍历数组，寻找 nums[i] > nums[i+1] 的情况，一旦这种情况出现超过 2 次，则不可能最多改变 1 个元素，直接返回 False。

遇到 nums[i] > nums[i+1] 的情况，应该手动调节某位置上元素使数组有序。此时，有两种选择：

- 将 nums[i] 调低，与 nums[i-1] 持平
- 将 nums[i+1] 调高，与 nums[i] 持平

若选择第一种调节方式，如果调节前 nums[i-1] > nums[i+1]，那么调节完 nums[i] 之后，nums[i-1] 还是比 nums[i+1] 大，不可取。

所以应选择第二种调节方式，如果调节前 nums[i-1] > nums[i+1]，那么调节完 nums[i+1] 之后 nums[i-1] < nums[i] <= nums[i+1]，满足非递减要求。

最终如果最多调整过一次，且 nums[i] > nums[i+1] 的情况也最多出现过一次，则返回 True。

## 代码

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1:
                    return False
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]

        return True
```

