# [0656. 成本最小路径](https://leetcode.cn/problems/coin-path/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [0656. 成本最小路径 - 力扣](https://leetcode.cn/problems/coin-path/)

## 题目大意

**描述**：

给定一个整数数组 $coins$（下标从 $1$ 开始）长度为 $n$，以及一个整数 $maxJump$。你可以跳到数组 $coins$ 的任意下标 $i$（满足 $coins[i] \ne -1$），访问下标 $i$ 时需要支付 $coins[i]$。此外，如果你当前位于下标 $i$，你只能跳到下标 $i + k$（满足 $i + k \le n$），其中 $k$ 是范围 $[1, maxJump]$ 内的一个值。

初始时你位于下标 $1$（$coins[1]$ 不是 $-1$）。

**要求**：

找到一条到达下标 $n$ 的成本最小路径。

返回一个整数数组，包含你访问的下标顺序，以便你以最小成本达到下标 $n$。如果存在多条成本相同的路径，返回 **字典序最小** 的路径。如果无法达到下标 $n$，返回一个空数组。

路径 $p_1 = [Pa_1, Pa_2, ..., Pa_x]$ 的长度为 $x$，路径 $p_2 = [Pb_1, Pb_2, ..., Pb_x]$ 的长度为 $y$，如果在两条路径的第一个不同的下标 $j$ 处，$Pa_j$ 小于 $Pb_j$，则 $p_1$ 在字典序上小于 $p_2$；如果不存在这样的 $j$，则较短的路径字典序较小。

**说明**：

- $1 \le coins.length \le 10^3$。
- $-1 \le coins[i] \le 10^3$。
- $coins[1] \ne -1$。
- $1 \le maxJump \le 10^3$。

**示例**：

- 示例 1：

```python
输入：coins = [1,2,4,-1,2], maxJump = 2
输出：[1,3,5]
```

- 示例 2：

```python
输入：coins = [1,2,4,-1,2], maxJump = 1
输出：[]
```

## 解题思路

### 思路 1：动态规划（反向）

这道题目要求找到一条到达终点的成本最小路径，如果存在多条成本相同的路径，返回字典序最小的路径。

我们可以使用**反向动态规划**来解决这个问题。从终点往前推，定义 $dp[i]$ 表示从位置 $i$ 到达终点的最小成本。

**为什么使用反向DP？**
- 当成本相同时，我们需要选择字典序最小的路径
- 从后往前DP时，如果成本相同，我们选择索引较小的下一个节点，这样可以保证字典序最小
- 如果从前往后DP，即使选择索引较小的前驱节点，也无法保证整个路径的字典序最小

**算法步骤**：

1. 初始化 $dp$ 数组，$dp[n-1] = coins[n-1]$（终点位置）。
2. 从后往前遍历每个位置 $i$，枚举所有可能的下一个位置 $j$（满足 $i < j \le i + maxJump$ 且 $j < n$），更新 $dp[i]$。
3. 使用 $next[i]$ 数组记录从位置 $i$ 出发的下一个节点。如果成本相同，选择索引较小的下一个节点（保证字典序最小）。
4. 从起点开始，沿着 $next$ 数组构造路径。

**注意**：如果某个位置的 $coins[i] = -1$，则该位置不可达。

### 思路 1：代码

```python
class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        
        # 如果起点或终点不可达，返回空数组
        if coins[0] == -1 or coins[n - 1] == -1:
            return []
        
        # dp[i] 表示从位置 i 到达终点的最小成本
        dp = [float('inf')] * n
        dp[n - 1] = coins[n - 1]
        
        # next[i] 表示从位置 i 出发的下一个节点（用于构造字典序最小的路径）
        next_node = [-1] * n
        
        # 从后往前进行动态规划
        for i in range(n - 2, -1, -1):
            if coins[i] == -1:
                continue
            
            # 枚举所有可能的下一个位置
            for j in range(i + 1, min(i + maxJump + 1, n)):
                if coins[j] == -1:
                    continue
                
                # 如果从 j 无法到达终点，跳过
                if dp[j] == float('inf'):
                    continue
                
                cost = coins[i] + dp[j]
                
                # 更新最小成本和下一个节点
                if cost < dp[i]:
                    dp[i] = cost
                    next_node[i] = j
                elif cost == dp[i] and (next_node[i] == -1 or j < next_node[i]):
                    # 成本相同，选择索引较小的下一个节点（保证字典序最小）
                    next_node[i] = j
        
        # 如果无法从起点到达终点
        if dp[0] == float('inf'):
            return []
        
        # 从起点开始，沿着 next_node 数组构造路径
        path = []
        i = 0
        
        # 沿着 next_node 数组遍历，直到到达终点
        while i < n and next_node[i] >= 0:
            path.append(i + 1)  # 题目中位置从 1 开始
            i = next_node[i]
        
        # 检查是否成功到达终点
        if i == n - 1 and coins[i] >= 0:
            path.append(n)
        else:
            return []
        
        return path
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times maxJump)$，其中 $n$ 是数组的长度。需要两层循环，外层循环 $n$ 次，内层循环最多 $maxJump$ 次。
- **空间复杂度**：$O(n)$。需要使用两个长度为 $n$ 的数组存储动态规划的状态和下一个节点信息。
