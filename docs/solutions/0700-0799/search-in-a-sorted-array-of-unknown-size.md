# [0702. 搜索长度未知的有序数组](https://leetcode.cn/problems/search-in-a-sorted-array-of-unknown-size/)

- 标签：数组、二分查找、交互
- 难度：中等

## 题目链接

- [0702. 搜索长度未知的有序数组 - 力扣](https://leetcode.cn/problems/search-in-a-sorted-array-of-unknown-size/)

## 题目大意

**描述**：给定一个升序数组 $secret$，但是数组的大小是未知的。我们无法直接访问数组，智能通过 `ArrayReader` 接口去访问他。我们可以通过接口 `reader.get(k)`：

1. 如果数组访问未越界，则返回数组 $secret$ 中第 $k$ 个下标位置的元素值。
2. 如果数组访问越界，则接口返回 $2^{31} - 1$。

现在再给定一个数字 $target$。

**要求**：从 $secret$ 中找出 $secret[k] == target$ 的下标位置 $k$，如果 $secret$ 中不存在 $target$，则返回 $-1$。

**说明**：

- $1 \le secret.length \le 10^4$。
- $-10^4 \le secret[i], target \le 10^4$。
- $secret$ 严格递增。

**示例**：

- 示例 1：

```python
输入: secret = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 存在在 nums 中，下标为 4
```

- 示例 2：

```python
输入: secret = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不在数组中所以返回 -1
```

## 解题思路

### 思路 1：二分查找算法

这道题的关键点在于找到数组的大小，以便确定查找的右边界位置。右边界可以通过倍增的方式快速查找。在查找右边界的同时，也能将左边界的范围进一步缩小。等确定了左右边界，就可以使用二分查找算法快速查找 $target$。

### 思路 1：代码

```python
class Solution:
    def binarySearch(self, reader, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if target > reader.get(mid):
                left = mid + 1
            else:
                right = mid
        if reader.get(left) == target:
            return left
        else:
            return -1

    def search(self, reader, target):
        left = 0
        right = 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        return self.binarySearch(reader, left, right, target)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$，其中 $n$ 为数组长度。
- **空间复杂度**：$O(1)$。

