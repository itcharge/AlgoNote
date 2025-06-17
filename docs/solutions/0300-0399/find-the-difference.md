# [0389. 找不同](https://leetcode.cn/problems/find-the-difference/)

- 标签：位运算、哈希表、字符串、排序
- 难度：简单

## 题目链接

- [0389. 找不同 - 力扣](https://leetcode.cn/problems/find-the-difference/)

## 题目大意

给定两个只包含小写字母的字符串 s、t。字符串 t 是由 s 进行随机重拍之后，再在随机位置添加一个字母得到的。要求：找出字符串 t 中被添加的字母。

## 解题思路

字符串 t 比字符串 s 多了一个随机字母。可以使用哈希表存储一下字符串 s 中各个字符的数量，再遍历一遍字符串 t 中的字符，从哈希表中减去对应数量的字符，最后剩的那一个字符就是多余的字符。

## 代码

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = dict()
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1

        for ch in t:
            if ch in s_dict and s_dict[ch] != 0:
                s_dict[ch] -= 1
            else:
                return ch
```

