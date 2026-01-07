# [0813. 最大平均值和的分组](https://leetcode.cn/problems/largest-sum-of-averages/)

- 标签：数组、动态规划、前缀和
- 难度：中等

## 题目链接

- [0813. 最大平均值和的分组 - 力扣](https://leetcode.cn/problems/largest-sum-of-averages/)

## 题目大意

**描述**：

给定数组 $nums$ 和一个整数 $k$。我们将给定的数组 $nums$ 分成「最多 $k$ 个非空子数组」，且数组内部是连续的 。 

「分数」由每个子数组内的平均值的总和构成。

注意我们必须使用 $nums$ 数组中的每一个数进行分组，并且分数不一定需要是整数。

**要求**：

返回我们所能得到的最大 分数 是多少。答案误差在 $10^{-6}$ 内被视为是正确的。

**说明**：

- $1 \le nums.length \le 10^{3}$。
- $1 \le nums[i] \le 10^{4}$。
- $1 \le k \le nums.length$。

**示例**：

- 示例 1：

```python
输入: nums = [9,1,2,3,9], k = 3
输出: 20.00000
解释: 
nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20. 
我们也可以把 nums 分成[9, 1], [2], [3, 9]. 
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
```

- 示例 2：

```python
输入: nums = [1,2,3,4,5,6,7], k = 4
输出: 20.50000
```

## 解题思路

### 思路 1：动态规划

这道题要求将数组分成最多 $k$ 个连续子数组，使得每个子数组的平均值之和最大。

定义状态：

- $dp[i][j]$ 表示将前 $i$ 个元素分成 $j$ 个子数组时的最大平均值和。

状态转移方程：

- $dp[i][j] = \max(dp[p][j-1] + \frac{\sum_{t=p+1}^{i} nums[t]}{i-p})$，其中 $j-1 \le p < i$。

边界条件：

- $dp[i][1] = \frac{\sum_{t=1}^{i} nums[t]}{i}$，即前 $i$ 个元素分成 $1$ 个子数组。

为了优化计算，可以使用前缀和数组 $prefix$ 来快速计算子数组的和。

算法步骤：
1. 计算前缀和数组 $prefix$。
2. 初始化 $dp$ 数组。
3. 填充 $dp$ 数组，枚举分组数 $j$ 和元素数 $i$，以及分割点 $p$。
4. 返回 $dp[n][k]$。

### 思路 1：代码

```python
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        # 计算前缀和
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # 初始化 dp 数组
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        
        # 边界条件：前 i 个元素分成 1 个子数组
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i
        
        # 状态转移
        for j in range(2, k + 1):  # 枚举分组数
            for i in range(j, n + 1):  # 枚举元素数（至少需要 j 个元素）
                for p in range(j - 1, i):  # 枚举分割点
                    # 前 p 个元素分成 j-1 组，后面 i-p 个元素作为第 j 组
                    avg = (prefix[i] - prefix[p]) / (i - p)
                    dp[i][j] = max(dp[i][j], dp[p][j - 1] + avg)
        
        return dp[n][k]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 \times k)$，其中 $n$ 是数组的长度。需要填充 $n \times k$ 个状态，每个状态需要枚举 $O(n)$ 个分割点。
- **空间复杂度**：$O(n \times k)$，需要使用 $dp$ 数组存储状态。
