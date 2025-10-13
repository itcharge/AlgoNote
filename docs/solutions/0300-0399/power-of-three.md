# [0326. 3 的幂](https://leetcode.cn/problems/power-of-three/)

- 标签：递归、数学
- 难度：简单

## 题目链接

- [0326. 3 的幂 - 力扣](https://leetcode.cn/problems/power-of-three/)

## 题目大意

给定一个整数 n，判断 n 是否是 3 的幂次方。$-2^{31} \le n \le 2^{31}-1$

## 解题思路

首先排除负数，因为 3 的幂次方不可能为负数。

因为 n 的最大值为 $2^{31}-1$。计算出在 n 的范围内，3 的幂次方最大为 $3^{19} = 1162261467$。

3 为质数，则 $3^{19}$ 的除数只有 $3^0, 3^1, …, 3^{19}$。所以如果 n 为 3 的幂次方，则 n 肯定能被 $3^{19}$ 整除，直接判断即可。

## 代码

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if (3 ** 19) % n == 0:
            return True
        return False
```

