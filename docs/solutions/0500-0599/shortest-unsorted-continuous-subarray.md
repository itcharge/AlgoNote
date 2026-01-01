# [0581. 最短无序连续子数组](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/)

- 标签：栈、贪心、数组、双指针、排序、单调栈
- 难度：中等

## 题目链接

- [0581. 最短无序连续子数组 - 力扣](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/)

## 题目大意

**描述**：

给定一个整数数组 $nums$。

**要求**：

找出一个「连续子数组」，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请找出符合题意的「最短」子数组，并输出它的长度。

**说明**：

- $1 \le nums.length \le 10^{4}$。
- $-10^{5} \le nums[i] \le 10^{5}$。
- 进阶：你可以设计一个时间复杂度为 $O(n)$ 的解决方案吗？

**示例**：

- 示例 1：

```python
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
```

- 示例 2：

```python
输入：nums = [1,2,3,4]
输出：0
```

## 解题思路

### 思路 1：双指针找边界

要找到最短的未排序连续子数组，我们需要找到：

1. 左边界：从右往左遍历，找到第一个不满足"右边所有元素都大于等于它"的位置。
2. 右边界：从左往右遍历，找到第一个不满足"左边所有元素都小于等于它"的位置。

具体算法：

- 从右往左遍历，维护右边的最小值 $min\_right$。如果 $nums[i] > min\_right$，说明 $i$ 位置需要排序，更新左边界 $left = i$。
- 从左往右遍历，维护左边的最大值 $max\_left$。如果 $nums[i] < max\_left$，说明 $i$ 位置需要排序，更新右边界 $right = i$。
- 返回 $right - left + 1$（如果 $left < right$），否则返回 0。

### 思路 1：代码

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 从右往左找左边界
        min_right = float('inf')
        left = -1
        for i in range(n - 1, -1, -1):
            if nums[i] > min_right:
                left = i
            min_right = min(min_right, nums[i])
        
        # 从左往右找右边界
        max_left = float('-inf')
        right = -1
        for i in range(n):
            if nums[i] < max_left:
                right = i
            max_left = max(max_left, nums[i])
        
        # 如果找到了需要排序的子数组
        if left != -1 and right != -1:
            return right - left + 1
        return 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，需要遍历数组两次。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
