# [1827. 最少操作使数组递增](https://leetcode.cn/problems/minimum-operations-to-make-the-array-increasing/)

- 标签：贪心、数组
- 难度：简单

## 题目链接

- [1827. 最少操作使数组递增 - 力扣](https://leetcode.cn/problems/minimum-operations-to-make-the-array-increasing/)

## 题目大意

**描述**：给定一个整数数组 $nums$（下标从 $0$ 开始）。每一次操作中，你可以选择数组中的一个元素，并将它增加 $1$。

- 比方说，如果 $nums = [1,2,3]$，你可以选择增加 $nums[1]$ 得到 $nums = [1,3,3]$。

**要求**：请你返回使 $nums$ 严格递增的最少操作次数。

**说明**：

- 我们称数组 $nums$ 是严格递增的，当它满足对于所有的 $0 \le i < nums.length - 1$ 都有 $nums[i] < nums[i + 1]$。一个长度为 $1$ 的数组是严格递增的一种特殊情况。
- $1 \le nums.length \le 5000$。
- $1 \le nums[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [1,1,1]
输出：3
解释：你可以进行如下操作：
1) 增加 nums[2] ，数组变为 [1,1,2]。
2) 增加 nums[1] ，数组变为 [1,2,2]。
3) 增加 nums[2] ，数组变为 [1,2,3]。
```

- 示例 2：

```python
输入：nums = [1,5,2,4,1]
输出：14
```

## 解题思路

### 思路 1：贪心算法

题目要求使 $nums$ 严格递增的最少操作次数。当遇到 $nums[i - 1] \ge nums[i]$ 时，我们应该在满足要求的同时，尽可能使得操作次数最少，则 $nums[i]$ 应增加到 $nums[i - 1] + 1$ 时，此时操作次数最少，并且满足 $nums[i - 1] < nums[i]$。

具体操作步骤如下：

1. 从左到右依次遍历数组元素。
2. 如果遇到 $nums[i - 1] \ge nums[i]$ 时：
   1. 本次增加的最少操作次数为 $nums[i - 1] + 1 - nums[i]$，将其计入答案中。
   2. 将 $nums[i]$ 变为 $nums[i - 1] + 1$。
3. 遍历完返回答案 $ans$。

### 思路 1：代码

```Python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                ans += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(1)$。
