# [1406. 石子游戏 III](https://leetcode.cn/problems/stone-game-iii/)

- 标签：数组、数学、动态规划、博弈
- 难度：困难

## 题目链接

- [1406. 石子游戏 III - 力扣](https://leetcode.cn/problems/stone-game-iii/)

## 题目大意

**描述**：Alice 和 Bob 玩取石子游戏。有一排石子 $stoneValue$，每人每次可以从左边取 $1 \sim 3$ 堆石子。双方都采取最优策略。

**要求**：比较最终得分，返回 `"Alice"`、`"Bob"` 或 `"Tie"`。

**说明**：
- $1 \le stoneValue.length \le 5 \times 10^4$。
- $-1000 \le stoneValue[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：values = [1,2,3,7]
输出："Bob"
解释：Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。
```

- 示例 2：

```python
输入：values = [1,2,3,-9]
输出："Alice"
解释：Alice 要想获胜就必须在第一个回合拿走前三堆石子，给 Bob 留下负分。
如果 Alice 只拿走第一堆，那么她的得分为 1，接下来 Bob 拿走第二、三堆，得分为 5 。之后 Alice 只能拿到分数 -9 的石子堆，输掉比赛。
如果 Alice 拿走前两堆，那么她的得分为 3，接下来 Bob 拿走第三堆，得分为 3 。之后 Alice 只能拿到分数 -9 的石子堆，同样会输掉比赛。
注意，他们都应该采取 最优策略 ，所以在这里 Alice 将选择能够使她获胜的方案。
```

## 解题思路

### 思路 1：DP

#### 1. 核心思想

定义 $dp[i]$ 表示从第 $i$ 堆石子开始取，当前玩家能获得的最大净胜分（当前玩家得分 - 对手得分）。

#### 2. 阶段划分

从后向前递推。

#### 3. 定义状态

$dp[i]$：在 $stoneValue[i \dots n-1]$ 这个子游戏中，当前先手玩家能获得的最大净胜分。

#### 4. 状态转移方程

当前玩家在第 $i$ 堆可以取 $1 \sim 3$ 堆，取 $k$ 堆的得分 = $sum[i \dots i+k-1]$。然后对手从 $i+k$ 开始先手，获得最大净胜分 $dp[i+k]$。

当前玩家从第 $i$ 堆开始的净胜分 = 当前得分 - 对手未来净胜分。所以：

$$dp[i] = \max_{k=1,2,3} \left( sum[i \dots i+k-1] - dp[i+k] \right)$$

#### 5. 初始条件

$dp[n] = 0$（没有石子，先手玩家净胜分 $0$）。
对于越界位置，按 $0$ 处理。

#### 6. 最终结果

- 如果 $dp[0] > 0$：Alice 胜。
- 如果 $dp[0] < 0$：Bob 胜。
- 如果 $dp[0] == 0$：平局。

#### 7. 举例说明

以 $stoneValue = [1, 2, 3, 7]$ 为例：

$n=4$

- $dp[4] = 0$
- $i=3$：取 $7$，$7-dp[4]=7$ → $dp[3] = 7$
- $i=2$：取 $3$ → $3-dp[3]=-4$；取 $3+7=10$ → $10-dp[4]=10$ → $dp[2] = 10$
- $i=1$：取 $2$ → $2-dp[2]=-8$；取 $2+3=5$ → $5-dp[3]=-2$；取 $2+3+7=12$ → $12-dp[4]=12$ → $dp[1] = 12$
- $i=0$：取 $1$ → $1-dp[1]=-11$；取 $1+2=3$ → $3-dp[2]=-7$；取 $1+2+3=6$ → $6-dp[3]=-1$ → $dp[0] = -1$

$dp[0] < 0$，Bob 胜。

### 思路 1：代码

```python
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            total = 0
            best = float('-inf')
            for k in range(1, 4):
                if i + k - 1 >= n:
                    break
                total += stoneValue[i + k - 1]
                best = max(best, total - dp[i + k])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个位置最多检查 $3$ 种取法。
- **空间复杂度**：$O(n)$，可优化为 $O(1)$（只保留最近 $3$ 个 $dp$ 值）。
