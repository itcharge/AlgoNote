# [0461. 汉明距离](https://leetcode.cn/problems/hamming-distance/)

- 标签：位运算
- 难度：简单

## 题目链接

- [0461. 汉明距离 - 力扣](https://leetcode.cn/problems/hamming-distance/)

## 题目大意

给定两个整数 x 和 y，计算他们之间的汉明距离。

- 汉明距离：两个数字对应二进制位上不同的位置的数目

## 解题思路

先对两个数进行异或运算（相同位置上，值相同，结果为 0，值不同，结果为 1），用于记录 x 和 y 不同位置上的异同情况。

然后再按位统计异或结果中 1 的位数。

这里统计 1 的位数可以逐位移动，检查每一位是否为 1。

也可以借助  $n \text{ \& } (n - 1)$  运算。这个运算刚好可以将 n 的二进制中最低位的 1 变为 0。

## 代码

1. 逐位移动
```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor >>= 1
        return distance
```

2. $n \text{ \& } (n - 1)$  运算
```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            xor = xor & (xor - 1)
        return distance
```

