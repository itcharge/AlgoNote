# [LCR 133. 位 1 的个数](https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)

- 标签：位运算
- 难度：简单

## 题目链接

- [LCR 133. 位 1 的个数 - 力扣](https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)

## 题目大意

给定一个无符号整数 `n`。

要求：统计其对应二进制表达式中 `1` 的个数。

## 解题思路

### 1. 循环按位计算

对整数 n 的每一位进行按位与运算，并统计结果。

### 2. 改进位运算

利用 $n \text{ \& } (n-1)$ 。这个运算刚好可以将 n 的二进制中最低位的 $1$ 变为 $0$。 比如 $n = 6$ 时，$6 = (110)_2$，$6 - 1 = (101)_2$，$(110)_2 \text{ \& } (101)_2 = (100)_2$ 。

利用这个位运算，不断的将 $n$ 中最低位的 $1$ 变为 $0$，直到 $n$ 变为 $0$ 即可，其变换次数就是我们要求的结果。

## 代码

1. 循环按位计算

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += (n & 1)
            n = n >> 1
        return ans
```

2. 改进位运算

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n-1
            ans += 1
        return ans
```



