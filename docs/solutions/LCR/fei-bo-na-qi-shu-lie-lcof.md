# [LCR 126. 斐波那契数](https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/)

- 标签：记忆化搜索、数学、动态规划
- 难度：简单

## 题目链接

- [LCR 126. 斐波那契数 - 力扣](https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/)

## 题目大意

给定一个整数 `n`。

要求：计算斐波那契数列的第 `n` 项。

注意：答案需对 `1000000007` 进行取余操作。

## 解题思路

斐波那契的递推公式为：`F(n) = F(n-1) + F(n-2)`。

直接根据递推公式求解即可。注意答案需要取余。

## 代码

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        f1 = 0
        f2 = 0
        f3 = 1
        for i in range(2, n + 1):
            f1, f2 = f2, f3
            f3 = (f1 + f2) % 1000000007
        return f3
```

