# [0740. 删除并获得点数](https://leetcode.cn/problems/delete-and-earn/)

- 标签：数组、哈希表、动态规划
- 难度：中等

## 题目链接

- [0740. 删除并获得点数 - 力扣](https://leetcode.cn/problems/delete-and-earn/)

## 题目大意

**描述**：

给定一个整数数组 $nums$，你可以对它进行一些操作。

每次操作中，选择任意一个 $nums[i]$，删除它并获得 $nums[i]$ 的点数。之后，你必须删除所有等于 $nums[i] - 1$ 和 $nums[i] + 1$ 的元素。

开始你拥有 $0$ 个点数。

**要求**：

返回你能通过这些操作获得的最大点数。

**说明**：

- $1 \le nums.length \le 2 * 10^{4}$。
- $1 \le nums[i] \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
```

- 示例 2：

```python
输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
```

## 解题思路

### 思路 1：动态规划

这道题可以转化为「打家劫舍」问题。选择数字 $x$ 后，所有 $x - 1$ 和 $x + 1$ 都会被删除，相当于不能选择相邻的数字。

**实现步骤**：

1. 统计每个数字的总点数：$total[i]$ 表示选择所有数字 $i$ 能获得的总点数。
2. 问题转化为：在数组 $total$ 中选择一些不相邻的元素，使得和最大。
3. 定义 $dp[i]$ 表示考虑前 $i$ 个数字能获得的最大点数：
   - $dp[i] = \max(dp[i-1], dp[i-2] + total[i])$
   - 不选择 $i$：$dp[i-1]$
   - 选择 $i$：$dp[i-2] + total[i]$（不能选择 $i-1$）

### 思路 1：代码

```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 统计每个数字的总点数
        max_num = max(nums)
        total = [0] * (max_num + 1)
        for num in nums:
            total[num] += num
        
        # 动态规划
        if max_num == 0:
            return total[0]
        
        # dp[i] 表示考虑前 i 个数字能获得的最大点数
        prev2 = total[0]  # dp[i-2]
        prev1 = max(total[0], total[1])  # dp[i-1]
        
        for i in range(2, max_num + 1):
            curr = max(prev1, prev2 + total[i])
            prev2 = prev1
            prev1 = curr
        
        return prev1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 是 $nums$ 的长度，$m$ 是 $nums$ 中的最大值。
- **空间复杂度**：$O(m)$，$total$ 数组的空间。
