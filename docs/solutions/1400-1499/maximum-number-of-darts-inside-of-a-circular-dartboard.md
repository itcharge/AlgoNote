# [1453. 圆形靶内的最大飞镖数量](https://leetcode.cn/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/)

- 标签：几何、数组、数学
- 难度：困难

## 题目链接

- [1453. 圆形靶内的最大飞镖数量 - 力扣](https://leetcode.cn/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/)

## 题目大意

**描述**：给定平面上的 $n$ 个点和一个半径 $r$。

**要求**：返回一个半径为 $r$ 的圆最多能覆盖多少个点（包括边界）。

**说明**：
- $1 \le n \le 100$。
- $1 \le r \le 5000$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/04/29/sample_1_1806.png)

```python
输入：darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
输出：4
解释：如果圆形靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/04/29/sample_2_1806.png)

```python
输入：darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
输出：5
解释：如果圆形靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
```

## 解题思路

### 思路 1：几何 + 枚举

#### 1. 核心思想

一个能覆盖最多点的圆，可以通过将圆周经过两个点来得到（或者只覆盖一个点）。枚举所有点对 $(i, j)$，计算以 $r$ 为半径且圆周经过 $i$ 和 $j$ 的两个可能的圆心，然后计算该圆心能覆盖的点数。

为什么最优解一定可以通过调整使圆周经过至少两个点或只覆盖一个点？因为如果一个圆只覆盖一个点或没有经过边界上的点，可以平移使圆周经过一个点，再旋转经过另一个点同时不减少覆盖点数。

#### 2. 具体步骤

**第 1 步**：计算距离函数 $dist(p, q)$。

**第 2 步**：如果 $n=1$，返回 $1$。

**第 3 步**：初始化 $ans = 1$（至少能覆盖 $1$ 个点）。

**第 4 步**：枚举所有点对 $(i, j)$，如果 $dist(i, j) > 2 \times r$，跳过（无法同时覆盖两点）。

**第 5 步**：计算以 $r$ 为半径且过 $i$ 和 $j$ 的两个圆心：
- 连接 $i$ 和 $j$ 的中点 $mid$。
- 从 $mid$ 到圆心的距离 $d = \sqrt{r^2 - (dist(i,j)/2)^2}$。
- 垂直方向单位向量，得到两个圆心。

**第 6 步**：对每个圆心，统计距其 $\le r$ 的点数，更新 $ans$。

**第 7 步**：返回 $ans$。

#### 3. 举例说明

以 $points = [[-2,0],[2,0],[0,2]], r = 2$ 为例：

$dist((0,2),(-2,0)) = \sqrt{4+4} \approx 2.828$，$2r=4$，可以覆盖。

圆心计算略（需要解几何方程）。枚举可得最大覆盖 $3$（圆心在 $(0,0)$ 处覆盖所有三个点）。

### 思路 1：代码

```python
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        n = len(points)
        if n == 1:
            return 1

        def dist2(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        def dist(a, b):
            return math.sqrt(dist2(a, b))

        ans = 1
        r2 = r * r

        for i in range(n):
            for j in range(i + 1, n):
                d2 = dist2(points[i], points[j])
                if d2 > 4 * r2:
                    continue
                # 计算中点
                mx = (points[i][0] + points[j][0]) / 2
                my = (points[i][1] + points[j][1]) / 2
                d = math.sqrt(d2) / 2
                # 从 i 到 j 的向量
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                # 垂直方向
                h = math.sqrt(r2 - d * d)
                if d == 0:
                    # i 和 j 重合
                    hx1 = mx + h
                    hy1 = my
                    hx2 = mx - h
                    hy2 = my
                else:
                    # 单位垂直向量
                    hx1 = mx + h * (-dy) / (2 * d)
                    hy1 = my + h * dx / (2 * d)
                    hx2 = mx - h * (-dy) / (2 * d)
                    hy2 = my - h * dx / (2 * d)

                for cx, cy in [(hx1, hy1), (hx2, hy2)]:
                    cnt = 0
                    for p in points:
                        if (p[0] - cx) ** 2 + (p[1] - cy) ** 2 <= r2 + 1e-7:
                            cnt += 1
                    ans = max(ans, cnt)

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$，枚举 $O(n^2)$ 圆点对，每个统计 $O(n)$，$n \le 100$ 可行。
- **空间复杂度**：$O(1)$。
