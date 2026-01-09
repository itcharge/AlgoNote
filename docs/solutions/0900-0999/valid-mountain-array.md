# [0941. 有效的山脉数组](https://leetcode.cn/problems/valid-mountain-array/)

- 标签：数组
- 难度：简单

## 题目链接

- [0941. 有效的山脉数组 - 力扣](https://leetcode.cn/problems/valid-mountain-array/)

## 题目大意

**描述**：

如果 $arr$ 满足下述条件，那么它是一个山脉数组：

- $arr.length \ge 3$
- 在 0 < i < arr.length - 1$ 条件下，存在 $i$ 使得：
- $arr[0] < arr[1] < ... arr[i-1] < arr[i]$
- $arr[i] > arr[i+1] > ... > arr[arr.length - 1]$

![](https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png)

给定一个整数数组 $arr$。

**要求**：

如果 $arr$ 是有效的山脉数组就返回 true，否则返回 false。

**说明**：

- $1 \le arr.length \le 10^{4}$。
- $0 \le arr[i] \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：arr = [2,1]
输出：false
```

- 示例 2：

```python
输入：arr = [3,5,5]
输出：false
```

## 解题思路

### 思路 1：双指针

使用双指针分别从左右两端向中间移动，找到山峰位置。

1. 如果数组长度小于 $3$，直接返回 $False$。
2. 使用指针 $left$ 从左向右移动，找到第一个不再递增的位置。
3. 使用指针 $right$ 从右向左移动，找到第一个不再递减的位置。
4. 检查 $left$ 和 $right$ 是否相等，且不在数组的两端（必须有上升和下降部分）。

### 思路 1：代码

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        # 长度小于 3，不可能是山脉数组
        if n < 3:
            return False
        
        left = 0
        # 从左向右找到山峰
        while left < n - 1 and arr[left] < arr[left + 1]:
            left += 1
        
        # 山峰不能在两端
        if left == 0 or left == n - 1:
            return False
        
        # 从山峰向右检查是否递减
        while left < n - 1 and arr[left] > arr[left + 1]:
            left += 1
        
        # 如果到达数组末尾，说明是有效的山脉数组
        return left == n - 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $arr$ 的长度。
- **空间复杂度**：$O(1)$，只使用了常数级别的额外空间。
