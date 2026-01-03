# [0747. 至少是其他数字两倍的最大数](https://leetcode.cn/problems/largest-number-at-least-twice-of-others/)

- 标签：数组、排序
- 难度：简单

## 题目链接

- [0747. 至少是其他数字两倍的最大数 - 力扣](https://leetcode.cn/problems/largest-number-at-least-twice-of-others/)

## 题目大意

**描述**：

给定一个整数数组 $nums$，其中总是存在「唯一的」一个最大整数。

**要求**：

找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍。如果是，则返回「最大元素的下标」，否则返回 $-1$。

**说明**：

- $2 \le nums.length \le 50$。
- $0 \le nums[i] \le 10^{3}$。
- $nums$ 中的最大元素是唯一的。

**示例**：

- 示例 1：

```python
输入：nums = [3,6,1,0]
输出：1
解释：6 是最大的整数，对于数组中的其他整数，6 至少是数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。
```

- 示例 2：

```python
输入：nums = [1,2,3,4]
输出：-1
解释：4 没有超过 3 的两倍大，所以返回 -1 。
```

## 解题思路

### 思路 1：一次遍历

这道题要求找到数组中的最大元素，并检查它是否至少是其他所有元素的两倍。

**解题步骤**：

1. 遍历数组，找到最大元素及其索引，同时记录第二大元素。
2. 检查最大元素是否至少是第二大元素的两倍。
3. 如果是，返回最大元素的索引；否则返回 $-1$。

**优化**：只需要一次遍历即可完成。

### 思路 1：代码

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        max_val = -1
        max_idx = -1
        second_max = -1
        
        # 找到最大值和第二大值
        for i, num in enumerate(nums):
            if num > max_val:
                second_max = max_val
                max_val = num
                max_idx = i
            elif num > second_max:
                second_max = num
        
        # 检查最大值是否至少是第二大值的两倍
        if max_val >= second_max * 2:
            return max_idx
        else:
            return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $nums$ 的长度。需要遍历数组一次。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量。
