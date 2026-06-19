# [1326. 灌溉花园的最少水龙头数目](https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/)

- 标签：贪心、数组、动态规划
- 难度：困难

## 题目链接

- [1326. 灌溉花园的最少水龙头数目 - 力扣](https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/)

## 题目大意

**描述**：在 $x$ 轴上有一个一维的花园，长度为 $n$。在点 $0, 1, 2, \dots, n$ 处共有 $n + 1$ 个水龙头。给定整数 $n$ 和一个长度为 $n + 1$ 的数组 $ranges$，其中 $ranges[i]$ 表示第 $i$ 个水龙头可以灌溉的区间为 $[i - ranges[i], i + ranges[i]]$。

**要求**：返回可以灌溉整个花园的最少水龙头数目。如果无法灌溉整个花园，返回 $-1$。

**说明**：
- $1 \le n \le 10^4$。
- $ranges.length = n + 1$。
- $0 \le ranges[i] \le 100$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/19/1685_example_1.png)

```python
输入：n = 5, ranges = [3,4,1,1,0,0]
输出：1
解释：
点 0 处的水龙头可以灌溉区间 [-3,3]
点 1 处的水龙头可以灌溉区间 [-3,5]
点 2 处的水龙头可以灌溉区间 [1,3]
点 3 处的水龙头可以灌溉区间 [2,4]
点 4 处的水龙头可以灌溉区间 [4,4]
点 5 处的水龙头可以灌溉区间 [5,5]
只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
```

- 示例 2：

```python
输入：n = 3, ranges = [0,0,0,0]
输出：-1
解释：即使打开所有水龙头，你也无法灌溉整个花园。
```


## 解题思路

### 思路 1：贪心 + 区间覆盖

#### 1. 核心思想

本题可以转化为经典的**区间覆盖问题**。每个水龙头覆盖一个区间 $[L_i, R_i]$，其中：
- $L_i = \max(0, i - ranges[i])$
- $R_i = \min(n, i + ranges[i])$

问题转化为：从 $n + 1$ 个区间中选出最少数量的区间，使它们的并集覆盖 $[0, n]$。

区间覆盖问题的贪心策略：按左端点排序，每次选择覆盖当前起点且右端点最远的区间。

#### 2. 具体步骤

**第 1 步：构建最远右端点映射**

用数组 $max\_right[pos]$ 记录从位置 $pos$ 出发能覆盖到的最远右端点。遍历每个水龙头 $i$：计算 $left = \max(0, i - ranges[i])$ 和 $right = \min(n, i + ranges[i])$，然后更新 $max\_right[left] = \max(max\_right[left], right)$。

**第 2 步：贪心扫描**

维护三个变量：
- $cur\_end$：当前已选区间能覆盖到的最远位置
- $next\_end$：扫描过程中能延伸到的最远右端点
- $count$：已选水龙头数量

遍历 $i = 0 \to n$：
1. 用 $max\_right[i]$ 更新 $next\_end$
2. 如果 $i == cur\_end$（当前区间已到尽头），必须选择下一个区间：
   - 如果 $next\_end \le i$，说明无法继续延伸，返回 $-1$
   - 否则 $cur\_end = next\_end$，$count++$

**第 3 步：返回 $count$**。

#### 3. 正确性证明

对于当前覆盖到的位置 $i = cur\_end$，所有左端点 $\le i$ 的区间中，选择右端点最远的那个是最优的。如果选择右端点更近的区间，后续需要更多区间来覆盖剩余部分，不会更优。这就是贪心选择性质。

#### 4. 举例说明

以 $n = 5$，$ranges = [3, 4, 1, 1, 0, 0]$ 为例：

每个水龙头覆盖区间：

| $i$ | $ranges[i]$ | 左端点 | 右端点 |
| --- | ----------- | ------ | ------ |
| 0   | 3           | 0      | 3      |
| 1   | 4           | 0      | 5      |
| 2   | 1           | 1      | 3      |
| 3   | 1           | 2      | 4      |
| 4   | 0           | 4      | 4      |
| 5   | 0           | 5      | 5      |

构建 $max\_right$：
- $max\_right[0] = \max(3, 5) = 5$
- $max\_right[1] = 3$
- $max\_right[2] = 4$
- $max\_right[4] = 4$
- $max\_right[5] = 5$

贪心过程：
- $i=0$：$next\_end = \max(0, 5) = 5$，$i == cur\_end$，选区间，$cur\_end=5$，$count=1$
- $i=1$：$next\_end = \max(5, 3)=5$
- $i=2$：$next\_end = \max(5, 4)=5$
- $i=3$：$next\_end=5$（$max\_right[3]$ 不存在）
- $i=4$：$next\_end = \max(5, 4)=5$
- $i=5$：$i == cur\_end$，已覆盖到 $5$，结束

最少 $1$ 个水龙头即可覆盖 $[0, 5]$。

### 思路 1：代码

```python
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 第 1 步：构建从每个左端点出发能到达的最远右端点
        max_right = [0] * (n + 1)
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            max_right[left] = max(max_right[left], right)

        # 第 2 步：贪心覆盖
        cur_end = 0      # 当前已覆盖的最远位置
        next_end = 0     # 下一步能覆盖的最远位置
        count = 0        # 已选水龙头数

        for i in range(n):
            # 用当前位置能到达的最远右端点更新 next_end
            next_end = max(next_end, max_right[i])
            # 到达当前区间的终点，必须选择下一个区间
            if i == cur_end:
                if next_end <= i:
                    return -1          # 无法继续延伸
                cur_end = next_end
                count += 1

        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，只需遍历一次 $ranges$ 和一次 $[0, n]$。
- **空间复杂度**：$O(n)$，使用长度为 $n + 1$ 的 $max\_right$ 数组。

---

### 思路 2：动态规划

#### 1. 核心思想

也可以用动态规划解决。定义 $dp[i]$ 表示覆盖 $[0, i]$ 所需的最少水龙头数目。

#### 2. 状态转移方程

对于第 $j$ 个水龙头，其覆盖区间为 $[L_j, R_j]$。利用它，我们只需覆盖到 $L_j$，再加这个水龙头即可覆盖到 $[L_j, R_j]$ 内任意位置。因此：

$$dp[i] = \min(dp[i], \; dp[L_j] + 1) \quad \text{其中 } L_j < i \le R_j$$

初始 $dp[0] = 0$，其余为 $+\infty$。最终 $dp[n]$ 即为答案。

#### 3. 思路 2：代码

```python
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            for j in range(left + 1, right + 1):
                dp[j] = min(dp[j], dp[left] + 1)

        return dp[n] if dp[n] != INF else -1
```

#### 4. 思路 2：复杂度分析

- **时间复杂度**：$O(n \times k)$，其中 $k$ 是水龙头的平均覆盖范围，最坏 $O(n^2)$。
- **空间复杂度**：$O(n)$。

---

### 思路 3：对比与总结

| 思路 | 时间复杂度 | 空间复杂度 | 优缺点 |
| --- | --------- | --------- | ------ |
| 贪心 | $O(n)$ | $O(n)$ | 高效，只需线性扫描 |
| DP | $O(n^2)$ 最坏 | $O(n)$ | 直观易理解，但 $n=10^4$ 时可能超时 |

推荐使用贪心解法，时间复杂度最优。
