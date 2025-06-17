## 4. 矩阵线性 DP问题

> **矩阵线性 DP 问题**：问题的输入为二维矩阵的线性 DP 问题。状态一般可定义为 $dp[i][j]$，表示为：从「位置 $(0, 0)$」到达「位置 $(i, j)$」的相关解。

### 4.1 最小路径和

#### 4.1.1 题目链接

- [64. 最小路径和 - 力扣](https://leetcode.cn/problems/minimum-path-sum/)

#### 4.1.2 题目大意

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

#### 4.1.3 解题思路

##### 思路 1：动态规划

###### 1. 划分阶段

按照路径的结尾位置（行位置、列位置组成的二维坐标）进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 为：从位置 $(0, 0)$ 到达位置 $(i, j)$ 的最小路径和。

###### 3. 状态转移方程

当前位置 $(i, j)$ 只能从左侧位置 $(i, j - 1)$ 或者上方位置 $(i - 1, j)$ 到达。为了使得从左上角到达 $(i, j)$ 位置的最小路径和最小，应从 $(i, j - 1)$ 位置和 $(i - 1, j)$ 位置选择路径和最小的位置达到 $(i, j)$。

即状态转移方程为：$dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]$。

###### 4. 初始条件

- 当左侧和上方是矩阵边界时（即 $i = 0, j = 0$），$dp[i][j] = grid[i][j]$。
- 当只有左侧是矩阵边界时（即 $i \ne 0, j = 0$），只能从上方到达，$dp[i][j] = dp[i - 1][j] + grid[i][j]$。
- 当只有上方是矩阵边界时（即 $i = 0, j \ne 0$），只能从左侧到达，$dp[i][j] = dp[i][j - 1] + grid[i][j]$。

###### 5. 最终结果

根据状态定义，最后输出 $dp[rows - 1][cols - 1]$（即从左上角到达 $(rows - 1, cols - 1)$ 位置的最小路径和）即可。其中 $rows$、$cols$ 分别为 $grid$ 的行数、列数。

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

### 4.2 最大正方形

#### 4.2.1 题目链接

