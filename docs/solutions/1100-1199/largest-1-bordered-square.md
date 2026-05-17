# [1139. 最大的以 1 为边界的正方形](https://leetcode.cn/problems/largest-1-bordered-square/)

- 标签：数组、动态规划、矩阵
- 难度：中等

## 题目链接

- [1139. 最大的以 1 为边界的正方形 - 力扣](https://leetcode.cn/problems/largest-1-bordered-square/)

## 题目大意

**描述**：给定一个由 $0$ 和 $1$ 组成的二维网格 $grid$。

**要求**：找到边界全部由 $1$ 组成的最大正方形，返回它的面积（即包含的格子数）。如果不存在，返回 $0$。

**说明**：

- $1 \le grid.length \le 10^{3}$。
- $1 \le grid[0].length \le 10^{3}$。
- $grid[i][j]$ 为 $0$ 或 $1$。

**示例**：

```python
输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9
解释：整个 3×3 的外围全是 1，中间是 0 没关系（只要求边界是 1）。
```

## 解题思路

### 思路 1：预处理 + 枚举

要判断一个正方形是否「边界全是 1」，关键在于快速知道四条边是不是都由连续的一串 1 组成。如果每次去数，就太慢了。

**预处理技巧：** 我们可以提前算出每个位置向左有多少个连续的 1（包括自己），以及向上有多少个连续的 1。这样就能 $O(1)$ 时间判断一个边是否全 1。

**步骤拆解：**

1. **预处理两个辅助数组：**
   - `left[i][j]`：位置 $(i, j)$ 向左看，连续 1 的个数（含自己）。
   - `up[i][j]`：位置 $(i, j)$ 向上看，连续 1 的个数（含自己）。

2. **枚举每个格子作为右下角，尝试不同边长的正方形。**
   - 以 $(i, j)$ 为右下角的可能最大边长 = $\min(left[i][j], up[i][j])$。
   - 从大到小枚举边长 $k$，检查：
     - 上边界：左上角 $(i-k+1, j)$ 向左有至少 $k$ 个 1。
     - 左边界：左上角 $(i, j-k+1)$ 向上有至少 $k$ 个 1。
   - 如果满足条件，说明找到了一个合法的正方形，更新最大边长。

3. 返回最大面积（边长 $\times$ 边长）。

### 思路 1：代码

```python
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 预处理：每个位置向左和向上连续 1 的个数
        left = [[0] * n for _ in range(m)]
        up = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left[i][j] = 1 if j == 0 else left[i][j-1] + 1
                    up[i][j] = 1 if i == 0 else up[i-1][j] + 1
        
        max_side = 0  # 记录最大边长
        for i in range(m):
            for j in range(n):
                # 能取的最大边长
                max_possible = min(left[i][j], up[i][j])
                # 从大到小尝试，找到第一个合法正方形就停下
                for k in range(max_possible, 0, -1):
                    # 检查上边界和左边界的另一条边
                    if (left[i-k+1][j] >= k and    # 上边
                        up[i][j-k+1] >= k):         # 左边
                        max_side = max(max_side, k)
                        break  # 当前格子最大边长已找到
        
        return max_side * max_side
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n \times \min(m, n))$。最坏情况下每个格子都要尝试多种边长。
- **空间复杂度**：$O(m \times n)$。需要两个辅助数组。
