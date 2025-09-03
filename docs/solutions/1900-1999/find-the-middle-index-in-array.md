# [1991. 找到数组的中间位置](https://leetcode.cn/problems/find-the-middle-index-in-array/)

- 标签：数组、前缀和
- 难度：简单

## 题目链接

- [1991. 找到数组的中间位置 - 力扣](https://leetcode.cn/problems/find-the-middle-index-in-array/)

## 题目大意

**描述**：给定一个下标从 $0$ 开始的整数数组 $nums$。

**要求**：返回最左边的中间位置 $middleIndex$（也就是所有可能中间位置下标做小的一个）。如果找不到这样的中间位置，则返回 $-1$。

**说明**：

- **中间位置 $middleIndex$**：满足 $nums[0] + nums[1] + … + nums[middleIndex - 1] == nums[middleIndex + 1] + nums[middleIndex + 2] + … + nums[nums.length - 1]$ 的数组下标。
- 如果 $middleIndex == 0$，左边部分的和定义为 $0$。类似的，如果 $middleIndex == nums.length - 1$，右边部分的和定义为 $0$。

**示例**：

- 示例 1：

```python
输入：nums = [2,3,-1,8,4]
输出：3
解释：
下标 3 之前的数字和为：2 + 3 + -1 = 4
下标 3 之后的数字和为：4 = 4
```

- 示例 2：

```python
输入：nums = [1,-1,4]
输出：2
解释：
下标 2 之前的数字和为：1 + -1 = 0
下标 2 之后的数字和为：0
```

## 解题思路

### 思路 1：前缀和

1. 先遍历一遍数组，求出数组中全部元素和为 $total$。
2. 再遍历一遍数组，使用变量 $prefix\_sum$ 为前 $i$ 个元素和。
3. 当遍历到第 $i$ 个元素时，其数组左侧元素之和为 $prefix\_sum$，右侧元素和为 $total - prefix\_sum - nums[i]$。
   1. 如果左右元素之和相等，即 $prefix\_sum == total - prefix\_sum - nums[i]$（$2 \times prefix\_sum + nums[i] == total$） 时，$i$ 为中间位置。此时返回 $i$。
   2. 如果不满足，则继续累加当前元素到 $prefix\_sum$ 中，继续向后遍历。
4. 如果找不到符合要求的中间位置，则返回 $-1$。

### 思路 1：代码

```python
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        prefix_sum = 0
        for i in range(len(nums)):
            if 2 * prefix_sum + nums[i] == total:
                return i
            prefix_sum += nums[i]
        
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

