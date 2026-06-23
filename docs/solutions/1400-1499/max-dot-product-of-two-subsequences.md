# [1458. 两个子序列的最大点积](https://leetcode.cn/problems/max-dot-product-of-two-subsequences/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [1458. 两个子序列的最大点积 - 力扣](https://leetcode.cn/problems/max-dot-product-of-two-subsequences/)

## 题目大意

**描述**：给定两个数组 $nums1$ 和 $nums2$。

**要求**：返回两个长度相等的非空子序列的最大点积。点积定义为对应位置元素的乘积之和。

**说明**：
- $1 \le nums1.length, nums2.length \le 500$。
- $-1000 \le nums1[i], nums2[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
输出：18
解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
它们的点积为 (2*3 + (-2)*(-6)) = 18 。
```

- 示例 2：

```python
输入：nums1 = [3,-2], nums2 = [2,-6,7]
输出：21
解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
它们的点积为 (3*7) = 21 。
```

## 解题思路

### 思路 1：二维 DP

#### 1. 核心思想

定义 $dp[i][j]$ 表示 $nums1$ 前 $i$ 个元素和 $nums2$ 前 $j$ 个元素中，能得到的最大点积（至少选一组对阵）。

#### 2. 阶段划分

按 $i$ 和 $j$ 作为阶段，从 $1$ 递增。

#### 3. 定义状态

$dp[i][j]$：考虑 $nums1[0 \dots i-1]$ 和 $nums2[0 \dots j-1]$，能得到的最大点积。

#### 4. 状态转移方程

对于 $(i, j)$，有几个选择：
1. 不选 $nums1[i-1]$：$dp[i-1][j]$
2. 不选 $nums2[j-1]$：$dp[i][j-1]$
3. 不选两个：$dp[i-1][j-1]$（事实上被前两种覆盖）
4. 选这一对：$dp[i-1][j-1] + nums1[i-1] \times nums2[j-1]$
5. 只选这一对（前面都不选）：$nums1[i-1] \times nums2[j-1]$

$$dp[i][j] = \max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + nums1[i-1] \times nums2[j-1], nums1[i-1] \times nums2[j-1])$$

#### 5. 初始条件

$dp[0][\dots] = 0$，$dp[\dots][0] = 0$。

#### 6. 最终结果

$dp[n][m]$。

#### 7. 举例说明

以 $nums1 = [2,1,-2,5], nums2 = [3,0,-6]$ 为例：

$dp[1][1] = max(0, 0, 0+6, 6) = 6$
$dp[1][2] = max(0, 6, 6+0=6, 0) = 6$
$dp[1][3] = max(0, 6, 6-12=-6, -12) = 6$

...逐步递推...

最终最大点积为 $18$（取 $2 \times 3 + 5 \times (-6) + 5 \times 0$ 等）。

等等，让我重新计算：$2 \times 3 = 6$，$2 \times (-6) = -12$，$1 \times 3 = 3$，$5 \times 0 = 0$，$5 \times (-6) = -30$。

实际上最优可能是 $2 \times 3 + 1 \times 0 = 6$ 或 $5 \times 0 = 0$ 或 $2 \times 3 = 6$。但 $2 \times 3 + (-2) \times (-6) = 6 + 12 = 18$？$-2$ 是 $nums1[2]$，$-6$ 是 $nums2[2]$，$2 \times 3 + (-2) \times (-6) = 6 + 12 = 18$，这就是最大点积。

### 思路 1：代码

```python
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                product = nums1[i - 1] * nums2[j - 1]
                # 四种情况取最大值
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1] + product,
                    product
                )

        return dp[n][m]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$。
- **空间复杂度**：$O(n \times m)$，可优化为 $O(m)$。