- [221. 最大正方形 - 力扣](https://leetcode.cn/problems/maximal-square/)

#### 4.2.2 题目大意

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

#### 4.2.3 解题思路

##### 思路 1：动态规划

###### 1. 划分阶段

按照正方形的右下角坐标进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 表示为：以矩阵位置 $(i, j)$ 为右下角，且值包含 $1$ 的正方形的最大边长。

###### 3. 状态转移方程

只有当矩阵位置 $(i, j)$ 值为 $1$ 时，才有可能存在正方形。

- 如果矩阵位置 $(i, j)$ 上值为 $0$，则 $dp[i][j] = 0$。
- 如果矩阵位置 $(i, j)$ 上值为 $1$，则 $dp[i][j]$ 的值由该位置上方、左侧、左上方三者共同约束的，为三者中最小值加 $1$。即：$dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1$。

###### 4. 初始条件

- 默认所有以矩阵位置 $(i, j)$ 为右下角，且值包含 $1$ 的正方形的最大边长都为 $0$，即 $dp[i][j] = 0$。

###### 5. 最终结果

根据我们之前定义的状态， $dp[i][j]$ 表示为：以矩阵位置 $(i, j)$ 为右下角，且值包含 $1$ 的正方形的最大边长。则最终结果为所有 $dp[i][j]$ 中的最大值。

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

## 5. 无串线性 DP 问题

> **无串线性 DP 问题**：问题的输入不是显式的数组或字符串，但依然可分解为若干子问题的线性 DP 问题。

### 5.1 整数拆分

#### 5.1.1 题目链接

- [343. 整数拆分 - 力扣](https://leetcode.cn/problems/integer-break/)

#### 5.1.2 题目大意

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

#### 5.1.3 解题思路

##### 思路 1：动态规划

###### 1. 划分阶段

按照正整数进行划分。

###### 2. 定义状态

定义状态 $dp[i]$ 表示为：将正整数 $i$ 拆分为至少 $2$ 个正整数的和之后，这些正整数的最大乘积。

###### 3. 状态转移方程

当 $i \ge 2$ 时，假设正整数 $i$ 拆分出的第 $1$ 个正整数是 $j(1 \le j < i)$，则有两种方法：

1. 将 $i$ 拆分为 $j$ 和 $i - j$ 的和，且 $i - j$ 不再拆分为多个正整数，此时乘积为：$j \times (i - j)$。
2. 将 $i$ 拆分为 $j$ 和 $i - j$ 的和，且 $i - j$ 继续拆分为多个正整数，此时乘积为：$j \times dp[i - j]$。

则 $dp[i]$ 取两者中的最大值。即：$dp[i] = max(j \times (i - j), j \times dp[i - j])$。

由于 $1 \le j < i$，需要遍历 $j$ 得到 $dp[i]$ 的最大值，则状态转移方程如下：

$dp[i] = max_{1 \le j < i}\lbrace max(j \times (i - j), j \times dp[i - j]) \rbrace$。

###### 4. 初始条件

- $0$ 和 $1$ 都不能被拆分，所以 $dp[0] = 0, dp[1] = 0$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i]$ 表示为：将正整数 $i$ 拆分为至少 $2$ 个正整数的和之后，这些正整数的最大乘积。则最终结果为 $dp[n]$。

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

### 5.2 只有两个键的键盘

#### 5.2.1 题目链接

- [650. 只有两个键的键盘](https://leetcode.cn/problems/2-keys-keyboard/)

#### 5.2.2 题目大意

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

#### 5.2.3 解题思路

##### 思路 1：动态规划

###### 1. 划分阶段

按照字符 `'A'`  的个数进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i]$ 表示为：通过「复制」和「粘贴」操作，得到 $i$ 个字符 `'A'`，最少需要的操作数。

###### 3. 状态转移方程

1. 对于 $i$ 个字符 `'A'`，如果 $i$ 可以被一个小于 $i$ 的整数 $j$ 除尽（$j$ 是 $i$ 的因子），则说明 $j$ 个字符 `'A'` 可以通过「复制」+「粘贴」总共 $\frac{i}{j}$ 次得到 $i$ 个字符 `'A'`。
2. 而得到 $j$ 个字符 `'A'`，最少需要的操作数可以通过 $dp[j]$ 获取。

则我们可以枚举 $i$ 的因子，从中找到在满足 $j$ 能够整除 $i$ 的条件下，最小的 $dp[j] + \frac{i}{j}$，即为 $dp[i]$，即 $dp[i] = min_{j | i}(dp[i], dp[j] + \frac{i}{j})$。

由于 $j$ 能够整除 $i$，则 $j$ 与 $\frac{i}{j}$ 都是 $i$ 的因子，两者中必有一个因子是小于等于 $\sqrt{i}$ 的，所以在枚举 $i$ 的因子时，我们只需要枚举区间 $[1, \sqrt{i}]$ 即可。

综上所述，状态转移方程为：$dp[i] = min_{j | i}(dp[i], dp[j] + \frac{i}{j}, dp[\frac{i}{j}] + j)$。

###### 4. 初始条件

- 当 $i = 1$ 时，最少需要的操作数为 $0$。所以 $dp[1] = 0$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i]$ 表示为：通过「复制」和「粘贴」操作，得到 $i$ 个字符 `'A'`，最少需要的操作数。 所以最终结果为 $dp[n]$。

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

## 题目练习

- [矩阵线性 DP 问题题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E7%9F%A9%E9%98%B5%E7%BA%BF%E6%80%A7-dp-%E9%97%AE%E9%A2%98)
- [矩阵线性 DP 问题题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E6%97%A0%E4%B8%B2%E7%BA%BF%E6%80%A7-dp-%E9%97%AE%E9%A2%98)

## 参考资料

- 【书籍】算法竞赛进阶指南
- 【文章】[动态规划概念和基础线性DP | 潮汐朝夕](https://chengzhaoxi.xyz/1a4a2483.html)
