# [LCR 120. 寻找文件副本](https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

- 标签：数组、哈希表、排序
- 难度：简单

## 题目链接

- [LCR 120. 寻找文件副本 - 力扣](https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

## 题目大意

给定一个包含 `n + 1` 个整数的数组 `nums`，里边包含的值都在 `1 ~ n` 之间。假设 `nums` 中只存在一个重复的整数，要求找出这个重复的数。

## 解题思路

使用哈希表存储数组每个元素，遇到重复元素则直接返回该元素。

## 代码

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                return num
            nums_dict[num] = 1
        return -1
```

