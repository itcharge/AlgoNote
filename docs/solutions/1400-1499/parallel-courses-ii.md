# [1494. 并行课程 II](https://leetcode.cn/problems/parallel-courses-ii/)

- 标签：位运算、图、动态规划、状态压缩
- 难度：困难

## 题目链接

- [1494. 并行课程 II - 力扣](https://leetcode.cn/problems/parallel-courses-ii/)

## 题目大意

**描述**：给定 $n$ 门课程（编号 $1 \sim n$），$relations[i] = [a, b]$ 表示课程 $a$ 是课程 $b$ 的先修课。每个学期最多可以上 $k$ 门课，且必须先修完先修课才能上后续课。

**要求**：返回修完所有课程所需的最少学期数。

**说明**：
- $1 \le n \le 15$。
- $0 \le relations.length \le n \times (n-1)/2$。
- $1 \le k \le n$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_1.png)

```python
输入：n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
输出：3 
解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_2.png)

```python
输入：n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
输出：4 
解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
```

## 解题思路

### 思路 1：状压 DP

#### 1. 核心思想

$n \le 15$，可以使用状态压缩。$mask$ 表示已经学完的课程集合，$dp[mask]$ 表示学完 $mask$ 中课程所需的最少学期数。

#### 2. 具体步骤

**第 1 步**：预处理每门课的先修条件 $pre[i]$（位掩码）。

**第 2 步**：预处理所有状态中可以在一学期内修完的课程子集（不超过 $k$ 门，且先修条件已满足）。

如何枚举子集？对于状态 $mask$，$available = (\text{未学课程}) \& (\text{先修条件已满足})$。然后枚举 $available$ 的所有子集，取大小 $\le k$ 的子集。

枚举子集的技巧：`sub = available; while sub: ... sub = (sub-1) & available`

**第 3 步**：DP 转移。

$$dp[mask | sub] = \min(dp[mask | sub], dp[mask] + 1) \quad \text{其中 sub 是 available 的子集且 } |sub| \le k$$

#### 3. 初始条件

$dp[0] = 0$，其余 $INF$。

#### 4. 最终结果

$dp[(1<<n)-1]$。

### 思路 1：代码

```python
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # 每门课的先修条件（位掩码，0 索引）
        pre = [0] * n
        for a, b in relations:
            pre[b - 1] |= 1 << (a - 1)

        total_states = 1 << n
        dp = [float('inf')] * total_states
        dp[0] = 0

        for mask in range(total_states):
            if dp[mask] == float('inf'):
                continue
            # 当前可以修的课：先修条件已满足且未修
            available = 0
            for i in range(n):
                if not (mask >> i) & 1 and (pre[i] & mask) == pre[i]:
                    available |= 1 << i

            # 枚举 available 的所有子集
            sub = available
            while sub:
                if bin(sub).count('1') <= k:
                    dp[mask | sub] = min(dp[mask | sub], dp[mask] + 1)
                sub = (sub - 1) & available

        return dp[total_states - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(3^n)$，每个状态 $mask$ 枚举子集的复杂度是 $O(3^n)$（所有子集的子集总数）。
- **空间复杂度**：$O(2^n)$。

$n=15$，$3^n \approx 1400$ 万，可接受。
