# [LCR 003. 比特位计数](https://leetcode.cn/problems/w3tCBm/)

- 标签：位运算、动态规划
- 难度：简单

## 题目链接

- [LCR 003. 比特位计数 - 力扣](https://leetcode.cn/problems/w3tCBm/)

## 题目大意

给定一个整数 `n`。

要求：对于 `0 ≤ i ≤ n` 的每一个 `i`，计算其二进制表示中 `1` 的个数，返回一个长度为 `n + 1` 的数组 `ans` 作为答案。

## 解题思路

可以根据整数的二进制特点将其分为两类：

- 奇数：一定比前面相邻的偶数多一个 `1`。
- 偶数：一定和除以 `2` 之后的数一样多。
- 边界 `0`：`1` 的个数为 `0`。

于是可以根据规律，从 `0` 开始到 `n` 进行递推求解。

## 代码

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i % 2 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp
```

