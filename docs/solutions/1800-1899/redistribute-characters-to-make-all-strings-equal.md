# [1897. 重新分配字符使所有字符串都相等](https://leetcode.cn/problems/redistribute-characters-to-make-all-strings-equal/)

- 标签：哈希表、字符串、计数
- 难度：简单

## 题目链接

- [1897. 重新分配字符使所有字符串都相等 - 力扣](https://leetcode.cn/problems/redistribute-characters-to-make-all-strings-equal/)

## 题目大意

**描述**：给定一个字符串数组 $words$（下标从 $0$ 开始计数）。

在一步操作中，需先选出两个 不同 下标 $i$ 和 $j$，其中 $words[i]$ 是一个非空字符串，接着将 $words[i]$ 中的任一字符移动到 $words[j]$ 中的 任一 位置上。

**要求**：如果执行任意步操作可以使 $words$ 中的每个字符串都相等，返回 $True$；否则，返回 $False$。

**说明**：

- $1 <= words.length <= 100$。
- $1 <= words[i].length <= 100$
- $words[i]$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：words = ["abc","aabc","bc"]
输出：true
解释：将 words[1] 中的第一个 'a' 移动到 words[2] 的最前面。
使 words[1] = "abc" 且 words[2] = "abc"。
所有字符串都等于 "abc" ，所以返回 True。
```

- 示例 2：

```python
输入：words = ["ab","a"]
输出：False
解释：执行操作无法使所有字符串都相等。
```

## 解题思路

### 思路 1：哈希表

如果通过重新分配字符能够使所有字符串都相等，则所有字符串的字符需要满足：

1. 每个字符串中字符种类相同，
2. 每个字符串中各种字符的个数相同。

则我们可以使用哈希表来统计字符串中字符种类及个数。具体步骤如下：

1. 遍历单词数组 $words$ 中的所有单词 $word$。
2. 遍历所有单词 $word$ 中的所有字符 $ch$。
3. 使用哈希表 $cnts$ 统计字符种类及个数。
4. 如果所有字符个数都是单词个数的倍数，则说明通过重新分配字符能够使所有字符串都相等，则返回 $True$。
5. 否则返回 $False$。

### 思路 1：代码

```Python
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        size = len(words)
        cnts = Counter()
        for word in words:
            for ch in word:
                cnts[ch] += 1

        return all(value % size == 0 for key, value in cnts.items())
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(s + |\sum|)$，其中 $s$ 为数组 $words$ 中所有单词的长度之和，$\sum$ 是字符集，本题中 $|\sum| = 26$。
- **空间复杂度**：$O(|\sum|)$。
