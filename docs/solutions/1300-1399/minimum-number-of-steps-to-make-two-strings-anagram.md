# [1347. 制造字母异位词的最小步骤数](https://leetcode.cn/problems/minimum-number-of-steps-to-make-two-strings-anagram/)

- 标签：哈希表、字符串、计数
- 难度：中等

## 题目链接

- [1347. 制造字母异位词的最小步骤数 - 力扣](https://leetcode.cn/problems/minimum-number-of-steps-to-make-two-strings-anagram/)

## 题目大意

**描述**：给定两个长度相等的字符串 $s$ 和 $t$。每一个步骤中，你可以选择将 $t$ 中任一个字符替换为另一个字符。

**要求**：返回使 $t$ 成为 $s$ 的字母异位词的最小步骤数。

**说明**：

- **字母异位词**：指字母相同，但排列不同（也可能相同）的字符串。
- $1 \le s.length \le 50000$。
- $s.length == t.length$。
- $s$ 和 $t$ 只包含小写英文字母。

**示例**：

- 示例 1：

```python
输出：s = "bab", t = "aba"
输出：1
提示：用 'b' 替换 t 中的第一个 'a'，t = "bba" 是 s 的一个字母异位词。
```

- 示例 2：

```python
输出：s = "leetcode", t = "practice"
输出：5
提示：用合适的字符替换 t 中的 'p', 'r', 'a', 'i' 和 'c'，使 t 变成 s 的字母异位词。
```

## 解题思路

### 思路 1：哈希表

题目要求使 $t$ 成为 $s$ 的字母异位词，则只需要 $t$ 和 $s$ 对应的每种字符数量相一致即可，无需考虑字符位置。

因为每一次转换都会减少一个字符，并增加另一个字符。

1. 我们使用两个哈希表 $cnts\underline{\hspace{0.5em}}s$、$cnts\underline{\hspace{0.5em}}t$ 分别对 $t$ 和 $s$ 中的字符进行计数，并求出两者的交集。
2. 遍历交集中的字符种类，以及对应的字符数量。
3. 对于当前字符 $key$，如果当前字符串 $s$ 中的字符 $key$ 的数量小于字符串 $t$ 中字符 $key$ 的数量，即 $cnts\underline{\hspace{0.5em}}s[key] < cnts\underline{\hspace{0.5em}}t[key]$。则 $s$ 中需要补齐的字符数量就是需要的最小步数，将其累加到答案中。
4.  遍历完返回答案。

### 思路 1：代码

```Python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnts_s, cnts_t = Counter(s), Counter(t)
        cnts = cnts_s | cnts_t

        ans = 0
        for key, cnt in cnts.items():
            if cnts_s[key] < cnts_t[key]:
                ans += cnts_t[key] - cnts_s[key]

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n)$，其中 $m$、$n$ 分别为字符串 $s$、$t$ 的长度。
- **空间复杂度**：$O(|\sum|)$，其中 $\sum$ 是字符集，本题中 $| \sum | = 26$。

