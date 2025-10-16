# [0097. 交错字符串](https://leetcode.cn/problems/interleaving-string/)

- 标签：字符串、动态规划
- 难度：中等

## 题目链接

- [0097. 交错字符串 - 力扣](https://leetcode.cn/problems/interleaving-string/)

## 题目大意

**描述**：

两个字符串 $s$ 和 $t$ 交错的定义与过程如下，其中每个字符串都会被分割成若干非空子字符串：

- $s = s1 + s2 + ... + sn$
- $t = t1 + t2 + ... + tm$
- $|n - m| \le 1$
- 「交错」是 $s1 + t1 + s2 + t2 + s3 + t3 + ...$ 或者 $t1 + s1 + t2 + s2 + t3 + s3 + ...$

注意：$a + b$ 意味着字符串 $a$ 和 $b$ 连接。

现在给定三个字符串 $s1$、$s2$、$s3$。

**要求**：

帮忙验证 $s3$ 是否是由 $s1$ 和 $s2$ 「交错」组成的。

**说明**：

- $0 \le s1.length, s2.length \le 100$。
- $0 \le s3.length \le 200$。
- $s1$、$s2$、和 $s3$ 都由小写英文字母组成。

- 进阶：您能否仅使用 $O(s2.length)$ 额外的内存空间来解决它?

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)

```python
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
```

- 示例 2：

```python
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
```

## 解题思路

### 思路 1：动态规划

**核心思想**：

使用二维动态规划来解决这个问题。定义 $dp[i][j]$ 表示 $s1$ 的前 $i$ 个字符和 $s2$ 的前 $j$ 个字符能否交错组成 $s3$ 的前 $i + j$ 个字符。

**状态转移方程**：

- 如果 $s1$ 的第 $i$ 个字符等于 $s3$ 的第 $i+j$ 个字符，且 $s1$ 的前 $i-1$ 个字符和 $s2$ 的前 $j$ 个字符能组成 $s3$ 的前 $i+j-1$ 个字符，则 $dp[i][j] = True$。
- 如果 $s2$ 的第 $j$ 个字符等于 $s3$ 的第 $i+j$ 个字符，且 $s1$ 的前 $i$ 个字符和 $s2$ 的前 $j-1$ 个字符能组成 $s3$ 的前 $i+j-1$ 个字符，则 $dp[i][j] = True$。
- 否则 $dp[i][j] = False$。

**边界条件**：

- $dp[0][0] = True$（空字符串可以组成空字符串）。
- $dp[i][0]$ 取决于 $s1$ 的前 $i$ 个字符是否等于 $s3$ 的前 $i$ 个字符。
- $dp[0][j]$ 取决于 $s2$ 的前 $j$ 个字符是否等于 $s3$ 的前 $j$ 个字符。

### 思路 1：代码

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        
        # 长度不匹配直接返回 False
        if len1 + len2 != len3:
            return False
        
        # 创建 DP 数组
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        
        # 初始化边界条件
        dp[0][0] = True
        
        # 初始化第一行：只使用 s2
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        # 初始化第一列：只使用 s1
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        # 填充 DP 数组
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # 状态转移方程
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[len1][len2]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$，其中 $m$ 是 $s1$ 的长度，$n$ 是 $s2$ 的长度。需要填充 $m \times n$ 的 DP 数组。
- **空间复杂度**：$O(m \times n)$，需要创建 $m \times n$ 的 DP 数组来存储中间结果。
