# [0712. 两个字符串的最小ASCII删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [0712. 两个字符串的最小ASCII删除和 - 力扣](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/)

## 题目大意

**描述**：

给定两个字符串 $s1$ 和 $s2$。

**要求**：

返回使两个字符串相等所需删除字符的 ASCII 值的最小。

**说明**：

- $0 \le s1.length, s2.length \le 10^{3}$。
- $s1$ 和 $s2$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
```

- 示例 2：

```python
输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
```

## 解题思路

### 思路 1：动态规划

这道题类似于最长公共子序列（LCS）问题，但要求的是删除字符的 ASCII 值之和最小。

**状态定义**：

- 定义 $dp[i][j]$ 表示使 $s1[0:i]$ 和 $s2[0:j]$ 相等所需删除字符的最小 ASCII 值之和。

**状态转移**：

- 如果 $s1[i-1] = s2[j-1]$，不需要删除，$dp[i][j] = dp[i-1][j-1]$。
- 如果 $s1[i-1] \neq s2[j-1]$，有两种选择：
  - 删除 $s1[i-1]$：$dp[i][j] = dp[i-1][j] + \text{ord}(s1[i-1])$。
  - 删除 $s2[j-1]$：$dp[i][j] = dp[i][j-1] + \text{ord}(s2[j-1])$。
  - 取两者的最小值。

**初始化**：

- $dp[0][0] = 0$。
- $dp[i][0] = \sum_{k=0}^{i-1} \text{ord}(s1[k])$，删除 $s1$ 的前 $i$ 个字符。
- $dp[0][j] = \sum_{k=0}^{j-1} \text{ord}(s2[k])$，删除 $s2$ 的前 $j$ 个字符。

### 思路 1：代码

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        # dp[i][j] 表示使 s1[0:i] 和 s2[0:j] 相等所需删除字符的最小 ASCII 值之和
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化：删除 s1 的前 i 个字符
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        
        # 初始化：删除 s2 的前 j 个字符
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        
        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    # 字符相同，不需要删除
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 字符不同，选择删除 s1[i-1] 或 s2[j-1]
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),  # 删除 s1[i-1]
                        dp[i][j - 1] + ord(s2[j - 1])   # 删除 s2[j-1]
                    )
        
        return dp[m][n]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$，其中 $m$ 和 $n$ 分别是字符串 $s1$ 和 $s2$ 的长度。
- **空间复杂度**：$O(m \times n)$。可以优化到 $O(\min(m, n))$。
