# [0312. 戳气球](https://leetcode.cn/problems/burst-balloons/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [0312. 戳气球 - 力扣](https://leetcode.cn/problems/burst-balloons/)

## 题目大意

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

## 解题思路

### 思路 1：动态规划

根据题意，如果 $i - 1$ 或 $i + 1$ 超出了数组的边界，那么就当它是一个数字为 $1$ 的气球。我们可以预先在 $nums$ 的首尾位置，添加两个数字为 $1$ 的虚拟气球，这样变成了 $n + 2$ 个气球，气球对应编号也变为了 $0 \sim n + 1$。

对应问题也变成了：给定 $n + 2$ 个气球，每个气球上有 $1$ 个数字，代表气球上的硬币数量，当我们戳破气球 $nums[i]$ 时，就能得到对应 $nums[i - 1] \times nums[i] \times nums[i + 1]$ 枚硬币。现在要戳破 $0 \sim n + 1$ 之间的所有气球（不包括编号 $0$ 和编号 $n + 1$ 的气球），请问最多能获得多少枚硬币？

###### 1. 划分阶段

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

根据我们之前定义的状态，$dp[i][j]$ 表示为：戳破所有气球 $i$ 与气球 $j$ 之间的气球（不包含气球 $i$ 和 气球 $j$），所能获取的最多硬币数。。所以最终结果为 $dp[0][n + 1]$。

### 思路 1：代码

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

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$，其中 $n$ 为气球数量。
- **空间复杂度**：$O(n^2)$。
