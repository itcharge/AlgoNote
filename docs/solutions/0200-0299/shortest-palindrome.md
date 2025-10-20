# [0214. 最短回文串](https://leetcode.cn/problems/shortest-palindrome/)

- 标签：字符串、字符串匹配、哈希函数、滚动哈希
- 难度：困难

## 题目链接

- [0214. 最短回文串 - 力扣](https://leetcode.cn/problems/shortest-palindrome/)

## 题目大意

**描述**：

给定一个字符串 $s$，你可以通过在字符串前面添加字符将其转换为回文串。

**要求**：

找到并返回可以用这种方式转换的最短回文串。

**说明**：

- $0 \le s.length \le 5 \times 10^{4}$。
- s 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "aacecaaa"
输出："aaacecaaa"
```

- 示例 2：

```python
输入：s = "abcd"
输出："dcbabcd"
```

## 解题思路

### 思路 1：KMP 算法

这道题的关键在于找到字符串 $s$ 的最长回文前缀。如果我们能找到字符串 $s$ 的最长回文前缀，那么剩余部分的反转就是我们需要添加的前缀。

具体思路如下：

1. **构造新字符串**：将字符串 $s$ 和其反转字符串 $s'$ 用特殊字符连接，构造新字符串 `pattern = s + '\#' + s'`。
2. **使用 KMP 算法**：对新字符串 $pattern$ 计算 next 数组，找到最长公共前后缀。
3. **找到最长回文前缀**：next 数组的最后一个值 $next[len-1]$ 就是字符串 $s$ 的最长回文前缀长度。
4. **构造结果**：将 $s$ 中非回文前缀部分反转后添加到 $s$ 前面。

算法步骤：
- 设字符串 $s$ 的长度为 $n$，最长回文前缀长度为 $k$。
- 需要添加的字符为 $s[n-1:n-k-1:-1]$（即从第 $n-k-1$ 个字符到第 $n-1$ 个字符的反转）。
- 最终结果为 $s[n-1:n-k-1:-1] + s$。

### 思路 1：代码

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # 构造新字符串：s + '#' + s的反转
        reversed_s = s[::-1]
        pattern = s + '#' + reversed_s
        
        # 计算 next 数组（KMP 算法）
        n = len(pattern)
        next_array = [0] * n
        
        # 计算 next 数组
        for i in range(1, n):
            j = next_array[i - 1]
            # 如果不匹配，回退到前一个匹配位置
            while j > 0 and pattern[i] != pattern[j]:
                j = next_array[j - 1]
            # 如果匹配，next 值加 1
            if pattern[i] == pattern[j]:
                j += 1
            next_array[i] = j
        
        # next_array[n-1] 就是 s 的最长回文前缀长度
        max_palindrome_length = next_array[n - 1]
        
        # 构造最短回文串
        # 将非回文前缀部分反转后添加到前面
        return s[max_palindrome_length:][::-1] + s
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串 $s$ 的长度。KMP 算法计算 $next$ 数组的时间复杂度为 $O(n)$。
- **空间复杂度**：$O(n)$，需要额外的 $O(n)$ 空间存储 $next$ 数组和构造的新字符串。
