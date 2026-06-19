# [1392. 最长快乐前缀](https://leetcode.cn/problems/longest-happy-prefix/)

- 标签：字符串、字符串匹配、哈希函数、滚动哈希
- 难度：困难

## 题目链接

- [1392. 最长快乐前缀 - 力扣](https://leetcode.cn/problems/longest-happy-prefix/)

## 题目大意

**描述**：给定一个字符串 $s$。快乐前缀是既是前缀又是后缀（不包括自身）的子串。

**要求**：返回最长的快乐前缀。

**说明**：
- $1 \le s.length \le 10^5$。

**示例**：

- 示例 1：

```python
输入：s = "level"
输出："l"
解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel", "evel"）。最长的既是前缀也是后缀的字符串是 "l" 。
```

- 示例 2：

```python
输入：s = "ababab"
输出："abab"
解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
```


## 解题思路

### 思路 1：KMP 前缀函数

#### 1. 核心思想

KMP 的前缀函数 $\pi[i]$ 表示 $s[0:i]$ 的最长相等真前后缀长度。其中 $\pi[n-1]$ 就是整个字符串的最长快乐前缀的长度。

#### 2. 具体步骤

**第 1 步**：计算 KMP 的 $\pi$ 数组。

**第 2 步**：返回 $s[0:\pi[n-1]]$。

### 思路 1：代码

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        return s[:pi[-1]]
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

### 思路 2：滚动哈希

也可以预计算前缀哈希，从大到小遍历长度 $len$，比较前缀和后缀的哈希值是否相等。但 KMP 更简洁。
