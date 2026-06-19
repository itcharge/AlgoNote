# [1353. 最多可以参加的会议数目](https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/)

- 标签：贪心、数组、堆（优先队列）
- 难度：中等

## 题目链接

- [1353. 最多可以参加的会议数目 - 力扣](https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/)

## 题目大意

**描述**：给定 $n$ 个会议，每个会议 $i$ 的开始时间为 $startDay_i$，结束时间为 $endDay_i$。你每天最多参加一个会议。

**要求**：返回最多能参加的会议数。

**说明**：
- $1 \le n \le 10^5$。
- $1 \le startDay_i \le endDay_i \le 10^5$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/16/e1.png)

```python
输入：events = [[1,2],[2,3],[3,4]]
输出：3
解释：你可以参加所有的三个会议。
安排会议的一种方案如上图。
第 1 天参加第一个会议。
第 2 天参加第二个会议。
第 3 天参加第三个会议。
```

- 示例 2：

```python
输入：events= [[1,2],[2,3],[3,4],[1,2]]
输出：4
```


## 解题思路

### 思路 1：贪心 + 最小堆

#### 1. 核心思想

按开始时间升序处理，将当前天可以参加的会议（已经开始且未结束）入堆，堆按结束时间排序。每天选取结束时间最早的会议参加。

#### 2. 具体步骤

**第 1 步**：按开始时间排序会议。

**第 2 步**：遍历每一天，将所有在今天开始的会议入堆（结束时间），弹出并参加结束时间最早的会议。

### 思路 1：代码

```python
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        i, n = 0, len(events)
        day = 1
        ans = 0
        while i < n or heap:
            # 将今天开始的会议入堆
            while i < n and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1
            # 移除已经结束的会议
            while heap and heap[0] < day:
                heapq.heappop(heap)
            # 参加结束时间最早的会议
            if heap:
                heapq.heappop(heap)
                ans += 1
            day += 1
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \log n)$。
- **空间复杂度**：$O(n)$。
