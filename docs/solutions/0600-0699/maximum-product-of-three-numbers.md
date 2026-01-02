# [0628. 三个数的最大乘积](https://leetcode.cn/problems/maximum-product-of-three-numbers/)

- 标签：数组、数学、排序
- 难度：简单

## 题目链接

- [0628. 三个数的最大乘积 - 力扣](https://leetcode.cn/problems/maximum-product-of-three-numbers/)

## 题目大意

**描述**：

给定一个整型数组 $nums$。

**要求**：

在数组中找出由三个数组成的最大乘积，并输出这个乘积。

**说明**：

- $3 \le nums.length \le 10^{4}$。
- $-10^{3} \le nums[i] \le 10^{3}$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3]
输出：6
```

- 示例 2：

```python
输入：nums = [1,2,3,4]
输出：24
```

## 解题思路

### 思路 1：排序 + 数学

这道题目要求找出三个数的最大乘积。需要考虑负数的情况。

最大乘积可能有两种情况：
1. 三个最大的正数相乘。
2. 两个最小的负数（绝对值最大）与最大的正数相乘。

因此，对数组排序后，比较这两种情况的结果即可。

### 思路 1：代码

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # 情况 1：三个最大的数相乘
        product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]
        
        # 情况 2：两个最小的数（可能是负数）与最大的数相乘
        product2 = nums[0] * nums[1] * nums[n - 1]
        
        return max(product1, product2)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数组的长度。主要时间消耗在排序上。
- **空间复杂度**：$O(\log n)$，排序所需的栈空间。

### 思路 2：线性扫描

不需要完整排序，只需要找到最大的三个数和最小的两个数即可。

### 思路 2：代码

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 找到最大的三个数
        max1 = max2 = max3 = float('-inf')
        # 找到最小的两个数
        min1 = min2 = float('inf')
        
        for num in nums:
            # 更新最大的三个数
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            
            # 更新最小的两个数
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        
        return max(max1 * max2 * max3, min1 * min2 * max1)
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。只需要遍历数组一次。
- **空间复杂度**：$O(1)$，只使用了常数级别的额外空间。
