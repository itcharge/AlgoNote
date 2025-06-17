# [1941. 检查是否所有字符出现次数相同](https://leetcode.cn/problems/check-if-all-characters-have-equal-number-of-occurrences/)

- 标签：哈希表、字符串、计数
- 难度：简单

## 题目链接

- [1941. 检查是否所有字符出现次数相同 - 力扣](https://leetcode.cn/problems/check-if-all-characters-have-equal-number-of-occurrences/)

## 题目大意

**描述**：给定一个字符串 $s$。如果 $s$ 中出现过的所有字符的出现次数相同，那么我们称字符串 $s$ 是「好字符串」。

**要求**：如果 $s$ 是一个好字符串，则返回 `True`，否则返回 `False`。

**说明**：

- $1 \le s.length \le 1000$。
- $s$ 只包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：s = "abacbc"
输出：true
解释：s 中出现过的字符为 'a'，'b' 和 'c' 。s 中所有字符均出现 2 次。
```

- 示例 2：

```python
输入：s = "aaabb"
输出：false
解释：s 中出现过的字符为 'a' 和 'b' 。
'a' 出现了 3 次，'b' 出现了 2 次，两者出现次数不同。
```

## 解题思路

### 思路 1：哈希表

1. 使用哈希表记录字符串 $s$ 中每个字符的频数。
2. 然后遍历哈希表中的键值对，检测每个字符的频数是否相等。
3. 如果发现频数不相等，则直接返回 `False`。
4. 如果检查完发现所有频数都相等，则返回 `True`。

### 思路 1：代码

```python
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        flag = -1
        for key in counter:
            if flag == -1:
                flag = counter[key]
            else:
                if flag != counter[key]:
                    return False
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
