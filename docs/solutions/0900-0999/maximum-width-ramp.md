# [0962. 最大宽度坡](https://leetcode.cn/problems/maximum-width-ramp/)

- 标签：栈、数组、双指针、单调栈
- 难度：中等

## 题目链接

- [0962. 最大宽度坡 - 力扣](https://leetcode.cn/problems/maximum-width-ramp/)

## 题目大意

**描述**：

给定一个整数数组 A，坡是元组 $(i, j)$，其中 $i < j$ 且 $A[i] \le A[j]$。这样的坡的宽度为 $j - i$。

**要求**：

找出 A 中的坡的最大宽度，如果不存在，返回 0。

**说明**：

- $2 \le A.length \le 50000$。
- $0 \le A[i] \le 50000$。

**示例**：

- 示例 1：

```python
输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
```

- 示例 2：

```python
输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
```

## 解题思路

### 思路 1：单调栈

#### 思路

这道题要求找到最大宽度的坡，即满足 $i < j$ 且 $nums[i] \le nums[j]$ 的最大 $j - i$。

我们可以使用单调栈来解决：
1. **构建单调递减栈**：从左到右遍历数组，将索引压入栈中，保持栈中索引对应的值单调递减。这样栈中存储的是可能作为坡起点的候选位置。
2. **从右向左查找最大宽度**：从右向左遍历数组，对于每个位置 $j$，尝试从栈顶弹出满足 $nums[stack[-1]] \le nums[j]$ 的索引 $i$，计算宽度 $j - i$ 并更新最大值。

为什么从右向左遍历？因为对于栈顶的索引 $i$，我们希望找到最远的 $j$ 使得 $nums[i] \le nums[j]$，从右向左可以保证找到的是最大宽度。

#### 代码

```python
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []  # 单调递减栈，存储索引
        
        # 构建单调递减栈
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        
        # 从右向左遍历，寻找最大宽度
        for j in range(n - 1, -1, -1):
            # 当栈不为空且当前值大于等于栈顶索引对应的值
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width
```

#### 复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。每个元素最多入栈和出栈各一次。
- **空间复杂度**：$O(n)$，栈的空间最多存储 $n$ 个元素。
