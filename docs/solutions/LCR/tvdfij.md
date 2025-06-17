# [LCR 012. 寻找数组的中心下标](https://leetcode.cn/problems/tvdfij/)

- 标签：数组、前缀和
- 难度：简单

## 题目链接

- [LCR 012. 寻找数组的中心下标 - 力扣](https://leetcode.cn/problems/tvdfij/)

## 题目大意

给定一个数组 `nums`。

要求：找到「左侧元素和」与「右侧元素和相等」的位置，若找不到，则返回 `-1`。

## 解题思路

两次遍历，第一次遍历先求出数组全部元素和。第二次遍历找到左侧元素和恰好为全部元素和一半的位置。

## 代码

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum * 2 + nums[i] == sum:
                return i
            curr_sum += nums[i]
        return -1
```

