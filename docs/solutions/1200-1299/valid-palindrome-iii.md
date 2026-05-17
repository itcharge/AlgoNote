# [1216. 验证回文串 III](https://leetcode.cn/problems/valid-palindrome-iii/)

- 标签：字符串、动态规划
- 难度：困难

## 题目链接

- [1216. 验证回文串 III - 力扣](https://leetcode.cn/problems/valid-palindrome-iii/)

## 题目大意

**描述**：给定一个字符串 $s$ 和一个整数 $k$。

**要求**：判断是否可以通过删除最多 $k$ 个字符，使得剩下的字符串是回文串。

**说明**：

- $1 \le s.length \le 1000$。
- $0 \le k \le s.length$。

**示例**：

- 示例 1：

```python
输入：s = "abcdeca", k = 2
输出：true
解释：删除 'b' 和 'e' 得到 "acdca"。
```

- 示例 2：

```python
输入：s = "abbababa", k = 1
输出：true
```

## 解题思路

### 思路 1：动态规划（最长回文子序列）

#### 1. 核心思想

删除字符使字符串变为回文串，等价于找到字符串中最长的回文子序列（LPS，Longest Palindromic Subsequence）。如果 $s$ 的长度减去 LPS 的长度 $\le k$，说明可以做到。

所以问题转化为：**计算字符串 $s$ 的最长回文子序列的长度**。

#### 2. 阶段划分

区间 DP，按区间长度从小到大计算。

#### 3. 定义状态

$dp[i][j]$ 表示 $s[i:j]$（从 $i$ 到 $j$，包含两端）中最长回文子序列的长度。

#### 4. 状态转移方程

- 如果 $s[i] == s[j]$：两端字符相同，它们可以同时加入回文子序列中：
  $$dp[i][j] = dp[i+1][j-1] + 2$$
- 如果 $s[i] \ne s[j]$：两端字符不能同时选，取去掉一端后的较大值：
  $$dp[i][j] = \max(dp[i+1][j], dp[i][j-1])$$

#### 5. 初始条件

- $dp[i][i] = 1$（单个字符是长度为 $1$ 的回文子序列）。

#### 6. 最终结果

- 最长回文子序列长度 $lps = dp[0][n-1]$。
- 判断 $n - lps \le k$。

#### 7. 结合示例走一遍

$s = \text{"abcdeca"}, k = 2$

计算 $dp$：

- $dp[0][6]$：$a==a$ → $dp[1][5] + 2$
- $dp[1][5]$：$b \ne c$ → $\max(dp[2][5], dp[1][4])$
- ...（完整计算较复杂，这里省略中间步骤）

最终 $lps = dp[0][6] = 5$（最长回文子序列为 $\text{"acdca"}$）。

$n - lps = 7 - 5 = 2 \le k=2$ → $True$。

### 思路 1：代码

```python
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # 初始化：单字符回文长度为 1
        for i in range(n):
            dp[i][i] = 1

        # 区间 DP
        for length in range(2, n + 1):          # 区间长度
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        lps = dp[0][n - 1]
        return n - lps <= k
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是字符串长度。区间 DP 需要两层循环。
- **空间复杂度**：$O(n^2)$，需要 $dp$ 表。$n \le 1000$，$10^6$ 元素在可接受范围内。

### 思路 2：另一种 DP（直接求最少删除次数）

也可以直接定义 $dp[i][j]$ 为将 $s[i:j]$ 变为回文串需要的最少删除次数，转移类似。最终检查 $dp[0][n-1] \le k$。但思路 1（LPS）更经典，理解起来也更直观。
