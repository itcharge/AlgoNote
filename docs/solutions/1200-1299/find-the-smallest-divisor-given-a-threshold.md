# [1283. 使结果不超过阈值的最小除数](https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/)

- 标签：数组、二分查找
- 难度：中等

## 题目链接

- [1283. 使结果不超过阈值的最小除数 - 力扣](https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/)

## 题目大意

**描述**：给你一个整数数组 $nums$ 和一个正整数 $threshold$，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和（向上取整）。例如 $7/3 = 3$，$10/2 = 5$。

**要求**：找出能够使上述结果小于等于阈值 $threshold$ 的除数中最小的那个。题目保证一定有解。

**说明**：

- $1 \le nums.length \le 5 \times 10^4$。
- $1 \le nums[i] \le 10^6$。
- $nums.length \le threshold \le 10^6$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,5,9], threshold = 6
输出：5
解释：如果除数为 1，我们可以得到和为 17（1+2+5+9）。
如果除数为 4，我们可以得到和为 7（1+1+2+3）。如果除数为 5，和为 5（1+1+1+2）。
```

- 示例 2：

```python
输入：nums = [2,3,5,7,11], threshold = 11
输出：3
```

## 解题思路

### 思路 1：二分查找

###### 1. 核心思想

这道题的关键是观察到**单调性**：除数越大，每个数除完向上取整后的和就越小。反之亦然。

利用这个单调性，我们可以用二分查找来找到临界点——最小的那个满足「和 $\le threshold$」的除数。

为什么用二分而不是从 $1$ 开始逐步增大？因为 $nums[i] \le 10^6$，如果线性扫描最坏可能需要尝试 $10^6$ 次，而二分只需要 $\log_2(10^6) \approx 20$ 次。

###### 2. 具体步骤

**第 1 步：确定二分范围**

- 下界 $left = 1$：除数的可能最小值。
- 上界 $right = max(nums)$：因为当除数 $\ge$ 最大值时，每个数除完向上取整的结果都是 $1$，总和 $= len(nums)$。题目保证 $len(nums) \le threshold$，所以这个除数一定满足条件。更小的除数可能也满足，所以这是搜索边界。

**第 2 步：二分查找**

使用「找最小值」模板：
- 当 $left < right$ 时循环：
  - 取 $mid = (left + right) // 2$。
  - 计算以 $mid$ 为除数的结果和 $total = \sum \lceil \frac{num}{mid} \rceil$。
  - 如果 $total \le threshold$，说明 $mid$ 可行，尝试更小的除数：$right = mid$。
  - 否则 $total > threshold$，需要增大除数：$left = mid + 1$。

**第 3 步：返回结果**

$left$ 就是最小的满足条件的除数。

**结合示例 1 走一遍：**

$nums = [1,2,5,9], threshold = 6$

$left = 1, right = 9$

- $mid = (1+9)//2 = 5$：$\lceil 1/5 \rceil + \lceil 2/5 \rceil + \lceil 5/5 \rceil + \lceil 9/5 \rceil = 1+1+1+2 = 5 \le 6$ → $right = 5$
- $mid = (1+5)//2 = 3$：$\lceil 1/3 \rceil + \lceil 2/3 \rceil + \lceil 5/3 \rceil + \lceil 9/3 \rceil = 1+1+2+3 = 7 > 6$ → $left = 4$
- $mid = (4+5)//2 = 4$：$\lceil 1/4 \rceil + \lceil 2/4 \rceil + \lceil 5/4 \rceil + \lceil 9/4 \rceil = 1+1+2+3 = 7 > 6$ → $left = 5$
- $left = right = 5$，返回 $5$。

### 思路 1：代码

```python
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 二分查找范围
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            # 计算以 mid 为除数时每个数除完向上取整的和
            # (num + mid - 1) // mid 是向上取整的常用技巧
            total = sum((num + mid - 1) // mid for num in nums)
            if total <= threshold:
                right = mid   # mid 可行，但也许可以更小，向左收缩
            else:
                left = mid + 1  # 和太大了，需要更大的除数

        return left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log M)$，其中 $n$ 是数组 $nums$ 的长度，$M = \max(nums)$。二分查找进行 $O(\log M)$ 轮，每轮需要 $O(n)$ 时间求和。
- **空间复杂度**：$O(1)$，只使用了常数个变量。
