# [1335. 工作计划的最低难度](https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [1335. 工作计划的最低难度 - 力扣](https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/)

## 题目大意

**描述**：给定一个数组 $jobDifficulty$ 和整数 $d$，需要将 $n$ 个工作按顺序在 $d$ 天内完成。每天至少完成一个工作，且一天内完成的工作中最大难度即为当天的难度。

**要求**：返回整个计划的最小总难度。如果无法完成，返回 $-1$。

**说明**：
- $1 \le n, d \le 300$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/26/untitled.png)

```python
输入：jobDifficulty = [6,5,4,3,2,1], d = 2
输出：7
解释：第一天，您可以完成前 5 项工作，总难度 = 6.
第二天，您可以完成最后一项工作，总难度 = 1.
计划表的难度 = 6 + 1 = 7
```

- 示例 2：

```python
输入：jobDifficulty = [9,9,9], d = 4
输出：-1
解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。
```


## 解题思路

### 思路 1：动态规划

#### 1. 阶段划分

按天划分阶段。$dp[i][j]$ 表示前 $i$ 天完成前 $j$ 个工作的最小总难度。

#### 2. 状态转移

$$dp[i][j] = \min_{k=i-1}^{j-1} (dp[i-1][k] + \max_{t=k+1}^{j} jobDifficulty[t])$$

其中 $k$ 是第 $i$ 天之前完成的工作数，第 $i$ 天完成 $k+1$ 到 $j$ 的工作。

#### 3. 初始条件

- $dp[0][0] = 0$。
- 如果 $n < d$，返回 $-1$。

### 思路 1：代码

```python
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0

        for i in range(1, d + 1):
            for j in range(i, n + 1):
                max_diff = 0
                for k in range(j - 1, i - 2, -1):
                    max_diff = max(max_diff, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + max_diff)
        return dp[d][n]
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(d \times n^2)$。
- **空间复杂度**：$O(dn)$。
