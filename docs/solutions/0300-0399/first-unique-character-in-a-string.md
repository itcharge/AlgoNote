# [0387. 字符串中的第一个唯一字符](https://leetcode.cn/problems/first-unique-character-in-a-string/)

- 标签：队列、哈希表、字符串、计数
- 难度：简单

## 题目链接

- [0387. 字符串中的第一个唯一字符 - 力扣](https://leetcode.cn/problems/first-unique-character-in-a-string/)

## 题目大意

给定一个只包含小写字母的字符串 `s`。

要求：找到第一个不重复的字符，并返回它的索引。

## 解题思路

遍历字符串，使用哈希表存储字符串中每个字符的出现次数。然后第二次遍历时，找出只出现一次的字符。

## 代码

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        strDict = dict()
        for i in range(len(s)):
            if s[i] in strDict:
                strDict[s[i]] += 1
            else:
                strDict[s[i]] = 1

        for i in range(len(s)):
            if s[i] in strDict and strDict[s[i]] == 1:
                return i
        return -1
```

- 思路 2 代码：
