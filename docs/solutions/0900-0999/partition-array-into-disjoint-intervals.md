# [0915. 分割数组](https://leetcode.cn/problems/partition-array-into-disjoint-intervals/)

- 标签：数组
- 难度：中等

## 题目链接

- [0915. 分割数组 - 力扣](https://leetcode.cn/problems/partition-array-into-disjoint-intervals/)

## 题目大意

**描述**：

给定一个数组 $nums$，将其划分为两个连续子数组 $left$ 和 $right$，使得：

- $left$ 中的每个元素都小于或等于 $right$ 中的每个元素。
- $left$ 和 $right$ 都是非空的。
- $left$ 的长度要尽可能小。

**要求**：

在完成这样的分组后返回 $left$ 的「长度」。

用例可以保证存在这样的划分方法。

**说明**：

- $2 \le nums.length \le 10^{5}$。
- $0 \le nums[i] \le 10^{6}$。
- 可以保证至少有一种方法能够按题目所描述的那样对 $nums$ 进行划分。

**示例**：

- 示例 1：

```python
输入：nums = [5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]
```

- 示例 2：

```python
输入：nums = [1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]
```

## 解题思路

### 思路 1：前缀最大值 + 后缀最小值

要满足 $left$ 中的每个元素都小于或等于 $right$ 中的每个元素，即 $left$ 的最大值要小于或等于 $right$ 的最小值。

1. **预处理**：
   - 计算前缀最大值数组 $max\_left[i]$：表示 $[0, i]$ 范围内的最大值
   - 计算后缀最小值数组 $min\_right[i]$：表示 $[i, n-1]$ 范围内的最小值
2. **查找分割点**：从左到右遍历，找到第一个满足 $max\_left[i] \le min\_right[i+1]$ 的位置 $i$，返回 $i+1$（即 $left$ 的长度）。

### 思路 1：代码

```python
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 计算前缀最大值
        max_left = [0] * n
        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])
        
        # 计算后缀最小值
        min_right = [0] * n
        min_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])
        
        # 查找分割点
        for i in range(n - 1):
            if max_left[i] <= min_right[i + 1]:
                return i + 1
        
        return n - 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度，需要遍历三次数组。
- **空间复杂度**：$O(n)$，需要存储前缀最大值和后缀最小值数组。
