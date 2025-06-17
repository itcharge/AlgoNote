# [1099. 小于 K 的两数之和](https://leetcode.cn/problems/two-sum-less-than-k/)

- 标签：数组、双指针、二分查找、排序
- 难度：简单

## 题目链接

- [1099. 小于 K 的两数之和 - 力扣](https://leetcode.cn/problems/two-sum-less-than-k/)

## 题目大意

**描述**：给定一个整数数组 $nums$ 和整数 $k$。 

**要求**：返回最大和 $sum$，满足存在 $i < j$ 使得 $nums[i] + nums[j] = sum$ 且 $sum < k$。如果没有满足此等式的 $i$, $j$ 存在，则返回 $-1$。

**说明**：

- $1 \le nums.length \le 100$。
- $1 \le nums[i] \le 1000$。
- $1 \le k \le 2000$。

**示例**：

- 示例 1：

```python
输入：nums = [34,23,1,24,75,33,54,8], k = 60
输出：58
解释：34 和 24 相加得到 58，58 小于 60，满足题意。
```

- 示例 2：

```python
输入：nums = [10,20,30], k = 15
输出：-1
解释：我们无法找到和小于 15 的两个元素。
```

## 解题思路

### 思路 1：对撞指针

常规暴力枚举时间复杂度为 $O(n^2)$。可以通过双指针降低时间复杂度。具体做法如下：

- 先对数组进行排序（时间复杂度为 $O(n \log n$），使用 $res$ 记录答案，初始赋值为最小值 `float('-inf')`。
- 使用两个指针 $left$、$right$。$left$ 指向第 $0$ 个元素位置，$right$ 指向数组的最后一个元素位置。 
- 计算 $nums[left] + nums[right]$，与 $k$ 进行比较。
  - 如果 $nums[left] + nums[right] \ge k$，则将 $right$ 左移，继续查找。
  - 如果 $nums[left] + nums[rigth] < k$，则将 $left$ 右移，并更新答案值。
- 当 $left == right$ 时，区间搜索完毕，判断 $res$ 是否等于 `float('-inf')`，如果等于，则返回 $-1$，否则返回 $res$。

### 思路 1：代码

```python
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()
        res = float('-inf')
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total >= k:
                right -= 1
            else:
                res = max(res, total)
                left += 1

        return res if res != float('-inf') else -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为数组中元素的个数。
- **空间复杂度**：$O(\log n)$，排序需要 $\log n$ 的栈空间。

