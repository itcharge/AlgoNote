# [0879. 盈利计划](https://leetcode.cn/problems/profitable-schemes/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [0879. 盈利计划 - 力扣](https://leetcode.cn/problems/profitable-schemes/)

## 题目大意

**描述**：

集团里有 $n$ 名员工，他们可以完成各种各样的工作创造利润。

第 $i$ 种工作会产生 $profit[i]$ 的利润，它要求 $group[i]$ 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。

工作的任何至少产生 $minProfit$ 利润的子集称为「盈利计划」。并且工作的成员总数最多为 $n$。

**要求**：

计算出有多少种计划可以选择？因为答案很大，所以 返回结果模 $10^9 + 7$ 的值。

**说明**：

- $1 \le n \le 10^{3}$。
- $0 \le minProfit \le 10^{3}$。
- $1 \le group.length \le 10^{3}$。
- $1 \le group[i] \le 10^{3}$。
- $profit.length == group.length$。
- $0 \le profit[i] \le 10^{3}$。

**示例**：

- 示例 1：

```python
输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
输出：2
解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
总的来说，有两种计划。
```

- 示例 2：

```python
输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
输出：7
解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
```

## 解题思路

### 思路 1:三维动态规划

这是一个多维约束的 01 背包问题。我们需要在员工数量不超过 $n$ 的约束下,选择若干工作,使得利润至少为 $minProfit$。

**状态定义**:

定义 $dp[i][j][k]$ 表示考虑前 $i$ 个工作,使用了 $j$ 个员工,获得的利润至少为 $k$ 的方案数。

**状态转移**:

对于第 $i$ 个工作(需要 $group[i-1]$ 个员工,产生 $profit[i-1]$ 利润):

1. **不选择第 $i$ 个工作**:$dp[i][j][k] = dp[i-1][j][k]$

2. **选择第 $i$ 个工作**(前提是 $j \ge group[i-1]$):
   - 需要从 $dp[i-1][j-group[i-1]][k-profit[i-1]]$ 转移过来
   - 注意:当 $k - profit[i-1] \le 0$ 时,说明利润已经足够,应该从 $dp[i-1][j-group[i-1]][0]$ 转移
   - 因此:$dp[i][j][k] += dp[i-1][j-group[i-1]][\max(0, k-profit[i-1])]$

**初始状态**:

$dp[0][0][0] = 1$,表示不选择任何工作,使用 0 个员工,获得 0 利润的方案数为 1。

**答案**:

$\sum_{j=0}^{n} dp[length][j][minProfit]$,即考虑所有工作后,使用不超过 $n$ 个员工,获得至少 $minProfit$ 利润的方案数之和。

### 思路 1:代码

```python
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        length = len(group)
        
        # dp[i][j][k] 表示考虑前 i 个工作,使用 j 个员工,获得至少 k 利润的方案数
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        
        # 初始状态:不选择任何工作,使用 0 个员工,获得 0 利润
        dp[0][0][0] = 1
        
        # 枚举每个工作
        for i in range(1, length + 1):
            members = group[i - 1]  # 第 i 个工作需要的员工数
            earn = profit[i - 1]    # 第 i 个工作产生的利润
            
            # 枚举员工数
            for j in range(n + 1):
                # 枚举利润
                for k in range(minProfit + 1):
                    # 不选择第 i 个工作
                    dp[i][j][k] = dp[i - 1][j][k]
                    
                    # 选择第 i 个工作(需要足够的员工)
                    if j >= members:
                        # 利润超过 minProfit 的部分都算作 minProfit
                        prev_profit = max(0, k - earn)
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - members][prev_profit]) % MOD
        
        # 统计答案:使用不超过 n 个员工,获得至少 minProfit 利润的方案数
        result = 0
        for j in range(n + 1):
            result = (result + dp[length][j][minProfit]) % MOD
        
        return result
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(length \times n \times minProfit)$,其中 $length$ 是工作数量。需要填充三维 $dp$ 数组。
- **空间复杂度**:$O(length \times n \times minProfit)$,需要存储三维 $dp$ 数组。可以使用滚动数组优化到 $O(n \times minProfit)$。
