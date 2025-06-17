# [0643. 子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/)

- 标签：数组、滑动窗口
- 难度：简单

## 题目链接

- [0643. 子数组最大平均数 I - 力扣](https://leetcode.cn/problems/maximum-average-subarray-i/)

## 题目大意

**描述**：给定一个由 $n$ 个元素组成的整数数组 $nums$ 和一个整数 $k$。

**要求**：找出平均数最大且长度为 $k$ 的连续子数组，并输出该最大平均数。

**说明**：

- 任何误差小于 $10^{-5}$ 的答案都将被视为正确答案。
- $n == nums.length$。
- $1 \le k \le n \le 10^5$。
- $-10^4 \le nums[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
```

- 示例 2：

```python
输入：nums = [5], k = 1
输出：5.00000
```

## 解题思路

### 思路 1：滑动窗口（固定长度）

这道题目是典型的固定窗口大小的滑动窗口题目。窗口大小为 $k$。具体做法如下：

1. $ans$ 用来维护子数组最大平均数，初始值为负无穷，即 `float('-inf')`。$window\underline{\hspace{0.5em}}total$ 用来维护窗口中元素的和。
2. $left$ 、$right$ 都指向序列的第一个元素，即：`left = 0`，`right = 0`。
3. 向右移动 $right$，先将 $k$ 个元素填入窗口中。
4. 当窗口元素个数为 $k$ 时，即：$right - left + 1 >= k$ 时，计算窗口内的元素和平均值，并维护子数组最大平均数。
5. 然后向右移动 $left$，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为 $k$。
6. 重复 $4 \sim 5$ 步，直到 $right$ 到达数组末尾。
7. 最后输出答案 $ans$。

### 思路 1：代码

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        window_total = 0
        ans = float('-inf')
        while right < len(nums):
            window_total += nums[right]

            if right - left + 1 >= k:
                ans = max(window_total / k, ans)
                window_total -= nums[left]
                left += 1

            # 向右侧增大窗口
            right += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 为数组 $nums$ 的元素个数。
- **空间复杂度**：$O(1)$。