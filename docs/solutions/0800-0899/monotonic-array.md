# [0896. 单调数列](https://leetcode.cn/problems/monotonic-array/)

- 标签：数组
- 难度：简单

## 题目链接

- [0896. 单调数列 - 力扣](https://leetcode.cn/problems/monotonic-array/)

## 题目大意

**描述**：

如果数组是单调递增或单调递减的，那么它是「单调」的。

如果对于所有 $i \le j$，$nums[i] \le nums[j]$，那么数组 $nums$ 是单调递增的。如果对于所有 $i \le j$，$nums[i] \ge nums[j]$，那么数组 $nums$ 是单调递减的。

**要求**：

当给定的数组 $nums$ 是单调数组时返回 true，否则返回 false。

**说明**：

- $1 \le nums.length \le 10^{5}$。
- $-10^{5} \le nums[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,2,3]
输出：true
```

- 示例 2：

```python
输入：nums = [6,5,4,4]
输出：true
```

## 解题思路

### 思路 1：一次遍历

这道题要求判断数组是否单调（单调递增或单调递减）。

算法步骤：

1. 使用两个布尔变量 $increasing$ 和 $decreasing$ 分别表示数组是否单调递增和单调递减，初始值都为 $True$。
2. 遍历数组，比较相邻元素：
   - 如果 $nums[i] > nums[i-1]$，说明不是单调递减，设置 $decreasing = False$。
   - 如果 $nums[i] < nums[i-1]$，说明不是单调递增，设置 $increasing = False$。
3. 最后返回 $increasing$ 或 $decreasing$ 是否为 $True$。

### 思路 1：代码

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        
        # 标记是否单调递增和单调递减
        increasing = True
        decreasing = True
        
        # 遍历数组，比较相邻元素
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                decreasing = False  # 不是单调递减
            if nums[i] < nums[i - 1]:
                increasing = False  # 不是单调递增
        
        # 只要满足其中一个条件即可
        return increasing or decreasing
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。只需遍历一次数组。
- **空间复杂度**：$O(1)$，只使用常数额外空间。
