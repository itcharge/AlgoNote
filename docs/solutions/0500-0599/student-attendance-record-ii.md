# [0552. 学生出勤记录 II](https://leetcode.cn/problems/student-attendance-record-ii/)

- 标签：动态规划
- 难度：困难

## 题目链接

- [0552. 学生出勤记录 II - 力扣](https://leetcode.cn/problems/student-attendance-record-ii/)

## 题目大意

**描述**：

可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：

- `A`：Absent，缺勤
- `L`：Late，迟到
- `P`：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

- 按「总出勤」计，学生缺勤（`A`）严格 少于两天。
- 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（`L`）记录。

给定一个整数 $n$，表示出勤记录的长度（次数）。

**要求**：

返回记录长度为 $n$ 时，可能获得出勤奖励的记录情况数量。答案可能很大，所以返回对 $10^9 + 7$ 取余的结果。

**说明**：

- $1 \le n \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：n = 2
输出：8
解释：
有 8 种长度为 2 的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL" 
只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。
```

- 示例 2：

```python
输入：n = 1
输出：3
```

## 解题思路

### 思路 1：动态规划（状态机）

定义状态 $dp[i][j][k]$ 表示前 $i$ 天，有 $j$ 次缺勤（$j \in \{0, 1\}$），连续迟到 $k$ 次（$k \in \{0, 1, 2\}$）的可奖励记录数量。

状态转移：

- 如果第 $i$ 天是 $P$（到场）：$dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1] + dp[i-1][j][2]$
- 如果第 $i$ 天是 $A$（缺勤）：$dp[i][1][0] = dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]$
- 如果第 $i$ 天是 $L$（迟到）：
  - $dp[i][j][1] = dp[i-1][j][0]$
  - $dp[i][j][2] = dp[i-1][j][1]$

初始状态：$dp[1][0][0] = 1$（P），$dp[1][1][0] = 1$（A），$dp[1][0][1] = 1$（L）

### 思路 1：代码

```python
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][k] 表示第 i 天，j 次缺勤，连续 k 次迟到的记录数
        # j: 0 或 1（缺勤次数）
        # k: 0, 1, 2（连续迟到次数）
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        # 初始状态
        dp[0][0][0] = 1
        
        for i in range(1, n + 1):
            # 第 i 天是 P（到场）
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
            
            # 第 i 天是 A（缺勤）
            for k in range(3):
                dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][k]) % MOD
            
            # 第 i 天是 L（迟到）
            for j in range(2):
                for k in range(1, 3):
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MOD
        
        # 统计所有可奖励的记录数
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，需要遍历 $n$ 天，每天的状态转移是常数时间。
- **空间复杂度**：$O(n)$，需要存储 DP 数组。可以优化到 $O(1)$ 使用滚动数组。
