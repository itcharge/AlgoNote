# [0467. 环绕字符串中唯一的子字符串](https://leetcode.cn/problems/unique-substrings-in-wraparound-string/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [0467. 环绕字符串中唯一的子字符串 - 力扣](https://leetcode.cn/problems/unique-substrings-in-wraparound-string/)

## 题目大意

把字符串 `s` 看作是 `abcdefghijklmnopqrstuvwxyz` 的无限环绕字符串，所以 `s` 看起来是这样的：`...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....`。 

给定一个字符串 `p`。

要求：你需要的是找出 `s` 中有多少个唯一的 `p` 的非空子串，尤其是当你的输入是字符串 `p` ，你需要输出字符串 `s` 中 `p` 的不同的非空子串的数目。 

注意: `p` 仅由小写的英文字母组成，`p` 的大小可能超过 `10000`。

## 解题思路

字符串 `s` 是个 `a` ~ `z` 无限循环的字符串，题目要求计算字符串 `s` 和字符串 `p` 中有多少个相等的非空子串。发现以该字符结尾的连续子串的长度，就等于以该字符结尾的相等子串的个数。所以我们可以按以下步骤求解：

- 记录以每个字符结尾的字符串最长长度。
- 将其累加起来就是最终答案。

## 代码

```python
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = collections.defaultdict(int)
        dp[p[0]] = 1
        max_len = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                max_len += 1
            else:
                max_len = 1
            dp[p[i]] = max(dp[p[i]], max_len)

        ans = 0
        for key, value in dp.items():
            ans += value
        return ans
```

