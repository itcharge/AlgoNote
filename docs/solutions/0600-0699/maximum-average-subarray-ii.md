# [0644. 子数组最大平均数 II](https://leetcode.cn/problems/maximum-average-subarray-ii/)

- 标签：数组、二分查找、前缀和
- 难度：困难

## 题目链接

- [0644. 子数组最大平均数 II - 力扣](https://leetcode.cn/problems/maximum-average-subarray-ii/)

## 题目大意

**描述**：

给你一个包含 $n$ 个整数的数组 $nums$，和一个整数 $k$。

**要求**：

找出 **长度大于等于** $k$ 且含最大平均值的连续子数组。并输出这个最大平均值。任何计算误差小于 $10^{-5}$ 的结果都将被视为正确答案。

**说明**：

- $n == nums.length$。
- $1 \le k \le n \le 10^4$。
- $-10^4 \le nums[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75000
解释：
- 当长度为 4 的时候，连续子数组平均值分别为 [0.5, 12.75, 10.5]，其中最大平均值是 12.75。
- 当长度为 5 的时候，连续子数组平均值分别为 [10.4, 10.8]，其中最大平均值是 10.8。
- 当长度为 6 的时候，连续子数组平均值分别为 [9.16667]，其中最大平均值是 9.16667。
当取长度为 4 的子数组（即，子数组 [12, -5, -6, 50]）的时候，可以得到最大的连续子数组平均值 12.75，所以返回 12.75。
根据题目要求，无需考虑长度小于 4 的子数组。
```

- 示例 2：

```python
输入：nums = [5], k = 1
输出：5.00000
```

## 解题思路

### 思路 1：二分查找 + 前缀和

这道题目要求找到长度大于等于 $k$ 的子数组的最大平均值。

**核心思路**：

- 使用二分查找来确定最大平均值。
- 对于一个给定的平均值 $mid$，判断是否存在长度大于等于 $k$ 的子数组，其平均值大于等于 $mid$。
- 判断方法：将数组中每个元素减去 $mid$，如果存在长度大于等于 $k$ 的子数组和大于等于 $0$，则说明存在平均值大于等于 $mid$ 的子数组。

**算法步骤**：

1. 二分查找的范围是 $[min(nums), max(nums)]$。
2. 对于每个 $mid$，将数组中每个元素减去 $mid$，得到新数组 $arr$。
3. 使用前缀和 + 滑动窗口，判断是否存在长度大于等于 $k$ 的子数组和大于等于 $0$。
4. 如果存在，说明最大平均值在 $[mid, right]$ 范围内；否则在 $[left, mid]$ 范围内。
5. 重复步骤 2-4，直到 $left$ 和 $right$ 的差值小于 $10^{-5}$。

### 思路 1：代码

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check(mid):
            """判断是否存在长度 >= k 的子数组，平均值 >= mid"""
            # 将数组中每个元素减去 mid，计算前缀和
            n = len(nums)
            prefix_sum = 0
            prev_sum = 0  # 前 i-k 个元素的前缀和
            min_prev_sum = 0  # 前 i-k 个元素中的最小前缀和
            
            for i in range(n):
                prefix_sum += nums[i] - mid
                
                # 长度至少为 k
                if i >= k - 1:
                    # prefix_sum - min_prev_sum 表示某个长度 >= k 的子数组和
                    if prefix_sum - min_prev_sum >= 0:
                        return True
                    
                    # 更新 prev_sum 和 min_prev_sum
                    # prev_sum 是前 i-k+1 个元素的前缀和
                    prev_sum += nums[i - k + 1] - mid
                    min_prev_sum = min(min_prev_sum, prev_sum)
            
            return False
        
        # 二分查找
        left, right = min(nums), max(nums)
        
        while right - left > 1e-5:
            mid = (left + right) / 2
            if check(mid):
                left = mid
            else:
                right = mid
        
        return left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log(max - min))$，其中 $n$ 是数组长度，$max$ 和 $min$ 分别是数组的最大值和最小值。二分查找的次数为 $O(\log(max - min))$，每次检查需要 $O(n)$ 时间。
- **空间复杂度**：$O(1)$。只使用了常数额外空间。
