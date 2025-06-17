# [1400. 构造 K 个回文字符串](https://leetcode.cn/problems/construct-k-palindrome-strings/)

- 标签：贪心、哈希表、字符串、计数
- 难度：中等

## 题目链接

- [1400. 构造 K 个回文字符串 - 力扣](https://leetcode.cn/problems/construct-k-palindrome-strings/)

## 题目大意

**描述**：给定一个字符串 $s$ 和一个整数 $k$。

**要求**：用 $s$ 字符串中所有字符构造 $k$ 个非空回文串。如果可以用 $s$ 中所有字符构造 $k$ 个回文字符串，那么请你返回 `True`，否则返回 `False`。

**说明**：

- $1 \le s.length \le 10^5$。
- $s$ 中所有字符都是小写英文字母。
- $1 \le k \le 10^5$。

**示例**：

- 示例 1：

```python
输入：s = "annabelle", k = 2
输出：True
解释：可以用 s 中所有字符构造 2 个回文字符串。
一些可行的构造方案包括："anna" + "elble"，"anbna" + "elle"，"anellena" + "b"
```

## 解题思路

### 思路 1：贪心算法

- 用字符串 $s$ 中所有字符构造回文串最多可以构造 $len(s)$ 个（将每个字符当做一个回文串）。所以如果 $len(s) < k$，则说明字符数量不够，无法构成 $k$ 个回文串，直接返回 `False`。
- 如果 $len(s) == k$，则可以直接使用单个字符构建回文串，直接返回 `True`。
- 如果 $len(s) > k$，则需要判断一下字符串 $s$ 中每个字符的个数。因为当字符是偶数个时，可以直接构造成回文串。所以我们只需要考虑个数为奇数的字符即可。如果个位为奇数的字符种类小于等于 $k$，则说明可以构造 $k$ 个回文串，返回 `True`。如果个位为奇数的字符种类大于 $k$，则说明无法构造 $k$ 个回文串，返回 `Fasle`。

### 思路 1：贪心算法代码

```python
import collections

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        size = len(s)
        if size < k:
            return False
        if size == k:
            return True
        letter_dict = dict()
        for i in range(size):
            if s[i] in letter_dict:
                letter_dict[s[i]] += 1
            else:
                letter_dict[s[i]] = 1

        odd = 0
        for key in letter_dict:
            if letter_dict[key] % 2 == 1:
               odd += 1
        return odd <= k
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + |\sum|)$，其中 $n$ 为字符串 $s$ 的长度，$\sum$ 是字符集，本题中 $|\sum| = 26$。
- **空间复杂度**：$O(|\sum|)$。
