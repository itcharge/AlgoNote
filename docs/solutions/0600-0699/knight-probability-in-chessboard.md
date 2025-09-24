# [0688. 骑士在棋盘上的概率](https://leetcode.cn/problems/knight-probability-in-chessboard/)

- 标签：动态规划
- 难度：中等

## 题目链接

- [0688. 骑士在棋盘上的概率 - 力扣](https://leetcode.cn/problems/knight-probability-in-chessboard/)

## 题目大意

**描述**：在一个 `n * n` 的国际象棋棋盘上，一个骑士从单元格 `(row, column)` 开始，尝试进行 `k` 次 移动。行和列是从 `0` 开始的，左上角的单元格是 `(0, 0)`，右下角的单元格是 `(n - 1, n - 1)`。

象棋骑士有 `8` 种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/knight.png)

每次骑士要移动时，它都会随机从 `8` 种可能的移动中选择一种（即使棋子会离开棋盘），然后移动到那里。骑士继续移动，直到它走了 `k` 步或离开了棋盘。

现在给定代表棋盘大小的整数 `n`、代表骑士移动次数的整数 `k`，以及代表骑士初始位置的坐标 `row` 和 `column`。

**要求**：返回骑士在棋盘停止移动后仍留在棋盘上的概率。

**说明**：

- $1 \le n \le 25$。
- $0 \le k \le 100$。
- $0 \le row, column \le n$。

**示例**：

- 示例 1：

```python
输入：n = 3, k = 2, row = 0, column = 0
输出：0.0625
解释：有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。在每一个位置上，也有两种移动可以让骑士留在棋盘上。骑士留在棋盘上的总概率是 0.0625。
```

## 解题思路

### 思路 1：动态规划

###### 1. 阶段划分

按照骑士所在位置和所走步数进行阶段划分。

###### 2. 定义状态

定义状态 `dp[i][j][p]` 表示为：从位置 `(i, j)` 出发，移动不超过 `p` 步的情况下，最后仍留在棋盘内的概率。

###### 3. 状态转移方程

根据象棋骑士的 `8` 种可能的走法，`dp[i][j][p]` 的来源有八个方向（超出棋盘的无需再考虑）：

- 假设下一步的落点为 `(new_i, new_j)`。从当前步选择 `8` 个方向其中之一作为下一步方向的概率为 $\frac{1}{8}$。
- 而每个方向上落点仍在棋盘内的概率为 `dp[new_i][new_j][p - 1]`。所以从 `(i, j)` 走到 `(new_i, new_j)` 的可能性为 $dp[new_i][new_j] \times \frac{1}{8}$。

最终 $dp[i][j][p]$ 来源为 `8` 个方向上落点的概率之和，即：$dp[i][j][p] = \sum{ dp[new_i][new_j] \times \frac{1}{8} }$。

###### 4. 初始条件

- 从位置 `(i, j)` 出发，移动不超过 `0` 步的情况下，最后仍留在棋盘内的概率为 `1`。

###### 5. 最终结果

根据我们之前定义的状态，`dp[i][j][p]` 表示为：从位置 `(i, j)` 出发，移动不超过 `p` 步的情况下，最后仍留在棋盘内的概率。则最终结果为 `dp[row][column][k]`。

### 思路 1：动态规划代码

```python
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = 1

        directions = {(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)}

        for p in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for direction in directions:
                        new_i = i + direction[0]
                        new_j = j + direction[1]
                        if 0 <= new_i < n and 0 <= new_j < n:
                            dp[i][j][p] += dp[new_i][new_j][p - 1] / 8
        
        return dp[row][column][k]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 * k)$。外三层循环的时间复杂度为 $O(n^2 * k)$，内层关于 `directions` 的循环每次执行 `8` 次，可以看做是常数级时间复杂度。
- **空间复杂度**：$O(n^2 * k)$。用到了三维数组保存状态。
