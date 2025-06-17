# [LCR 081. 组合总和](https://leetcode.cn/problems/Ygoe9J/)

- 标签：数组、回溯
- 难度：中等

## 题目链接

- [LCR 081. 组合总和 - 力扣](https://leetcode.cn/problems/Ygoe9J/)

## 题目大意

给定一个无重复元素的正整数数组 `candidates` 和一个正整数 `target`。

要求：找出 `candidates` 中所有可以使数字和为目标数 `target` 的唯一组合。

注意：数组 `candidates` 中的数字可以无限重复选取，且 `1 ≤ candidates[i] ≤ 200`。

## 解题思路

回溯算法，因为 `1 ≤ candidates[i] ≤ 200`，所以即便是 `candidates[i]` 值为 `1`，重复选取也会等于或大于 target，从而终止回溯。

建立两个数组 `res`、`path`。`res` 用于存放所有满足题意的组合，`path` 用于存放当前满足题意的一个组合。

定义回溯方法，`start_index = 1` 开始进行回溯。

- 如果 `sum > target`，则直接返回。
- 如果 `sum == target`，则将 `path` 中的元素加入到 `res` 数组中。
- 然后对 `[start_index, n]` 范围内的数进行遍历取值。
    - 如果 `sum + candidates[i] > target`，可以直接跳出循环。
    - 将和累积，即 `sum += candidates[i]`，然后将当前元素 `i` 加入 `path` 数组。
    - 递归遍历 `[start_index, n]` 上的数。
    - 加之前的和回退，即 `sum -= candidates[i]`，然后将遍历的 `i` 元素进行回退。
- 最终返回 `res` 数组。

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
            sum += candidates[i]
            self.path.append(candidates[i])
            self.backtrack(candidates, target, sum, i)
            sum -= candidates[i]
            self.path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res.clear()
        self.path.clear()
        candidates.sort()
        self.backtrack(candidates, target, 0, 0)
        return self.res
```

