# [1229. 安排会议日程](https://leetcode.cn/problems/meeting-scheduler/)

- 标签：数组、双指针、排序
- 难度：中等

## 题目链接

- [1229. 安排会议日程 - 力扣](https://leetcode.cn/problems/meeting-scheduler/)

## 题目大意

**描述**：给定两位客户的空闲时间表：$slots1$ 和 $slots2$，再给定会议的预计持续时间 $duration$。

其中 $slots1[i] = [start_i, end_i]$ 表示空闲时间第从 $start_i$ 开始，到 $end_i$ 结束。$slots2$ 也是如此。

**要求**：为他们安排合适的会议时间，如果有合适的会议时间，则返回该时间的起止时刻。如果没有满足要求的会议时间，就请返回一个 空数组。

**说明**：

- **会议时间**：两位客户都有空参加，并且持续时间能够满足预计时间 $duration$ 的最早的时间间隔。
- 题目保证数据有效。同一个人的空闲时间不会出现交叠的情况，也就是说，对于同一个人的两个空闲时间 $[start1, end1]$ 和 $[start2, end2]$，要么 $start1 > end2$，要么 $start2 > end1$。
- $1 \le slots1.length, slots2.length \le 10^4$。
- $slots1[i].length, slots2[i].length == 2$。
- $slots1[i][0] < slots1[i][1]$。
- $slots2[i][0] < slots2[i][1]$。
- $0 \le slots1[i][j], slots2[i][j] \le 10^9$。
- $1 \le duration \le 10^6$。

**示例**：

- 示例 1：

```python
输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
输出：[60,68]
```

- 示例 2：

```python
输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
输出：[]
```

## 解题思路

### 思路 1：分离双指针

题目保证了同一个人的空闲时间不会出现交叠。那么可以先直接对两个客户的空间时间表按照开始时间从小到大排序。然后使用分离双指针来遍历两个数组，求出重合部分，并判断重合区间是否大于等于 $duration$。具体做法如下：

1. 先对两个数组排序。
2. 然后使用两个指针 $left\_1$、$left\_2$。$left\_1$ 指向第一个数组开始位置，$left\_2$ 指向第二个数组开始位置。
3. 遍历两个数组。计算当前两个空闲时间区间的重叠范围。
   1. 如果重叠范围大于等于 $duration$，直接返回当前重叠范围开始时间和会议结束时间，即 $[start, start + duration]$，$start$ 为重叠范围开始时间。
   2. 如果第一个客户的空闲结束时间小于第二个客户的空闲结束时间，则令 $left\_1$ 右移，即 `left_1 += 1`，继续比较重叠范围。
   3. 如果第一个客户的空闲结束时间大于等于第二个客户的空闲结束时间，则令 $left\_2$ 右移，即 `left_2 += 1`，继续比较重叠范围。
4. 直到 $left\_1 == len(slots1)$ 或者 $left\_2 == len(slots2)$ 时跳出循环，返回空数组 $[]$。

### 思路 1：代码

```python
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        size1 = len(slots1)
        size2 = len(slots2)
        left_1, left_2 = 0, 0
        while left_1 < size1 and left_2 < size2:
            start_1, end_1 = slots1[left_1]
            start_2, end_2 = slots2[left_2]
            start = max(start_1, start_2)
            end = min(end_1, end_2)
            if end - start >= duration:
                return [start, start + duration]
            if end_1 < end_2:
                left_1 += 1
            else:
                left_2 += 1
        return []
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n + m \times \log m)$，其中 $n$、$m$ 分别为数组 $slots1$、$slots2$  中的元素个数。
- **空间复杂度**：$O(\log n + \log m)$。

