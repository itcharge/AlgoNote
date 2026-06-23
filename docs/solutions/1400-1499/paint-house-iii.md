# [1473. 粉刷房子 III](https://leetcode.cn/problems/paint-house-iii/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [1473. 粉刷房子 III - 力扣](https://leetcode.cn/problems/paint-house-iii/)

## 题目大意

**描述**：给定 $n$ 个房子排成一行，$m$ 种颜色，$houses[i] = 0$ 表示未粉刷，否则表示已粉刷的颜色（$1$ ~ $m$）。每个未粉刷的房子涂颜色 $j$ 需要 $cost[i][j]$ 的成本。

**要求**：粉刷所有未粉刷的房子，使得最终形成恰好 $target$ 个街区的最小成本。每个街区由连续相同颜色的房子组成。如果无法完成，返回 $-1$。

**说明**：
- $1 \le n \le 100$。
- $1 \le m \le 20$。
- $1 \le target \le n$。

**示例**：

- 示例 1：

```python
输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：9
解释：房子涂色方案为 [1,2,2,1,1]
此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
```

- 示例 2：

```python
输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：11
解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
```

## 解题思路

### 思路 1：三维 DP

#### 1. 核心思想

定义 $dp[i][j][k]$ 表示前 $i$ 个房子，第 $i$ 个房子的颜色为 $j$，共有 $k$ 个街区的最小成本。

#### 2. 阶段划分

按房子索引 $i$ 和当前颜色 $j$ 划分。

#### 3. 定义状态

$dp[i][j][k]$：前 $i$ 个房子（$1$ 索引），第 $i$ 个房子颜色为 $j$，街区数为 $k$ 的最小成本。

初始化：如果第 $1$ 个房子已染色，$dp[1][color][1] = 0$；如果未染色，$dp[1][j][1] = cost[0][j]$。

#### 4. 状态转移方程

对于第 $i$ 个房子颜色 $j$，来自第 $i-1$ 个房子颜色 $p$：
- 如果 $j == p$：街区数不变 $dp[i][j][k] = \min(dp[i][j][k], dp[i-1][p][k] + paint\_cost)$
- 如果 $j \ne p$：街区数 $+1$，$dp[i][j][k] = \min(dp[i][j][k], dp[i-1][p][k-1] + paint\_cost)$

其中 $paint\_cost$ 是粉刷第 $i$ 个房子为颜色 $j$ 的成本（如果已粉刷则为 $0$，否则为 $cost[i-1][j-1]$）。

#### 5. 最终结果

$\min_{1 \le j \le m} dp[n][j][target]$。

#### 6. 举例说明

以 $houses=[0,0,0,0,0]$, $cost=[[1,10],[10,1],[10,1],[1,10],[5,1]]$, $m=2$, $target=3$ 为例：

需要将 5 个未粉刷的房子涂成 2 种颜色，最后形成 3 个街区。

最优方案可能是：颜色 1,1,2,2,1 → 街区为 [1,1][2,2][1] 共 3 个街区，成本 = 1+1+1+10+1=14。

### 思路 1：代码

```python
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = float('inf')
        # dp[i][j][k]：前 i 个房子，第 i 个颜色 j，k 个街区的最小成本
        dp = [[[INF] * (target + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        # 初始化第 1 个房子
        for j in range(1, n + 1):
            if houses[0] == 0:
                dp[1][j][1] = cost[0][j - 1]
            elif houses[0] == j:
                dp[1][j][1] = 0

        for i in range(2, m + 1):
            for j in range(1, n + 1):
                # 如果已粉刷且颜色不是 j，跳过
                if houses[i - 1] != 0 and houses[i - 1] != j:
                    continue
                paint_cost = 0 if houses[i - 1] != 0 else cost[i - 1][j - 1]

                for k in range(1, target + 1):
                    for p in range(1, n + 1):
                        if p == j:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][p][k] + paint_cost)
                        else:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][p][k - 1] + paint_cost)

        ans = min(dp[m][j][target] for j in range(1, n + 1))
        return -1 if ans == INF else ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n^2 \times target)$，其中 $m \le 100, n \le 20, target \le 100$，$400$ 万级别可行。
- **空间复杂度**：$O(m \times n \times target)$。

---

### 思路 2：优化转移

内层循环 $p$ 可以优化为维护两个最小值（不同颜色的 $dp[i-1][p][k]$ 最小值和次小值），将 $O(n)$ 转移降为 $O(1)$。实现较复杂但可大幅提升效率。
