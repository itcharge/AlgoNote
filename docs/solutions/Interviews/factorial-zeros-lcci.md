# [面试题 16.05. 阶乘尾数](https://leetcode.cn/problems/factorial-zeros-lcci/)

- 标签：数学
- 难度：简单

## 题目链接

- [面试题 16.05. 阶乘尾数 - 力扣](https://leetcode.cn/problems/factorial-zeros-lcci/)

## 题目大意

给定一个整数 `n`。

要求：计算 `n` 的阶乘中尾随零的数量。

注意：$0 <= n <= 10^4$。

## 解题思路

阶乘中，末尾 `0` 的来源只有 `2 * 5`。所以尾随 `0` 的个数为 `2` 的倍数个数和 `5` 的倍数个数的最小值。又因为 `2 < 5`，`2` 的倍数个数肯定小于等于 `5` 的倍数，所以直接统计 `5` 的倍数个数即可。

## 代码

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n // 5
            n = n // 5
        return count
```

