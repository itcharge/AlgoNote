# [LCR 190. 加密运算](https://leetcode.cn/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)

- 标签：位运算、数学
- 难度：简单

## 题目链接

- [LCR 190. 加密运算 - 力扣](https://leetcode.cn/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)

## 题目大意

给定两个整数 `a`、`b`。

要求：不能使用运算符 `+`、`-`、`*`、`/`，计算两整数 `a` 、`b` 之和。

## 解题思路

需要用到位运算的一些知识。

- 异或运算 a ^ b ：可以获得 a + b 无进位的加法结果。
- 与运算 a & b：对应位置为 1，说明 a、b 该位置上原来都为 1，则需要进位。
- 座椅运算 a << 1：将 a 对应二进制数左移 1 位。

这样，通过 a^b 运算，我们可以得到相加后无进位结果，再根据 (a&b) << 1，计算进位后结果。

进行 a^b 和 (a&b) << 1操作之后判断进位是否为 0，如果不为 0，则继续上一步操作，直到进位为 0。

> 注意：
>
> Python 的整数类型是无限长整数类型，负数不确定符号位是第几位。所以我们可以将输入的数字手动转为 32 位无符号整数。
>
> 通过 a &= 0xFFFFFFFF 即可将 a 转为 32 位无符号整数。最后通过对 a 的范围判断，将其结果映射为有符号整数。

## 代码

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        a &= MASK
        b &= MASK
        while b:
            carry = ((a & b) << 1) & MASK
            a ^= b
            b = carry
        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)
```

