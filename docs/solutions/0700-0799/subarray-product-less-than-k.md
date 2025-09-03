# [0713. 乘积小于 K 的子数组](https://leetcode.cn/problems/subarray-product-less-than-k/)

- 标签：数组、滑动窗口
- 难度：中等

## 题目链接

- [0713. 乘积小于 K 的子数组 - 力扣](https://leetcode.cn/problems/subarray-product-less-than-k/)

## 题目大意

**描述**：给定一个正整数数组 $nums$ 和整数 $k$。

**要求**：找出该数组内乘积小于 $k$ 的连续的子数组的个数。

**说明**：

- $1 \le nums.length \le 3 * 10^4$。
- $1 \le nums[i] \le 1000$。
- $0 \le k \le 10^6$。

**示例**：

- 示例 1：

```python
输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
```

- 示例 2：

```python
输入：nums = [1,2,3], k = 0
输出：0
```

## 解题思路

### 思路 1：滑动窗口（不定长度）

1. 设定两个指针：$left$、$right$，分别指向滑动窗口的左右边界，保证窗口内所有数的乘积 $window\_product$ 都小于 $k$。使用 $window\_product$ 记录窗口中的乘积值，使用 $count$ 记录符合要求的子数组个数。
2. 一开始，$left$、$right$ 都指向 $0$。
3. 向右移动 $right$，将最右侧元素加入当前子数组乘积 $window\_product$ 中。
4. 如果 $window\_product \ge k$，则不断右移 $left$，缩小滑动窗口长度，并更新当前乘积值 $window\_product$  直到 $window\_product < k$。
5. 记录累积答案个数加 $1$，继续右移 $right$，直到 $right \ge len(nums)$ 结束。
6. 输出累积答案个数。

### 思路 1：代码

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        size = len(nums)
        left = 0
        right = 0
        window_product = 1
        
        count = 0
        
        while right < size:
            window_product *= nums[right]

            while window_product >= k:
                window_product /= nums[left]
                left += 1

            count += (right - left + 1)
            right += 1
            
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

