# [0516. 最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [0516. 最长回文子序列 - 力扣](https://leetcode.cn/problems/longest-palindromic-subsequence/)

## 题目大意

**描述**：给定一个字符串 $s$。

**要求**：找出其中最长的回文子序列，并返回该序列的长度。

**说明**：

- **子序列**：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
- $1 \le s.length \le 1000$。
- $s$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb"。
```

- 示例 2：

```python
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb"。
```

## 解题思路

### 思路 1：动态规划

###### 1. 划分阶段

按照区间长度进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 表示为：字符串 $s$ 在区间 $[i, j]$ 范围内的最长回文子序列长度。

###### 3. 状态转移方程

我们对区间 $[i, j]$ 边界位置上的字符 $s[i]$ 与 $s[j]$ 进行分类讨论：

1. 如果 $s[i] = s[j]$，则 $dp[i][j]$ 为区间 $[i + 1, j - 1]$ 范围内最长回文子序列长度 + $2$，即 $dp[i][j] = dp[i + 1][j - 1] + 2$。
2. 如果 $s[i] \ne s[j]$，则 $dp[i][j]$ 取决于以下两种情况，取其最大的一种：
	1. 加入 $s[i]$ 所能组成的最长回文子序列长度，即：$dp[i][j] = dp[i][j - 1]$。
	2. 加入 $s[j]$ 所能组成的最长回文子序列长度，即：$dp[i][j] = dp[i - 1][j]$。

则状态转移方程为：

$dp[i][j] = \begin{cases} max \lbrace dp[i + 1][j - 1] + 2 \rbrace & s[i] = s[j]  \cr max \lbrace dp[i][j - 1], dp[i - 1][j] \rbrace & s[i] \ne s[j] \end{cases}$

###### 4. 初始条件

- 单个字符的最长回文序列是 $1$，即 $dp[i][i] = 1$。

###### 5. 最终结果

由于 $dp[i][j]$ 依赖于 $dp[i + 1][j - 1]$、$dp[i + 1][j]$、$dp[i][j - 1]$，所以我们应该按照从下到上、从左到右的顺序进行遍历。

根据我们之前定义的状态，$dp[i][j]$ 表示为：字符串 $s$ 在区间 $[i, j]$ 范围内的最长回文子序列长度。所以最终结果为 $dp[0][size - 1]$。

### 思路 1：代码

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1

        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][size - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为字符串 $s$ 的长度。
- **空间复杂度**：$O(n^2)$。

