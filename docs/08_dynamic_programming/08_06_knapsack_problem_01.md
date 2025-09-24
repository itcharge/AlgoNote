## 1. 背包问题简介

### 1.1 背包问题的定义

> **背包问题**：背包问题是线性 DP 问题中一类经典模型。其基本描述为：给定若干物品，每种物品有各自的重量、价值和数量限制，以及一个最大承重为 $W$ 的背包。要求在不超过背包承重上限的前提下，选择若干物品放入背包，使得背包内物品的总价值最大。

![背包问题](https://qcdn.itcharge.cn/images/20240514111553.png)

根据物品数量和选择方式的不同，背包问题主要分为：0-1 背包问题、完全背包问题、多重背包问题、分组背包问题和混合背包问题等类型。

### 1.2 背包问题的暴力解法思路

背包问题的暴力解法非常直接。假设有 $n$ 件物品，我们可以枚举所有 $n$ 件物品的选取方案（每件物品选或不选），即遍历所有 $2^n$ 种组合。对于每一种组合，判断其总重量是否不超过背包容量，并计算其总价值，最终取所有可行方案中的最大价值。该方法的时间复杂度为 $O(2^n)$，属于指数级，效率较低。

由于暴力解法效率低下，实际应用中我们通常采用动态规划方法来大幅降低时间复杂度。

接下来将详细介绍如何利用动态规划高效地解决各类背包问题。

## 2. 0-1 背包问题简介

> **0-1 背包问题**：给定 $n$ 件物品和一个最大承重为 $W$ 的背包。每件物品的重量为 $weight[i]$，价值为 $value[i]$，每种物品只能选择一次。请问在不超过背包承重的前提下，最多能获得多少总价值？

![0-1 背包问题](https://qcdn.itcharge.cn/images/20240514111617.png)

## 3. 0-1 背包问题的基本思路

> **0-1 背包问题的核心**：每种物品只能选一次，可以选择放或不放。

#### 思路 1：动态规划（二维数组）

###### 1. 阶段划分

以物品序号和当前背包剩余容量为阶段。

###### 2. 定义状态

令 $dp[i][w]$ 表示前 $i$ 件物品，放入容量不超过 $w$ 的背包时可获得的最大价值。

其中 $i$ 表示考虑前 $i$ 件物品，$w$ 表示当前背包容量。

###### 3. 状态转移方程

对于「将前 $i$ 件物品放入容量为 $w$ 的背包，能获得的最大价值」这个子问题，我们只需关注第 $i - 1$ 件物品的选择情况（即放或不放），即可将问题递归地转化为只与前 $i - 1$ 件物品相关的子问题：

1. **不放第 $i - 1$ 件物品**：此时最大价值为 $dp[i - 1][w]$，即前 $i - 1$ 件物品放入容量为 $w$ 的背包的最大价值。
2. **放第 $i - 1$ 件物品**：前提是背包剩余容量足够（$w \ge weight[i - 1]$），此时最大价值为 $dp[i-1][w - weight[i - 1]] + value[i - 1]$，即前 $i - 1$ 件物品放入剩余容量为 $w - weight[i - 1]$ 的背包的最大价值，再加上第 $i - 1$ 件物品的价值。

因此，状态转移分两种情况：

- 当 $w < weight[i - 1]$ 时，第 $i - 1$ 件物品无法放入背包，$dp[i][w] = dp[i - 1][w]$。
- 当 $w \ge weight[i - 1]$ 时，第 $i - 1$ 件物品可选可不选，$dp[i][w] = \max\{dp[i - 1][w],\ dp[i - 1][w - weight[i - 1]] + value[i - 1]\}$。

综上，状态转移方程为：

$dp[i][w] = \begin{cases} dp[i - 1][w] & w < weight[i - 1] \\ \max\{dp[i - 1][w],\ dp[i-1][w - weight[i - 1]] + value[i - 1]\} & w \ge weight[i-1] \end{cases}$

###### 4. 初始条件

- 当背包容量为 $0$ 时，无论有多少物品，最大价值为 $0$，即 $dp[i][0] = 0$，$0 \le i \le size$。
- 当没有物品时，无论背包容量多少，最大价值为 $0$，即 $dp[0][w] = 0$，$0 \le w \le W$。

###### 5. 最终结果

最终答案为 $dp[size][W]$，即用前 $size$ 件物品，背包容量为 $W$ 时能获得的最大价值。

#### 思路 1：代码

```python
class Solution:
    # 思路 1：动态规划（二维数组）
    def zeroOnePackMethod1(self, weight: [int], value: [int], W: int) -> int:
        """
        0-1 背包问题二维动态规划解法
        :param weight: List[int]，每件物品的重量
        :param value: List[int]，每件物品的价值
        :param W: int，背包最大承重
        :return: int，最大可获得价值
        """
        size = len(weight)
        # dp[i][w] 表示前 i 件物品，容量不超过 W 时的最大价值
        dp = [[0] * (W + 1) for _ in range(size + 1)]

        # 遍历每一件物品
        for i in range(1, size + 1):
            # 遍历每一种可能的背包容量
            for w in range(W + 1):
                if w < weight[i - 1]:
                    # 当前物品放不下，继承上一个状态
                    dp[i][w] = dp[i - 1][w]
                else:
                    # 当前物品可选，取放与不放的最大值
                    dp[i][w] = max(
                        dp[i - 1][w],  # 不放当前物品
                        dp[i - 1][w - weight[i - 1]] + value[i - 1]  # 放当前物品
                    )
        # 返回前 size 件物品、容量为 W 时的最大价值
        return dp[size][W]
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times W)$，其中 $n$ 为物品数量，$W$ 为背包的载重上限。
- **空间复杂度**：$O(n \times W)$。

## 4. 0-1 背包问题的滚动数组优化

通过前面的分析可以发现，在依次处理第 $1 \sim n$ 件物品时，「前 $i$ 件物品的状态」只依赖于「前 $i - 1$ 件物品的状态」，与更早之前的状态无关。

换句话说，状态转移时只涉及当前行（第 $i$ 行）的 $dp[i][w]$ 和上一行（第 $i - 1$ 行）的 $dp[i - 1][w]$、$dp[i - 1][w - weight[i-1]]$。

因此，我们无需保存所有阶段的状态，只需保留当前阶段和上一阶段的状态即可。可以用两个一维数组分别存储相邻两阶段的所有状态：$dp[0][w]$ 存储 $dp[i - 1][w]$，$dp[1][w]$ 存储 $dp[i][w]$。

进一步优化时，其实只需一个一维数组 $dp[w]$，利用「滚动数组」思想，将动态规划的第一维去掉，从而实现空间优化。

#### 思路 2：动态规划 + 滚动数组优化

###### 1. 阶段划分

以当前背包的剩余容量 $w$ 作为阶段。

###### 2. 定义状态

令 $dp[w]$ 表示：在背包容量不超过 $w$ 的情况下，能够获得的最大总价值。

###### 3. 状态转移方程

状态转移如下：

$$
dp[w] = \begin{cases}
dp[w], & w < weight[i - 1] \\
\max\{dp[w],\ dp[w - weight[i - 1]] + value[i - 1]\}, & w \geq weight[i - 1]
\end{cases}
$$

在处理第 $i$ 件物品时，$dp[w]$ 只依赖于上一阶段（即第 $i - 1$ 件物品处理完后）的 $dp[w]$ 和 $dp[w - weight[i - 1]]$。因此，为了避免状态被提前覆盖，必须对 $w$ 采用从大到小（即从 $W$ 到 $0$）的逆序遍历。这样可以确保每次转移用到的 $dp[w - weight[i - 1]]$ 仍然是上一阶段的值。

如果采用从小到大（正序）遍历，则 $dp[w - weight[i - 1]]$ 可能已经被本轮更新，导致状态转移错误。

实际上，当 $w < weight[i-1]$ 时，当前物品无法放入背包，$dp[w]$ 保持不变，无需更新。因此逆序遍历时只需从 $W$ 遍历到 $weight[i - 1]$。

###### 4. 初始条件

- 对于所有 $0 \leq w \leq W$，$dp[w] = 0$，表示背包容量为 $w$ 时，尚未放入任何物品，最大价值为 $0$。

###### 5. 最终结果

最终答案为 $dp[W]$，即背包容量为 $W$ 时能够获得的最大总价值。

#### 思路 2：代码

```python
class Solution:
    # 思路 2：动态规划 + 滚动数组优化
    def zeroOnePackMethod2(self, weight: [int], value: [int], W: int) -> int:
        """
        0-1 背包问题的滚动数组优化解法
        :param weight: List[int]，每件物品的重量
        :param value: List[int]，每件物品的价值
        :param W: int，背包最大承重
        :return: int，背包可获得的最大价值
        """
        size = len(weight)
        # dp[w] 表示容量为 w 时背包可获得的最大价值
        dp = [0] * (W + 1)

        # 遍历每一件物品
        for i in range(size):
            # 必须逆序遍历容量，防止状态被提前覆盖
            for w in range(W, weight[i] - 1, -1):
                # 状态转移：不选第 i 件物品 or 选第 i 件物品
                # dp[w] = max(不选, 选)
                dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
                # 解释：
                # dp[w]：不选第 i 件物品，价值不变
                # dp[w - weight[i]] + value[i]：选第 i 件物品，容量减少，相应加上价值

        return dp[W]
```

#### 思路 2：复杂度分析

- **时间复杂度**：$O(n \times W)$，其中 $n$ 为物品数量，$W$ 为背包的载重上限。
- **空间复杂度**：$O(W)$。

## 5. 0-1 背包问题的应用

### 5.1 经典例题：分割等和子集

#### 5.1.1 题目链接

- [416. 分割等和子集 - 力扣](https://leetcode.cn/problems/partition-equal-subset-sum/)

#### 5.1.2 题目大意

**描述**：给定一个只包含正整数的非空数组 $nums$。

**要求**：判断是否可以将这个数组分成两个子集，使得两个子集的元素和相等。

**说明**：

- $1 \le nums.length \le 200$。
- $1 \le nums[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11]。
```

- 示例 2：

```python
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
```

#### 5.1.3 解题思路

##### 思路 1：动态规划

本题实质是：能否从数组中选出若干元素，使其和恰好等于整个数组元素和的一半。

这实际上就是典型的「0-1 背包问题」：

1. 设数组元素和为 $sum$，目标为 $target = \frac{sum}{2}$，即背包容量。
2. 数组中的每个元素 $nums[i]$ 视为一件物品，其重量和价值均为 $nums[i]$。
3. 每种物品只能选择一次。
4. 若能恰好装满容量为 $target$ 的背包，则最大价值也为 $target$。

因此，问题转化为：给定物品数组 $nums$，每件物品重量和价值均为 $nums[i]$，背包容量为 $target$，每件物品最多选一次，问能否恰好装满背包。

###### 1. 阶段划分

以当前背包容量 $w$ 作为阶段。

###### 2. 定义状态

令 $dp[w]$ 表示：从 $nums$ 中选取若干元素，恰好装入容量为 $w$ 的背包时，元素和的最大值。

###### 3. 状态转移方程

$dp[w] = \begin{cases}
dp[w] & w < nums[i - 1] \\
\max\{dp[w],\ dp[w - nums[i - 1]] + nums[i - 1]\} & w \geq nums[i - 1]
\end{cases}$

###### 4. 初始条件

- 对所有 $0 \leq w \leq W$，$dp[w] = 0$，即不选任何物品时最大和为 $0$。

###### 5. 最终结果

只需判断 $dp[target]$ 是否等于 $target$。若 $dp[target] == target$，说明存在子集和为 $target$，返回 `True`；否则返回 `False`。

##### 思路 1：代码

```python
class Solution:
    # 动态规划 + 滚动数组优化的 0-1 背包实现
    def zeroOnePackMethod2(self, weight: list[int], value: list[int], W: int) -> int:
        size = len(weight)
        dp = [0] * (W + 1)  # dp[w] 表示容量为 w 时的最大价值

        # 枚举每一件物品
        for i in range(size):
            # 必须逆序遍历容量，防止同一物品被重复选择
            for w in range(W, weight[i] - 1, -1):
                # 状态转移：不选 / 选第 i 件物品
                dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
        return dp[W]

    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        # 如果总和为奇数，无法平分
        if total % 2 != 0:
            return False
        target = total // 2
        # 0-1 背包：每个数只能选一次，能否恰好装满 target
        return self.zeroOnePackMethod2(nums, nums, target) == target
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times target)$，其中 $n$ 为数组 $nums$ 的元素个数，$target$ 是整个数组元素和的一半。
- **空间复杂度**：$O(target)$。

## 练习题目

- [0416. 分割等和子集](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0400-0499/partition-equal-subset-sum.md)
- [0494. 目标和](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0400-0499/target-sum.md)
- [1049. 最后一块石头的重量 II](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1000-1099/last-stone-weight-ii.md)

- [0-1 背包问题题目列表](https://github.com/itcharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#0-1-%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E9%A2%98%E7%9B%AE)


## 参考资料

- 【资料】[背包九讲 - 崔添翼](https://github.com/tianyicui/pack)
- 【文章】[背包 DP - OI Wiki](https://oi-wiki.org/dp/knapsack/)
- 【文章】[背包问题 第四讲 - 宫水三叶的刷题日记](https://juejin.cn/post/7003243733604892685)
- 【文章】[Massive Algorithms: 讲透完全背包算法](https://massivealgorithms.blogspot.com/2015/06/unbounded-knapsack-problem.html)
