## 1. 矩阵线性 DP 问题简介

> **矩阵线性 DP 问题**：是指输入为二维矩阵的动态规划问题。常见的状态定义为 $dp[i][j]$，表示从起点「$(0, 0)$」到达「$(i, j)$」的最优解（如最小路径和、最大路径和等）。

## 2. 矩阵线性 DP 问题经典题目

### 2.1 经典例题：最小路径和

#### 2.1.1 题目链接

- [64. 最小路径和 - 力扣](https://leetcode.cn/problems/minimum-path-sum/)

#### 2.1.2 题目大意

**描述**：给定一个包含非负整数的 $m \times n$  大小的网格 $grid$。

**要求**：找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明**：

- 每次只能向下或者向右移动一步。
- $m == grid.length$。
- $n == grid[i].length$。
- $1 \le m, n \le 200$。
- $0 \le grid[i][j] \le 100$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg) 

```python
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
```

- 示例 2：

```python
输入：grid = [[1,2,3],[4,5,6]]
输出：12
```

#### 2.1.3 解题思路

##### 思路 1：动态规划

###### 1. 阶段划分

以路径终点的位置（即二维坐标 $(i, j)$）作为阶段。

###### 2. 定义状态

设 $dp[i][j]$ 表示从左上角 $(0, 0)$ 出发，到达 $(i, j)$ 的最小路径和。

###### 3. 状态转移方程

当前位置 $(i, j)$ 只能从左边 $(i, j - 1)$ 或上方 $(i - 1, j)$ 转移过来。为了保证路径和最小，应选择这两者中较小的路径和，再加上当前格子的值 $grid[i][j]$。

则状态转移方程为：$dp[i][j] = \min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]$。

###### 4. 初始条件

- 当 $i = 0, j = 0$ 时，$dp[0][0] = grid[0][0]$。
- 当 $i > 0, j = 0$ 时，只能从上方到达，$dp[i][0] = dp[i - 1][0] + grid[i][0]$。
- 当 $i = 0, j > 0$ 时，只能从左侧到达，$dp[0][j] = dp[0][j - 1] + grid[0][j]$。

###### 5. 最终结果

最终答案为 $dp[rows - 1][cols - 1]$，即从左上角到右下角的最小路径和。其中 $rows$ 和 $cols$ 分别为 $grid$ 的行数和列数。

##### 思路 1：代码

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        dp[0][0] = grid[0][0]
        
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
            
        return dp[rows - 1][cols - 1]
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(m * n)$，其中 $m$、$n$ 分别为 $grid$ 的行数和列数。
- **空间复杂度**：$O(m * n)$。

### 2.2 经典例题：最大正方形

#### 2.2.1 题目链接

- [221. 最大正方形 - 力扣](https://leetcode.cn/problems/maximal-square/)

#### 2.2.2 题目大意

**描述**：给定一个由 `'0'` 和 `'1'` 组成的二维矩阵 $matrix$。

**要求**：找到只包含 `'1'` 的最大正方形，并返回其面积。

**说明**：

- $m == matrix.length$。
- $n == matrix[i].length$。
- $1 \le m, n \le 300$。
- $matrix[i][j]$ 为 `'0'` 或 `'1'`。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)

