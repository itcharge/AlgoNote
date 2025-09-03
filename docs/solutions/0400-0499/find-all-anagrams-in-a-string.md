# [0438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

- 标签：哈希表、字符串、滑动窗口
- 难度：中等

## 题目链接

- [0438. 找到字符串中所有字母异位词 - 力扣](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

## 题目大意

**描述**：给定两个字符串 $s$ 和 $p$。

**要求**：找到 $s$ 中所有 $p$ 的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

**说明**：

- **异位词**：指由相同字母重排列形成的字符串（包括相同的字符串）。
- $1 <= s.length, p.length <= 3 * 10^4$。
- $s$ 和 $p$ 仅包含小写字母。

**示例**：

- 示例 1：

```python
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
```

- 示例 2：

```python
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
```

## 解题思路

### 思路 1：滑动窗口

维护一个固定长度为 $len(p)$ 的滑动窗口。于是问题的难点变为了如何判断 $s$ 的子串和 $p$ 是异位词。可以使用两个字典来分别存储 $s$ 的子串中各个字符个数和 $p$ 中各个字符个数。如果两个字典对应的键值全相等，则说明 $s$ 的子串和 $p$ 是异位词。但是这样每一次比较的操作时间复杂度是 $O(n)$，我们可以通过在滑动数组中逐字符比较的方式来减少两个字典之间相互比较的复杂度，并用 $valid$ 记录经过验证的字符个数。整个算法步骤如下：

- 使用哈希表 $need$ 记录 $p$ 中各个字符出现次数。使用字典 $window$ 记录 $s$ 的子串中各个字符出现的次数。使用数组 $res$ 记录答案。使用 $valid$ 记录 $s$ 的子串中经过验证的字符个数。使用 $window\_size$ 表示窗口大小，值为 $len(p)$。使用两个指针 $left$、$right$。分别指向滑动窗口的左右边界。
- 一开始，$left$、$right$ 都指向 $0$。
- 如果 $s[right]$ 出现在 $need$ 中，将最右侧字符 $s[right]$ 加入当前窗口 $window$ 中，记录该字符个数。并验证该字符是否和 $need$ 中个对应字符个数相等。如果相等则验证的字符个数加 $1$，即 `valid += 1`。
- 如果该窗口字符长度大于等于 $window\_size$ 个，即 $right - left + 1 \ge window\_size$。则不断右移 $left$，缩小滑动窗口长度。
  - 如果验证字符个数 $valid$ 等于窗口长度 $window\_size$，则 $s[left, right + 1]$ 为 $p$ 的异位词，所以将 $left$ 加入到答案数组中。
  - 如果$s[left]$ 在 $need$ 中，则更新窗口中对应字符的个数，同时维护 $valid$ 值。
- 右移 $right$，直到 $right \ge len(nums)$ 结束。
- 输出答案数组 $res$。

### 思路 1：代码

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.defaultdict(int)
        for ch in p:
            need[ch] += 1

        window = collections.defaultdict(int)
        window_size = len(p)
        res = []
        left, right = 0, 0
        valid = 0
        while right < len(s):
            if s[right] in need:
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    valid += 1

            if right - left + 1 >= window_size:
                if valid == len(need):
                    res.append(left)
                if s[left] in need:
                    if window[s[left]] == need[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1
            right += 1
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m + |\sum|)$，其中 $n$、$m$ 分别为字符串 $s$、$p$ 的长度，$\sum$ 为字符集，本题中 $|\sum| = 26$。
- **空间复杂度**：$|\sum|$。

