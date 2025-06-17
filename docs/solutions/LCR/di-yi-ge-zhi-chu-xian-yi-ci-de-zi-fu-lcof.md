# [LCR 169. 招式拆解 II](https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)

- 标签：队列、哈希表、字符串、计数
- 难度：简单

## 题目链接

- [LCR 169. 招式拆解 II - 力扣](https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)

## 题目大意

给定一个字符串 `s`。

要求：从字符串 `s` 中找到第一个只出现一次的字符。如果没有，则返回空格 ` `。

## 解题思路

遍历字符串 `s`，使用哈希表存储每个字符频数。

再次遍历字符串 `s`，返回第一个频数为 `1` 的字符。

## 代码

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = dict()
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

        for ch in s:
            if ch in dic and dic[ch] == 1:
                return ch
        return ' '
```

