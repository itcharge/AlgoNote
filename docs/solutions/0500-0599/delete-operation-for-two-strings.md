# [0583. 两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [0583. 两个字符串的删除操作 - 力扣](https://leetcode.cn/problems/delete-operation-for-two-strings/)

## 题目大意

给定两个单词 `word1` 和 `word2`，找到使得 `word1` 和 `word2` 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

## 解题思路

动态规划求解。

先定义状态 `dp[i][j]` 为以 `i - 1` 为结尾的字符串 `word1` 和以 `j - 1` 字结尾的字符串 `word2` 想要达到相等，所需要删除元素的最少次数。

然后确定状态转移方程。

- 如果 `word1[i - 1] == word2[j - 1]`，`dp[i][j]` 取源于以 `i - 2` 结尾结尾的字符串 `word1` 和以 `j - 1` 结尾的字符串 `word2`，即 `dp[i][j] = dp[i - 1][j - 1]`。
- 如果 `word1[i - 1] != word2[j - 1]`，`dp[i][j]` 取源于以下三种情况中的最小情况：
  - 删除 `word1[i - 1]`，最少操作次数为：`dp[i - 1][j] + 1`。
  - 删除 `word2[j - 1]`，最少操作次数为：`dp[i][j - 1] + 1`。
  - 同时删除 `word1[i - 1]`、`word2[j - 1]`，最少操作次数为 `dp[i - 1][j - 1] + 2`。

然后确定一下边界条件。

- 当 `word1` 为空字符串，以 `j - 1` 结尾的字符串 `word2` 要删除 `j` 个字符才能和 `word1` 相同，即 `dp[0][j] = j`。
- 当 `word2` 为空字符串，以 `i - 1` 结尾的字符串 `word1` 要删除 `i` 个字符才能和 `word2` 相同，即 `dp[i][0] = i`。

最后递推求解，最终输出 `dp[size1][size2]` 为答案。

## 代码

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        size1 = len(word1)
        size2 = len(word2)
        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]

        for i in range(size1 + 1):
            dp[i][0] = i
        for j in range(size2 + 1):
            dp[0][j] = j

        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        return dp[size1][size2]
```

