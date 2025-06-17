# [1763. 最长的美好子字符串](https://leetcode.cn/problems/longest-nice-substring/)

- 标签：位运算、哈希表、字符串、分治、滑动窗口
- 难度：简单

## 题目链接

- [1763. 最长的美好子字符串 - 力扣](https://leetcode.cn/problems/longest-nice-substring/)

## 题目大意

**描述**： 给定一个字符串 $s$。

**要求**：返回 $s$ 最长的美好子字符串。 

**说明**：

- **美好字符串**：当一个字符串 $s$ 包含的每一种字母的大写和小写形式同时出现在 $s$ 中，就称这个字符串 $s$ 是美好字符串。
- $1 \le s.length \le 100$。

**示例**：

- 示例 1：

```python
输入：s = "YazaAay"
输出："aAa"
解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
"aAa" 是最长的美好子字符串。
```

- 示例 2：

```python
输入：s = "Bb"
输出："Bb"
解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。
```

## 解题思路

### 思路 1：枚举

字符串 $s$ 的范围为 $[1, 100]$，长度较小，我们可以枚举所有的子串，判断该子串是否为美好字符串。

由于大小写英文字母各有 $26$ 位，则我们可以利用二进制来标记某字符是否在子串中出现过，我们使用 $lower$ 标记子串中出现过的小写字母，使用 $upper$ 标记子串中出现过的大写字母。如果满足 $lower == upper$，则说明该子串为美好字符串。

具体解法步骤如下：

1. 使用二重循环遍历字符串。对于子串 $s[i]…s[j]$，使用 $lower$ 标记子串中出现过的小写字母，使用 $upper$ 标记子串中出现过的大写字母。
2. 如果 $s[j]$ 为小写字母，则 $lower$ 对应位置标记为出现过该小写字母，即：`lower |= 1 << (ord(s[j]) - ord('a'))`。
3. 如果 $s[j]$ 为大写字母，则 $upper$ 对应位置标记为出现过该小写字母，即：`upper |= 1 << (ord(s[j]) - ord('A'))`。
4. 判断当前子串对应 $lower$ 和 $upper$ 是否相等，如果相等，并且子串长度大于记录的最长美好字符串长度，则更新最长美好字符串长度。
5. 遍历完返回记录的最长美好字符串长度。

### 思路 1：代码

```Python
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        size = len(s)
        max_pos, max_len = 0, 0
        for i in range(size):
            lower, upper = 0, 0
            for j in range(i, size):
                if s[j].islower():
                    lower |= 1 << (ord(s[j]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[j]) - ord('A'))
                if lower == upper and j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_pos = i
        return s[max_pos: max_pos + max_len]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为字符串 $s$ 的长度。
- **空间复杂度**：$O(1)$。

