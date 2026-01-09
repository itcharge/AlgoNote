# [0910. 最小差值 II](https://leetcode.cn/problems/smallest-range-ii/)

- 标签：贪心、数组、数学、排序
- 难度：中等

## 题目链接

- [0910. 最小差值 II - 力扣](https://leetcode.cn/problems/smallest-range-ii/)

## 题目大意

**描述**：

给定一个整数数组 $nums$，和一个整数 $k$。

对于每个下标 $i$（$0 \le i < nums.length$），将 $nums[i]$ 变成 $nums[i] + k$ 或 $nums[i] - k$。

$nums$ 的「分数」是 $nums$ 中最大元素和最小元素的差值。

**要求**：

在更改每个下标对应的值之后，返回 $nums$ 的最小「分数」。

**说明**：

- $1 \le nums.length \le 10^{4}$。
- $0 \le nums[i] \le 10^{4}$。
- $0 \le k \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：nums = [1], k = 0
输出：0
解释：分数 = max(nums) - min(nums) = 1 - 1 = 0 。
```

- 示例 2：

```python
输入：nums = [0,10], k = 2
输出：6
解释：将数组变为 [2, 8] 。分数 = max(nums) - min(nums) = 8 - 2 = 6 。
```

## 解题思路

### 思路 1：贪心 + 排序

这道题的关键是理解：对于排序后的数组，最优策略是将数组分为两部分，前一部分都加 $k$，后一部分都减 $k$。

1. **排序**：首先对数组进行排序。
2. **贪心策略**：排序后，我们尝试在每个位置 $i$ 进行分割，使得 $[0, i]$ 的元素都加 $k$，$[i+1, n-1]$ 的元素都减 $k$。
3. **计算分数**：对于每个分割点，计算可能的最大值和最小值：
   - 最大值可能是 $\text{nums}[i] + k$ 或 $\text{nums}[n-1] - k$
   - 最小值可能是 $\text{nums}[0] + k$ 或 $\text{nums}[i+1] - k$
4. **更新答案**：取所有分割点中的最小分数。

**特殊情况**：如果所有元素都加 $k$ 或都减 $k$，分数为 $\text{nums}[n-1] - \text{nums}[0]$。

### 思路 1：代码

```python
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        # 初始答案：所有元素都加 k 或都减 k
        ans = nums[n - 1] - nums[0]
        
        # 尝试在每个位置分割
        for i in range(n - 1):
            # [0, i] 加 k，[i+1, n-1] 减 k
            max_val = max(nums[i] + k, nums[n - 1] - k)
            min_val = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, max_val - min_val)
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数组长度，主要是排序的时间复杂度。
- **空间复杂度**：$O(\log n)$，排序所需的栈空间。
