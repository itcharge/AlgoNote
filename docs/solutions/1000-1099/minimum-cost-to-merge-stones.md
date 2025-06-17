# [1000. 合并石头的最低成本](https://leetcode.cn/problems/minimum-cost-to-merge-stones/)

- 标签：数组、动态规划、前缀和
- 难度：困难

## 题目链接

- [1000. 合并石头的最低成本 - 力扣](https://leetcode.cn/problems/minimum-cost-to-merge-stones/)

## 题目大意

**描述**：给定一个代表 $n$ 堆石头的整数数组 $stones$，其中 $stones[i]$ 代表第 $i$ 堆中的石头个数。再给定一个整数 $k$， 每次移动需要将连续的 $k$ 堆石头合并为一堆，而这次移动的成本为这 $k$ 堆中石头的总数。

**要求**：返回把所有石头合并成一堆的最低成本。如果无法合并成一堆，则返回 $-1$。

**说明**：

- $n == stones.length$。
- $1 \le n \le 30$。
- $1 \le stones[i] \le 100$。
- $2 \le k \le 30$。

**示例**：

- 示例 1：

```python
输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。
```

- 示例 2：

```python
输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。
```

## 解题思路

### 思路 1：动态规划 + 前缀和

每次将 $k$ 堆连续的石头合并成 $1$ 堆，石头堆数就会减少 $k - 1$ 堆。总共有 $n$ 堆石子，则：

1. 当 $(n - 1) \mod (k - 1) == 0$ 时，一定可以经过 $\frac{n - 1}{k - 1}$ 次合并，将 $n$ 堆石头合并为 $1$ 堆。
2. 当 $(n - 1) \mod (k - 1) \ne 0$ 时，则无法将所有的石头合并成一堆。

根据以上情况，我们可以先将无法将所有的石头合并成一堆的情况排除出去，接下来只考虑合法情况。

由于每次合并石头的成本为合并的 $k$ 堆的石子总数，即数组 $stones$ 中长度为 $k$ 的连续子数组和，因此为了快速计算数组 $stones$ 的连续子数组和，我们可以使用「前缀和」的方式，预先计算出「前 $i$ 堆的石子总数」，从而可以在 $O(1)$ 的时间复杂度内得到数组 $stones$ 的连续子数组和。

$k$ 堆石头合并为 $1$ 堆石头的过程，可以看做是长度为 $k$ 的连续子数组合并为长度为 $1$ 的子数组的过程，也可以看做是将长度为 $k$ 的区间合并为长度为 $1$ 的区间。

接下来我们就可以按照「区间 DP 问题」的基本思路来做。

###### 1. 划分阶段

按照区间长度进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j][m]$ 表示为：将区间 $[i, j]$ 的石堆合并成 $m$ 堆的最低成本，其中 $m$ 的取值为 $[1,k]$。

###### 3. 状态转移方程

我们将区间 $[i, j]$ 的石堆合并成 $m$ 堆，可以枚举 $i \le n \le j$，将区间 $[i, j]$ 拆分为两个区间 $[i, n]$ 和 $[n + 1, j]$。然后将 $[i, n]$ 中的石头合并为 $1$ 堆，将 $[n + 1, j]$ 中的石头合并成 $m - 1$ 堆。最后将 $1$ 堆石头和 $m - 1$ 堆石头合并成 $1$ 堆，这样就可以将 $[i, j]$ 的石堆合并成 $k$ 堆。则状态转移方程为：$dp[i][j][m] = min_{i \le n < j} \lbrace dp[i][n][1] + dp[n + 1][j][m - 1] \rbrace$。

我们再将区间 $[i, j]$ 的 $k$ 堆石头合并成 $1$ 堆，其成本为 区间 $[i, j]$ 的石堆合并成 $k$ 堆的成本，加上将这 $k$ 堆石头合并成 $1$ 堆的成本，即状态转移方程为：$dp[i][j][1] = dp[i][j][k] + \sum_{t = i}^{t = j} stones[t]$。

###### 4. 初始条件

- 长度为 $1$ 的区间 $[i, i]$ 合并为 $1$ 堆成本为 $0$，即：$dp[i][i][1] = 0$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i][j][m]$ 表示为：将区间 $[i, j]$ 的石堆合并成 $m$ 堆的最低成本，其中 $m$ 的取值为 $[1,k]$。 所以最终结果为 $dp[1][size][1]$，其中 $size$ 为数组 $stones$ 的长度。

