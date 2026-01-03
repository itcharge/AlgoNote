# [0730. 统计不同回文子序列](https://leetcode.cn/problems/count-different-palindromic-subsequences/)

- 标签：字符串、动态规划
- 难度：困难

## 题目链接

- [0730. 统计不同回文子序列 - 力扣](https://leetcode.cn/problems/count-different-palindromic-subsequences/)

## 题目大意

**描述**：

给定一个字符串 $s$。

**要求**：

返回 $s$ 中不同的非空回文子序列个数 。由于答案可能很大，请返回对 $10^9 + 7$ 取余的结果。

**说明**：

- 字符串的子序列可以经由字符串删除 $0$ 个或多个字符获得。
- 如果一个序列与它反转后的序列一致，那么它是回文序列。
- 如果存在某个 $i$，满足 $ai \ne bi$，则两个序列 $a1, a2, ...$ 和 $b1, b2, ...$ 不同。
- $1 \le s.length \le 10^{3}$。
- $s[i]$ 仅包含 `'a'`, `'b'`, `'c'` 或 `'d'`。

**示例**：

- 示例 1：

```python
输入：s = 'bccb'
输出：6
解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
```

- 示例 2：

```python
输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：共有 3104860382 个不同的非空回文子序列，104860361 是对 109 + 7 取余后的值。
```

## 解题思路

### 思路 1：区间动态规划

这道题要求统计不同的回文子序列个数。可以使用区间动态规划来解决。

**状态定义**：

- 定义 $dp[i][j]$ 表示字符串 $s[i:j+1]$ 中不同回文子序列的个数。

**状态转移**：

- 如果 $s[i] \neq s[j]$，则 $dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]$。
  - 减去 $dp[i+1][j-1]$ 是因为它被重复计算了。
- 如果 $s[i] = s[j]$，需要考虑更复杂的情况：
  - 在 $s[i+1:j]$ 中找到第一个和最后一个与 $s[i]$ 相同的字符位置 $left$ 和 $right$。
  - 如果 $left > right$：说明中间没有相同字符，$dp[i][j] = dp[i+1][j-1] \times 2 + 2$。
  - 如果 $left = right$：说明中间只有一个相同字符，$dp[i][j] = dp[i+1][j-1] \times 2 + 1$。
  - 如果 $left < right$：说明中间有多个相同字符，$dp[i][j] = dp[i+1][j-1] \times 2 - dp[left+1][right-1]$。

### 思路 1：代码

```python
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(n)]
        
        # 初始化：单个字符是一个回文子序列
        for i in range(n):
            dp[i][i] = 1
        
        # 按区间长度从小到大遍历
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    # 在 s[i+1:j] 中找第一个和最后一个与 s[i] 相同的字符
                    left = i + 1
                    right = j - 1
                    
                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[i]:
                        right -= 1
                    
                    if left > right:
                        # 中间没有相同字符
                        dp[i][j] = (dp[i + 1][j - 1] * 2 + 2) % MOD
                    elif left == right:
                        # 中间只有一个相同字符
                        dp[i][j] = (dp[i + 1][j - 1] * 2 + 1) % MOD
                    else:
                        # 中间有多个相同字符
                        dp[i][j] = (dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]) % MOD
                else:
                    # s[i] != s[j]
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
        
        return (dp[0][n - 1] + MOD) % MOD
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是字符串 $s$ 的长度。需要填充 $O(n^2)$ 个状态，每个状态的计算时间为 $O(1)$ 到 $O(n)$。
- **空间复杂度**：$O(n^2)$。需要存储 $dp$ 数组。
