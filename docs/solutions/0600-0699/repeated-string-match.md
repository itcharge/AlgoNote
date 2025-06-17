# [0686. 重复叠加字符串匹配](https://leetcode.cn/problems/repeated-string-match/)

- 标签：字符串、字符串匹配
- 难度：中等

## 题目链接

- [0686. 重复叠加字符串匹配 - 力扣](https://leetcode.cn/problems/repeated-string-match/)

## 题目大意

**描述**：给定两个字符串 `a` 和 `b`。

**要求**：寻找重复叠加字符串 `a` 的最小次数，使得字符串 `b` 成为叠加后的字符串 `a` 的子串，如果不存在则返回 `-1`。

**说明**：

- 字符串 `"abc"` 重复叠加 `0` 次是 `""`，重复叠加 `1` 次是 `"abc"`，重复叠加 `2` 次是 `"abcabc"`。
- $1 \le a.length \le 10^4$。
- $1 \le b.length \le 10^4$。
- `a` 和 `b` 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：a = "abcd", b = "cdabcdab"
输出：3
解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
```

- 示例 2：

```python
输入：a = "a", b = "aa"
输出：2
```

## 解题思路

### 思路 1：KMP 算法

假设字符串 `a` 的长度为 `n`，`b` 的长度为 `m`。

把 `b` 看做是模式串，把字符串 `a` 叠加后的字符串看做是文本串，这道题就变成了单模式串匹配问题。

我们可以模拟叠加字符串 `a` 后进行单模式串匹配问题。模拟叠加字符串可以通过在遍历字符串匹配时对字符串 `a` 的长度 `n` 取余来实现。

那么问题关键点就变为了如何高效的进行单模式串匹配，以及字符串循环匹配的退出条件是什么。

**单模式串匹配问题**：可以用 KMP 算法来做。

**循环匹配退出条件问题**：假设我们用 `i` 遍历 `a` 叠加后字符串，用 `j` 遍历字符串 `b`。如果字符串 `b` 是 `a` 叠加后字符串的子串，那么 `b` 有两种可能：

1. `b` 直接是原字符串 `a` 的子串：这种情况下，最多遍历到 `len(a)`。
2. `b` 是 `a` 叠加后的字符串的子串：
   1. 最多遍历到 `len(a) + len(b)`，可以写为 `while i < len(a) + len(b):`，当 `i == len(a) + len(b)` 时跳出循环。
   2. 也可以写为 `while i - j < len(a):`，这种写法中 `i - j ` 表示的是字符匹配开始的位置，如果匹配到 `len(a)` 时（即 `i - j == len(a)` 时）最开始位置的字符仍没有匹配，那么 `b` 也不可能是 `a` 叠加后的字符串的子串了，此时跳出循环。

最后我们需要计算一下重复叠加字符串 `a` 的最小次数。假设 `index` 使我们求出的匹配位置。

1. 如果 `index == -1`，则说明 `b` 不可能是 `a` 叠加后的字符串的子串，返回 `False`。
2. 如果 `len(a) - index >= len(b)`，则说明匹配位置未超过字符串 `a` 的长度，叠加 `1` 次（字符串 `a` 本身）就可以匹配。
3. 如果 `len(a) - index < len(b)`，则说明需要叠加才能匹配。此时最小叠加次数为 $\lfloor \frac{index + len(b) - 1}{len(a)} \rfloor + 1$。其中 `index`  代笔匹配开始前的字符串长度，加上 `len(b)` 后就是匹配到字符串 `b` 结束时最少需要的字符数，再 `-1` 是为了向下取整。 除以 `len(a)` 表示至少需要几个 `a`， 因为是向下取整，所以最后要加上 `1`。写成代码就是：`(index + len(b) - 1) // len(a) + 1`。

### 思路 1：代码

```python
class Solution:
    # KMP 匹配算法，T 为文本串，p 为模式串
    def kmp(self, T: str, p: str) -> int:
        n, m = len(T), len(p)

        next = self.generateNext(p)

        i, j = 0, 0
        while i - j < n:
            while j > 0 and T[i % n] != p[j]:
                j = next[j - 1]
            if T[i % n] == p[j]:
                j += 1
            if j == m:
                return i - m + 1
            i += 1
        return -1

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

    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)
        index = self.kmp(a, b)
        if index == -1:
            return -1
        if len_a - index >= len_b:
            return 1
        return (index + len(b) - 1) // len(a) + 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中文本串 $a$ 的长度为 $n$，模式串 $b$ 的长度为 $m$。
- **空间复杂度**：$O(m)$。

