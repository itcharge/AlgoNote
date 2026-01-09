# [0956. 最高的广告牌](https://leetcode.cn/problems/tallest-billboard/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [0956. 最高的广告牌 - 力扣](https://leetcode.cn/problems/tallest-billboard/)

## 题目大意

**描述**：

你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。

你有一堆可以焊接在一起的钢筋 $rods$。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。

**要求**：

返回「广告牌的最大可能安装高度」。如果没法安装广告牌，请返回 0。

**说明**：

- $0 \le rods.length \le 20$。
- $1 \le rods[i] \le 10^{3}$。
- $sum(rods[i]) \le 5000$。

**示例**：

- 示例 1：

```python
输入：[1,2,3,6]
输出：6
解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。
```

- 示例 2：

```python
输入：[1,2,3,4,5,6]
输出：10
解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。
```

## 解题思路

### 思路 1：动态规划

这道题可以转化为：将钢筋分成两组，使得两组的和相等，求最大的和。

使用动态规划，$dp[diff]$ 表示当两组差值为 $diff$ 时，较小组的最大高度。

1. 初始化 $dp[0] = 0$，表示差值为 $0$ 时，较小组高度为 $0$。
2. 对于每根钢筋 $rod$，有三种选择：
   - 不选：不更新 $dp$。
   - 放入较大组：$dp[diff + rod] = \max(dp[diff + rod], dp[diff])$。
   - 放入较小组：$dp[|diff - rod|] = \max(dp[|diff - rod|], dp[diff] + \min(diff, rod))$。
3. 最终答案为 $dp[0]$。

### 思路 1：代码

```python
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[diff] 表示差值为 diff 时，较小组的最大高度
        dp = {0: 0}
        
        for rod in rods:
            new_dp = dp.copy()
            for diff, smaller in dp.items():
                # 将 rod 加到较大组
                new_diff = diff + rod
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), smaller)
                
                # 将 rod 加到较小组
                if rod > diff:
                    # 较小组变成较大组
                    new_diff = rod - diff
                    new_smaller = smaller + diff
                else:
                    # 较小组仍是较小组
                    new_diff = diff - rod
                    new_smaller = smaller + rod
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_smaller)
            
            dp = new_dp
        
        return dp[0]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times S)$，其中 $n$ 是钢筋数量，$S$ 是所有钢筋长度之和。
- **空间复杂度**：$O(S)$，需要存储所有可能的差值状态。
