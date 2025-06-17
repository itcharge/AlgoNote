# [0491. 非递减子序列](https://leetcode.cn/problems/non-decreasing-subsequences/)

- 标签：位运算、数组、哈希表、回溯
- 难度：中等

## 题目链接

- [0491. 非递减子序列 - 力扣](https://leetcode.cn/problems/non-decreasing-subsequences/)

## 题目大意

给定一个整数数组 `nums`，找出并返回该数组的所有递增子序列，递增子序列的长度至少为 2。

## 解题思路

可以利用回溯算法求解。

建立两个数组 res、path。res 用于存放所有递增子序列，path 用于存放当前的递增子序列。

定义回溯方法，从 `start_index = 0` 的位置开始遍历。

- 如果当前子序列的长度大于等于 2，则将当前递增子序列添加到 res 数组中（注意：不用返回，因为还要继续向下查找）
- 对数组 `[start_index, len(nums) - 1]` 范围内的元素进行取值，判断当前元素是否在本层出现过。如果出现过则跳出循环。
  - 将 `nums[i]` 标记为使用过。
  - 将 `nums[i]` 加入到当前 path 中。
  - 继续从 `i + 1` 开发遍历下一节点。
  - 进行回退操作。
- 最终返回 res 数组。

## 代码

```python
class Solution:
    res = []
    path = []
    def backtrack(self, nums: List[int], start_index):
        if len(self.path) > 1:
            self.res.append(self.path[:])

        num_set = set()
        for i in range(start_index, len(nums)):
            if self.path and nums[i] < self.path[-1] or nums[i] in num_set:
                continue

            num_set.add(nums[i])
            self.path.append(nums[i])
            self.backtrack(nums, i + 1)
            self.path.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res.clear()
        self.path.clear()
        self.backtrack(nums, 0)
        return self.res
```

