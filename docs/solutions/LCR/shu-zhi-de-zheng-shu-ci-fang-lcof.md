# [LCR 134. Pow(x, n)](https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)

- 标签：递归、数学
- 难度：中等

## 题目链接

- [LCR 134. Pow(x, n) - 力扣](https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)

## 题目大意

给定浮点数 `x` 和整数 `n`。

要求：实现 `pow(x, n)`，即计算 $x^n$，不能使用库函数，不需要考虑大数问题。

## 解题思路

常规方法是直接将 x 累乘 n 次得出结果，时间复杂度为 $O(n)$。可以利用快速幂来减少时间复杂度。

如果 n 为偶数，$x^n = x^{n/2} * x^{n/2}$。如果 n 为奇数，$x^n = x * x^{(n-1)/2} * x^{(n-1)/2}$。

$x^(n/2)$ 又可以继续向下递归划分。则我们可以利用低纬度的幂计算结果，来得到高纬度的幂计算结果。

这样递归求解，时间复杂度为 $O(logn)$，并且递归也可以转为递推来做。

需要注意如果 n 为负数，可以转换为 $\frac{1}{x} ^{(-n)}$。

## 代码

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        res = 1
        if n < 0:
            x = 1 / x
            n = -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
```

