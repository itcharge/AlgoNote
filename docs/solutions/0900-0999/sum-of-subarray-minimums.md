# [0907. 子数组的最小值之和](https://leetcode.cn/problems/sum-of-subarray-minimums/)

- 标签：栈、数组、动态规划、单调栈
- 难度：中等

## 题目链接

- [0907. 子数组的最小值之和 - 力扣](https://leetcode.cn/problems/sum-of-subarray-minimums/)

## 题目大意

**描述**：

给定一个整数数组 $arr$。

**要求**：

找到 `min(b)` 的总和，其中 $b$ 的范围为 $arr$ 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 $10^9 + 7$。

**说明**：

- $1 \le arr.length \le 3 \times 10^{4}$。
- $1 \le arr[i] \le 3 \times 10^{4}$。

**示例**：

- 示例 1：

```python
输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
```

- 示例 2：

```python
输入：arr = [11,81,94,43,3]
输出：444
```

## 解题思路

### 思路 1：单调栈

对于每个元素 $arr[i]$，我们需要找到它作为最小值的所有子数组。使用单调栈可以高效地找到每个元素左边和右边第一个比它小的元素。

1. 使用单调栈找到每个元素 $arr[i]$ 左边第一个比它小的元素位置 $left[i]$。
2. 使用单调栈找到每个元素 $arr[i]$ 右边第一个比它小的元素位置 $right[i]$。
3. 对于元素 $arr[i]$，它作为最小值的子数组个数为 $(i - left[i]) \times (right[i] - i)$。
4. 累加所有元素的贡献：$arr[i] \times (i - left[i]) \times (right[i] - i)$。

### 思路 1：代码

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # left[i] 表示左边第一个小于 arr[i] 的位置
        left = [-1] * n
        # right[i] 表示右边第一个小于 arr[i] 的位置
        right = [n] * n
        
        # 单调递增栈，找左边第一个更小的元素
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        # 单调递增栈，找右边第一个更小的元素
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:  # 注意这里用 >= 避免重复计算
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        # 计算每个元素的贡献
        result = 0
        for i in range(n):
            # arr[i] 作为最小值的子数组个数
            count = (i - left[i]) * (right[i] - i)
            result = (result + arr[i] * count) % MOD
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $arr$ 的长度。每个元素最多入栈和出栈各一次。
- **空间复杂度**：$O(n)$，需要使用栈和辅助数组。
