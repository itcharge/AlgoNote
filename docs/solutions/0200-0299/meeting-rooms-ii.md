# [0253. 会议室 II](https://leetcode.cn/problems/meeting-rooms-ii/)

- 标签：贪心、数组、双指针、前缀和、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0253. 会议室 II - 力扣](https://leetcode.cn/problems/meeting-rooms-ii/)

## 题目大意

**描述**：

给定一个会议时间安排的数组 $intervals$，每个会议时间都会包括开始和结束的时间 $intervals[i] = [start_i, end_i]$。

**要求**：

返回「所需会议室的最小数量」。

**说明**：

- $1 \le intervals.length \le 10^{4}$。
- $0 \le start_i \lt end_i \le 10^{6}$。

**示例**：

- 示例 1：

```python
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2
```

- 示例 2：

```python
输入：intervals = [[7,10],[2,4]]
输出：1
```

## 解题思路

### 思路 1：优先队列（最小堆）

这是一个经典的区间调度问题。我们需要找出同时进行的会议的最大数量，这就是所需会议室的最小数量。

核心思想是：

- 使用优先队列（最小堆）来维护当前正在进行的会议的结束时间。
- 按照会议开始时间 $start_i$ 对区间进行排序。
- 对于每个会议，检查是否有会议室可用（堆顶的结束时间 $\le$ 当前会议开始时间）。
- 如果有可用会议室，则复用；否则需要新的会议室。

具体算法步骤：

1. 对会议区间按开始时间排序：$intervals.sort(key=lambda x: x[0])$。
2. 初始化最小堆 $heap = []$ 用于存储当前会议的结束时间。
3. 遍历排序后的会议：
   - 如果堆不为空且堆顶元素（最早结束时间）$\le$ 当前会议开始时间，则弹出堆顶（复用会议室）。
   - 将当前会议的结束时间加入堆中。
4. 堆的大小就是所需会议室的最小数量。

### 思路 1：代码

```python
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 处理空数组情况
        if not intervals:
            return 0
        
        # 按开始时间排序
        intervals.sort(key=lambda x: x[0])
        
        # 使用最小堆存储当前会议的结束时间
        heap = []
        
        # 遍历每个会议
        for start, end in intervals:
            # 如果堆不为空且最早结束的会议已经结束，则复用该会议室
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # 将当前会议的结束时间加入堆中
            heapq.heappush(heap, end)
        
        # 堆的大小就是所需会议室的最小数量
        return len(heap)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是会议数量。排序需要 $O(n \log n)$ 时间，每个会议最多进行一次堆操作（插入和删除），堆操作的时间复杂度为 $O(\log n)$。
- **空间复杂度**：$O(n)$，最坏情况下所有会议都需要同时进行，堆的大小为 $n$。
