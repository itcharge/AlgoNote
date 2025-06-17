# [1876. 长度为三且各字符不同的子字符串](https://leetcode.cn/problems/substrings-of-size-three-with-distinct-characters/)

- 标签：哈希表、字符串、计数、滑动窗口
- 难度：简单

## 题目链接

- [1876. 长度为三且各字符不同的子字符串 - 力扣](https://leetcode.cn/problems/substrings-of-size-three-with-distinct-characters/)

## 题目大意

**描述**：给定搞一个字符串 $s$。

**要求**：返回 $s$ 中长度为 $3$ 的好子字符串的数量。如果相同的好子字符串出现多次，则每一次都应该被记入答案之中。

**说明**：

- **子字符串**：指的是一个字符串中连续的字符序列。
- **好子字符串**：如果一个字符串中不含有任何重复字符，则称这个字符串为好子字符串。
- $1 \le s.length \le 100$。
- $s$ 只包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：s = "xyzzaz"
输出：1
解释：总共有 4 个长度为 3 的子字符串："xyz"，"yzz"，"zza" 和 "zaz" 。
唯一的长度为 3 的好子字符串是 "xyz" 。
```

- 示例 2：

```python
输入：s = "aababcabc"
输出：4
解释：总共有 7 个长度为 3 的子字符串："aab"，"aba"，"bab"，"abc"，"bca"，"cab" 和 "abc" 。
好子字符串包括 "abc"，"bca"，"cab" 和 "abc" 。
```

## 解题思路

### 思路 1：模拟

1. 遍历字符串 $s$ 中长度为 3 的子字符串。
2. 判断子字符串中的字符是否有重复。如果没有重复，则答案进行计数。
3. 遍历完输出答案。

### 思路 1：代码

```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(2, len(s)):
            if s[i - 2] != s[i - 1] and s[i - 1] != s[i] and s[i - 2] != s[i]:
                ans += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。