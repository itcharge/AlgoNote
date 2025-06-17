# [1695. 删除子数组的最大得分](https://leetcode.cn/problems/maximum-erasure-value/)

- 标签：数组、哈希表、滑动窗口
- 难度：中等

## 题目链接

- [1695. 删除子数组的最大得分 - 力扣](https://leetcode.cn/problems/maximum-erasure-value/)

## 题目大意

**描述**：给定一个正整数数组 $nums$，从中删除一个含有若干不同元素的子数组。删除子数组的「得分」就是子数组各元素之和 。

**要求**：返回只删除一个子数组可获得的最大得分。

**说明**：

- **子数组**：如果数组 $b$ 是数组 $a$ 的一个连续子序列，即如果它等于 $a[l],a[l+1],...,a[r]$ ，那么它就是 $a$ 的一个子数组。
- $1 \le nums.length \le 10^5$。
- $1 \le nums[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
```

- 示例 2：

```python
输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
```

## 解题思路

### 思路 1：滑动窗口

题目要求的是含有不同元素的连续子数组最大和，我们可以用滑动窗口来做，维护一个不包含重复元素的滑动窗口，计算最大的窗口和。具体方法如下：

- 用滑动窗口 $window$ 来记录不重复的元素个数，$window$ 为哈希表类型。用 $window\underline{\hspace{0.5em}}sum$ 来记录窗口内子数组元素和，$ans$ 用来维护最大子数组和。设定两个指针：$left$、$right$，分别指向滑动窗口的左右边界，保证窗口中没有重复元素。

- 一开始，$left$、$right$ 都指向 $0$。
- 将最右侧数组元素 $nums[right]$ 加入当前窗口 $window$ 中，记录该元素个数。
- 如果该窗口中该元素的个数多于 $1$ 个，即 $window[s[right]] > 1$，则不断右移 $left$，缩小滑动窗口长度，并更新窗口中对应元素的个数，直到 $window[s[right]] \le 1$。
- 维护更新无重复元素的最大子数组和。然后右移 $right$，直到 $right \ge len(nums)$ 结束。
- 输出无重复元素的最大子数组和。

### 思路 1：代码

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window_sum = 0
        left, right = 0, 0
        window = dict()
        ans = 0
        while right < len(nums):
            window_sum += nums[right]
            if nums[right] not in window:
                window[nums[right]] = 1
            else:
                window[nums[right]] += 1

            while window[nums[right]] > 1:
                window[nums[left]] -= 1
                window_sum -= nums[left]
                left += 1
            ans = max(ans, window_sum)
            right += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(n)$。

