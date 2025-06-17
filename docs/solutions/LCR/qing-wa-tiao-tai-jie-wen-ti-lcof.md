# [LCR 127. 跳跃训练](https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

- 标签：记忆化搜索、数学、动态规划
- 难度：简单

## 题目链接

- [LCR 127. 跳跃训练 - 力扣](https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

## 题目大意

一直青蛙一次可以跳上 `1` 级台阶，也可以跳上 `2` 级台阶。

要求：求该青蛙跳上 `n` 级台阶共有多少中跳法。答案需要对 `1000000007` 取余。

## 解题思路

先来看一下规律：

第 0 级台阶：1 种方法（比较特殊）

第 1 级台阶：1 种方法（从 0 阶爬 1 阶）

第 2 阶台阶：2 种方法（从 0 阶爬 2 阶，从 1 阶爬 1 阶）

第 i 阶台阶：从第 i-1 阶台阶爬 1 阶，或者从第 i-2 阶台阶爬 2 阶。

则推出递推公式为：

- 当 `n = 0` 时，`F(i) = 1`。
- 当 `n > 0` 时，`F(i) = F(i-1) + F(i-2)`。

## 代码

```python
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1

        f1, f2, f3 = 0, 1, 1
        for i in range(2, n + 1):
            f1, f2 = f2, f3
            f3 = (f1 + f2) % 1000000007
        return f3
```

