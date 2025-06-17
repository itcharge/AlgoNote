# [0290. 单词规律](https://leetcode.cn/problems/word-pattern/)

- 标签：哈希表、字符串
- 难度：简单

## 题目链接

- [0290. 单词规律 - 力扣](https://leetcode.cn/problems/word-pattern/)

## 题目大意

给定一种规律 `pattern` 和一个字符串 `str` ，判断 `str` 是否完全匹配相同的规律。

- 完全匹配相同的规律：pattern 的每个字母和字符串 str 中的每个非空单词之间存在这双向连接的对应规律。
- 比如：pattern = "abba", str = "dog cat cat dog"，其对应关系为：`a <=> dog，b <=> cat`

## 解题思路

这道题要求判断规律串中的字符与所给字符串中的非空单词，是否是一一对应的。即每个字符都能映射到对应的非空单词，每个非空单词也能映射为字符。

考虑使用两个哈希表，一个用来存储字符到非空单词的映射，另一个用来存储非空单词到字符的映射。

遍历 pattern 中的字符：

- 如果字符出现在第一个字典中，且字典中的值不等于对应的非空单词，则返回 False。
- 如果单词出现在第二个字典中，且字典中的值不等于对应的字符，则返回 False。

- 如果遍历完仍没发现不满足要求的情况，则返回 True。

## 代码

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = dict()
        word_dict = dict()
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            p = pattern[i]
            word = words[i]
            if p in pattern_dict and pattern_dict[p] != word:
                return False
            if word in word_dict and word_dict[word] != p:
                return False
            pattern_dict[p] = word
            word_dict[word] = p
        return True
```

