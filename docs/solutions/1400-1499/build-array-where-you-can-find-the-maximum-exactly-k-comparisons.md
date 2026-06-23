# [1420. 生成数组](https://leetcode.cn/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)

- 标签：动态规划
- 难度：困难

## 题目链接

- [1420. 生成数组 - 力扣](https://leetcode.cn/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)

## 题目大意

**描述**：给定三个整数 $n$、$m$ 和 $k$。考虑一个长度为 $n$ 的数组 $arr$，元素范围 $[1, m]$。定义在 $arr$ 上使用如下算法找到最大值，同时统计比较次数：

```python
def find_max(arr):
    max_val = -1
    comparisons = 0
    for x in arr:
        if x > max_val:
            max_val = x
            comparisons += 1
    return comparisons
```

**要求**：返回有多少种长度为 $n$ 的数组 $arr$ 能使该算法的比较次数恰好为 $k$。结果对 $10^9 + 7$ 取模。

**说明**：
- $1 \le n \le 50$。
- $1 \le m \le 100$。
- $0 \le k \le n$。

**示例**：

- 示例 1：

```python
输入：n = 2, m = 3, k = 1
输出：6
解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
```

- 示例 2：

```python
输入：n = 5, m = 2, k = 3
输出：0
解释：没有数组可以满足上述条件
```

## 解题思路

### 思路 1：动态规划

#### 1. 核心思想

算法记录的是更新最大值的次数。每次遇到比当前最大值更大的数时，"比较"次数 $+1$。

这是一个计数 DP：$dp[i][j][c]$ 表示长度为 $i$、当前最大值为 $j$、已经发生了 $c$ 次比较的数组方案数。

#### 2. 阶段划分

按数组长度 $i$ 划分阶段，逐步增加元素。

#### 3. 定义状态

$dp[i][j][c]$：长度为 $i$ 的数组，当前最大值为 $j$，比较次数恰好为 $c$ 的方案数。

#### 4. 状态转移方程

考虑在第 $i$ 个位置放入数字 $x$（$1 \le x \le m$）：

- 如果 $x \le j$（新元素不大于当前最大值）：比较次数不变。
  $$dp[i][j][c] += dp[i-1][j][c] \times j$$

- 如果 $x > j$（新元素更新了最大值）：比较次数 $+1$。
  $$dp[i][x][c+1] += dp[i-1][j][c] \quad \text{对于 } x > j$$

其中 $dp[i-1][j][c] \times j$ 表示前 $i-1$ 项最大值为 $j$，第 $i$ 项可以放入 $1 \sim j$ 中任意一个。

#### 5. 初始条件

$dp[1][j][1] = 1$（$1 \le j \le m$），表示只有一个元素且它本身就是最大值，比较次数为 $1$。

如果 $k = 0$，返回 $0$（至少一次比较）。

#### 6. 最终结果

$\sum_{j=1}^{m} dp[n][j][k] \mod (10^9 + 7)$。

#### 7. 举例说明

以 $n=2, m=3, k=1$ 为例：
- 只需要 $1$ 次比较（只在第一个元素时更新最大值）。
- 第一个数必须 $\ge$ 第二个数。
- 合法数组：$[1,1], [2,1], [2,2], [3,1], [3,2], [3,3]$，共 $6$ 个。

$dp[2][1][1] = 1$（$[1,1]$），$dp[2][2][1] = 2$（$[2,1],[2,2]$），$dp[2][3][1] = 3$（$[3,1],[3,2],[3,3]$），总和 $6$。

### 思路 1：代码

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        if k == 0:
            return 0

        # dp[i][j][c]：长度 i，最大值 j，比较次数 c
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        # 初始化：长度为 1
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for c in range(1, k + 1):
                    # 放 <= j 的数，比较次数不变
                    dp[i][j][c] = (dp[i][j][c] + dp[i - 1][j][c] * j) % MOD
                    # 放 > j 的数，比较次数 +1
                    if c < k:
                        for x in range(j + 1, m + 1):
                            dp[i][x][c + 1] = (dp[i][x][c + 1] + dp[i - 1][j][c]) % MOD

        ans = 0
        for j in range(1, m + 1):
            ans = (ans + dp[n][j][k]) % MOD
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m^2 \times k)$，其中 $n \le 50, m \le 100, k \le 50$，可以接受。
- **空间复杂度**：$O(n \times m \times k)$，可用滚动数组优化。

---

### 思路 2：前缀和优化

对 $x > j$ 的循环可以用前缀和优化到 $O(1)$，将 $O(m^2)$ 降为 $O(m)$。

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        if k == 0:
            return 0

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for c in range(1, k + 1):
                # 维护大于某值的 dp 和
                suffix = 0
                for j in range(m, 0, -1):
                    # 放 <= j，比较次数不变
                    dp[i][j][c] = (dp[i][j][c] + dp[i - 1][j][c] * j) % MOD
                    # 放新最大值（= j），来自之前的最大值 < j
                    if c > 1:
                        dp[i][j][c] = (dp[i][j][c] + suffix) % MOD
                    suffix = (suffix + dp[i - 1][j][c - 1]) % MOD

        ans = sum(dp[n][j][k] for j in range(1, m + 1)) % MOD
        return ans
```
