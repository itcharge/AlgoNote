# [0414. 第三大的数](https://leetcode.cn/problems/third-maximum-number/)

- 标签：数组、排序
- 难度：简单

## 题目链接

- [0414. 第三大的数 - 力扣](https://leetcode.cn/problems/third-maximum-number/)

## 题目大意

**描述**：

给定一个非空数组，返回此数组中「第三大的数」。

**要求**：

如果不存在，则返回数组中最大的数。

**说明**：

- $1 \le nums.length \le 10^{4}$。
- $-2^{31} \le nums[i] \le 2^{31} - 1$。

- 进阶：你能设计一个时间复杂度 $O(n)$ 的解决方案吗？

**示例**：

- 示例 1：

```python
输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
```

- 示例 2：

```python
输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。
```

## 解题思路

### 思路 1：一次遍历维护前三大的数

**核心思想**：遍历一次数组，使用三个变量 $first$、$second$、$third$ 分别维护第一大、第二大和第三大的数。

**算法步骤**：

1. 初始化 $first = second = third = -\infty$（表示三个变量都未设置）。
2. 遍历数组中的每个数 $num$：
   - 如果 $num > first$：更新 $third = second$、$second = first$、$first = num$。
   - 如果 $num < first$ 且 $num > second$：更新 $third = second$、$second = num$。
   - 如果 $num < second$ 且 $num > third$：更新 $third = num$。
   - 其他情况忽略（重复数字）。
3. 遍历结束后，如果 $third$ 仍然为 $-\infty$，说明不存在第三大的数，返回 $first$；否则返回 $third$。

**关键点**：通过一次遍历实时维护前三大元素，避免排序带来的 $O(n \log n)$ 时间复杂度。

### 思路 1：代码

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 初始化三个变量，使用 None 表示未设置
        first = second = third = None
        
        # 遍历数组
        for num in nums:
            # 更新 first
            if first is None or num > first:
                third = second
                second = first
                first = num
            # 更新 second（避免重复）
            elif num != first and (second is None or num > second):
                third = second
                second = num
            # 更新 third（避免重复）
            elif num != first and num != second and (third is None or num > third):
                third = num
        
        # 如果第三大的数不存在，返回最大的数
        if third is None:
            return first
        else:
            return third
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是数组 $nums$ 的长度。只需要遍历一次数组。
- **空间复杂度**：$O(1)$。只使用了三个变量存储状态。
