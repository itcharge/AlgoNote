# [0266. 回文排列](https://leetcode.cn/problems/palindrome-permutation/)

- 标签：位运算、哈希表、字符串
- 难度：简单

## 题目链接

- [0266. 回文排列 - 力扣](https://leetcode.cn/problems/palindrome-permutation/)

## 题目大意

**描述**：

给定一个字符串 $s$。

**要求**：

如果该字符串的某个排列是「回文串」，则返回 $true$；否则，返回 $false$。

**说明**：

- $1 \le s.length \le 5000$。
- $s$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "code"
输出：false
```

- 示例 2：

```python
输入：s = "aab"
输出：true
```

## 解题思路

### 思路 1：

利用「字符出现次数的奇偶性」判断。记字符串长度为 $n$，字符集为小写字母（至多 $26$ 种）。一个字符串能被重排成回文，当且仅当至多有 $1$ 个字符的出现次数为奇数。

做法：用一个 $26$ 位的位掩码 `mask` 表示每个字符计数的奇偶性。遍历每个字符 $s[i]$：将对应位取反（异或 $1$），遍历完成后：

- 如果 `mask == 0`（所有字符出现偶数次），必然可以构成回文；
- 如果 `mask` 只有 $1$ 位为 $1$（即 $\text{popcount}(mask) = 1$），也可构成回文（该字符放在中间）；
- 否则不行。

### 思路 1：代码

```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 位掩码记录每个字符出现次数的奇偶性（仅小写字母）
        mask = 0
        base = ord('a')
        for ch in s:
            bit = 1 << (ord(ch) - base)
            mask ^= bit  # 对应位取反：出现一次翻转一次

        # 条件：至多 1 位为 1（允许 0 位）
        return mask == 0 or (mask & (mask - 1)) == 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。单次遍历字符串，每个字符 $O(1)$ 更新位掩码。
- **空间复杂度**：$O(1)$。仅常数级变量，与 $n$ 和字符集大小无关（字符集固定为 $26$）。