### 思路 1：代码

```python
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        size = len(stones)
        if (size - 1) % (k - 1) != 0:
            return -1

        prefix = [0 for _ in range(size + 1)]
        for i in range(1, size + 1):
            prefix[i] = prefix[i - 1] + stones[i - 1]

        dp = [[[float('inf') for _ in range(k + 1)] for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i][1] = 0

        for l in range(2, size + 1):
            for i in range(size):
                j = i + l - 1
                if j >= size:
                    break
                for m in range(2, k + 1):
                    for n in range(i, j, k - 1):
                        dp[i][j][m] = min(dp[i][j][m], dp[i][n][1] + dp[n + 1][j][m - 1])
                dp[i][j][1] = dp[i][j][k] + prefix[j + 1] - prefix[i]

        return dp[0][size - 1][1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3 \times k)$，其中 $n$ 是数组 $stones$ 的长度。
- **空间复杂度**：$O(n^2 \times k)$。

### 思路 2：动态规划 + 状态优化

在思路 1 中，我们使用定义状态 $dp[i][j][m]$ 表示为：将区间 $[i, j]$ 的石堆合并成 $m$ 堆的最低成本，其中 $m$ 的取值为 $[1,k]$。

事实上，对于固定区间 $[i, j]$，初始时堆数为 $j - i + 1$，每次合并都会减少 $k - 1$ 堆，合并到无法合并时的堆数固定为 $(j - i) \mod (k - 1) + 1$。

所以，我们可以直接定义状态 $dp[i][j]$ 表示为：将区间 $[i, j]$ 的石堆合并到无法合并时的最低成本。

具体步骤如下：

###### 1. 划分阶段

按照区间长度进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 表示为：将区间 $[i, j]$ 的石堆合并到无法合并时的最低成本。

###### 3. 状态转移方程

枚举 $i \le n \le j$，将区间 $[i, j]$ 拆分为两个区间 $[i, n]$ 和 $[n + 1, j]$。然后将区间 $[i, n]$ 合并成 $1$ 堆，$[n + 1, j]$ 合并成 $m$ 堆。

$dp[i][j] = min_{i \le n < j} \lbrace dp[i][n] + dp[n + 1][j] \rbrace$。

如果 $(j - i) \mod (k - 1) == 0$，则说明区间 $[i, j]$ 能狗合并为 1 堆，则加上区间子数组和，即 $dp[i][j] += prefix[j + 1] - prefix[i]$。

###### 4. 初始条件

- 长度为 $1$ 的区间 $[i, i]$ 合并到无法合并时的最低成本为 $0$，即：$dp[i][i] = 0$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i][j]$ 表示为：将区间 $[i, j]$ 的石堆合并到无法合并时的最低成本。所以最终结果为 $dp[0][size - 1]$，其中 $size$ 为数组 $stones$ 的长度。

### 思路 2：代码

```python
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        size = len(stones)
        if (size - 1) % (k - 1) != 0:
            return -1

        prefix = [0 for _ in range(size + 1)]
        for i in range(1, size + 1):
            prefix[i] = prefix[i - 1] + stones[i - 1]

        dp = [[float('inf') for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i] = 0

        for l in range(2, size + 1):
            for i in range(size):
                j = i + l - 1
                if j >= size:
                    break
                # 遍历每一个可以组成 k 堆石子的分割点 n，每次递增 k - 1 个
                for n in range(i, j, k - 1):
                    # 判断 [i, n] 到 [n + 1, j] 是否比之前花费小
                    dp[i][j] = min(dp[i][j], dp[i][n] + dp[n + 1][j])
                # 如果 [i, j] 能狗合并为 1 堆，则加上区间子数组和
                if (l - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][size - 1]
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n^3)$，其中 $n$ 是数组 $stones$ 的长度。
- **空间复杂度**：$O(n^2)$。

## 参考资料

- 【题解】[一题一解：动态规划（区间 DP）+ 前缀和（清晰题解） - 合并石头的最低成本](https://leetcode.cn/problems/minimum-cost-to-merge-stones/solution/python3javacgo-yi-ti-yi-jie-dong-tai-gui-lr9q/)
