# [0459. 重复的子字符串](https://leetcode.cn/problems/repeated-substring-pattern/)

- 标签：字符串、字符串匹配
- 难度：简单

## 题目链接

- [0459. 重复的子字符串 - 力扣](https://leetcode.cn/problems/repeated-substring-pattern/)

## 题目大意

**描述**：给定一个非空的字符串 `s`。

**要求**：检查该字符串 `s` 是否可以通过由它的一个子串重复多次构成。

**说明**：

- $1 \le s.length \le 10^4$。
- `s` 由小写英文字母组成

**示例**：

- 示例 1：

```python
输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。
```

- 示例 2：

```python
输入: s = "aba"
输出: false
```

## 解题思路

### 思路 1：KMP 算法

这道题我们可以使用 KMP 算法的 `next` 数组来解决。我们知道 `next[j]` 表示的含义是：**记录下标 `j` 之前（包括 `j`）的模式串 `p` 中，最长相等前后缀的长度。**

而如果整个模式串 `p` 的最长相等前后缀长度不为 `0`，即 `next[len(p) - 1] != 0` ，则说明整个模式串 `p` 中有最长相同的前后缀，假设 `next[len(p) - 1] == k`，则说明 `p[0: k] == p[m - k: m]`。比如字符串 `"abcabcabc"`，最长相同前后缀为 `"abcabc" = "abcabc"`。

- 如果最长相等的前后缀是重叠的，比如之前的例子 `"abcabcabc"`。
  - 如果我们去除字符串中相同的前后缀的重叠部分，剩下两头前后缀部分（这两部分是相同的）。然后再去除剩余的后缀部分，只保留剩余的前缀部分。比如字符串 `"abcabcabc"` 去除重叠部分和剩余的后缀部分之后就是 `"abc"`。实际上这个部分就是字符串去除整个后缀部分的剩余部分。
  - 如果整个字符串可以通过子串重复构成的话，那么这部分就是最小周期的子串。
  - 我们只需要判断整个子串的长度是否是剩余部分长度的整数倍即可。也就是判断 `len(p) % (len(p) - next[size - 1]) == 0` 是否成立，如果成立，则字符串 `s` 可由 `s[0: len(p) - next[size - 1]]` 构成的子串重复构成，返回 `True`。否则返回 `False`。
- 如果最长相等的前后缀是不重叠的，那我们可将重叠部分视为长度为 `0` 的空串，则剩余的部分其实就是去除后缀部分的剩余部分，上述结论依旧成立。 

### 思路 1：代码

```python
class Solution:
    def generateNext(self, p: str):
        m = len(p)
        next = [0 for _ in range(m)]

        left = 0
        for right in range(1, m):
            while left > 0 and p[left] != p[right]:
                left = next[left - 1]
            if p[left] == p[right]:
                left += 1
            next[right] = left

        return next

    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        if size == 0:
            return False
        next = self.generateNext(s)
        if next[size - 1] != 0 and size % (size - next[size - 1]) == 0:
            return True
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m)$，其中模式串 $p$ 的长度为 $m$。
- **空间复杂度**：$O(m)$。

