# [0456. 132 模式](https://leetcode.cn/problems/132-pattern/)

- 标签：栈、数组、二分查找、有序集合、单调栈
- 难度：中等

## 题目链接

- [0456. 132 模式 - 力扣](https://leetcode.cn/problems/132-pattern/)

## 题目大意

**描述**：

给定一个整数数组 $nums$ ，数组中共有 $n$ 个整数。「132 模式的子序列」由三个整数 $nums[i]$、$nums[j]$ 和 $nums[k]$ 组成，并同时满足：$i < j < k$ 和 $nums[i] < nums[k] < nums[j]$。

**要求**：

如果 $nums$ 中存在「132 模式的子序列」，返回 $true$；否则，返回 $false$。

**说明**：

- $n == nums.length$。
- $1 \le n \le 2 \times 10^{5}$。
- $-10^{9} \le nums[i] \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。
```

- 示例 2：

```python
输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2]。
```

## 解题思路

### 思路 1：单调栈

1. 我们需要找到三个位置 $i < j < k$，使得 $nums[i] < nums[k] < nums[j]$。
2. 从右往左遍历数组，维护一个单调递减的栈 $stack$，栈中存储的是可能的 $nums[j]$ 值。
3. 同时维护一个变量 $max\_k$，表示当前找到的最大的 $nums[k]$ 值。
4. 对于当前位置 $i$：
   - 如果 $nums[i] < max\_k$，说明找到了 132 模式，返回 $true$。
   - 否则，将栈中所有小于 $nums[i]$ 的元素弹出，更新 $max\_k$ 为这些弹出元素的最大值。
   - 将 $nums[i]$ 压入栈中。
5. 遍历结束后，如果没有找到 132 模式，返回 $false$。

### 思路 1：代码

```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # 单调栈，存储可能的 nums[j] 值
        stack = []
        # max_k 表示当前找到的最大的 nums[k] 值
        max_k = float('-inf')
        
        # 从右往左遍历
        for i in range(n - 1, -1, -1):
            # 如果当前元素小于 max_k，说明找到了 132 模式
            if nums[i] < max_k:
                return True
            
            # 维护单调递减栈
            # 弹出所有小于当前元素的栈顶元素
            while stack and stack[-1] < nums[i]:
                # 更新 max_k 为弹出元素的最大值
                max_k = max(max_k, stack.pop())
            
            # 将当前元素压入栈中
            stack.append(nums[i])
        
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。每个元素最多入栈和出栈一次。
- **空间复杂度**：$O(n)$，其中 $n$ 是数组的长度。最坏情况下栈的大小为 $n$。
