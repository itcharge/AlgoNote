# [0462. 最小操作次数使数组元素相等 II](https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/)

- 标签：数组、数学、排序
- 难度：中等

## 题目链接

- [0462. 最小操作次数使数组元素相等 II - 力扣](https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/)

## 题目大意

**描述**：

给定一个长度为 $n$ 的整数数组 $nums$。

**要求**：

返回使所有数组元素相等需要的最小操作数。

在一次操作中，你可以使数组中的一个元素加 $1$ 或者减 $1$。

**说明**：

- 测试用例经过设计以使答案在 32 位整数范围内。
- $n == nums.length$。
- $1 \le nums.length \le 10^{5}$。
- $-10^{9} \le nums[i] \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3]
输出：2
解释：
只需要两次操作（每次操作指南使一个元素加 1 或减 1）：
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
```

- 示例 2：

```python
输入：nums = [1,10,2,9]
输出：16
```

## 解题思路

### 思路 1：排序 + 中位数

这道题要求使所有数组元素相等的最少操作数，每次操作可以将一个元素加 $1$ 或减 $1$。

假设最终所有元素都变成 $x$，那么操作次数为：$\sum_{i=0}^{n-1} |nums[i] - x|$。

根据数学性质，使 $\sum_{i=0}^{n-1} |nums[i] - x|$ 最小的 $x$ 值就是数组的中位数。

**算法思路**：

1. 对数组进行排序。
2. 找到数组的中位数 $median$。如果数组长度为奇数，中位数为中间元素；如果数组长度为偶数，中位数为中间两个元素中的任意一个。
3. 遍历数组，计算所有元素到中位数的绝对距离之和。

### 思路 1：代码

```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 对数组进行排序
        nums.sort()
        
        # 计算中位数
        n = len(nums)
        median = nums[n // 2]
        
        # 计算所有元素到中位数的绝对距离之和
        moves = 0
        for num in nums:
            moves += abs(num - median)
        
        return moves
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$。排序的时间复杂度为 $O(n \log n)$，遍历数组的时间复杂度为 $O(n)$。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量。
