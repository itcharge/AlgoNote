# [0263. 丑数](https://leetcode.cn/problems/ugly-number/)

- 标签：数学
- 难度：简单

## 题目链接

- [0263. 丑数 - 力扣](https://leetcode.cn/problems/ugly-number/)

## 题目大意

给定一个整数 `n`。

要求：判断 `n` 是否为丑数。如果是，则返回 `True`，否则，返回 `False`。

- 丑数：只包含质因数 `2`、`3`、`5` 的正整数。

## 解题思路

- 如果 `n <= 0`，则 `n` 必然不是丑数，直接返回 `False`。
- 对 `n` 分别进行 `2`、`3`、`5` 的整除操作，直到 `n` 被除完，如果 `n` 最终为 `1`，则 `n` 是丑数，否则不是丑数。

## 代码

```python
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor

        return n == 1
```

