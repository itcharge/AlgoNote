# [1467. 两个盒子中球的颜色数相同的概率](https://leetcode.cn/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)

- 标签：数学、动态规划、回溯、组合数学、概率与统计
- 难度：困难

## 题目链接

- [1467. 两个盒子中球的颜色数相同的概率 - 力扣](https://leetcode.cn/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)

## 题目大意

**描述**：有 $n$ 种颜色的球，每种颜色的球有 $balls[i]$ 个。将所有球随机均分到两个盒子中（每个盒子球数相等）。

**要求**：返回两个盒子中颜色种类数相同的概率。

**说明**：
- $1 \le n \le 8$。
- $1 \le balls[i] \le 6$。
- 球总数不超过 $48$。

**示例**：

- 示例 1：

```python
输入：balls = [1,1]
输出：1.00000
解释：球平均分配的方式只有两种：
- 颜色为 1 的球放入第一个盒子，颜色为 2 的球放入第二个盒子
- 颜色为 2 的球放入第一个盒子，颜色为 1 的球放入第二个盒子
这两种分配，两个盒子中球的颜色数都相同。所以概率为 2/2 = 1 。
```

- 示例 2：

```python
输入：balls = [2,1,1]
输出：0.66667
解释：球的列表为 [1, 1, 2, 3]
随机打乱，得到 12 种等概率的不同打乱方案，每种方案概率为 1/12 ：
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
然后，我们将前两个球放入第一个盒子，后两个球放入第二个盒子。
这 12 种可能的随机打乱方式中的 8 种满足「两个盒子中球的颜色数相同」。
概率 = 8/12 = 0.66667
```

## 解题思路

### 思路 1：DFS 枚举分配方案

#### 1. 核心思想

总球数 $total$，每个盒子分到 $total/2$ 个球。枚举每种颜色的球分配到两个盒子中的数量组合。

对每种颜色 $i$，从 $0$ 到 $balls[i]$ 枚举分给盒 1 的数量 $cnt$，则盒 2 分到 $balls[i] - cnt$。

DFS 过程中维护：
- 盒 1 和盒 2 的球数。
- 盒 1 和盒 2 的颜色种类数。
- 当前分配方式的方案数（组合数乘积）。

最终答案 = (盒1颜色数 == 盒2颜色数 的方案数) / (总方案数)。

#### 2. 具体步骤

**第 1 步**：计算总方案数 = $\frac{(total/2)!}{\prod balls[i]!}$ 的分子（多重集排列）。

优化：在 DFS 过程中用组合数计算。对于每种颜色，分 $cnt$ 个给盒 1，盒2 分到 $balls[i]-cnt$，乘上 $C(box1\_remain, cnt)$（从盒1剩余位置中选 $cnt$ 个放这种颜色的球）。

但实际上更简单：DFS 枚举分配，用组合数相乘得到当前分配方案数。

**第 2 步**：DFS 参数：
- $idx$：当前处理到第几种颜色
- $cnt1, cnt2$：盒 1 和盒 2 当前球数
- $color1, color2$：盒 1 和盒 2 当前颜色种类数
- $ways$：当前分配方式的组合数

**第 3 步**：终止条件：处理完所有颜色后，$cnt1 == cnt2$（球数平等）才有效，然后根据 $color1 == color2$ 统计。

**第 4 步**：返回 $good\_ways / total\_ways$。

### 思路 1：代码

```python
import math
from functools import lru_cache

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = len(balls)
        total = sum(balls)
        half = total // 2

        # 预处理组合数
        C = [[0] * (half + 1) for _ in range(half + 1)]
        for i in range(half + 1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

        self.good = 0
        self.total_ways = 0

        def dfs(idx, cnt1, cnt2, color1, color2, ways):
            if idx == n:
                if cnt1 == cnt2:
                    self.total_ways += ways
                    if color1 == color2:
                        self.good += ways
                return

            ball = balls[idx]
            # 枚举分给盒 1 的数量
            for c1 in range(ball + 1):
                c2 = ball - c1
                if cnt1 + c1 > half or cnt2 + c2 > half:
                    continue
                new_color1 = color1 + (1 if c1 > 0 else 0)
                new_color2 = color2 + (1 if c2 > 0 else 0)
                # 从剩余位置中选 c1 个给盒1
                new_ways = ways * C[half - cnt1][c1] * C[half - cnt2][c2]
                dfs(idx + 1, cnt1 + c1, cnt2 + c2,
                    new_color1, new_color2, new_ways)

        dfs(0, 0, 0, 0, 0, 1)

        return self.good / self.total_ways
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\prod (balls[i]+1))$，枚举所有颜色分配组合。$n \le 8$，每种球 $\le 6$，最坏 $7^8 \approx 576$ 万，可行。
- **空间复杂度**：$O(n)$，递归栈深度。
