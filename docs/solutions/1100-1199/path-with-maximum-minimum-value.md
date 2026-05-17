# [1102. 得分最高的路径](https://leetcode.cn/problems/path-with-maximum-minimum-value/)

- 标签：深度优先搜索、广度优先搜索、并查集、数组、二分查找、矩阵、堆（优先队列）
- 难度：中等

## 题目链接

- [1102. 得分最高的路径 - 力扣](https://leetcode.cn/problems/path-with-maximum-minimum-value/)

## 题目大意

**描述**：给定一个 $m \times n$ 的整数矩阵 $grid$。从左上角 $(0, 0)$ 出发，每次可以向上、下、左、右四个方向移动，到达右下角 $(m-1, n-1)$。一条路径的分数是该路径上经过的所有格子中的**最小值**。

例如，路径 $8 \to 4 \to 5 \to 9$ 的得分为 $4$（这 $4$ 个数字中最小的那个）。

**要求**：返回从左上角到右下角的所有路径中，分数的最大值。

**说明**：

- $m == grid.length$。
- $n == grid[i].length$。
- $1 \le m, n \le 10^3$。
- $0 \le grid[i][j] \le 10^9$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/08/05/maxgrid1.jpg)

```python
输入：grid = [[5,4,5],[1,2,6],[7,4,6]]
输出：4
解释：得分最高的路径用黄色突出显示。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/08/05/maxgrid2.jpg)

```python
输入：grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
输出：2
```

## 解题思路

### 思路 1：最大堆 + BFS

**为什么用最大堆？** 普通的 BFS 用队列，先进先出，不考虑格子值的大小。但这里我们想优先走大值的格子，所以需要一个能按值的大小取格子的结构——最大堆正好合适。

**关键点**：路径的分数 = 路径上所有格子的最小值。我们每次从堆中取出当前可达的最大值格子，然后更新当前路径的最小值（取 min）。当我们到达终点时，这个最小值就是这条"始终优先走大值"路径的分数。

**拆解步骤**：

1. 把起点 $(0, 0)$ 的值和坐标加入最大堆（Python 的 `heapq` 是最小堆，用负数模拟最大堆）。
2. 用 visited 数组记录已经访问过的格子。
3. 用变量 `min_val` 记录当前路径上的最小值，初始为起点的值。
4. **循环直到到达终点**：
   - 从堆中取出值最大的格子
   - 更新 `min_val = min(min_val, 当前格子值)`
   - 如果当前格子是终点，直接返回 `min_val`
   - 把上下左右四个相邻的未访问格子加入堆中

### 思路 1：代码

```python
import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 最大堆，Python 的 heapq 是最小堆，所以存入负值
        heap = [(-grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        # 四个移动方向：右、下、左、上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # 记录当前路径上的最小值
        min_val = grid[0][0]

        while heap:
            neg_val, x, y = heapq.heappop(heap)
            val = -neg_val  # 把负值转回正值

            # 更新路径上的最小值
            min_val = min(min_val, val)

            # 到达终点，直接返回
            if x == m - 1 and y == n - 1:
                return min_val

            # 尝试四个方向的移动
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 在矩阵范围内且未访问过
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap, (-grid[nx][ny], nx, ny))

        return min_val
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(mn \log(mn))$。用人话说就是：每个格子最多入堆一次，每次堆操作（放入或取出）需要 $\log(mn)$ 时间，总时间 ≈ 格子数 × log(格子数)。
- **空间复杂度**：$O(mn)$。visited 数组和堆需要存储所有格子的信息。
