# [1334. 阈值距离内邻居最少的城市](https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

- 标签：图、动态规划、最短路
- 难度：中等

## 题目链接

- [1334. 阈值距离内邻居最少的城市 - 力扣](https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

## 题目大意

**描述**：有 $n$ 个城市，城市间有若干条带权无向边 $edges$。给定阈值 $distanceThreshold$。

**要求**：找出能到达的其他城市数量最少（路径长度 $\le distanceThreshold$）的城市。如果数量相同，返回编号最大的城市。

**说明**：
- $2 \le n \le 100$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2024/08/23/problem1334example1.png)

```python
输入：n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
输出：3
解释：城市分布图如上。
每个城市阈值距离 distanceThreshold = 4 内的邻居城市分别是：
城市 0 -> [城市 1, 城市 2] 
城市 1 -> [城市 0, 城市 2, 城市 3] 
城市 2 -> [城市 0, 城市 1, 城市 3] 
城市 3 -> [城市 1, 城市 2] 
城市 0 和 3 在阈值距离 4 以内都有 2 个邻居城市，但是我们必须返回城市 3，因为它的编号最大。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2024/08/23/problem1334example0.png)

```python
输入：n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
输出：0
解释：城市分布图如上。 
每个城市阈值距离 distanceThreshold = 2 内的邻居城市分别是：
城市 0 -> [城市 1] 
城市 1 -> [城市 0, 城市 4] 
城市 2 -> [城市 3, 城市 4] 
城市 3 -> [城市 2, 城市 4]
城市 4 -> [城市 1, 城市 2, 城市 3] 
城市 0 在阈值距离 2 以内只有 1 个邻居城市。
```


## 解题思路

### 思路 1：Floyd 全源最短路

#### 1. 核心思想

$n \le 100$，可以用 Floyd 算法计算任意两点之间的最短路径，然后统计每个城市在阈值内能到达的城市数量。

#### 2. 具体步骤

**第 1 步**：初始化距离矩阵 $dist$，直接相连的边赋值为对应权重，其余为无穷大。

**第 2 步**：Floyd 三重循环更新最短路径。

**第 3 步**：对每个城市，统计 $dist[i][j] \le distanceThreshold$ 的城市数，取最小值对应的最大编号。

### 思路 1：代码

```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        ans, min_cnt = -1, n
        for i in range(n):
            cnt = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if cnt <= min_cnt:
                min_cnt = cnt
                ans = i
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n^3)$。$n \le 100$，$10^6$ 次操作可接受。
- **空间复杂度**：$O(n^2)$。