```python
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)

```python
输入：matrix = [["0","1"],["1","0"]]
输出：1
```

#### 2.2.3 解题思路

##### 思路 1：动态规划

###### 1. 阶段划分

以正方形的右下角坐标 $(i, j)$ 作为阶段。

###### 2. 定义状态

令 $dp[i][j]$ 表示以 $(i, j)$ 为右下角、且全部为 $1$ 的最大正方形的边长。

###### 3. 状态转移方程

仅当 $matrix[i][j] == 1$ 时，$(i, j)$ 位置才能作为正方形的右下角：

- 如果 $matrix[i][j] == 0$，则 $dp[i][j] = 0$；
- 如果 $matrix[i][j] == 1$，则 $dp[i][j] = \min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1$，即取其上方、左方、左上方的最小值加 $1$。

###### 4. 初始条件

初始时，令所有 $dp[i][j] = 0$，即默认以 $(i, j)$ 为右下角的最大正方形边长为 $0$。

###### 5. 最终结果

遍历所有 $dp[i][j]$，取最大值即为只包含 $1$ 的最大正方形的边长，面积为其平方。

##### 思路 1：代码

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_size = 0
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    max_size = max(max_size, dp[i][j])
        return max_size * max_size
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$，其中 $m$、$n$ 分别为二维矩阵 $matrix$ 的行数和列数。
- **空间复杂度**：$O(m \times n)$。

## 3. 无串线性 DP 问题简介

> **无串线性 DP 问题**：问题的输入不是显式的数组或字符串，但依然可分解为若干子问题的线性 DP 问题。

## 4. 无串线性 DP 问题经典题目

### 4.1 经典例题：整数拆分

#### 4.1.1 题目链接

- [343. 整数拆分 - 力扣](https://leetcode.cn/problems/integer-break/)

#### 4.1.2 题目大意

**描述**：给定一个正整数 $n$，将其拆分为 $k (k \ge 2)$ 个正整数的和，并使这些整数的乘积最大化。

**要求**：返回可以获得的最大乘积。

**说明**：

- $2 \le n \le 58$。

**示例**：

- 示例 1：

```python
输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
```

- 示例 2：

```python
输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
```

#### 4.1.3 解题思路

##### 思路 1：动态规划

###### 1. 阶段划分

以正整数 $i$ 为阶段，从小到大依次考虑每个 $i$。

###### 2. 定义状态

设 $dp[i]$ 表示将正整数 $i$ 至少拆分成两个正整数之和后，所得的最大乘积。

###### 3. 状态转移方程

对于每个 $i \ge 2$，枚举第一个拆分出的正整数 $j$，其中 $1 \le j < i$。此时有两种选择：

1. 将 $i$ 拆分为 $j$ 和 $i - j$，如果 $i - j$ 不再继续拆分，则乘积为 $j \times (i - j)$；
2. 将 $i$ 拆分为 $j$ 和 $i - j$，如果 $i - j$ 继续拆分，则乘积为 $j \times dp[i - j]$；

最终 $dp[i]$ 取上述两种情况的最大值，即：

$$
dp[i] = \max_{1 \le j < i} \left\{ \max\left(j \times (i-j),\ j \times dp[i-j]\right) \right\}
$$

###### 4. 初始条件

- $dp[0] = 0, dp[1] = 0$，因为 $0$ 和 $1$ 无法拆分。

###### 5. 最终结果

最终答案为 $dp[n]$，即将正整数 $n$ 拆分为至少两个正整数之和后所得的最大乘积。

##### 思路 1：代码

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)
        return dp[n]
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(n)$。

### 4.2 经典例题：只有两个键的键盘

#### 4.2.1 题目链接

- [650. 只有两个键的键盘](https://leetcode.cn/problems/2-keys-keyboard/)

#### 4.2.2 题目大意

**描述**：最初记事本上只有一个字符 `'A'`。你每次可以对这个记事本进行两种操作：

- **Copy All（复制全部）**：复制这个记事本中的所有字符（不允许仅复制部分字符）。
- **Paste（粘贴）**：粘贴上一次复制的字符。

现在，给定一个数字 $n$，需要使用最少的操作次数，在记事本上输出恰好 $n$ 个 `'A'` 。

**要求**：返回能够打印出 $n$ 个 `'A'` 的最少操作次数。

**说明**：

- $1 \le n \le 1000$。

**示例**：

- 示例 1：

```python
输入：3
输出：3
解释
最初, 只有一个字符 'A'。
第 1 步, 使用 Copy All 操作。
第 2 步, 使用 Paste 操作来获得 'AA'。
第 3 步, 使用 Paste 操作来获得 'AAA'。
```

- 示例 2：

```python
输入：n = 1
输出：0
```

#### 4.2.3 解题思路

##### 思路 1：动态规划

###### 1. 阶段划分

以当前记事本上字符 `'A'` 的个数 $i$ 作为阶段。

###### 2. 定义状态

设 $dp[i]$ 表示通过若干次「复制全部」和「粘贴」操作，得到恰好 $i$ 个字符 `'A'` 所需的最少操作次数。

###### 3. 状态转移方程

对于每个 $i$，我们可以枚举 $i$ 的所有因子 $j$（$1 \leq j < i$ 且 $i \bmod j = 0$）。如果 $i$ 可以由 $j$ 通过若干次粘贴得到，即 $i = j \times k$，那么可以先通过 $dp[j]$ 步得到 $j$ 个 `'A'`，再执行一次「复制全部」和 $k - 1$ 次「粘贴」，共 $dp[j] + k$ 步。由于 $k = i / j$，因此状态转移为 $dp[i] = \min(dp[i], dp[j] + i / j)$。

同理，$j$ 和 $i/j$ 都是 $i$ 的因子，二者至少有一个不大于 $\sqrt{i}$，因此只需枚举 $j$ 从 $1$ 到 $\sqrt{i}$，并同时考虑 $j$ 和 $i/j$ 两种分解方式：

$$
dp[i] = \min\left(dp[i],\ dp[j] + \frac{i}{j},\ dp[\frac{i}{j}] + j\right)
$$

###### 4. 初始条件

- $dp[1] = 0$，即初始只有一个 `'A'` 时不需要任何操作。

###### 5. 最终结果

最终答案为 $dp[n]$，即得到 $n$ 个字符 `'A'` 所需的最少操作次数。

##### 思路 1：动态规划代码

```python
import math

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = float('inf')
            for j in range(1, int(math.sqrt(n)) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)

        return dp[n]
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n \sqrt{n})$。外层循环遍历的时间复杂度是 $O(n)$，内层循环遍历的时间复杂度是 $O(\sqrt{n})$，所以总体时间复杂度为 $O(n \sqrt{n})$。
- **空间复杂度**：$O(n)$。用到了一维数组保存状态，所以总体空间复杂度为 $O(n)$。

## 练习题目

- [0718. 最长重复子数组](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/maximum-length-of-repeated-subarray.md)
- [0072. 编辑距离](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/edit-distance.md)
- [0064. 最小路径和](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/minimum-path-sum.md)
- [0221. 最大正方形](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/maximal-square.md)
- [0343. 整数拆分](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/integer-break.md)
- [0650. 两个键的键盘](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/2-keys-keyboard.md)

- [矩阵线性 DP 问题题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E7%9F%A9%E9%98%B5%E7%BA%BF%E6%80%A7-dp-%E9%97%AE%E9%A2%98)
- [无串线性 DP 问题题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E6%97%A0%E4%B8%B2%E7%BA%BF%E6%80%A7-dp-%E9%97%AE%E9%A2%98)

## 参考资料

- 【书籍】算法竞赛进阶指南
- 【文章】[动态规划概念和基础线性DP | 潮汐朝夕](https://chengzhaoxi.xyz/1a4a2483.html)
