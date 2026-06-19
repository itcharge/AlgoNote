# [1397. 找到所有好字符串](https://leetcode.cn/problems/find-all-good-strings/)

- 标签：字符串、动态规划、字符串匹配
- 难度：困难

## 题目链接

- [1397. 找到所有好字符串 - 力扣](https://leetcode.cn/problems/find-all-good-strings/)

## 题目大意

**描述**：给定两个长度为 $n$ 的字符串 $s1$ 和 $s2$，以及一个字符串 $evil$。好字符串定义为长度 $n$、字典序在 $[s1, s2]$ 之间、且不包含 $evil$ 作为子串的字符串。

**要求**：返回好字符串的个数，对 $10^9 + 7$ 取模。

**说明**：
- $1 \le n \le 500$。
- $1 \le evil.length \le 50$。

**示例**：

- 示例 1：

```python
输入：n = 2, s1 = "aa", s2 = "da", evil = "b"
输出：51 
解释：总共有 25 个以 'a' 开头的好字符串："aa"，"ac"，"ad"，...，"az"。还有 25 个以 'c' 开头的好字符串："ca"，"cc"，"cd"，...，"cz"。最后，还有一个以 'd' 开头的好字符串："da"。
```

- 示例 2：

```python
输入：n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
输出：0 
解释：所有字典序大于等于 s1 且小于等于 s2 的字符串都以 evil 字符串 "leet" 开头。所以没有好字符串。
```


## 解题思路

### 思路 1：数位 DP + KMP

#### 1. 核心思想

这是一个典型的数位 DP（字符串范围统计）问题，结合 KMP 自动机处理模式串匹配。

定义 $dp[pos][match][bound1][bound2]$：
- $pos$：当前处理到的位置。
- $match$：当前与 $evil$ 匹配的长度（KMP 自动机的状态）。
- $bound1$：是否达到 $s1$ 的下界。
- $bound2$：是否达到 $s2$ 的上界。

转移时枚举 $pos$ 位置可选的字符（受 $s1$ 和 $s2$ 限制），用 KMP 的 next 数组更新匹配状态。

#### 2. 具体步骤

**第 1 步**：预处理 $evil$ 的 KMP next 数组 $pi$。

**第 2 步**：记忆化搜索 $dfs(pos, match, bound1, bound2)$：
- 如果 $match == m$，说明包含了 $evil$，返回 $0$。
- 如果 $pos == n$，返回 $1$。
- 确定当前可选字符范围：$low$ 到 $high$。
- 对每个字符 $c$：
  - 计算新的匹配长度 $new\_match$（用 KMP 自动机）。
  - 递归累加。

### 思路 1：代码

```python
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10**9 + 7
        m = len(evil)

        # KMP 前缀函数
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and evil[i] != evil[j]:
                j = pi[j - 1]
            if evil[i] == evil[j]:
                j += 1
            pi[i] = j

        # KMP 自动机（预计算从状态 k 读入字符 c 后的新状态）
        nxt = [[0] * 26 for _ in range(m)]
        for k in range(m):
            for c in range(26):
                ch = chr(ord('a') + c)
                j = k
                while j > 0 and ch != evil[j]:
                    j = pi[j - 1]
                if ch == evil[j]:
                    j += 1
                nxt[k][c] = j

        from functools import lru_cache

        @lru_cache(None)
        def dfs(pos: int, match: int, bound1: bool, bound2: bool) -> int:
            if match == m:
                return 0
            if pos == n:
                return 1
            lo = ord(s1[pos]) if bound1 else ord('a')
            hi = ord(s2[pos]) if bound2 else ord('z')
            total = 0
            for c in range(lo, hi + 1):
                new_match = nxt[match][c - ord('a')]
                total += dfs(pos + 1, new_match,
                             bound1 and c == lo,
                             bound2 and c == hi)
            return total % mod

        return dfs(0, 0, True, True)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \times m \times 26)$。$n \le 500$，$m \le 50$。
- **空间复杂度**：$O(n \times m)$。
