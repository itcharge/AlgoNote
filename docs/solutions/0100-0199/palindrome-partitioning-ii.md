# [0132. 分割回文串 II](https://leetcode.cn/problems/palindrome-partitioning-ii/)

- 标签：字符串、动态规划
- 难度：困难

## 题目链接

- [0132. 分割回文串 II - 力扣](https://leetcode.cn/problems/palindrome-partitioning-ii/)

## 题目大意

**描述**：

给定一个字符串 $s$。

**要求**：

将 $s$ 分割成一些子串，使每个子串都是回文串。

返回符合要求的「最少分割次数」。


**说明**：

- $1 \le s.length \le 2000$。
- $s$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
```

- 示例 2：

```python
输入：s = "a"
输出：0
```

## 解题思路

### 思路 1：动态规划

这是一个典型的动态规划问题。我们需要找到将字符串分割成回文子串的最少分割次数。

**核心思想**：

1. **预处理回文信息**：使用动态规划预处理所有子串是否为回文，用 $is\_palindrome[i][j]$ 表示字符串 $s[i:j+1]$ 是否为回文。
2. **状态定义**：用 $dp[i]$ 表示字符串 $s[0:i+1]$ 的最少分割次数。
3. **状态转移**：对于位置 $i$，如果 $s[j:i+1]$ 是回文，则 $dp[i] = \min(dp[i], dp[j-1] + 1)$。

**算法步骤**：

1. **预处理回文判断**：
   - 单个字符都是回文：$is\_palindrome[i][i] = true$
   - 两个相邻字符：$is\_palindrome[i][i+1] = (s[i] == s[i+1])$
   - 长度大于2的子串：$is\_palindrome[i][j] = (s[i] == s[j]) \land is\_palindrome[i+1][j-1]$

2. **动态规划求解**：
   - 初始化：$dp[i] = i$（最坏情况，每个字符都单独分割）
   - 状态转移：$dp[i] = \min(dp[i], dp[j-1] + 1)$，其中 $j \le i$ 且 $s[j:i+1]$ 是回文

**关键点**：

- 使用二维数组预处理回文判断，避免重复计算。
- 状态转移时只需要考虑以当前位置结尾的回文子串。

### 思路 1：代码

```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # 预处理：判断所有子串是否为回文
        is_palindrome = [[False] * n for _ in range(n)]
        
        # 单个字符都是回文
        for i in range(n):
            is_palindrome[i][i] = True
        
        # 两个相邻字符
        for i in range(n - 1):
            is_palindrome[i][i + 1] = (s[i] == s[i + 1])
        
        # 长度大于2的子串
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = (s[i] == s[j]) and is_palindrome[i + 1][j - 1]
        
        # 动态规划求解最少分割次数
        dp = [0] * n
        
        for i in range(n):
            # 最坏情况：每个字符都单独分割
            dp[i] = i
            
            # 如果整个子串是回文，不需要分割
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                # 尝试所有可能的分割点
                for j in range(1, i + 1):
                    if is_palindrome[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        
        return dp[n - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是字符串长度。预处理回文判断需要 $O(n^2)$ 时间，动态规划求解也需要 $O(n^2)$ 时间。
- **空间复杂度**：$O(n^2)$，用于存储回文判断的二维数组和动态规划数组。
