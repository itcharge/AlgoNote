# [0775. 全局倒置与局部倒置](https://leetcode.cn/problems/global-and-local-inversions/)

- 标签：数组、数学
- 难度：中等

## 题目链接

- [0775. 全局倒置与局部倒置 - 力扣](https://leetcode.cn/problems/global-and-local-inversions/)

## 题目大意

**描述**：

给定一个长度为 $n$ 的整数数组 $nums$ ，表示由范围 $[0, n - 1]$ 内所有整数组成的一个排列。

- 「全局倒置」的数目等于满足下述条件不同下标对 $(i, j)$ 的数目：
   - $0 \le i < j < n$
   - $nums[i] > nums[j]$

- 「局部倒置」的数目等于满足下述条件的下标 i 的数目：
   - $0 <= i < n - 1$
   - $nums[i] > nums[i + 1]$

**要求**：

当数组 $nums$ 中「全局倒置」的数量等于「局部倒置」的数量时，返回 true；否则，返回 false。

**说明**：

- $n == nums.length$。
- $1 \le n \le 10^{5}$。
- $0 \le nums[i] \lt n$。
- $nums$ 中的所有整数 互不相同。
- $nums$ 是范围 $[0, n - 1]$ 内所有数字组成的一个排列。

**示例**：

- 示例 1：

```python
输入：nums = [1,0,2]
输出：true
解释：有 1 个全局倒置，和 1 个局部倒置。
```

- 示例 2：

```python
输入：nums = [1,2,0]
输出：false
解释：有 2 个全局倒置，和 1 个局部倒置。
```

## 解题思路

### 思路 1：数学规律

这道题的关键在于观察全局倒置和局部倒置的关系。

**核心观察**：

- 局部倒置是指相邻元素的倒置：$nums[i] > nums[i+1]$。
- 全局倒置是指任意两个元素的倒置：$i < j$ 且 $nums[i] > nums[j]$。
- 显然，所有局部倒置都是全局倒置。
- 要使全局倒置数量等于局部倒置数量，就要保证不存在非局部的全局倒置。
- 即：不存在 $i < j - 1$ 且 $nums[i] > nums[j]$ 的情况。

**等价条件**：

- 对于每个位置 $i$，$nums[i]$ 与其原本应该在的位置 $i$ 的差距不能超过 $1$。
- 即：$|nums[i] - i| \leq 1$。

**解题步骤**：

1. 遍历数组，检查每个元素是否满足 $|nums[i] - i| \leq 1$。
2. 如果所有元素都满足，返回 `True`。
3. 否则返回 `False`。

### 思路 1：代码

```python
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # 检查每个元素是否与其索引的差距不超过 1
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $nums$ 的长度。需要遍历数组一次。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量。
