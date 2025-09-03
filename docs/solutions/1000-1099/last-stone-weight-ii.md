# [1049. 最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [1049. 最后一块石头的重量 II - 力扣](https://leetcode.cn/problems/last-stone-weight-ii/)

## 题目大意

**描述**：有一堆石头，用整数数组 $stones$ 表示，其中 $stones[i]$ 表示第 $i$​ 块石头的重量。每一回合，从石头中选出任意两块石头，将这两块石头一起粉碎。假设石头的重量分别为 $x$ 和 $y$。且 $x \le y$，则结果如下：

- 如果 $x = y$，则两块石头都会被完全粉碎；
- 如果 $x < y$，则重量为 $x$ 的石头被完全粉碎，而重量为 $y$ 的石头新重量为 $y - x$。

**要求**：最后，最多只会剩下一块石头，返回此石头的最小可能重量。如果没有石头剩下，则返回 $0$。

**说明**：

- $1 \le stones.length \le 30$。
- $1 \le stones[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
```

- 示例 2：

```python
输入：stones = [31,26,33,21,40]
输出：5
```

## 解题思路

### 思路 1：动态规划

选取两块石头，重新放回去的重量是两块石头的差值绝对值。重新放回去的石头还会进行选取，然后进行粉碎，直到最后只剩一块或者不剩石头。

这个问题其实可以转化为：把一堆石头尽量平均的分成两对，求两堆石头重量差的最小值。

这就和「[0416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)」有点相似。两堆石头的重量要尽可能的接近数组总数量和的一半。

进一步可以变为：「0-1 背包问题」。

1. 假设石头总重量和为 $sum$，将一堆石头放进载重上限为 $sum / 2$ 的背包中，获得的最大价值为 $max\_weight$（即其中一堆石子的重量）。另一堆石子的重量为 $sum - max\_weight$。
2. 则两者的差值为 $sum - 2 \times max\_weight$，即为答案。

###### 1. 划分阶段

按照石头的序号进行阶段划分。

###### 2. 定义状态

定义状态 $dp[w]$ 表示为：将石头放入载重上限为 $w$ 的背包中可以获得的最大价值。

###### 3. 状态转移方程

$dp[w] = max \lbrace dp[w], dp[w - stones[i - 1]] + stones[i - 1] \rbrace$。

###### 4. 初始条件

- 无论背包载重上限为多少，只要不选择石头，可以获得的最大价值一定是 $0$，即 $dp[w] = 0, 0 \le w \le W$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[w]$ 表示为：将石头放入载重上限为 $w$ 的背包中可以获得的最大价值，即第一堆石头的价值为 $dp[size]$，第二堆石头的价值为 $sum - dp[size]$，最终答案为两者的差值，即 $sum - dp[size] \times 2$。

### 思路 1：代码

```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        W = 1500
        size = len(stones)
        dp = [0 for _ in range(W + 1)]
        target = sum(stones) // 2
        for i in range(1, size + 1):
            for w in range(target, stones[i - 1] - 1, -1):
                dp[w] = max(dp[w], dp[w - stones[i - 1]] + stones[i - 1])

        return sum(stones) - dp[target] * 2
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times W)$，其中 $n$ 为数组 $stones$ 的元素个数，$W$ 为数组 $stones$ 中元素和的一半。
- **空间复杂度**：$O(W)$。
