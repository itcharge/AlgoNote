# [LCR 032. 有效的字母异位词](https://leetcode.cn/problems/dKk3P7/)

- 标签：哈希表、字符串、排序
- 难度：简单

## 题目链接

- [LCR 032. 有效的字母异位词 - 力扣](https://leetcode.cn/problems/dKk3P7/)

## 题目大意

给定两个字符串 `s` 和 `t`。

要求：判断 `t` 和 `s` 是否使用了相同的字符构成（字符出现的种类和数目都相同，字符顺序不完全相同）。

## 解题思路

1. 先判断字符串 `s` 和 `t` 的长度，不一样直接返回 `False`；
2. 如果 `s` 和 `t` 相等，则直接返回 `False`，因为变位词的字符顺序不完全相同；
3. 分别遍历字符串 `s` 和 `t`。先遍历字符串 `s`，用哈希表存储字符串 `s` 中字符出现的频次；
4. 再遍历字符串 `t`，哈希表中减去对应字符的频次，出现频次小于 `0` 则输出 `False`；
5. 如果没出现频次小于 `0`，则输出 `True`。

## 代码

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == t:
            return False
        strDict = dict()
        for ch in s:
            if ch in strDict:
                strDict[ch] += 1
            else:
                strDict[ch] = 1
        for ch in t:
            if ch in strDict:
                strDict[ch] -= 1
                if strDict[ch] < 0:
                    return False
            else:
                return False
        return True
```

