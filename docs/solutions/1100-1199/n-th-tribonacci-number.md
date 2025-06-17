# [1137. 第 N 个泰波那契数](https://leetcode.cn/problems/n-th-tribonacci-number/)

- 标签：记忆化搜索、数学、动态规划
- 难度：简单

## 题目链接

- [1137. 第 N 个泰波那契数 - 力扣](https://leetcode.cn/problems/n-th-tribonacci-number/)

## 题目大意

**描述**：给定一个整数 $n$。

**要求**：返回第 $n$ 个泰波那契数。

**说明**：

- **泰波那契数**：$T_0 = 0, T_1 = 1, T_2 = 1$，且在 $n >= 0$ 的条件下，$T_{n + 3} = T_{n} + T_{n+1} + T_{n+2}$。
- $0 \le n \le 37$。
- 答案保证是一个 32 位整数，即 $answer \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

- 示例 2：

```python
输入：n = 25
输出：1389537
```

## 解题思路

### 思路 1：记忆化搜索

1. 问题的状态定义为：第 $n$ 个泰波那契数。其状态转移方程为：$T_0 = 0, T_1 = 1, T_2 = 1$，且在 $n >= 0$ 的条件下，$T_{n + 3} = T_{n} + T_{n+1} + T_{n+2}$。
2. 定义一个长度为 $n + 1$ 数组 `memo` 用于保存一斤个计算过的泰波那契数。
3. 定义递归函数 `my_tribonacci(n, memo)`。
   1. 当 $n = 0$ 或者 $n = 1$，或者 $n = 2$ 时直接返回结果。
   2. 当 $n > 2$ 时，首先检查是否计算过 $T(n)$，即判断 $memo[n]$ 是否等于 $0$。
      1. 如果 $memo[n] \ne 0$，说明已经计算过 $T(n)$，直接返回 $memo[n]$。
      2. 如果 $memo[n] = 0$，说明没有计算过 $T(n)$，则递归调用 `my_tribonacci(n - 3, memo)`、`my_tribonacci(n - 2, memo)`、`my_tribonacci(n - 1, memo)`，并将计算结果存入 $memo[n]$ 中，并返回 $memo[n]$。

### 思路 1：代码

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        # 使用数组保存已经求解过的 T(k) 的结果
        memo = [0 for _ in range(n + 1)]
        return self.my_tribonacci(n, memo)
    
    def my_tribonacci(self, n: int, memo: List[int]) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.my_tribonacci(n - 3, memo) + self.my_tribonacci(n - 2, memo) + self.my_tribonacci(n - 1, memo)
        return memo[n]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

### 思路 2：动态规划

###### 1. 划分阶段

我们可以按照整数顺序进行阶段划分，将其划分为整数 $0 \sim n$。

###### 2. 定义状态

定义状态 `dp[i]` 为：第 `i` 个泰波那契数。

###### 3. 状态转移方程

根据题目中所给的泰波那契数的定义：$T_0 = 0, T_1 = 1, T_2 = 1$，且在 $n >= 0$ 的条件下，$T_{n + 3} = T_{n} + T_{n+1} + T_{n+2}$。，则直接得出状态转移方程为 $dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]$（当 $i > 2$ 时）。

###### 4. 初始条件

根据题目中所给的初始条件 $T_0 = 0, T_1 = 1, T_2 = 1$ 确定动态规划的初始条件，即 `dp[0] = 0, dp[1] = 1, dp[2] = 1`。

###### 5. 最终结果

根据状态定义，最终结果为 `dp[n]`，即第 `n` 个泰波那契数为 `dp[n]`。

### 思路 2：代码

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        return dp[n]
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

