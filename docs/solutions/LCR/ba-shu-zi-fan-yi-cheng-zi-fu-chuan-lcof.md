# [LCR 165. 解密数字](https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [LCR 165. 解密数字 - 力扣](https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

## 题目大意

给定一个数字 `num`，按照如下规则将其翻译为字符串：`0` 翻译为 `a`，`1` 翻译为 `b`，…，`11` 翻译为 `l`，…，`25` 翻译为 `z`。

要求：计算出共有多少种可能的翻译方案。

## 解题思路

可用动态规划来做。

将数字 `nums` 转为字符串 `s`。设 `dp[i]` 表示字符串 `s` 前 `i` 个数字 `s[0: i]` 的翻译方案数。`dp[i]` 的来源有两种情况：

1. 第 `i - 1`、`i - 2` 构成的数字在 `[10, 25]`之间，则 `dp[i]` 来源于： `s[i - 1]` 单独翻译的方案数（即 `dp[i - 1]`） +  `s[i - 2]` 和 `s[i - 1]` 连起来进行翻译的方案数（即 `dp[i - 2]`）。
2. 第 `i - 1`、`i - 2` 构成的数字在 `[10, 25]`之外，则 `dp[i]` 来源于：`s[i]` 单独翻译的方案数。

## 代码

```python
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        size = len(s)
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, size + 1):
            temp = int(s[i-2:i])
            if temp >= 10 and temp <= 25:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[size]
```

