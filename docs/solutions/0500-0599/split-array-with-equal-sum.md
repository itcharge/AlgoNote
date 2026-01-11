# [0548. 将数组分割成和相等的子数组](https://leetcode.cn/problems/split-array-with-equal-sum/)

- 标签：数组、哈希表、前缀和
- 难度：困难

## 题目链接

- [0548. 将数组分割成和相等的子数组 - 力扣](https://leetcode.cn/problems/split-array-with-equal-sum/)

## 题目大意

**描述**：

给定一个整数数组 $nums$。

**要求**：

判断是否能找到三个索引 $i$、$j$、$k$，将数组分成四个非空子数组，使得这四个子数组的和相等。

具体来说，需要找到三个分割点 $i$、$j$、$k$（$1 \le i < j < k < n-1$），使得：

- 子数组 $(0, i - 1)$，$(i + 1, j - 1)$，$(j + 1, k - 1)$，$(k + 1, n - 1)$ 的和应该相等。

如果可以找到这样的分割，返回 $true$，否则返回 $false$。

**说明**：

- $n == nums.length。
- $1 \le nums.length \le 2000$。
- $-10^6 \le nums[i] \le 10^6$。

**示例**：

- 示例 1：

```python
输入: nums = [1,2,1,2,1,2,1]
输出: True
解释:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
```

- 示例 2：

```python
输入: nums = [1,2,1,2,1,2,1,2]
输出: false
```

## 解题思路

### 思路 1：前缀和 + 哈希表

关键观察：固定中间的分割点 $j$，然后在左边找满足条件的 $i$，在右边找满足条件的 $k$。

**算法步骤**：

1. 计算前缀和数组 $prefix$，其中 $prefix[i]$ 表示 $nums[0:i]$ 的和。
2. 枚举中间分割点 $j$（范围：$[3, n-4]$，保证每部分至少有一个元素）。
3. 对于每个 $j$：
   - 在左边找所有可能的和：遍历 $i \in [1, j-2]$，如果 $sum(nums[0:i]) = sum(nums[i+1:j])$，将这个和加入集合 $left\_sums$。
   - 在右边找所有可能的和：遍历 $k \in [j+2, n-2]$，如果 $sum(nums[j+1:k]) = sum(nums[k+1:n])$，检查这个和是否在 $left\_sums$ 中。
4. 如果找到匹配，返回 $true$。

### 思路 1：代码

```python
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7:  # 至少需要 7 个元素
            return False
        
        # 计算前缀和
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # 枚举中间分割点 j
        for j in range(3, n - 3):
            # 左边可能的和
            left_sums = set()
            for i in range(1, j - 1):
                # sum[0:i] == sum[i+1:j]
                left_sum = prefix[i]
                middle_sum = prefix[j] - prefix[i + 1]
                if left_sum == middle_sum:
                    left_sums.add(left_sum)
            
            # 右边可能的和
            for k in range(j + 2, n - 1):
                # sum[j+1:k] == sum[k+1:n]
                middle_sum = prefix[k] - prefix[j + 1]
                right_sum = prefix[n] - prefix[k + 1]
                if middle_sum == right_sum and middle_sum in left_sums:
                    return True
        
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是数组长度。需要枚举 $j$，对于每个 $j$ 枚举 $i$ 和 $k$。
- **空间复杂度**：$O(n)$，需要存储前缀和数组和哈希集合。
