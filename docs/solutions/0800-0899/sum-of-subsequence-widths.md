# [0891. 子序列宽度之和](https://leetcode.cn/problems/sum-of-subsequence-widths/)

- 标签：数组、数学、排序
- 难度：困难

## 题目链接

- [0891. 子序列宽度之和 - 力扣](https://leetcode.cn/problems/sum-of-subsequence-widths/)

## 题目大意

**描述**：

一个序列的「宽度」定义为该序列中最大元素和最小元素的差值。

给定一个整数数组 $nums$。

**要求**：

返回 $nums$ 的所有非空「子序列」的「宽度之和」。由于答案可能非常大，请返回对 $10^9 + 7$ 取余后的结果。

**说明**：

- 「子序列」定义为从一个数组里删除一些（或者不删除）元素，但不改变剩下元素的顺序得到的数组。例如，$[3,6,2,7]$ 就是数组 $[0,3,1,6,2,2,7]$ 的一个子序列。
- $1 \le nums.length \le 10^{5}$。
- $1 \le nums[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：nums = [2,1,3]
输出：6
解释：子序列为 [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3] 。
相应的宽度是 0, 0, 0, 1, 1, 2, 2 。
宽度之和是 6 。
```

- 示例 2：

```python
输入：nums = [2]
输出：0
```

## 解题思路

### 思路 1:排序 + 数学

关键观察：子序列的宽度只与最大值和最小值有关,与中间元素无关。

对数组排序后，对于元素 $nums[i]$:

- 作为最大值时，有 $2^i$ 个子序列(从前 $i$ 个元素中任选)
- 作为最小值时，有 $2^{n-1-i}$ 个子序列(从后 $n-1-i$ 个元素中任选)

因此,元素 $nums[i]$ 对答案的贡献为:

$$nums[i] \times (2^i - 2^{n-1-i})$$

总答案为:

$$\sum_{i=0}^{n-1} nums[i] \times (2^i - 2^{n-1-i})$$

### 思路 1:代码

```python
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # 排序
        nums.sort()
        
        # 预计算 2 的幂次
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        
        result = 0
        
        # 计算每个元素的贡献
        for i in range(n):
            # 作为最大值的贡献 - 作为最小值的贡献
            contribution = (nums[i] * pow2[i] - nums[i] * pow2[n - 1 - i]) % MOD
            result = (result + contribution) % MOD
        
        return result
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n \log n)$,其中 $n$ 是数组长度。排序需要 $O(n \log n)$,计算贡献需要 $O(n)$。
- **空间复杂度**:$O(n)$,需要存储 2 的幂次数组。
