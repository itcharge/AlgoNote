# [LCR 181. 字符串中的单词反转](https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [LCR 181. 字符串中的单词反转 - 力扣](https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/)

## 题目大意

给定一个字符串 `s`。

要求：逐个翻转字符串中所有的单词。

说明：

- 数组字符串 `s` 可以再前面、后面或者单词间包含多余的空格。
- 翻转后的单词应当只有一个空格分隔。
- 翻转后的字符串不应该包含额外的空格。

## 解题思路

最简单的就是调用 API 进行切片，翻转。复杂一点的也可以根据 API 的思路写出模拟代码。

## 代码

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
```

