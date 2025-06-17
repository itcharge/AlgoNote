# [LCR 019. 验证回文串 II](https://leetcode.cn/problems/RQku0D/)

- 标签：贪心、双指针、字符串
- 难度：简单

## 题目链接

- [LCR 019. 验证回文串 II - 力扣](https://leetcode.cn/problems/RQku0D/)

## 题目大意

给定一个非空字符串 `s`。

要求：判断如果最多从字符串中删除一个字符能否得到一个回文字符串。

## 解题思路

双指针 + 贪心算法。

- 用两个指针 `left`、`right` 分别指向字符串的开始和结束位置。

- 判断 `s[left]` 是否等于 `s[right]`。
  - 如果等于，则 `left` 右移、`right`左移。
  - 如果不等于，则判断 `s[left: right - 1]` 或 `s[left + 1, right]` 是为回文串。
    - 如果是则返回 `True`。
    - 如果不是则返回 `False`，然后继续判断。
- 如果 `right >= left`，则说明字符串 `s` 本身就是回文串，返回 `True`。



## 代码

```python
class Solution:
    def checkPalindrome(self, s: str, left: int, right: int):
        i, j = left, right
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.checkPalindrome(s, left + 1, right) or self.checkPalindrome(s, left, right - 1)
        return True
```

