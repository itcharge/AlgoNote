# [0658. 找到 K 个最接近的元素](https://leetcode.cn/problems/find-k-closest-elements/)

- 标签：数组、双指针、二分查找、排序、滑动窗口、堆（优先队列）
- 难度：中等

## 题目链接

- [0658. 找到 K 个最接近的元素 - 力扣](https://leetcode.cn/problems/find-k-closest-elements/)

## 题目大意

**描述**：给定一个有序数组 $arr$，以及两个整数 $k$、$x$。

**要求**：从数组中找到最靠近 $x$（两数之差最小）的 $k$ 个数。返回包含这 $k$ 个数的有序数组。

**说明**：

- 整数 $a$ 比整数 $b$ 更接近 $x$ 需要满足：
  - $|a - x| < |b - x|$ 或者
  - $|a - x| == |b - x|$ 且 $a < b$。

- $1 \le k \le arr.length$。
- $1 \le arr.length \le 10^4$。
- $arr$ 按升序排列。
- $-10^4 \le arr[i], x \le 10^4$。

**示例**：

- 示例 1：

```python
输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
```

- 示例 2：

```python
输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]
```

## 解题思路

### 思路 1：二分查找算法

数组的区间为 $[0, n-1]$，查找的子区间长度为 $k$。我们可以通过查找子区间左端点位置，从而确定子区间。

查找子区间左端点可以通过二分查找来降低复杂度。

因为子区间为 $k$，所以左端点最多取到 $n - k$ 的位置。

设定两个指针 $left$，$right$。$left$ 指向 $0$，$right$ 指向 $n - k$。

每次取 $left$ 和 $right$ 中间位置，判断 $x$ 与左右边界的差值。$x$ 与左边的差值为 $x - arr[mid]$，$x$ 与右边界的差值为 $arr[mid + k] - x$。

- 如果 $x$ 与左边界的差值大于 $x$ 与右边界的差值，即 $x - arr[mid] > arr[mid + k] - x$，将 $left$ 右移，$left = mid + 1$，从右侧继续查找。
- 如果 $x$ 与左边界的差值小于等于 $x$ 与右边界的差值， 即 $x - arr[mid] \le arr[mid + k] - x$，则将 $right$ 向左侧靠拢，$right = mid$，从左侧继续查找。

最后返回 $arr[left, left + k]$ 即可。

### 思路 1：代码

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log (n - k) + k)$，其中 $n$ 为数组中的元素个数。
- **空间复杂度**：$O(1)$。

