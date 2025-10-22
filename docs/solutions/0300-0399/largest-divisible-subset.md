# [0368. 最大整除子集](https://leetcode.cn/problems/largest-divisible-subset/)

- 标签：数组、数学、动态规划、排序
- 难度：中等

## 题目链接

- [0368. 最大整除子集 - 力扣](https://leetcode.cn/problems/largest-divisible-subset/)

## 题目大意

**描述**：

给定一个由「无重复」正整数组成的集合 $nums$。

**要求**：

请你找出并返回其中最大的整除子集 $answer$，子集中每一元素对 $(answer[i], answer[j])$ 都应当满足：

- $answer[i] \% answer[j] == 0$，或
- $answer[j] \% answer[i] == 0$

如果存在多个有效解子集，返回其中任何一个均可。

**说明**：

- $1 \le nums.length \le 10^{3}$。
- $1 \le nums[i] \le 2 * 10^{9}$。
- nums 中的所有整数 互不相同。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。
```

- 示例 2：

```python
输入：nums = [1,2,4,8]
输出：[1,2,4,8]
```

## 解题思路

### 思路 1：动态规划 + 排序

这道题的核心思想是：**先对数组排序，然后使用动态规划找到最长的整除子集，最后回溯构造结果**。

解题步骤：

1. **排序**：将数组 $nums$ 按升序排序，这样对于任意 $i < j$，如果 $nums[j] \% nums[i] == 0$，则 $nums[i]$ 可以整除 $nums[j]$。

2. **动态规划**：
   - 定义 $dp[i]$ 表示以 $nums[i]$ 结尾的最长整除子集的长度。
   - 定义 $parent[i]$ 表示以 $nums[i]$ 结尾的最长整除子集中，$nums[i]$ 的前一个元素的索引。
   - 状态转移方程：$dp[i] = \max(dp[j] + 1)$，其中 $j < i$ 且 $nums[i] \% nums[j] == 0$。

3. **找最大值**：遍历 $dp$ 数组，找到最大值 $max\_len$ 和对应的索引 $max\_index$。

4. **回溯构造结果**：从 $max\_index$ 开始，通过 $parent$ 数组回溯构造最长整除子集。

**关键点**：

- 排序后，只需要检查 $nums[i] \% nums[j] == 0$（$j < i$），因为如果 $nums[j] > nums[i]$，则 $nums[j] \% nums[i] \neq 0$。
- 使用 $parent$ 数组记录路径，便于后续回溯构造结果。
- 时间复杂度主要由排序决定，为 $O(n^2)$。

### 思路 1：代码

```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # 对数组进行排序
        nums.sort()
        n = len(nums)
        
        # dp[i] 表示以 nums[i] 结尾的最长整除子集的长度
        dp = [1] * n
        # parent[i] 表示以 nums[i] 结尾的最长整除子集中，nums[i] 的前一个元素的索引
        parent = [-1] * n
        
        # 动态规划计算最长长度
        for i in range(1, n):
            for j in range(i):
                # 如果 nums[i] 能被 nums[j] 整除，且当前长度更优
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
        
        # 找到最长子集的长度和结束位置
        max_len = max(dp)
        max_index = dp.index(max_len)
        
        # 回溯构造结果
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        
        # 由于是回溯构造的，需要反转结果
        return result[::-1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是数组的长度。排序需要 $O(n \log n)$ 时间，动态规划需要 $O(n^2)$ 时间，回溯构造结果需要 $O(n)$ 时间。
- **空间复杂度**：$O(n)$，需要 $O(n)$ 的空间存储 $dp$ 数组和 $parent$ 数组。
