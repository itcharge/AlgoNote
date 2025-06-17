# [0719. 找出第 K 小的距离对](https://leetcode.cn/problems/find-k-th-smallest-pair-distance/)

- 标签：数组、双指针、二分查找、排序
- 难度：困难

## 题目链接

- [0719. 找出第 K 小的距离对 - 力扣](https://leetcode.cn/problems/find-k-th-smallest-pair-distance/)

## 题目大意

**描述**：给定一个整数数组 $nums$，对于数组中不同的数 $nums[i]$、$nums[j]$ 之间的距离定义为 $nums[i]$ 和 $nums[j]$ 的绝对差值，即 $dist(nums[i], nums[j]) = abs(nums[i] - nums[j])$。

**要求**：求所有数对之间第 $k$ 个最小距离。

**说明**：

- $n == nums.length$
- $2 \le n \le 10^4$。
- $0 \le nums[i] \le 10^6$。
- $1 \le k \le n \times (n - 1) / 2$。

**示例**：

- 示例 1：

```python
输入：nums = [1,3,1], k = 1
输出：0
解释：数对和对应的距离如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
距离第 1 小的数对是 (1,1) ，距离为 0。
```

- 示例 2：

```python
输入：nums = [1,1,1], k = 2
输出：0
```

## 解题思路

### 思路 1：二分查找算法

一般来说 topK 问题都可以用堆排序来解决。但是这道题使用堆排序超时了。所以需要换其他方法。

先来考虑第 $k$ 个最小距离的范围。这个范围一定在 $[0, max(nums) - min(nums)]$ 之间。

我们可以对 $nums$ 先进行排序，然后得到最小距离为 $0$，最大距离为 $nums[-1] - nums[0]$。我们可以在这个区间上进行二分，对于二分的位置 $mid$，统计距离小于等于 $mid$ 的距离对数，并根据它和 $k$ 的关系调整区间上下界。

统计对数可以使用双指针来计算出所有小于等于 $mid$ 的距离对数目。

1. 维护两个指针 $left$、$right$。$left$、$right$ 都指向数组开头位置。
2. 然后不断移动 $right$，计算 $nums[right]$ 和 $nums[left]$ 之间的距离。
3. 如果大于 $mid$，则 $left$ 向右移动，直到距离小于等于 $mid$ 时，统计当前距离对数为 $right - left$。
4. 最终将这些符合要求的距离对数累加，就得到了所有小于等于 $mid$ 的距离对数目。

### 思路 1：代码

```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def get_count(dist):
            left, count = 0, 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > dist:
                    left += 1
                count += (right - left)
            return count

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if get_count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 为数组 $nums$ 中的元素个数。
- **空间复杂度**：$O(\log n)$，排序算法所用到的空间复杂度为 $O(\log n)$。
