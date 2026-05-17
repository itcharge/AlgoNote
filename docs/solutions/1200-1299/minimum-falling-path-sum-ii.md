# [1289. 下降路径最小和 II](https://leetcode.cn/problems/minimum-falling-path-sum-ii/)

- 标签：数组、动态规划、矩阵
- 难度：困难

## 题目链接

- [1289. 下降路径最小和 II - 力扣](https://leetcode.cn/problems/minimum-falling-path-sum-ii/)

## 题目大意

**描述**：给定一个 $n \times n$ 的整数矩阵 $grid$。

**要求**：找出一条下降路径，使得路径上的数字之和最小，并返回这个最小和。

下降路径定义为：从第一行开始，每次可以向下移动到下一行的任意一列，但不能和当前列在同一列。即如果当前在第 $i$ 行第 $j$ 列，下一步可以走到第 $i+1$ 行的任意列 $k$，其中 $k \ne j$。

**说明**：

- $1 \le n \le 200$。
- $-99 \le grid[i][j] \le 99$。

**示例**：

- 示例 1：

```python
输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
输出：13
解释：最小下降路径为 1→5→7 或 1→6→8 或 2→4→8 或 2→6→7 或 3→4→7 或 3→5→8，总和为 13。
```

- 示例 2：

```python
输入：grid = [[-37,51,-36,34,-22],[82,4,30,14,38],[-68,-52,-92,65,-85],[-49,-3,-77,8,-19],[-60,-71,-21,-67,65]]
输出：-268
```

## 解题思路

### 思路 1：动态规划 + 最小值和次小值优化

#### 1. 阶段划分

按行划分阶段。从第 $0$ 行开始，逐行向下递推。每走到第 $i$ 行时，路径的和取决于上一行走到了哪一列。

#### 2. 定义状态

定义 $dp[i][j]$ 表示从第 $0$ 行走到第 $i$ 行第 $j$ 列时的最小路径和。

#### 3. 状态转移方程

要走到 $(i, j)$，上一行不能在同一列，所以：

$$dp[i][j] = grid[i][j] + \min\limits_{k \ne j} dp[i-1][k]$$

直接按这个公式做，每行每列都需要遍历上一行的 $n$ 列找最小值，总时间复杂度 $O(n^3)$（$n \le 200$ 时 $200^3 = 800$ 万，其实也可以接受）。

但还有更优的做法。

#### 4. 优化：记录上一行的最小值和次小值

注意到 $dp[i][j]$ 依赖于上一行除了第 $j$ 列之外的最小值。这意味着我们不需要为每个 $j$ 都扫描一整行，而是可以只记录上一行的**最小值**和**次小值**以及最小值所在的列：

- 如果 $j \ne min\_col$（当前列不是上一行最小值所在的列），那么 $\min_{k \ne j} dp[i-1][k]$ 就是上一行的最小值。
- 如果 $j == min\_col$（当前列是上一行最小值所在的列），那么 $\min_{k \ne j} dp[i-1][k]$ 就是上一行的次小值。

这样每行的状态转移可以 $O(n)$ 完成，总时间复杂度降到 $O(n^2)$。

#### 5. 初始条件

- $dp[0][j] = grid[0][j]$（第一行的值就是初始值）。
- 可以用滚动数组优化空间，因为 $dp[i]$ 只依赖于 $dp[i-1]$。

#### 6. 最终结果

最后一行的最小值 $\min\limits_{j} dp[n-1][j]$。

#### 7. 结合示例走一遍

$grid = [[1,2,3],[4,5,6],[7,8,9]]$

**第 0 行**：$dp[0] = [1, 2, 3]$，最小值 $1$（列 $0$），次小值 $2$（列 $1$）。

**第 1 行**：
- $j=0$：$min\_col=0$，取次小值 $2$ → $dp[1][0] = 4 + 2 = 6$
- $j=1$：$min\_col=0$，取最小值 $1$ → $dp[1][1] = 5 + 1 = 6$
- $j=2$：$min\_col=0$，取最小值 $1$ → $dp[1][2] = 6 + 1 = 7$
- 第 1 行 $dp[1] = [6, 6, 7]$，最小值 $6$（列 $0$ 或 $1$，选列 $0$），次小值 $6$（列 $1$）。

**第 2 行**：
- $j=0$：$min\_col=0$，取次小值 $6$ → $dp[2][0] = 7 + 6 = 13$
- $j=1$：$min\_col=0$，取最小值 $6$ → $dp[2][1] = 8 + 6 = 14$
- $j=2$：$min\_col=0$，取最小值 $6$ → $dp[2][2] = 9 + 6 = 15$

最小值为 $13$，对应路径 $1→5→7$ 或 $1→6→8$。

### 思路 1：代码

```python
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        # 上一行的 dp 值
        dp_prev = grid[0]

        for i in range(1, n):
            # 找出上一行的最小值和次小值，及其所在列
            min_val = second_min_val = float('inf')
            min_col = -1
            for j in range(n):
                val = dp_prev[j]
                if val < min_val:
                    second_min_val = min_val
                    min_val = val
                    min_col = j
                elif val < second_min_val:
                    second_min_val = val

            # 计算当前行的 dp 值
            dp_curr = [0] * n
            for j in range(n):
                if j == min_col:
                    dp_curr[j] = grid[i][j] + second_min_val
                else:
                    dp_curr[j] = grid[i][j] + min_val

            dp_prev = dp_curr

        return min(dp_prev)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是矩阵的边长。每行需要 $O(n)$ 找出最小值和次小值，$O(n)$ 计算当前行的 $dp$ 值，共 $n$ 行。
- **空间复杂度**：$O(n)$，使用滚动数组只存储上一行的 $dp$ 值。

### 思路 2：无优化的 $O(n^3)$ 版本（直观理解）

```python
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(n):
                best = float('inf')
                for k in range(n):
                    if k != j:
                        best = min(best, dp[i - 1][k])
                dp[i][j] = grid[i][j] + best

        return min(dp[n - 1])
```

这个版本更直观易懂，$n \le 200$ 时 $O(n^3) = 800$ 万次操作，在 Python 中也可以顺利通过。但面试时能给出 $O(n^2)$ 的最小-次小值优化版本会更好。
