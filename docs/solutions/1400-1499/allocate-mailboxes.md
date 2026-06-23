# [1478. 安排邮筒](https://leetcode.cn/problems/allocate-mailboxes/)

- 标签：数组、数学、动态规划、排序
- 难度：困难

## 题目链接

- [1478. 安排邮筒 - 力扣](https://leetcode.cn/problems/allocate-mailboxes/)

## 题目大意

**描述**：给定一个长度为 $n$ 的整数数组 $houses$，表示每个房子的坐标。需要在这条直线上建立 $k$ 个邮筒。

**要求**：返回每个房子到最近邮筒的最小距离之和的最小值。

**说明**：
- $1 \le k \le n \le 100$。
- $1 \le houses[i] \le 10^4$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/13/sample_11_1816.png)

```python
输入：houses = [1,4,8,10,20], k = 3
输出：5
解释：将邮筒分别安放在位置 3， 9 和 20 处。
每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/13/sample_2_1816.png)

```python
输入：houses = [2,3,5,12,18], k = 2
输出：9
解释：将邮筒分别安放在位置 3 和 14 处。
每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。
```

## 解题思路

### 思路 1：动态规划

#### 1. 核心思想

如果只有一个邮筒，将其放在所有房子的中位数的位置，距离和最小。如果多个邮筒，可以将房子分成连续的 $k$ 组，每组内部由一个邮筒服务，该邮筒放在这组房子的中位数位置。

因此问题转化为：将排序后的 $houses$ 分成 $k$ 个连续子段，每段用中位数计算距离和，使总距离和最小。

#### 2. 阶段划分

按房子数量（前 $i$ 个房子）和邮筒数量（$j$ 个邮筒）划分阶段。

#### 3. 定义状态

- 排序 $houses$。
- 预处理 $cost[i][j]$：第 $i$ 个到第 $j$ 个房子共用一个邮筒的最小距离和（中位数处）。
- $dp[j][i]$：前 $i$ 个房子放 $j$ 个邮筒的最小总距离。

#### 4. 状态转移方程

$$dp[j][i] = \min_{t = j-1}^{i-1} (dp[j-1][t] + cost[t+1][i])$$

其中 $t$ 表示前 $t$ 个房子由 $j-1$ 个邮筒服务，$t+1$ 到 $i$ 这组由第 $j$ 个邮筒服务。

初始化：$dp[0][0] = 0$，其余 $dp$ 为 $+\infty$。

#### 5. 计算 cost 数组

$cost[l][r]$：在 $houses[l \cdots r]$ 的中位数处放一个邮筒。中位数为 $mid = houses[(l+r)//2]$（排序后）。代价 = $\sum_{pos=l}^{r} |houses[pos] - houses[mid]|$。

可以 $O(n^3)$ 预处理或 $O(n^2)$ 递推（利用相邻区间的关系）。

#### 6. 最终结果

返回 $dp[k][n]$。

#### 7. 举例说明

以 $houses = [1, 4, 8, 10, 20]$，$k = 3$ 为例（已排序）：

$cost[1][5]$（放一个邮筒在中位数 $8$ 处）：$|1-8|+|4-8|+|8-8|+|10-8|+|20-8| = 7+4+0+2+12 = 25$

DP 过程：分成 3 组，最优分组可能是 $[1,4], [8,10], [20]$ → 每组中位数分别为 $1$ 和 $4$ 的中点 $2.5$ 取 $4$（实际取 $1$ 或 $4$），$8$ 和 $10$ 的中位数 $9$ 取 $8$ 或 $10$，$20$ 单独。计算距离和取最小。

### 思路 1：代码

```python
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        # 预处理 cost[l][r]：区间 [l, r] 内用同一个邮筒的最小距离和
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = houses[(i + j) // 2]  # 中位数
                total = 0
                for t in range(i, j + 1):
                    total += abs(houses[t] - mid)
                cost[i][j] = total

        # DP
        INF = float('inf')
        dp = [[INF] * n for _ in range(k + 1)]

        # 1 个邮筒的情况
        for i in range(n):
            dp[1][i] = cost[0][i]

        # 2 ~ k 个邮筒
        for j in range(2, k + 1):
            for i in range(j - 1, n):
                for t in range(j - 2, i):
                    dp[j][i] = min(dp[j][i], dp[j - 1][t] + cost[t + 1][i])

        return dp[k][n - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3 + k \times n^2)$，预处理 $cost$ $O(n^3)$，DP $O(k \times n^2)$。
- **空间复杂度**：$O(k \times n + n^2)$，DP 表和 $cost$ 表。可优化为 $O(n^2)$。

---

### 思路 2：空间优化版

注意到 $dp[j]$ 只依赖 $dp[j-1]$，可以滚动数组优化 DP 空间。同时 $cost$ 可以用递推 $O(n^2)$ 计算。

```python
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        # 递推计算 cost（利用中位数的性质）
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                if i == j:
                    cost[i][j] = 0
                elif (j - i) % 2 == 0:
                    # 偶数个元素，中位数位置不变
                    cost[i][j] = cost[i][j - 1] + houses[j] - houses[mid]
                else:
                    cost[i][j] = cost[i][j - 1] + houses[j] - houses[(i + j) // 2]

        # 滚动数组优化
        INF = float('inf')
        dp = [INF] * n
        for i in range(n):
            dp[i] = cost[0][i]  # 1 个邮筒

        for j in range(2, k + 1):
            new_dp = [INF] * n
            for i in range(j - 1, n):
                for t in range(j - 2, i):
                    new_dp[i] = min(new_dp[i], dp[t] + cost[t + 1][i])
            dp = new_dp

        return dp[n - 1]
```
