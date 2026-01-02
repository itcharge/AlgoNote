# [0689. 三个无重叠子数组的最大和](https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays/)

- 标签：数组、动态规划、前缀和、滑动窗口
- 难度：困难

## 题目链接

- [0689. 三个无重叠子数组的最大和 - 力扣](https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays/)

## 题目大意

**描述**：

给定一个整数数组 $nums$ 和一个整数 $k$。

**要求**：

找出三个长度为 $k$、互不重叠、且全部数字和最大的子数组，并返回这三个子数组。

以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 $0$ 开始）。如果有多个结果，返回字典序最小的一个。

**说明**：

- $1 \le nums.length \le 2 \times 10^{4}$。
- $1 \le nums[i] \lt 216$。
- $1 \le k \le floor(nums.length / 3)$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,1,2,6,7,5,1], k = 2
输出：[0,3,5]
解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
```

- 示例 2：

```python
输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
输出：[0,2,4]
```

## 解题思路

### 思路 1：动态规划 + 滑动窗口

这道题目要求找出三个长度为 $k$ 的无重叠子数组，使得它们的和最大。使用动态规划记录最优解。

1. 首先使用滑动窗口计算所有长度为 $k$ 的子数组的和，存储在数组 $sums$ 中。
2. 定义三个数组：
   - $left[i]$：表示在 $[0, i]$ 范围内，和最大的子数组的起始索引。
   - $right[i]$：表示在 $[i, n-k]$ 范围内，和最大的子数组的起始索引。
   - 中间的子数组通过遍历确定。
3. 遍历中间子数组的所有可能位置 $j$（范围 $[k, n-2k]$）：
   - 左侧子数组的最优位置为 $left[j-k]$。
   - 右侧子数组的最优位置为 $right[j+k]$。
   - 计算三个子数组的总和，更新最大值和对应的索引。
4. 返回三个子数组的起始索引。

### 思路 1：代码

```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # 计算所有长度为 k 的子数组的和
        sums = []
        window_sum = sum(nums[:k])
        sums.append(window_sum)
        
        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            sums.append(window_sum)
        
        # left[i] 表示在 [0, i] 范围内和最大的子数组的起始索引
        left = [0] * len(sums)
        best_idx = 0
        for i in range(len(sums)):
            if sums[i] > sums[best_idx]:
                best_idx = i
            left[i] = best_idx
        
        # right[i] 表示在 [i, len(sums)-1] 范围内和最大的子数组的起始索引
        right = [0] * len(sums)
        best_idx = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best_idx]:
                best_idx = i
            right[i] = best_idx
        
        # 遍历中间子数组的位置
        max_sum = 0
        result = [-1, -1, -1]
        
        for j in range(k, len(sums) - k):
            l = left[j - k]
            r = right[j + k]
            total = sums[l] + sums[j] + sums[r]
            
            if total > max_sum:
                max_sum = total
                result = [l, j, r]
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。需要遍历数组多次，但每次都是线性时间。
- **空间复杂度**：$O(n)$，需要使用数组存储子数组的和以及左右最优位置。
