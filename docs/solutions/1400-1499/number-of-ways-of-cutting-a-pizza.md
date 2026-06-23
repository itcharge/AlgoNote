# [1444. 切披萨的方案数](https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/)

- 标签：数组、动态规划、矩阵、前缀和
- 难度：困难

## 题目链接

- [1444. 切披萨的方案数 - 力扣](https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/)

## 题目大意

**描述**：给定一个 $m \times n$ 的披萨矩阵 $pizza$，其中 `'A'` 表示苹果，`'.'` 表示空位。要用 $k-1$ 刀切成 $k$ 块（每刀水平或垂直切，切完后剩下的右下部分继续切），且每块必须至少包含一个苹果。

**要求**：返回将披萨切成 $k$ 块的方案数。结果对 $10^9 + 7$ 取模。

**说明**：
- $1 \le m, n \le 50$。
- $1 \le k \le 10$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/10/ways_to_cut_apple_1.png)

```python
输入：pizza = ["A..","AAA","..."], k = 3
输出：3 
解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。
```

- 示例 2：

```python
输入：pizza = ["A..","AA.","..."], k = 3
输出：1
```

## 解题思路

### 思路 1：三维 DP + 前缀和

#### 1. 核心思想

每次切割后只保留右下部分，所以状态可以用左上角坐标 $(r, c)$ 表示披萨剩余部分。

定义 $dp[r][c][p]$ 表示从 $(r,c)$ 到右下角的子矩形切成 $p$ 块的方案数。

#### 2. 阶段划分

按 $p$ 从小到大（$1 \to k$）和 $(r,c)$ 从下到上、从右到左递推。

#### 3. 定义状态

$dp[r][c][p]$：将坐标 $(r,c)$ 到 $(m-1,n-1)$ 的披萨切成 $p$ 块的方案数。

#### 4. 状态转移方程

从 $(r,c)$ 切一刀，水平切或垂直切：
- 水平切：在 $r \le nr < m-1$ 处切，要求上半部分（从 $(r,c)$ 到 $(nr, n-1)$）至少有一个苹果，然后 $dp[r][c][p] += sum_{nr} dp[nr+1][c][p-1]$。
- 垂直切：在 $c \le nc < n-1$ 处切，要求左半部分至少有一个苹果，$dp[r][c][p] += sum_{nc} dp[r][nc+1][p-1]$。

需要快速判断某子矩形是否有苹果 → 前缀和。

#### 5. 初始条件

$dp[r][c][1] = 1$ 如果 $(r,c)$ 到右下角至少有一个苹果，否则 $0$。

#### 6. 最终结果

$dp[0][0][k]$。

### 思路 1：代码

```python
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # 二维前缀和，prefix[i][j] 表示以 (i,j) 为左上角到右下角的苹果数
        # 用后缀的方式：suffix[r][c] = 从 (r,c) 到 (m-1,n-1) 的苹果数
        suffix = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                suffix[r][c] = (suffix[r + 1][c] + suffix[r][c + 1]
                                - suffix[r + 1][c + 1])
                if pizza[r][c] == 'A':
                    suffix[r][c] += 1

        # hasApple[r1][c1][r2][c2] 检查 (r1,c1) 到 (r2,c2) 是否有苹果
        # 优化：用函数判断
        def has_apple(r, c, nr, nc):
            """(r,c) 到 (nr,nc) 是否有苹果，nc=n-1 表示到右边界"""
            total = (suffix[r][c] - suffix[nr + 1][c]
                     - suffix[r][nc + 1] + suffix[nr + 1][nc + 1])
            return total > 0

        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(m)]

        # 初始化 p = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if suffix[r][c] > 0:
                    dp[r][c][1] = 1

        for p in range(2, k + 1):
            for r in range(m - 1, -1, -1):
                for c in range(n - 1, -1, -1):
                    # 水平切
                    for nr in range(r, m - 1):
                        if has_apple(r, c, nr, n - 1):
                            dp[r][c][p] = (dp[r][c][p] + dp[nr + 1][c][p - 1]) % MOD
                    # 垂直切
                    for nc in range(c, n - 1):
                        if has_apple(r, c, m - 1, nc):
                            dp[r][c][p] = (dp[r][c][p] + dp[r][nc + 1][p - 1]) % MOD

        return dp[0][0][k]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(k \times m \times n \times (m + n))$，$m,n \le 50, k \le 10$，可行。
- **空间复杂度**：$O(m \times n \times k)$。
