# [1388. 3n 块披萨](https://leetcode.cn/problems/pizza-with-3n-slices/)

- 标签：贪心、数组、动态规划、堆（优先队列）
- 难度：困难

## 题目链接

- [1388. 3n 块披萨 - 力扣](https://leetcode.cn/problems/pizza-with-3n-slices/)

## 题目大意

**描述**：有一个大小为 $3n$ 的圆形披萨数组 $slices$，你和你的两位朋友将按以下规则取披萨：
1. 你选择任意一块披萨。
2. 你的两位朋友各取一块（相邻的披萨会被取走）。
3. 重复直到披萨取完。

**要求**：返回你能获得的最大披萨面积总和。

**说明**：
- $1 \le n \le 500$。
- $slices.length = 3n$。
- $1 \le slices[i] \le 1000$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/sample_3_1723.png)

```python
输入：slices = [1,2,3,4,5,6]
输出：10
解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/sample_4_1723.png)

```python
输入：slices = [8,9,8,6,1,1]
输出：16
解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。
```


## 解题思路

### 思路 1：转化为打家劫舍 III（环形 + 选 n 个）

#### 1. 核心思想

本题的取法规则可以这样理解：
- 每次你选一块披萨后，它的相邻两块会被朋友取走（你无法获得）。
- 即任意**相邻的两块披萨不能同时被你取到**。

但仅此还不够，因为 $3n$ 块披萨你和朋友们各取 $n$ 块，所以你需要恰好选 $n$ 块。

因此问题转化为：在**环形**数组 $slices$ 中，选择 $n$ 个不相邻的元素，使和最大。

这是「打家劫舍 III」（环形）的加强版：增加了恰好选 $n$ 个的约束。

#### 2. 阶段划分

按数组下标顺序处理，同时维护已选披萨数量。

#### 3. 定义状态

定义 $dp[i][j]$ 表示在数组 $slices$ 的前 $i$ 个元素中，选择 $j$ 个不相邻元素的最大和。

因为数组是环形的，首尾元素也相邻，需要分两种情况讨论：
- **情况 1**：不选第 $0$ 个元素，在 $slices[1:n]$ 范围内选取
- **情况 2**：不选第 $n-1$ 个元素，在 $slices[0:n-1]$ 范围内选取

取两种情况的最大值。

#### 4. 状态转移方程

$$dp[i][j] = \max(dp[i-1][j], \; dp[i-2][j-1] + slices[i])$$

解释：
- $dp[i-1][j]$：不选第 $i$ 块，前 $i-1$ 块中选 $j$ 块
- $dp[i-2][j-1] + slices[i]$：选第 $i$ 块，则第 $i-1$ 块不能选，从前 $i-2$ 块中选 $j-1$ 块

#### 5. 初始条件

- $dp[0][0] = 0$（前 0 块选 0 块）
- 其余 $dp$ 初始化为 $-\infty$（不可达状态）

#### 6. 最终结果

$$res = \max(\text{情况1的} dp[m-1][n], \; \text{情况2的} dp[m-1][n])$$

其中 $m = 3n$。

#### 7. 举例说明

以 $slices = [1, 2, 3, 4, 5, 6]$（$n=2$）为例：

分两种情况：
- 不选第 $0$ 块：在 $[2,3,4,5,6]$ 中选 $2$ 块不相邻
- 不选第 $5$ 块：在 $[1,2,3,4,5]$ 中选 $2$ 块不相邻

情况 1 最大：$4 + 6 = 10$
情况 2 最大：$5 + 3 = 8$

结果为 $10$。

### 思路 1：代码

```python
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        m = len(slices)
        n = m // 3

        def helper(arr):
            """在非环形数组 arr 中选 n 个不相邻元素的最大和"""
            size = len(arr)
            dp = [[float('-inf')] * (n + 1) for _ in range(size + 1)]
            dp[0][0] = 0

            for i in range(1, size + 1):
                dp[i][0] = 0  # 选 0 个
                for j in range(1, n + 1):
                    # 不选第 i 个
                    dp[i][j] = dp[i - 1][j]
                    # 选第 i 个（需要 i >= 2 以保证不相邻）
                    if i >= 2:
                        dp[i][j] = max(dp[i][j], dp[i - 2][j - 1] + arr[i - 1])
                    elif i == 1 and j == 1:
                        dp[i][j] = max(dp[i][j], arr[i - 1])
            return dp[size][n]

        # 环形处理：首尾取其一
        case1 = helper(slices[1:])   # 不取第 0 块
        case2 = helper(slices[:-1])  # 不取最后一块

        return max(case1, case2)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n) = O(3n \times n) = O(n^2)$，其中 $m = 3n$。
- **空间复杂度**：$O(m \times n)$，可使用滚动数组优化为 $O(n)$。

---

### 思路 2：空间优化版

使用滚动数组将 DP 空间优化到 $O(n)$。

```python
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        m = len(slices)
        n = m // 3

        def helper(arr):
            size = len(arr)
            # 滚动数组：只保留前两行
            dp_prev = [float('-inf')] * (n + 1)
            dp_curr = [float('-inf')] * (n + 1)
            dp_prev[0] = 0
            dp_curr[0] = 0

            for i in range(1, size + 1):
                dp_next = [float('-inf')] * (n + 1)
                dp_next[0] = 0
                for j in range(1, n + 1):
                    dp_next[j] = dp_curr[j]  # 不选
                    if i >= 2:
                        dp_next[j] = max(dp_next[j], dp_prev[j - 1] + arr[i - 1])
                    elif i == 1 and j == 1:
                        dp_next[j] = max(dp_next[j], arr[i - 1])
                dp_prev, dp_curr = dp_curr, dp_next

            return dp_curr[n]

        return max(helper(slices[1:]), helper(slices[:-1]))
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(n)$，滚动数组只保留两行。
