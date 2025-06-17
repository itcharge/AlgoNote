# [1930. 长度为 3 的不同回文子序列](https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/)

- 标签：哈希表、字符串、前缀和
- 难度：中等

## 题目链接

- [1930. 长度为 3 的不同回文子序列 - 力扣](https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/)

## 题目大意

**描述**：给定一个人字符串 $s$。

**要求**：返回 $s$ 中长度为 $s$ 的不同回文子序列的个数。即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。

**说明**：

- **回文**：指正着读和反着读一样的字符串。
- **子序列**：由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。
  - 例如，`"ace"` 是 `"abcde"` 的一个子序列。

- $3 \le s.length \le 10^5$。
- $s$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "aabca"
输出：3
解释：长度为 3 的 3 个回文子序列分别是：
- "aba" ("aabca" 的子序列)
- "aaa" ("aabca" 的子序列)
- "aca" ("aabca" 的子序列)
```

- 示例 2：

```python
输入：s = "bbcbaba"
输出：4
解释：长度为 3 的 4 个回文子序列分别是：
- "bbb" ("bbcbaba" 的子序列)
- "bcb" ("bbcbaba" 的子序列)
- "bab" ("bbcbaba" 的子序列)
- "aba" ("bbcbaba" 的子序列)
```

## 解题思路

### 思路 1：枚举 + 哈希表

字符集只包含 $26$ 个小写字母，所以我们可以枚举这 $26$ 个小写字母。

对于每个小写字母，使用对撞双指针，找到字符串 $s$ 首尾两侧与小写字母相同的最左位置和最右位置。

如果两个位置不同，则我们可以将两个位置中间不重复的字符当作是长度为 $3$ 的子序列最中间的那个字符。

则我们可以统计出两个位置中间不重复字符的个数，将其累加到答案中。

遍历完，返回答案。

### 思路 1：代码

```Python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        size = len(s)
        ans = 0

        for i in range(26):
            left, right = 0, size - 1
            
            while left < size and ord(s[left]) - ord('a') != i:
                left += 1
            
            while right >= 0 and ord(s[right]) - ord('a') != i:
                right -= 1

            if right - left < 2:
                continue

            char_set = set()
            for j in range(left + 1, right):
                char_set.add(s[j])
            ans += len(char_set)
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$n \times | \sum | + | \sum |^2$，其中 $n$ 为字符串 $s$ 的长度，$\sum$ 为字符集，本题中 $| \sum | = 26$。
- **空间复杂度**：$O(| \sum |)$。
