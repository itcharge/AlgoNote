# [0903. DI 序列的有效排列](https://leetcode.cn/problems/valid-permutations-for-di-sequence/)

- 标签：字符串、动态规划、前缀和
- 难度：困难

## 题目链接

- [0903. DI 序列的有效排列 - 力扣](https://leetcode.cn/problems/valid-permutations-for-di-sequence/)

## 题目大意

**描述**：

给定一个长度为 $n$ 的字符串 $s$，其中 $s[i]$ 是:

- `"D"` 意味着减少，或者
- `"I"` 意味着增加

「有效排列」是对有 $n + 1$ 个在 $[0, n]$ 范围内的整数的一个排列 $perm$，使得对所有的 $i$：

- 如果 $s[i] == 'D'$，那么 $perm[i] > perm[i+1]$，以及；
- 如果 $s[i] == 'I'$，那么 $perm[i] < perm[i+1]$。

**要求**：

返回「有效排列 $perm$」的数量。因为答案可能很大，所以请返回你的答案对 $10^9 + 7$ 取余。

**说明**：

- $n == s.length$。
- $1 \le n \le 200$。
- $s[i]$ 不是 `'I'` 就是 `'D'`。

**示例**：

- 示例 1：

```python
输入：s = "DID"
输出：5
解释：
(0, 1, 2, 3) 的五个有效排列是：
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
```

- 示例 2：

```python
输入: s = "D"
输出: 1
```

## 解题思路

### 思路 1：动态规划

使用动态规划，$dp[i][j]$ 表示长度为 $i + 1$ 的排列中，最后一个数字在这 $i + 1$ 个数字中排名第 $j$（从小到大排序后的位置）的方案数。

关键理解：
- 对于长度为 $i + 1$ 的排列，我们只关心相对大小关系，可以用 $0$ 到 $i$ 的排列表示。
- $dp[i][j]$ 表示前 $i + 1$ 个位置，最后一个位置的数字在这 $i + 1$ 个数字中排第 $j$ 小的方案数。

状态转移：
- 如果 $s[i - 1] == 'D'$（第 $i - 1$ 个位置大于第 $i$ 个位置）：
  - 前一个位置的数字必须大于当前位置，即前一个位置排名 $\ge j$
  - $dp[i][j] = \sum_{k=j}^{i-1} dp[i-1][k]$
- 如果 $s[i - 1] == 'I'$（第 $i - 1$ 个位置小于第 $i$ 个位置）：
  - 前一个位置的数字必须小于当前位置，即前一个位置排名 $< j$
  - $dp[i][j] = \sum_{k=0}^{j-1} dp[i-1][k]$

### 思路 1：代码

```python
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i][j] 表示长度为 i+1 的排列，最后一个数字排名第 j 的方案数
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        dp[0][0] = 1  # 长度为 1 的排列，只有一个数字，排名第 0
        
        for i in range(n):
            for j in range(i + 2):  # 长度为 i+2 的排列，排名范围是 0 到 i+1
                if s[i] == 'D':
                    # 前一个位置的数字要大于当前位置
                    # 前一个位置排名 >= j（因为插入新数字后，排名会变化）
                    for k in range(j, i + 1):
                        dp[i + 1][j] = (dp[i + 1][j] + dp[i][k]) % MOD
                else:  # s[i] == 'I'
                    # 前一个位置的数字要小于当前位置
                    # 前一个位置排名 < j
                    for k in range(j):
                        dp[i + 1][j] = (dp[i + 1][j] + dp[i][k]) % MOD
        
        # 统计所有可能的结果
        result = 0
        for j in range(n + 1):
            result = (result + dp[n][j]) % MOD
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$，其中 $n$ 是字符串 $s$ 的长度。
- **空间复杂度**：$O(n^2)$，需要存储动态规划数组。

### 思路 2：动态规划 + 前缀和优化

在思路 1 的基础上，使用前缀和优化求和过程，将时间复杂度降低到 $O(n^2)$。

### 思路 2：代码

```python
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[j] 表示当前长度的排列，最后一个数字排名第 j 的方案数
        dp = [1]  # 初始长度为 1，只有一种方案
        
        for i in range(n):
            new_dp = [0] * (i + 2)
            if s[i] == 'D':
                # 从右向左累加（前缀和）
                cumsum = 0
                for j in range(i, -1, -1):
                    cumsum = (cumsum + dp[j]) % MOD
                    new_dp[j] = cumsum
            else:  # s[i] == 'I'
                # 从左向右累加（前缀和）
                cumsum = 0
                for j in range(i + 1):
                    cumsum = (cumsum + dp[j]) % MOD
                    new_dp[j + 1] = cumsum
            dp = new_dp
        
        # 返回所有方案数之和
        return sum(dp) % MOD
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是字符串 $s$ 的长度。
- **空间复杂度**：$O(n)$，使用滚动数组优化空间。
