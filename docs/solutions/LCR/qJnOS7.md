# [LCR 095. 最长公共子序列](https://leetcode.cn/problems/qJnOS7/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [LCR 095. 最长公共子序列 - 力扣](https://leetcode.cn/problems/qJnOS7/)

## 题目大意

给定两个字符串 `text1` 和 `text2`。

要求：返回两个字符串的最长公共子序列的长度。如果不存在公共子序列，则返回 `0`。

- 子序列：原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
- 公共子序列：两个字符串所共同拥有的子序列。

## 解题思路

用动态规划来做。

动态规划的状态 `dp[i][j]` 表示为：前 `i` 个字符组成的字符串 `str1` 与前 `j` 个字符组成的字符串 `str2` 的最长公共子序列长度为 `dp[i][j]`。

遍历字符串 `text1` 和 `text2`，则状态转移方程为：

- 如果 `text1[i - 1] == text2[j - 1]`，则找到了一个公共元素，则 `dp[i][j] = dp[i - 1][j - 1] + 1`。
- 如果 `text1[i - 1] != text2[j - 1]`，则 `dp[i][j]` 需要考虑两种情况，取其中最大的那种：
    - `text1` 前 `i - 1` 个字符组成的字符串 `str1` 与 `text2` 前 `j` 个字符组成的 `str2` 的最长公共子序列长度，即 `dp[i - 1][j]`。
    - `text1` 前 `i` 个字符组成的字符串 `str1` 与 `text2` 前 `j - 1` 个字符组成的 `str2` 的最长公共子序列长度，即 `dp[i][j - 1]`。

最后输出 `dp[sise1][size2]` 即可，`size1`、`size2` 分别为 `text1`、`text2` 的字符串长度。

## 代码

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)
        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]
        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[size1][size2]
```

