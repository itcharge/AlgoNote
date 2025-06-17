# [0392. 判断子序列](https://leetcode.cn/problems/is-subsequence/)

- 标签：双指针、字符串、动态规划
- 难度：简单

## 题目链接

- [0392. 判断子序列 - 力扣](https://leetcode.cn/problems/is-subsequence/)

## 题目大意

**描述**：给定字符串 $s$ 和 $t$。

**要求**：判断 $s$ 是否为 $t$ 的子序列。

**说明**：

- $0 \le s.length \le 100$。
- $0 \le t.length \le 10^4$。
- 两个字符串都只由小写字符组成。

**示例**：

- 示例 1：

```python
输入：s = "abc", t = "ahbgdc"
输出：True
```

- 示例 2：

```python
输入：s = "axc", t = "ahbgdc"
输出：False
```

## 解题思路

### 思路 1：双指针

使用两个指针 $i$、$j$ 分别指向字符串 $s$ 和 $t$，然后对两个字符串进行遍历。

- 遇到 $s[i] == t[j]$ 的情况，则 $i$ 向右移。
- 不断右移 $j$。
- 如果超过 $s$ 或 $t$ 的长度则跳出。
- 最后判断指针 $i$ 是否指向了 $s$ 的末尾，即：判断 $i$ 是否等于 $s$ 的长度。如果等于，则说明 $s$ 是 $t$ 的子序列，如果不等于，则不是。

### 思路 1：代码

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        i, j = 0, 0
        while i < size_s and j < size_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == size_s
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$、$m$ 分别为字符串 $s$、$t$ 的长度。
- **空间复杂度**：$O(1)$。

