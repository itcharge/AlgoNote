# [0837. 新 21 点](https://leetcode.cn/problems/new-21-game/)

- 标签：数学、动态规划、滑动窗口、概率与统计
- 难度：中等

## 题目链接

- [0837. 新 21 点 - 力扣](https://leetcode.cn/problems/new-21-game/)

## 题目大意

**描述**：

爱丽丝参与一个大致基于纸牌游戏「21点」规则的游戏，描述如下：

爱丽丝以 0 分开始，并在她的得分少于 $k$ 分时抽取数字。 抽取时，她从 $[1, maxPts]$ 的范围中随机获得一个整数作为分数进行累计，其中 $maxPts$ 是一个整数。每次抽取都是独立的，其结果具有相同的概率。

当爱丽丝获得 $k$ 分或更多分时，她就停止抽取数字。

**要求**：

计算爱丽丝的分数不超过 $n$ 的概率。

**说明**：

- 与实际答案误差不超过 $10^{-5}$ 的答案将被视为正确答案。
- $0 \le k \le n \le 10^{4}$。
- $1 \le maxPts \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：n = 10, k = 1, maxPts = 10
输出：1.00000
解释：爱丽丝得到一张牌，然后停止。
```

- 示例 2：

```python
输入：n = 6, k = 1, maxPts = 10
输出：0.60000
解释：爱丽丝得到一张牌，然后停止。 在 10 种可能性中的 6 种情况下，她的得分不超过 6 分。
```

## 解题思路

### 思路 1:动态规划 + 滑动窗口

定义 $dp[x]$ 表示从分数为 $x$ 的情况开始,最终得分不超过 $n$ 的概率。

状态转移:
- 当 $x \ge k$ 时,游戏停止,如果 $x \le n$,则 $dp[x] = 1$,否则 $dp[x] = 0$
- 当 $x < k$ 时,可以抽取 $[1, maxPts]$ 中的任意数字,每个数字的概率为 $\frac{1}{maxPts}$:
  $$dp[x] = \frac{1}{maxPts} \sum_{i=1}^{maxPts} dp[x+i]$$

为了优化计算,我们可以维护一个滑动窗口的和 $sum$,表示 $\sum_{i=x+1}^{x+maxPts} dp[i]$。

### 思路 1:代码

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # 特判:如果 k = 0 或 n >= k + maxPts - 1,概率为 1
        if k == 0 or n >= k + maxPts - 1:
            return 1.0
        
        # dp[x] 表示从分数 x 开始,最终得分不超过 n 的概率
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        
        # sum 表示滑动窗口的和
        window_sum = 1.0
        
        for x in range(1, n + 1):
            # 当前分数的概率
            dp[x] = window_sum / maxPts
            
            if x < k:
                # 如果还可以继续抽牌,将当前概率加入窗口
                window_sum += dp[x]
            
            # 移除窗口左边界
            if x >= maxPts:
                window_sum -= dp[x - maxPts]
        
        # 答案是从 0 分开始,最终得分在 [k, n] 范围内的概率
        return dp[0] if k == 0 else sum(dp[k:n+1]) / maxPts * maxPts if k > 0 else dp[0]
```

实际上,我们需要重新理解题意。让我重写:

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # 特判
        if k == 0 or n >= k + maxPts - 1:
            return 1.0
        
        # dp[x] 表示得分为 x 时,最终得分不超过 n 的概率
        dp = [0.0] * (k + maxPts)
        
        # 初始化:得分在 [k, n] 范围内的概率为 1
        for i in range(k, min(n + 1, k + maxPts)):
            dp[i] = 1.0
        
        # 滑动窗口和
        window_sum = min(n - k + 1, maxPts)
        
        # 从 k-1 倒推到 0
        for x in range(k - 1, -1, -1):
            dp[x] = window_sum / maxPts
            # 更新窗口:加入 dp[x+1],移除 dp[x+maxPts+1]
            window_sum += dp[x]
            if x + maxPts < len(dp):
                window_sum -= dp[x + maxPts]
        
        return dp[0]
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(k + maxPts)$,需要计算 $k + maxPts$ 个状态。
- **空间复杂度**:$O(k + maxPts)$,需要存储 $dp$ 数组。
