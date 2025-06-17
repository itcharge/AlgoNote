# [0058. 最后一个单词的长度](https://leetcode.cn/problems/length-of-last-word/)

- 标签：字符串
- 难度：简单

## 题目链接

- [0058. 最后一个单词的长度 - 力扣](https://leetcode.cn/problems/length-of-last-word/)

## 题目大意

给定一个字符串 s，返回字符串中最后一个单词长度。

- 「单词」：指仅由字母组成、不包含任何空格字符的最大子字符串。

## 解题思路

从字符串末尾开始逆序遍历，先过滤掉末尾空白字符，然后统计字符数量，直到遇到空格或到达字符串开始位置。

## 代码

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if ans == 0:
                    continue
                else:
                    return ans
            else:
                ans += 1
        return ans
```

