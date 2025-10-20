# [0252. 会议室](https://leetcode.cn/problems/meeting-rooms/)

- 标签：数组、排序
- 难度：简单

## 题目链接

- [0252. 会议室 - 力扣](https://leetcode.cn/problems/meeting-rooms/)

## 题目大意

**描述**：

给定一个会议时间安排的数组 $intervals$，每个会议时间都会包括开始和结束的时间 $intervals[i] = [start_i, end_i]$。

**要求**：

判断一个人是否能够参加这里面的全部会议。

**说明**：

- $0 \le intervals.length \le 10^{4}$。
- $intervals[i].length == 2$。
- $0 \le start_i \lt end_i \le 10^{6}$。

**示例**：

- 示例 1：

```python
输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
```

- 示例 2：

```python
输入：intervals = [[7,10],[2,4]]
输出：true
```

## 解题思路

### 思路 1：排序 + 遍历

这是一个经典的区间重叠检测问题。我们需要判断是否存在两个会议时间重叠，如果存在重叠，则无法参加所有会议。

核心思想是：

- 对会议区间按开始时间 $start_i$ 进行排序。
- 遍历排序后的会议，检查相邻会议是否存在时间重叠。
- 如果存在重叠（前一个会议的结束时间 $end_{i-1} >$ 后一个会议的开始时间 $start_i$），则无法参加所有会议。

具体算法步骤：

1. 对会议区间按开始时间排序：$intervals.sort(key=lambda x: x[0])$。
2. 遍历排序后的会议，检查相邻会议是否重叠：
   - 如果 $intervals[i-1][1] > intervals[i][0]$，则存在重叠，返回 $false$。
3. 如果所有会议都不重叠，返回 $true$。

### 思路 1：代码

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 处理空数组或只有一个会议的情况
        if not intervals or len(intervals) <= 1:
            return True
        
        # 按开始时间排序
        intervals.sort(key=lambda x: x[0])
        
        # 检查相邻会议是否重叠
        for i in range(1, len(intervals)):
            # 如果前一个会议的结束时间 > 当前会议的开始时间，则存在重叠
            if intervals[i-1][1] > intervals[i][0]:
                return False
        
        # 所有会议都不重叠，可以参加所有会议
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是会议数量。排序需要 $O(n \log n)$ 时间，遍历需要 $O(n)$ 时间。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
