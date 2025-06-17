# [LCR 192. 把字符串转换成整数 (atoi)](https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)

- 标签：字符串
- 难度：中等

## 题目链接

- [LCR 192. 把字符串转换成整数 (atoi) - 力扣](https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)

## 题目大意

给定一个字符串 `str`。

要求：使其能换成一个 32 位有符号整数。并且该方法满足以下要求：

- 丢弃开头无用的空格字符，直到找到第一个非空格字符为止。
- 当找到的第一个非空字符为正负号时，将该符号与后面尽可能多的连续数组组合起来，作为该整数的正负号。如果第一个非空字符为数字，则直接将其与之后连续的数字字符组合起来，形成整数。
- 该字符串中除了有效的整数部分之后也可能会存在多余字符，可直接将这些字符忽略，不会对函数造成影响。
- 如果第一个非空格字符不是一个有效整数字符、或者字符串为空、字符串仅包含空白字符时，函数不需要进行转换。
- 需要检测有效性，无法读取返回 0。
- 所有整数范围为 $[-2^{31}, 2^{31} - 1]$，超过这个范围，则返回 $2^{31} - 1$ 或者 $-2^{31}$。

## 解题思路

根据题意直接模拟即可。

1. 先去除前后空格。
2. 检测正负号。
3. 读入数字，并用字符串存储数字结果
4. 将数字字符串转为整数，并根据正负号转换整数结果。
5. 判断整数范围，并返回最终结果。

## 代码

```python
class Solution:
    def strToInt(self, str: str) -> int:
        num_str = ""
        positive = True
        start = 0

        s = str.lstrip()
        if not s:
            return 0

        if s[0] == '-':
            positive = False
            start = 1
        elif s[0] == '+':
            positive = True
            start = 1
        elif not s[0].isdigit():
            return 0

        for i in range(start, len(s)):
            if s[i].isdigit():
                num_str += s[i]
            else:
                break
        if not num_str:
            return 0
        num = int(num_str)
        if not positive:
            num = -num
            return max(num, -2 ** 31)
        else:
            return min(num, 2 ** 31 - 1)
```

