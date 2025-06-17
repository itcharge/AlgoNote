# [LCR 018. 验证回文串](https://leetcode.cn/problems/XltzEq/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [LCR 018. 验证回文串 - 力扣](https://leetcode.cn/problems/XltzEq/)

## 题目大意

给定一个字符串 `s`。

要求：判断是否为回文串。（只考虑字符串中的字母和数字字符，并且忽略字母的大小写）

## 解题思路

左右两个指针 `start` 和 `end`，左指针 `start` 指向字符串头部，右指针 `end` 指向字符串尾部。先过滤掉除字母和数字字符以外的字符，在判断 `s[start]` 和 `s[end]` 是否相等。不相等返回 `False`，相等则继续过滤和判断。

## 代码

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True
```

