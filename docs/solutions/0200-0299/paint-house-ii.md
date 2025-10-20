# [0265. 粉刷房子 II](https://leetcode.cn/problems/paint-house-ii/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [0265. 粉刷房子 II - 力扣](https://leetcode.cn/problems/paint-house-ii/)

## 题目大意

**描述**：

假如有一排房子共有 $n$ 幢，每个房子可以被粉刷成 $k$ 种颜色中的一种。房子粉刷成不同颜色的花费成本也是不同的。你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
每个房子粉刷成不同颜色的花费以一个 $n \times k$ 的矩阵表示。

- 例如，$costs[0][0]$ 表示第 $0$ 幢房子粉刷成 $0$ 号颜色的成本；$costs[1][2]$ 表示第 $1$ 幢房子粉刷成 $2$ 号颜色的成本，以此类推。

**要求**：

返回「粉刷完所有房子的最低成本」。

**说明**：

- $costs.length == n$。
- $costs[i].length == k$。
- $1 \le n \le 10^{3}$。
- $2 \le k \le 20$。
- $1 \le costs[i][j] \le 20$。

- 进阶：您能否在 $O(n \times k)$ 的时间复杂度下解决此问题？

**示例**：

- 示例 1：

```python
输入: costs = [[1,5,3],[2,9,4]]
输出: 5
解释: 
将房子 0 刷成 0 号颜色，房子 1 刷成 2 号颜色。花费: 1 + 4 = 5; 
或者将 房子 0 刷成 2 号颜色，房子 1 刷成 0 号颜色。花费: 3 + 2 = 5. 
```

- 示例 2：

```python
输入: costs = [[1,3],[2,4]]
输出: 5
```

## 解题思路

### 思路 1：动态规划 + 优化

这是一个经典的动态规划问题。我们需要找到粉刷所有房子的最低成本，且相邻房子颜色不能相同。

核心思想是：

- 定义状态：$dp[i][j]$ 表示第 $i$ 个房子粉刷成第 $j$ 种颜色的最低成本。
- 状态转移：$dp[i][j] = costs[i][j] + \min_{k \neq j} dp[i-1][k]$，即当前房子选择颜色 $j$ 的成本加上前一个房子选择其他颜色的最小成本。
- 为了优化空间复杂度，我们只需要维护前一个房子的最小成本和次小成本，以及对应的颜色。

具体算法步骤：

1. 处理边界情况：如果只有一个房子，返回所有颜色中的最小成本。
2. 初始化：记录前一个房子的最小成本 $min1$、次小成本 $min2$ 和对应的颜色 $color1$、$color2$。
3. 状态转移：对于每个房子，计算选择每种颜色的成本，并更新最小和次小成本。
4. 返回最后一个房子的最小成本。

### 思路 1：代码

```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # 处理空数组情况
        if not costs or not costs[0]:
            return 0
        
        n, k = len(costs), len(costs[0])
        
        # 如果只有一个房子，返回所有颜色中的最小成本
        if n == 1:
            return min(costs[0])
        
        # 初始化前一个房子的最小成本和次小成本
        prev_min1 = prev_min2 = 0  # 前一个房子的最小成本和次小成本
        prev_color1 = -1  # 前一个房子最小成本对应的颜色
        
        # 遍历每个房子
        for i in range(n):
            # 当前房子的最小成本和次小成本
            curr_min1 = curr_min2 = float('inf')
            curr_color1 = -1
            
            # 遍历每种颜色
            for j in range(k):
                # 计算选择颜色 j 的总成本
                if j == prev_color1:
                    # 如果当前颜色与前一个房子的最小成本颜色相同，使用次小成本
                    cost = costs[i][j] + prev_min2
                else:
                    # 否则使用最小成本
                    cost = costs[i][j] + prev_min1
                
                # 更新当前房子的最小和次小成本
                if cost < curr_min1:
                    curr_min2 = curr_min1
                    curr_min1 = cost
                    curr_color1 = j
                elif cost < curr_min2:
                    curr_min2 = cost
            
            # 更新前一个房子的状态
            prev_min1, prev_min2 = curr_min1, curr_min2
            prev_color1 = curr_color1
        
        # 返回最后一个房子的最小成本
        return prev_min1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times k)$，其中 $n$ 是房子数量，$k$ 是颜色数量。需要遍历每个房子的每种颜色。
- **空间复杂度**：$O(1)$，只使用了常数个额外变量，不依赖于输入规模。
