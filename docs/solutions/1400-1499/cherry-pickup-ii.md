# [1463. 摘樱桃 II](https://leetcode.cn/problems/cherry-pickup-ii/)

- 标签：数组、动态规划、矩阵
- 难度：困难

## 题目链接

- [1463. 摘樱桃 II - 力扣](https://leetcode.cn/problems/cherry-pickup-ii/)

## 题目大意

**描述**：给定一个 $m \times n$ 的网格 $grid$，每个格子有若干樱桃 $grid[row][col]$。两个机器人分别从 $(0, 0)$ 和 $(0, n-1)$ 出发，每次可以向下、左下、右下移动一格，但不能移出边界。

**要求**：返回两个机器人能摘到的最大樱桃总数。同一个格子被两个机器人同时摘到时只计数一次。

**说明**：
- $m, n \le 70$。
- $grid[row][col] \le 100$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/30/sample_1_1802.png)

```python
输入：grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
输出：24
解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
机器人 1 摘的樱桃数目为 (3 + 2 + 5 + 2) = 12 。
机器人 2 摘的樱桃数目为 (1 + 5 + 5 + 1) = 12 。
樱桃总数为： 12 + 12 = 24 。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/30/sample_2_1802.png)

```python
输入：grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
输出：28
解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
机器人 1 摘的樱桃数目为 (1 + 9 + 5 + 2) = 17 。
机器人 2 摘的樱桃数目为 (1 + 3 + 4 + 3) = 11 。
樱桃总数为： 17 + 11 = 28 。
```

## 解题思路

### 思路 1：三维 DP

#### 1. 核心思想

两个机器人同时移动，每次各走一步。在第 $r$ 行时，机器人 1 在列 $c1$，机器人 2 在列 $c2$。下一行两个机器人分别可以移动到 $c1-1, c1, c1+1$ 和 $c2-1, c2, c2+1$，共 $9$ 种组合。

#### 2. 阶段划分

按行号 $r$ 划分阶段，从顶向下（或从底向上）递推。

#### 3. 定义状态

$dp[r][c1][c2]$：两个机器人分别到达 $(r, c1)$ 和 $(r, c2)$ 时能获得的最大樱桃数。

#### 4. 状态转移方程

$$dp[r][c1][c2] = grid[r][c1] + grid[r][c2] + \max_{\substack{dc1 \in \{-1,0,1\} \\ dc2 \in \{-1,0,1\}}} dp[r-1][c1+dc1][c2+dc2]$$

如果 $c1 == c2$，则 $grid[r][c1]$ 只加一次。

#### 5. 初始条件

$dp[0][0][n-1] = grid[0][0] + grid[0][n-1]$。

如果 $n=1$，起点重叠，只加一次。

#### 6. 最终结果

$\max_{0 \le c1, c2 < n} dp[m-1][c1][c2]$。

#### 7. 举例说明

以 $grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]$ 为例：

```
行0: 3 1 1
行1: 2 5 1
行2: 1 5 5
行3: 2 1 1
```

机器人 1 从 $(0,0)$ 出发，机器人 2 从 $(0,2)$ 出发。

最优路径：机器人 1 走 $(0,0)→(1,0)→(2,1)→(3,0)$，机器人 2 走 $(0,2)→(1,1)→(2,2)→(3,1)$。总樱桃数 $= 3+5+5+1+1+5+1+1 = 22$（注意重叠部分去重）。

### 思路 1：代码

```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[c1][c2] 滚动数组表示当前行
        dp = [[float('-inf')] * n for _ in range(n)]
        dp[0][n - 1] = grid[0][0] + grid[0][n - 1]
        if n == 1:
            dp[0][0] = grid[0][0]

        for r in range(1, m):
            new_dp = [[float('-inf')] * n for _ in range(n)]
            for c1 in range(n):
                for c2 in range(n):
                    # 从上一行的 9 种状态转移
                    for dc1 in (-1, 0, 1):
                        for dc2 in (-1, 0, 1):
                            nc1, nc2 = c1 + dc1, c2 + dc2
                            if 0 <= nc1 < n and 0 <= nc2 < n:
                                cher = grid[r][c1] + grid[r][c2]
                                if c1 == c2:
                                    cher -= grid[r][c1]  # 去重
                                new_dp[c1][c2] = max(new_dp[c1][c2],
                                                     dp[nc1][nc2] + cher)
            dp = new_dp

        ans = 0
        for c1 in range(n):
            for c2 in range(n):
                ans = max(ans, dp[c1][c2])
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n^2 \times 9) = O(m \times n^2)$，$n \le 70$，可行。
- **空间复杂度**：$O(n^2)$，滚动数组优化后仅存当前行和上一行。
