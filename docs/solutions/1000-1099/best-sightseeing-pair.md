# [1014. 最佳观光组合](https://leetcode.cn/problems/best-sightseeing-pair/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [1014. 最佳观光组合 - 力扣](https://leetcode.cn/problems/best-sightseeing-pair/)

## 题目大意

给你一个正整数数组 `values`，其中 `values[i]` 表示第 `i` 个观光景点的评分，并且两个景点 `i` 和 `j` 之间的距离 为 `j - i`。一对景点（`i < j`）组成的观光组合的得分为 `values[i] + values[j] + i - j`，也就是景点的评分之和减去它们两者之间的距离。

要求：返回一对观光景点能取得的最高分。

## 解题思路

求解的是 `ans = max(values[i] + values[j] + i - j)`。对于当前第 `j` 个位置上的元素来说，`values[j] - j` 的值是固定的，求解 `ans` 就是在求解 `values[i] + i` 的最大值。我们使用一个变量 `max_score` 来存储当前第 `j` 个位置元素之前 `values[i] + i` 的最大值。然后遍历数组，求出每一个元素位置之前 `values[i] + i` 的最大值，并找出其中最大的 `ans`。

## 代码

```python
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        max_score = values[0]
        for i in range(1, len(values)):
            ans = max(ans, max_score + values[i] - i)
            max_score = max(max_score, values[i] + i)
        return ans
```
