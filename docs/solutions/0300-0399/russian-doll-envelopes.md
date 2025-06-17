# [0354. 俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/)

- 标签：数组、二分查找、动态规划、排序
- 难度：困难

## 题目链接

- [0354. 俄罗斯套娃信封问题 - 力扣](https://leetcode.cn/problems/russian-doll-envelopes/)

## 题目大意

给定一个二维整数数组 envelopes 表示信封，其中 $envelopes[i] = [wi, hi]$，表示第 $i$ 个信封的宽度 $w_i$ 和高度 $h_i$。

当一个信封的宽度和高度比另一个信封大时，则小的信封可以放进大信封里，就像俄罗斯套娃一样。

现在要求：计算最多能有多少个信封组成一组「俄罗斯套娃」信封。

注意：不允许旋转信封（也就是说宽高不能互换）。

## 解题思路

如果最多有 k 个信封可以组成「俄罗斯套娃」信封。那么这 k 个信封按照宽高关系排序一定满足：

- $w_0 < w_1 < ... < w_{k-1}$
- $h_0 < h_1 < ... < h_{k-1}$

因为原二维数组是无序的，直接暴力搜素宽高升序序列并不容易。所以我们可以先固定一个维度，将其变为升序状态。再在另一个维度上进行选择。比如固定宽度为升序，则我们的问题就变为了：在高度这一维度下，求解数组的最长递增序列的长度。就变为了经典的「最长递增序列的长度问题」。即 [0300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)。

「最长递增序列的长度问题」的思路如下：

动态规划的状态 `dp[i]` 表示为：以第 i 个数字结尾的前 i 个元素中最长严格递增子序列的长度。

遍历前 i 个数字，`0 ≤ j ≤ i`：

- 当 `nums[j] < nums[i]` 时，`nums[i]` 可以接在 `nums[j]` 后面，此时以第 i 个数字结尾的最长严格递增子序列长度 + 1，即 `dp[i] = dp[j] + 1`。
- 当 `nums[j] ≥ nums[i]` 时，可以直接跳过。

则状态转移方程为：`dp[i] = max(dp[i], dp[j] + 1)`，`0 ≤ j ≤ i`，`nums[j] < nums[i]`。

最后再遍历一遍 dp 数组，求出最大值即可。

## 代码

```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        size = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = [1 for _ in range(size)]

        for i in range(size):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
```

