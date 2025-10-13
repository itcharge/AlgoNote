# [LCR 083. 全排列](https://leetcode.cn/problems/VvJkup/)

- 标签：数组、回溯
- 难度：中等

## 题目链接

- [LCR 083. 全排列 - 力扣](https://leetcode.cn/problems/VvJkup/)

## 题目大意

给定一个不含重复数字的数组 `nums` 。

要求：返回其有可能的全排列，可以按任意顺序返回。

## 解题思路

回溯算法递归遍历 `nums` 元素。同时使用 `visited` 数组来标记该元素在当前排列中是否被访问过。如果未被访问过则将其加入排列中，并在访问后将该元素变为未访问状态。

## 代码

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(size, arrange, index):
            if index == size:
                res.append(arrange)
                return
            for i in range(size):
                if visited[i] == True:
                    continue
                visited[i] = True
                backtrack(size, arrange + [nums[i]], index + 1)
                visited[i] = False

        size = len(nums)
        res = list()
        visited = [False for _ in range(size)]
        backtrack(size, [], 0)
        return res
```

