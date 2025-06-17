# [LCR 079. 子集](https://leetcode.cn/problems/TVdhkn/)

- 标签：位运算、数组、回溯
- 难度：中等

## 题目链接

- [LCR 079. 子集 - 力扣](https://leetcode.cn/problems/TVdhkn/)

## 题目大意

给定一个整数数组 `nums`，数组中的元素互不相同。

要求：返回该数组所有可能的不重复子集。

## 解题思路

回溯算法，遍历数组 `nums`。为了使得子集不重复，每次遍历从当前位置的下一个位置进行下一层遍历。

## 代码

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(size, subset, index):
            res.append(subset)
            for i in range(index, size):
                backtrack(size, subset + [nums[i]], i + 1)

        size = len(nums)
        res = list()
        backtrack(size, [], 0)
        return res
```

