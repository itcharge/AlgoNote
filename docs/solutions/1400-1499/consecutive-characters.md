# [1446. 连续字符](https://leetcode.cn/problems/consecutive-characters/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1446. 连续字符 - 力扣](https://leetcode.cn/problems/consecutive-characters/)

## 题目大意

给你一个字符串 `s` ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

要求：返回字符串的能量。

注意：

- `1 <= s.length <= 500`
- `s` 只包含小写英文字母。

## 解题思路

使用 `count` 统计连续不重复子串的长度，使用 `ans` 记录最长连续不重复子串的长度。

## 代码

```python
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans
```

