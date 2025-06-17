# [0258. 各位相加](https://leetcode.cn/problems/add-digits/)

- 标签：数学、数论、模拟
- 难度：简单

## 题目链接

- [0258. 各位相加 - 力扣](https://leetcode.cn/problems/add-digits/)

## 题目大意

给定一个非负整数  num，反复将各个位上的数字相加，直到结果为一位数。

## 解题思路

根据题意，循环模拟累加即可。

## 代码

```python
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            cur = 0
            while num:
                cur += num % 10
                num //= 10
            num = cur
        return num
```

