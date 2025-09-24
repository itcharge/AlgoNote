## 1. 区间动态规划简介

> **区间动态规划（区间 DP）**：是一类以区间为阶段、以区间的左右端点为状态的动态规划方法。它常用于解决「在一段区间内进行某种操作，使得总代价最小或总价值最大」这类问题。区间 DP 的核心思想是：先解决小区间的最优解，再逐步合并得到大区间的最优解，最终得到整个区间的最优解。

区间 DP 的状态通常用 $dp[i][j]$ 表示区间 $[i, j]$ 的最优解。状态的转移依赖于比 $[i, j]$ 更小的子区间的状态。

常见的区间 DP 问题大致分为两类：

1. **单区间扩展型**：通过在区间 $[i + 1, j - 1]$ 的基础上，向两侧扩展得到 $[i, j]$，例如回文串、石子合并等问题。
2. **多区间合并型**：将区间 $[i, j]$ 拆分为两个或多个更小的区间（如 $[i, k]$ 和 $[k + 1, j]$），通过合并这些小区间的最优解得到大区间的最优解。

接下来，我们将分别介绍这两类区间 DP 问题的基本解题思路。

## 2. 区间 DP 问题的基本思路

### 2.1 第 1 类区间 DP 问题的基本思路

这类区间 DP 通常是「从中间向两侧扩展」，其状态转移方程一般为：$dp[i][j] = \max \lbrace dp[i + 1][j - 1],\ dp[i + 1][j],\ dp[i][j - 1] \rbrace + cost[i][j]$，其中 $i \leq j$。

- $dp[i][j]$ 表示区间 $[i, j]$（即下标 $i$ 到 $j$ 的所有元素）上的最优解（如最大价值）。
- $cost[i][j]$ 表示将小区间扩展到 $[i, j]$ 时产生的代价。
- 取 $\max$ 或 $\min$ 取决于题目要求最大值还是最小值。

基本解题流程如下：

1. 枚举区间起点 $i$；
2. 枚举区间终点 $j$；
3. 按照状态转移方程，利用更小区间的最优解递推出更大区间的最优解。

对应代码如下：

```python
for i in range(size - 1, -1, -1):       # 枚举区间起点
    for j in range(i + 1, size):        # 枚举区间终点
        # 状态转移方程，计算转移到更大区间后的最优值
        dp[i][j] = max(dp[i + 1][j - 1], dp[i + 1][j], dp[i][j - 1]) + cost[i][j]
```

### 2.2 第 2 类区间 DP 问题的基本思路

这类区间 DP 的核心思想是：将一个大区间 $[i, j]$ 拆分成两个更小的子区间 $[i, k]$ 和 $[k + 1, j]$，通过合并子区间的最优解，得到大区间的最优解。常见的状态转移方程为：

$$
dp[i][j] = \max/\min \{dp[i][k] + dp[k+1][j] + cost[i][j]\},\quad i \leq k < j
$$

其中：

1. $dp[i][j]$ 表示区间 $[i, j]$（即下标 $i$ 到 $j$ 的所有元素）上的最优解（如最大价值或最小代价）。
2. $cost[i][j]$ 表示将 $[i, k]$ 和 $[k+1, j]$ 合并成 $[i, j]$ 时产生的额外代价。
3. 取 $\max$ 或 $\min$ 取决于题目要求最大值还是最小值。

这类区间 DP 的通用解题步骤如下：

1. 枚举区间长度（从小到大，保证子区间已被计算）；
2. 枚举区间起点 $i$，根据区间长度确定终点 $j$；
3. 枚举所有可能的分割点 $k$，用状态转移方程更新 $dp[i][j]$ 的最优值。

对应代码如下：

```python
for l in range(1, n):               # 枚举区间长度
    for i in range(n):              # 枚举区间起点
        j = i + l - 1               # 根据起点和长度得到终点
        if j >= n:
            break
        dp[i][j] = float('-inf')    # 初始化 dp[i][j]
        for k in range(i, j + 1):   # 枚举区间分割点
            # 状态转移方程，计算合并区间后的最优值
            dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + cost[i][j])
```

## 3. 区间 DP 问题的应用

下面我们根据几个例子来讲解一下区间 DP 问题的具体解题思路。

### 3.1 经典例题：最长回文子序列

#### 3.1.1 题目链接

