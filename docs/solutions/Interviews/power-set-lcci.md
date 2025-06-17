# [面试题 08.04. 幂集](https://leetcode.cn/problems/power-set-lcci/)

- 标签：位运算、数组、回溯
- 难度：中等

## 题目链接

- [面试题 08.04. 幂集 - 力扣](https://leetcode.cn/problems/power-set-lcci/)

## 题目大意

给定一个集合 `nums`，集合中不包含重复元素。

压枪欧秋：返回该集合的所有子集。

## 解题思路

回溯算法，遍历集合 `nums`。为了使得子集不重复，每次遍历从当前位置的下一个位置进行下一层遍历。

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

