# [1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [1143. 最长公共子序列 - 力扣](https://leetcode.cn/problems/longest-common-subsequence/)

## 题目大意

**描述**：给定两个字符串 $text1$ 和 $text2$。

**要求**：返回两个字符串的最长公共子序列的长度。如果不存在公共子序列，则返回 $0$。

**说明**：

- **子序列**：原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
- **公共子序列**：两个字符串所共同拥有的子序列。
- $1 \le text1.length, text2.length \le 1000$。
- $text1$ 和 $text2$ 仅由小写英文字符组成。

**示例**：

- 示例 1：

```python
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。
```

- 示例 2：

```python
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
```

## 解题思路

### 思路 1：动态规划

###### 1. 阶段划分

按照两个字符串的结尾位置进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 表示为：「以 $text1$ 中前 $i$ 个元素组成的子字符串 $str1$ 」与「以 $text2$ 中前 $j$ 个元素组成的子字符串 $str2$」的最长公共子序列长度为 $dp[i][j]$。

###### 3. 状态转移方程

双重循环遍历字符串 $text1$ 和 $text2$，则状态转移方程为：

1. 如果 $text1[i - 1] = text2[j - 1]$，说明两个子字符串的最后一位是相同的，所以最长公共子序列长度加 $1$。即：$dp[i][j] = dp[i - 1][j - 1] + 1$。
2. 如果 $text1[i - 1] \ne text2[j - 1]$，说明两个子字符串的最后一位是不同的，则 $dp[i][j]$ 需要考虑以下两种情况，取两种情况中最大的那种：$dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])$。
	1. 「以 $text1$ 中前 $i - 1$ 个元素组成的子字符串 $str1$ 」与「以 $text2$ 中前 $j$ 个元素组成的子字符串 $str2$」的最长公共子序列长度，即 $dp[i - 1][j]$。
	2. 「以 $text1$ 中前 $i$ 个元素组成的子字符串 $str1$ 」与「以 $text2$ 中前 $j - 1$ 个元素组成的子字符串 $str2$」的最长公共子序列长度，即 $dp[i][j - 1]$。

###### 4. 初始条件

1. 当 $i = 0$ 时，$str1$ 表示的是空串，空串与 $str2$ 的最长公共子序列长度为 $0$，即 $dp[0][j] = 0$。
2. 当 $j = 0$ 时，$str2$ 表示的是空串，$str1$ 与 空串的最长公共子序列长度为 $0$，即 $dp[i][0] = 0$。

###### 5. 最终结果

根据状态定义，最后输出 $dp[sise1][size2]$（即 $text1$ 与 $text2$ 的最长公共子序列长度）即可，其中 $size1$、$size2$ 分别为 $text1$、$text2$ 的字符串长度。

### 思路 1：代码

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

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$、$m$ 分别是字符串 $text1$、$text2$ 的长度。两重循环遍历的时间复杂度是 $O(n \times m)$，所以总的时间复杂度为 $O(n \times m)$。
- **空间复杂度**：$O(n \times m)$。用到了二维数组保存状态，所以总体空间复杂度为 $O(n \times m)$。

