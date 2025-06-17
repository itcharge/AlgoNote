# [0908. 最小差值 I](https://leetcode.cn/problems/smallest-range-i/)

- 标签：数组、数学
- 难度：简单

## 题目链接

- [0908. 最小差值 I - 力扣](https://leetcode.cn/problems/smallest-range-i/)

## 题目大意

**描述**：给定一个整数数组 `nums`，和一个整数 `k`。给数组中的每个元素 `nums[i]` 都加上一个任意数字 `x` （`-k <= x <= k`），从而得到一个新数组 `result`。

**要求**：返回数组 `result` 的最大值和最小值之间可能存在的最小差值。

**说明**：

- $1 \le nums.length \le 10^4$。
- $0 \le nums[i] \le 10^4$。
- $0 \le k \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [1], k = 0
输出：0
解释：分数是 max(nums) - min(nums) = 1 - 1 = 0。
```

- 示例 2：

```python
输入：nums = [0,10], k = 2
输出：6
解释：将 nums 改为 [2,8]。分数是 max(nums) - min(nums) = 8 - 2 = 6。
```

## 解题思路

### 思路 1：数学

`nums` 中的每个元素可以波动 `[-k, k]`。最小的差值就是「最大值减去 `k`」和「最小值加上 `k`」之间的差值。而如果差值小于 `0`，则说明每个数字都可以波动成相等的数字，此时直接返回 `0` 即可。

### 思路 1：代码

```python
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2*k)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

