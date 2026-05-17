# [1140. 石子游戏 II](https://leetcode.cn/problems/stone-game-ii/)

- 标签：数组、数学、动态规划、博弈、前缀和
- 难度：中等

## 题目链接

- [1140. 石子游戏 II - 力扣](https://leetcode.cn/problems/stone-game-ii/)

## 题目大意

**描述**：Alice 和 Bob 在玩一个石子游戏。许多堆石子排成一行，每堆有正整数颗石子 $piles[i]$。Alice 先开始。游戏规则如下：
- 初始时 $M = 1$。
- 每回合，玩家可以拿走**前** $X$ 堆的所有石子，其中 $1 \le X \le 2M$。
- 拿完后，$M = \max(M, X)$。
- 游戏持续到所有石子被拿完。

**要求**：假设两人都发挥最佳水平，返回 Alice 能得到的最大石子数。

**说明**：

- $1 \le piles.length \le 10^3$。
- $1 \le piles[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：piles = [2,7,9,4,4]
输出：10
解释：如果一开始 Alice 取了一堆，Bob 取了两堆，然后 Alice 再取两堆。Alice 可以得到 2 + 4 + 4 = 10 堆。
如果 Alice 一开始拿走了两堆，那么 Bob 可以拿走剩下的三堆。在这种情况下，Alice 得到 2 + 7 = 9 堆。返回 10，因为它更大。
```

- 示例 2：

```python
输入：piles = [1,2,3,4,5,100]
输出：104
```

## 解题思路

### 思路 1：动态规划 + 博弈

**为什么用后缀和？** $suffix\_sum[i]$ 表示从第 $i$ 堆到结尾的所有石子之和。这样当前玩家拿走前 $x$ 堆后，剩余石子总数就是 $suffix\_sum[i + x]$，方便计算。

**拆解步骤**：

1. **计算后缀和**：$suffix\_sum[i] = piles[i] + suffix\_sum[i + 1]$，表示从 $i$ 到结尾的总石子数。

2. **定义 DP 状态**：$dp[i][m]$ 表示从第 $i$ 堆开始，当前 $M = m$ 时，当前玩家能获得的最大石子数。

3. **状态转移**：当前玩家可以选择拿 $x$ 堆（$1 \le x \le 2m$）：
   - 如果 $i + 2m \ge n$（剩余堆数 $\le 2m$），可以直接全部拿走，收益 = $suffix\_sum[i]$
   - 否则，收益 = $suffix\_sum[i] - dp[i + x][\max(m, x)]$，即剩余总数减去对手在最优策略下能得到的石子数
   - 取所有 $x$ 中的最大值

4. **从后往前计算**：因为 $dp[i]$ 依赖 $dp[i + x]$，所以从数组末尾往前遍历。

5. **返回 $dp[0][1]$**：从第 $0$ 堆开始，初始 $M = 1$，Alice 能获得的最大石子数。

### 思路 1：代码

```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # 后缀和：suffix_sum[i] 表示从第 i 堆到结尾的总石子数
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # dp[i][m]：从第 i 堆开始，M=m 时当前玩家能获得的最大石子数
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # 从后往前填表
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                # 如果剩余堆数不超过 2M，可以全部拿走
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    # 尝试拿 x 堆 (1 <= x <= 2M)，取最优
                    for x in range(1, 2 * m + 1):
                        # 当前收益 = 剩余总数 - 对手最优收益
                        dp[i][m] = max(dp[i][m],
                                       suffix_sum[i] - dp[i + x][max(m, x)])

        return dp[0][1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$。用人话说就是：有 $n^2$ 个状态需要计算，每个状态最多需要尝试 $2m$ 种取法，最坏情况下 $m$ 和 $n$ 同阶，所以是 $n^3$。
- **空间复杂度**：$O(n^2)$。需要存储 $dp$ 二维数组和后缀和数组。
