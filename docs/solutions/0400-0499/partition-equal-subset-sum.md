# [0416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [0416. 分割等和子集 - 力扣](https://leetcode.cn/problems/partition-equal-subset-sum/)

## 题目大意

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

## 解题思路

### 思路 1：动态规划

这道题换一种说法就是：从数组中选择一些元素组成一个子集，使子集的元素和恰好等于整个数组元素和的一半。

这样的话，这道题就可以转变为「0-1 背包问题」。

1. 把整个数组中的元素和记为 $sum$，把元素和的一半 $target = \frac{sum}{2}$ 看做是「0-1 背包问题」中的背包容量。
2. 把数组中的元素 $nums[i]$ 看做是「0-1 背包问题」中的物品。
3. 第 $i$ 件物品的重量为 $nums[i]$，价值也为 $nums[i]$。
4. 因为物品的重量和价值相等，如果能装满载重上限为 $target$ 的背包，那么得到的最大价值也应该是 $target$。

这样问题就转变为：给定一个数组 $nums$ 代表物品，数组元素和的一半 $target = \frac{sum}{2}$ 代表背包的载重上限。其中第 $i$ 件物品的重量为 $nums[i]$，价值为 $nums[i]$，每件物品有且只有 $1$ 件。请问在总重量不超过背包装载重量上限的情况下，能否将背包装满从而得到最大价值？

###### 1. 划分阶段

当前背包的载重上限进行阶段划分。

###### 2. 定义状态

定义状态 $dp[w]$ 表示为：从数组 $nums$ 中选择一些元素，放入最多能装元素和为 $w$ 的背包中，得到的元素和最大为多少。

###### 3. 状态转移方程

$dp[w] = \begin{cases} dp[w] & w < nums[i - 1] \cr max \lbrace dp[w], \quad dp[w - nums[i - 1]] + nums[i - 1] \rbrace & w \ge nums[i - 1] \end{cases}$

###### 4. 初始条件

- 无论背包载重上限为多少，只要不选择物品，可以获得的最大价值一定是 $0$，即 $dp[w] = 0, 0 \le w \le W$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[target]$ 表示为：从数组 $nums$ 中选择一些元素，放入最多能装元素和为 $target = \frac{sum}{2}$ 的背包中，得到的元素和最大值。 

所以最后判断一下 $dp[target]$ 是否等于 $target$。如果 $dp[target] == target$，则说明集合中的子集刚好能够凑成总和 $target$，此时返回 `True`；否则返回 `False`。

### 思路 1：代码

```python
class Solution:
    # 思路 2：动态规划 + 滚动数组优化
    def zeroOnePackMethod2(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量（避免状态值错误）
            for w in range(W, weight[i - 1] - 1, -1):
                # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])
                
        return dp[W]

    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums & 1:
            return False

        target = sum_nums // 2
        return self.zeroOnePackMethod2(nums, nums, target) == target
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times target)$，其中 $n$ 为数组 $nums$ 的元素个数，$target$ 是整个数组元素和的一半。
- **空间复杂度**：$O(target)$。

