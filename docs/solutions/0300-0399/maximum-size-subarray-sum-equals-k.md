# [0325. 和等于 k 的最长子数组长度](https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/)

- 标签：数组、哈希表、前缀和
- 难度：中等

## 题目链接

- [0325. 和等于 k 的最长子数组长度 - 力扣](https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/)

## 题目大意

**描述**：

给定一个数组 $nums$ 和一个目标值 $k$。

**要求**：

找到和等于 $k$ 的最长连续子数组长度。如果不存在任意一个符合要求的子数组，则返回 $0$。

**说明**：

- $1 \le nums.length \le 2 \times 10^{5}$。
- $-10^{4} \le nums[i] \le 10^{4}$。
- $-10^{9} \le k \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入: nums = [1,-1,5,-2,3], k = 3
输出: 4 
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
```

- 示例 2：

```python
输入: nums = [-2,-1,2,1], k = 1
输出: 2 
解释: 子数组 [-1, 2] 和等于 1，且长度最长。
```

## 解题思路

### 思路 1：前缀和 + 哈希表

这道题的核心思想是：**使用前缀和配合哈希表来快速查找满足条件的子数组**。

解题步骤：

1. **计算前缀和**：定义 $prefix\_sum[i]$ 表示数组前 $i$ 个元素的和，即 $prefix\_sum[i] = \sum_{j=0}^{i-1} nums[j]$。

2. **利用前缀和性质**：对于子数组 $nums[i:j+1]$，其和为 $prefix\_sum[j+1] - prefix\_sum[i]$。如果这个和等于 $k$，则有 $prefix\_sum[j+1] - prefix\_sum[i] = k$，即 $prefix\_sum[i] = prefix\_sum[j+1] - k$。

3. **哈希表记录**：使用哈希表 $prefix\_map$ 记录每个前缀和第一次出现的位置。对于当前位置 $i$，如果 $prefix\_sum[i] - k$ 在哈希表中存在，说明存在一个子数组的和为 $k$。

4. **更新最长长度**：每次找到满足条件的子数组时，更新最大长度。

**关键点**：

- 初始化时，$prefix\_sum[0] = 0$ 对应空数组，位置为 $-1$。
- 哈希表只记录每个前缀和第一次出现的位置，这样可以保证找到的子数组长度最长。
- 对于每个位置，先检查是否存在满足条件的前缀和，再更新当前前缀和的位置。

### 思路 1：代码

```python
from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        # 哈希表记录前缀和第一次出现的位置
        prefix_map = {0: -1}  # 前缀和为0的位置为-1（空数组）
        prefix_sum = 0
        max_length = 0
        
        for i in range(len(nums)):
            # 计算当前位置的前缀和
            prefix_sum += nums[i]
            
            # 检查是否存在前缀和 prefix_sum - k
            # 如果存在，说明从 prefix_map[prefix_sum - k] + 1 到 i 的子数组和为 k
            if prefix_sum - k in prefix_map:
                # 计算当前子数组的长度
                current_length = i - prefix_map[prefix_sum - k]
                max_length = max(max_length, current_length)
            
            # 如果当前前缀和还没有记录，则记录其位置
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        
        return max_length
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。只需要遍历数组一次，每次哈希表的查找和插入操作都是 $O(1)$。
- **空间复杂度**：$O(n)$，哈希表最多存储 $n$ 个不同的前缀和。
