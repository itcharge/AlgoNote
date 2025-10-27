# [0453. 最小操作次数使数组元素相等](https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/)

- 标签：数组、数学
- 难度：中等

## 题目链接

- [0453. 最小操作次数使数组元素相等 - 力扣](https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/)

## 题目大意

**描述**：

给定一个长度为 $n$ 的整数数组，每次操作将会使 $n - 1$ 个元素增加 $1$。

**要求**：

返回让数组所有元素相等的最小操作次数。

**说明**：

- $n == nums.length$。
- $1 \le nums.length \le 10^{5}$。
- $-10^{9} \le nums[i] \le 10^{9}$。
- 答案保证符合 32-bit 整数。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3]
输出：3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
```

- 示例 2：

```python
输入：nums = [1,1,1]
输出：0
```

## 解题思路

### 思路 1：数学转化

这道题要求每次操作使 $n - 1$ 个元素增加 $1$，最终使所有元素相等。

我们可以从另一个角度思考：每次操作使 $n - 1$ 个元素增加 $1$，等价于每次操作使 $1$ 个元素减少 $1$。

假设最终所有元素都变成 $x$，且最小值为 $\min(nums)$，那么操作次数为：$\sum_{i=0}^{n-1} (nums[i] - x)$。

为了使操作次数最小，我们应该让所有元素都变成数组的最小值 $\min(nums)$，这样操作次数为：

$$moves = \sum_{i=0}^{n-1} (nums[i] - \min(nums)) = \sum_{i=0}^{n-1} nums[i] - n \times \min(nums)$$

**算法思路**：

1. 找到数组的最小值 $min\_val$。
2. 遍历数组，计算所有元素与最小值的差值之和，即为最小操作次数。

### 思路 1：代码

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 找到数组中的最小值
        min_val = min(nums)
        
        # 计算所有元素与最小值的差值之和
        moves = 0
        for num in nums:
            moves += num - min_val
        
        return moves
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组长度。需要遍历两次数组，一次找最小值，一次计算差值之和。
- **空间复杂度**：$O(1)$。只使用了常数额外空间。
