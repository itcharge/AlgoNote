# [1004. 最大连续1的个数 III](https://leetcode.cn/problems/max-consecutive-ones-iii/)

- 标签：数组、二分查找、前缀和、滑动窗口
- 难度：中等

## 题目链接

- [1004. 最大连续1的个数 III - 力扣](https://leetcode.cn/problems/max-consecutive-ones-iii/)

## 题目大意

**描述**：给定一个由 $0$、$1$ 组成的数组 $nums$，再给定一个整数 $k$。最多可以将 $k$ 个值从 $0$ 变到 $1$。

**要求**：返回仅包含 $1$ 的最长连续子数组的长度。

**说明**：

- $1 \le nums.length \le 10^5$。
- $nums[i]$ 不是 $0$ 就是 $1$。
- $0 \le k \le nums.length$。

**示例**：

- 示例 1：

```python
输入：nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K = 2
输出：6
解释：[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
将 nums[5]、nums[10] 从 0 翻转到 1，最长的子数组长度为 6。
```

- 示例 2：

```python
输入：nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K = 3
输出：10
解释：[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
将 nums[4]、nums[5]、nums[9] 从 0 翻转到 1，最长的子数组长度为 10。
```

## 解题思路

### 思路 1：滑动窗口（不定长度）

1. 使用两个指针 $left$、$right$ 指向数组开始位置。使用 $max\_count$ 来维护仅包含 $1$ 的最长连续子数组的长度。
2. 不断右移 $right$ 指针，扩大滑动窗口范围，并统计窗口内 $0$ 元素的个数。
3. 直到 $0$ 元素的个数超过 $k$ 时将 $left$ 右移，缩小滑动窗口范围，并减小 $0$ 元素的个数，同时维护 $max\_count$。
4. 最后输出最长连续子数组的长度 $max\_count$。

### 思路 1：代码

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        zero_count = 0
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            right += 1
            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_count = max(max_count, right - left)
        return max_count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

