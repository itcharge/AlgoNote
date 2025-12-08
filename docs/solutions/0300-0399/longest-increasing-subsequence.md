# [0300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

- 标签：数组、二分查找、动态规划
- 难度：中等

## 题目链接

- [0300. 最长递增子序列 - 力扣](https://leetcode.cn/problems/longest-increasing-subsequence/)

## 题目大意

**描述**：给定一个整数数组 $nums$。

**要求**：找到其中最长严格递增子序列的长度。

**说明**：

- **子序列**：由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，$[3,6,2,7]$ 是数组 $[0,3,1,6,2,2,7]$ 的子序列。
- $1 \le nums.length \le 2500$。
- $-10^4 \le nums[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4。
```

- 示例 2：

```python
输入：nums = [0,1,0,3,2,3]
输出：4
```

## 解题思路

### 思路 1：动态规划

###### 1. 阶段划分

按照子序列的结尾位置进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i]$ 表示为：以 $nums[i]$ 结尾的最长递增子序列长度。

###### 3. 状态转移方程

一个较小的数后边如果出现一个较大的数，则会形成一个更长的递增子序列。

对于满足 $0 \le j < i$ 的数组元素 $nums[j]$ 和 $nums[i]$ 来说：

- 如果 $nums[j] < nums[i]$，则 $nums[i]$ 可以接在 $nums[j]$ 后面，此时以 $nums[i]$ 结尾的最长递增子序列长度会在「以 $nums[j]$ 结尾的最长递增子序列长度」的基础上加 $1$，即 $dp[i] = dp[j] + 1$。

- 如果 $nums[j] \le nums[i]$，则 $nums[i]$ 不可以接在 $nums[j]$ 后面，可以直接跳过。

综上，我们的状态转移方程为：$dp[i] = max(dp[i], dp[j] + 1), 0 \le j < i, nums[j] < nums[i]$。

###### 4. 初始条件

默认状态下，把数组中的每个元素都作为长度为 $1$ 的递增子序列。即 $dp[i] = 1$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i]$ 表示为：以 $nums[i]$ 结尾的最长递增子序列长度。那为了计算出最大的最长递增子序列长度，则需要再遍历一遍 $dp$ 数组，求出最大值即为最终结果。

### 思路 1：动态规划代码

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1 for _ in range(size)]

        for i in range(size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$。两重循环遍历的时间复杂度是 $O(n^2)$，最后求最大值的时间复杂度是 $O(n)$，所以总体时间复杂度为 $O(n^2)$。
- **空间复杂度**：$O(n)$。用到了一维数组保存状态，所以总体空间复杂度为 $O(n)$。

### 思路 2：进阶的线性 DP + 二分查找

###### 1. 算法思想

使用 **数组作为可实时更新内部的单调栈**，结合 **贪心法** 和 **二分查找** 来优化时间复杂度。

核心思想：
- $tails[k]$ 表示长度为 $k+1$ 的 LIS 的最小末尾元素（无闲置索引，动态扩展）
- 对于每个元素 $x$，使用二分查找在 $tails$ 中找到第一个 $\ge x$ 的位置
- 如果 $x$ 比所有元素都大，则追加到 $tails$ 末尾，形成新的 LIS 长度
- 否则，用较小的 $x$ 更新 $tails[k]$，优化同长度 LIS 的末尾元素（变得更小）

###### 2. 算法步骤

1. 初始化 $tails$ 为空数组。
2. 遍历数组 $nums$ 中的每个元素 $x$：
   - 使用二分查找在 $tails$ 中找到第一个 $\ge x$ 的位置 $k$。
   - 如果 $k == len(tails)$，说明 $x$ 比所有元素都大，追加到 $tails$ 末尾。
   - 否则，用 $x$ 更新 $tails[k]$，优化同长度 LIS 的末尾元素。
3. 返回 $tails$ 的长度，即为最终 LIS 的长度。

### 思路 2：进阶的线性 DP + 二分查找代码

```python
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        # tails[k] 表示长度为 k+1 的 LIS 的最小末尾元素（无闲置索引，动态扩展）
        tails = list()
        for x in nums:
            # 二分查找：在tails中找首个≥x的位置
            k = bisect.bisect_left(tails, x)
            # 如果 x 比所有元素都大，k 的结果会是当前数组长度（末尾位置索引 +1）
            # x 直接新增在 tails 数组末尾，形成新问题（LIS 长度 +1）
            if k == len(tails):
                tails.append(x)
            # 用较小的 x 更新较大的 tails[k]，优化同长度 LIS 问题的末尾元素（变得更小）
            else:
                tails[k] = x
        
        # tails 的长度即为最终 LIS 问题的长度
        return len(tails)
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n \log n)$。遍历数组的时间复杂度是 $O(n)$，每个元素进行二分查找的时间复杂度是 $O(\log n)$，所以总体时间复杂度为 $O(n \log n)$。
- **空间复杂度**：$O(n)$。$tails$ 数组最多存储 $n$ 个元素，所以总体空间复杂度为 $O(n)$。

## 参考资料

- 【题解】[进阶的线性DP + 二分查找 ｜ 来自评论区](https://github.com/xiaos2021)