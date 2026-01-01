# [0556. 下一个更大元素 III](https://leetcode.cn/problems/next-greater-element-iii/)

- 标签：数学、双指针、字符串
- 难度：中等

## 题目链接

- [0556. 下一个更大元素 III - 力扣](https://leetcode.cn/problems/next-greater-element-iii/)

## 题目大意

**描述**：

给定一个正整数 $n$。

**要求**：

找出符合条件的最小整数，其由重新排列 $n$ 中存在的每位数字组成，并且其值大于 $n$。如果不存在这样的正整数，则返回 $-1$。

**说明**：

- 注意：返回的整数应当是一个 32 位整数，如果存在满足题意的答案，但不是 32 位整数，同样返回 $-1$。
- $1 \le n \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：n = 12
输出：21
```

- 示例 2：

```python
输入：n = 21
输出：-1
```

## 解题思路

### 思路 1：下一个排列

这个问题本质上是求数字的下一个排列。算法步骤：

1. 将数字转换为字符数组
2. 从右往左找到第一个满足 $nums[i] < nums[i+1]$ 的位置 $i$
3. 如果找不到，说明已经是最大排列，返回 $-1$
4. 从右往左找到第一个大于 $nums[i]$ 的位置 $j$
5. 交换 $nums[i]$ 和 $nums[j]$
6. 反转 $nums[i+1:]$ 使其升序
7. 将结果转换回整数，检查是否在 32 位整数范围内

### 思路 1：代码

```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        n_len = len(nums)
        
        # 从右往左找第一个 nums[i] < nums[i+1] 的位置
        i = n_len - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 如果找不到，说明已经是最大排列
        if i < 0:
            return -1
        
        # 从右往左找第一个大于 nums[i] 的位置
        j = n_len - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # 交换 nums[i] 和 nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # 反转 nums[i+1:] 使其升序
        nums[i + 1:] = reversed(nums[i + 1:])
        
        # 转换回整数
        result = int(''.join(nums))
        
        # 检查是否在 32 位整数范围内
        if result > 2**31 - 1:
            return -1
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(d)$，其中 $d$ 是数字的位数，需要遍历数字的每一位。
- **空间复杂度**：$O(d)$，需要存储字符数组。
