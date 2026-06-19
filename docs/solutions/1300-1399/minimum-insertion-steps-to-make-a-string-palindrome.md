# [1312. 让字符串成为回文串的最少插入次数](https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/)

- 标签：字符串、动态规划
- 难度：困难

## 题目链接

- [1312. 让字符串成为回文串的最少插入次数 - 力扣](https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/)

## 题目大意

**描述**：给定一个字符串 $s$。可以在任意位置插入任意字符。

**要求**：返回使 $s$ 变为回文串所需的最少插入次数。

**说明**：
- $1 \le s.length \le 500$。

**示例**：

- 示例 1：

```python
输入：s = "zzazz"
输出：0
解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
```

- 示例 2：

```python
输入：s = "mbadm"
输出：2
解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
```


## 解题思路

### 思路 1：区间 DP

#### 1. 核心思想

$dp[i][j]$ 表示 $s[i:j]$ 变成回文串的最小插入次数。

- 如果 $s[i] == s[j]$，两端已匹配，$dp[i][j] = dp[i+1][j-1]$。
- 否则，可以在 $i$ 左侧插入一个 $s[j]$，或在 $j$ 右侧插入一个 $s[i]$，取最小值：$dp[i][j] = \min(dp[i+1][j], dp[i][j-1]) + 1$。

#### 2. 代码

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(n^2)$。