- [516. 最长回文子序列 - 力扣](https://leetcode.cn/problems/longest-palindromic-subsequence/)

#### 3.1.2 题目大意

**描述**：给定一个字符串 $s$。

**要求**：找出其中最长的回文子序列，并返回该序列的长度。

**说明**：

- **子序列**：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
- $1 \le s.length \le 1000$。
- $s$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb"。
```

- 示例 2：

```python
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb"。
```

#### 3.1.3 解题思路

##### 思路 1：动态规划

###### 1. 阶段划分

按照区间长度进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 表示为：字符串 $s$ 在区间 $[i, j]$ 范围内的最长回文子序列长度。

###### 3. 状态转移方程

我们对区间 $[i, j]$ 边界位置上的字符 $s[i]$ 与 $s[j]$ 进行分类讨论：

1. 如果 $s[i] = s[j]$，则 $dp[i][j]$ 为区间 $[i + 1, j - 1]$ 范围内最长回文子序列长度 + $2$，即 $dp[i][j] = dp[i + 1][j - 1] + 2$。
2. 如果 $s[i] \ne s[j]$，则 $dp[i][j]$ 取决于以下两种情况，取其最大的一种：
	1. 加入 $s[i]$ 所能组成的最长回文子序列长度，即：$dp[i][j] = dp[i][j - 1]$。
	2. 加入 $s[j]$ 所能组成的最长回文子序列长度，即：$dp[i][j] = dp[i - 1][j]$。

则状态转移方程为：

$dp[i][j] = \begin{cases} max \lbrace dp[i + 1][j - 1] + 2 \rbrace & s[i] = s[j]  \cr max \lbrace dp[i][j - 1], dp[i - 1][j] \rbrace & s[i] \ne s[j] \end{cases}$

###### 4. 初始条件

- 单个字符的最长回文序列是 $1$，即 $dp[i][i] = 1$。

###### 5. 最终结果

由于 $dp[i][j]$ 依赖于 $dp[i + 1][j - 1]$、$dp[i + 1][j]$、$dp[i][j - 1]$，所以我们应该按照从下到上、从左到右的顺序进行遍历。

根据我们之前定义的状态，$dp[i][j]$ 表示为：字符串 $s$ 在区间 $[i, j]$ 范围内的最长回文子序列长度。所以最终结果为 $dp[0][size - 1]$。

##### 思路 1：代码

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1

        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][size - 1]
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为字符串 $s$ 的长度。
- **空间复杂度**：$O(n^2)$。

### 3.2 经典例题：戳气球

#### 3.2.1 题目链接

- [312. 戳气球 - 力扣](https://leetcode.cn/problems/burst-balloons/)

#### 3.2.2 题目大意

**描述**：有 $n$ 个气球，编号为 $0 \sim n - 1$，每个气球上都有一个数字，这些数字存在数组 $nums$ 中。现在开始戳破气球。其中戳破第 $i$ 个气球，可以获得 $nums[i - 1] \times nums[i] \times nums[i + 1]$ 枚硬币，这里的 $i - 1$ 和 $i + 1$ 代表和 $i$ 相邻的两个气球的编号。如果 $i - 1$ 或 $i + 1$ 超出了数组的边界，那么就当它是一个数字为 $1$ 的气球。

**要求**：求出能获得硬币的最大数量。

**说明**：

- $n == nums.length$。
- $1 \le n \le 300$。
- $0 \le nums[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
```

- 示例 2：

```python
输入：nums = [1,5]
输出：10
解释：
nums = [1,5] --> [5] --> []
coins = 1*1*5 +  1*5*1 = 10
```

#### 3.2.3 解题思路

##### 思路 1：动态规划

根据题意，如果 $i - 1$ 或 $i + 1$ 超出了数组的边界，那么就当它是一个数字为 $1$ 的气球。我们可以预先在 $nums$ 的首尾位置，添加两个数字为 $1$ 的虚拟气球，这样变成了 $n + 2$ 个气球，气球对应编号也变为了 $0 \sim n + 1$。

对应问题也变成了：给定 $n + 2$ 个气球，每个气球上有 $1$ 个数字，代表气球上的硬币数量，当我们戳破气球 $nums[i]$ 时，就能得到对应 $nums[i - 1] \times nums[i] \times nums[i + 1]$ 枚硬币。现在要戳破 $0 \sim n + 1$ 之间的所有气球（不包括编号 $0$ 和编号 $n + 1$ 的气球），请问最多能获得多少枚硬币？

###### 1. 阶段划分

按照区间长度进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 表示为：戳破所有气球 $i$ 与气球 $j$ 之间的气球（不包含气球 $i$ 和 气球 $j$），所能获取的最多硬币数。

###### 3. 状态转移方程

假设气球 $i$ 与气球 $j$ 之间最后一个被戳破的气球编号为 $k$。则 $dp[i][j]$ 取决于由 $k$ 作为分割点分割出的两个区间 $(i, k)$ 与 

$(k, j)$ 上所能获取的最多硬币数 + 戳破气球 $k$ 所能获得的硬币数，即状态转移方程为：

$dp[i][j] = max \lbrace dp[i][k] + dp[k][j] + nums[i] \times nums[k] \times nums[j] \rbrace, \quad i < k < j$

###### 4. 初始条件

- $dp[i][j]$ 表示的是开区间，则 $i < j - 1$。而当 $i \ge j - 1$ 时，所能获得的硬币数为 $0$，即 $dp[i][j] = 0, \quad i \ge j - 1$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i][j]$ 表示为：戳破所有气球 $i$ 与气球 $j$ 之间的气球（不包含气球 $i$ 和 气球 $j$），所能获取的最多硬币数。所以最终结果为 $dp[0][n + 1]$。

##### 思路 1：代码

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        size = len(nums)
        arr = [0 for _ in range(size + 2)]
        arr[0] = arr[size + 1] = 1
        for i in range(1, size + 1):
            arr[i] = nums[i - 1]
        
        dp = [[0 for _ in range(size + 2)] for _ in range(size + 2)]

        for l in range(3, size + 3):
            for i in range(0, size + 2):
                j = i + l - 1
                if j >= size + 2:
                    break
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + arr[i] * arr[j] * arr[k])
        
        return dp[0][size + 1]
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$，其中 $n$ 为气球数量。
- **空间复杂度**：$O(n^2)$。

## 练习题目

- [0005. 最长回文子串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/longest-palindromic-substring.md)
- [0516. 最长回文子序列](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0500-0599/longest-palindromic-subsequence.md)
- [0312. 戳气球](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/burst-balloons.md)
- [0486. 预测赢家](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0400-0499/predict-the-winner.md)
- [1547. 切棍子的最小成本](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1500-1599/minimum-cost-to-cut-a-stick.md)
- [0664. 奇怪的打印机](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/strange-printer.md)

- [区间 DP 题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8C%BA%E9%97%B4-dp-%E9%A2%98%E7%9B%AE)