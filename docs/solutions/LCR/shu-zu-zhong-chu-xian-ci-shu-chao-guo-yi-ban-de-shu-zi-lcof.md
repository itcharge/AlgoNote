# [LCR 158. 库存管理 II](https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)

- 标签：数组、哈希表、分治、计数、排序
- 难度：简单

## 题目链接

- [LCR 158. 库存管理 II - 力扣](https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)

## 题目大意

给定一个数组 `nums`，其中有一个数字出现次数超过数组长度一半。

要求：找到出现次数超过数组长度一半的数字。

## 解题思路

可以利用哈希表。遍历一遍数组 `nums`，用哈希表统计每个元素 `num` 出现的次数，再遍历一遍哈希表，找出元素个数最多的元素即可。

## 代码

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = dict()
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        max = 0
        max_index = -1
        for num in numDict:
            if numDict[num] > max:
                max = numDict[num]
                max_index = num
        return max_index
```

