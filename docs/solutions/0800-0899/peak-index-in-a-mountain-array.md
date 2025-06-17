# [0852. 山脉数组的峰顶索引](https://leetcode.cn/problems/peak-index-in-a-mountain-array/)

- 标签：数组、二分查找
- 难度：中等

## 题目链接

- [0852. 山脉数组的峰顶索引 - 力扣](https://leetcode.cn/problems/peak-index-in-a-mountain-array/)

## 题目大意

**描述**：给定由整数组成的山脉数组 $arr$。

**要求**：返回任何满足 $arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[len(arr) - 1] $ 的下标 $i$。

**说明**：

- **山脉数组**：满足以下属性的数组：
  1. $len(arr) \ge 3$；
  2. 存在 $i$（$0 < i < len(arr) - 1$），使得：
     1. $arr[0] < arr[1] < ... arr[i-1] < arr[i]$；
     2. $arr[i] > arr[i+1] > ... > arr[len(arr) - 1]$。
- $3 <= arr.length <= 105$
- $0 <= arr[i] <= 106$
- 题目数据保证 $arr$ 是一个山脉数组

**示例**：

- 示例 1：

```python
输入：arr = [0,1,0]
输出：1
```

- 示例 2：

```python
输入：arr = [0,2,1,0]
输出：1
```

## 解题思路

### 思路 1：二分查找

1. 使用两个指针 $left$、$right$ 。$left$ 指向数组第一个元素，$right$ 指向数组最后一个元素。
2. 取区间中间节点 $mid$，并比较 $nums[mid]$ 和 $nums[mid + 1]$ 的值大小。
   1. 如果 $nums[mid]< nums[mid + 1]$，则右侧存在峰值，令 `left = mid + 1`。
   2. 如果 $nums[mid] \ge nums[mid + 1]$，则左侧存在峰值，令 `right = mid`。
3. 最后，当 $left == right$ 时，跳出循环，返回 $left$。

### 思路 1：代码

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(1)$。

