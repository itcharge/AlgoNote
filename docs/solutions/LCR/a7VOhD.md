# [LCR 020. 回文子串](https://leetcode.cn/problems/a7VOhD/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [LCR 020. 回文子串 - 力扣](https://leetcode.cn/problems/a7VOhD/)

## 题目大意

给定一个字符串 `s`。

要求：计算 `s` 中有多少个回文子串。

## 解题思路

动态规划求解。

先定义状态 `dp[i][j]` 表示为区间 `[i, j]` 的子串是否为回文子串，如果是，则 `dp[i][j] = True`，如果不是，则 `dp[i][j] = False`。

接下来确定状态转移共识：

如果 `s[i] == s[j]`，分为以下几种情况：

- `i == j`，单字符肯定是回文子串，`dp[i][j] == True`。
- `j - i == 1`，比如 `aa` 肯定也是回文子串，`dp[i][j] = True`。
- 如果 `j - i > 1`，则需要看 `[i + 1, j - 1]` 区间是不是回文子串，`dp[i][j] = dp[i + 1][j - 1]`。

如果 `s[i] != s[j]`，那肯定不是回文子串，`dp[i][j] = False`。

下一步确定遍历方向。

由于 `dp[i][j]` 依赖于 `dp[i + 1][j - 1]`，所以我们可以从左下角向右上角遍历。

同时，在递推过程中记录下 `dp[i][j] == True` 的个数，即为最后结果。

## 代码

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        res = 0
        for i in range(size - 1, -1, -1):
            for j in range(i, size):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    res += 1
        return res
```

