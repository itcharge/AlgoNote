# [LCR 082. 组合总和 II](https://leetcode.cn/problems/4sjJUc/)

- 标签：数组、回溯
- 难度：中等

## 题目链接

- [LCR 082. 组合总和 II - 力扣](https://leetcode.cn/problems/4sjJUc/)

## 题目大意

给定一个数组 `candidates` 和一个目标数 `target`。

要求：找出 `candidates` 中所有可以使数字和为目标数 `target` 的组合。

数组 `candidates` 中的数字在每个组合中只能使用一次，且 `1 ≤ candidates[i] ≤ 50`。

## 解题思路

本题不能有重复组合，关键步骤在于去重。

在回溯遍历的时候，下一层递归的 `start_index` 要从当前节点的后一位开始遍历，即 `i + 1` 位开始。而且统一递归层不能使用相同的元素，即需要增加一句判断 `if i > start_index and candidates[i] == candidates[i - 1]: continue`。

## 代码

```python
class Solution:
    res = []
    path = []

    def backtrack(self, candidates: List[int], target: int, sum: int, start_index: int):
        if sum > target:
            return
        if sum == target:
            self.res.append(self.path[:])
            return

        for i in range(start_index, len(candidates)):
            if sum + candidates[i] > target:
                break
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
            sum += candidates[i]
            self.path.append(candidates[i])
            self.backtrack(candidates, target, sum, i + 1)
            sum -= candidates[i]
            self.path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res.clear()
        self.path.clear()
        candidates.sort()
        self.backtrack(candidates, target, 0, 0)
        return self.res
```

