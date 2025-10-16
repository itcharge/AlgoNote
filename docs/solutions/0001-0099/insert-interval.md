# [0057. 插入区间](https://leetcode.cn/problems/insert-interval/)

- 标签：数组
- 难度：中等

## 题目链接

- [0057. 插入区间 - 力扣](https://leetcode.cn/problems/insert-interval/)

## 题目大意

**描述**：

给定一个无重叠的、按照区间起始端点排序的区间列表 $intervals$，其中 $intervals[i] = [start_i, end_i]$ 表示第 $i$ 个区间的开始和结束，并且 $intervals$ 按照 $start_i$ 升序排列。同样给定一个区间 $newInterval = [start, end]$ 表示另一个区间的开始和结束。

**要求**：

在 $intervals$ 中插入区间 $newInterval$，使得 $intervals$ 依然按照 $start_i$ 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 $intervals$。

**说明**：

- $0 \le intervals.length \le 10^4$。
- $intervals[i].$length == 2$。
- $0 \le starti \le endi \le 10^5$。
- $intervals 根据 starti 按升序排列。
- $newInterval.length == 2$。
- $0 \le start \le end \le 10^5$。

**示例**：

- 示例 1：

```python
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
```

- 示例 2：

```python
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
```

## 解题思路

### 思路 1：模拟插入 + 区间合并

由于原区间列表已经按照起始端点排序，我们可以采用以下策略：

1. **遍历原区间列表**：从左到右遍历所有区间
2. **分类处理**：
   - 如果当前区间完全在新区间之前（当前区间的结束 < 新区间的开始），直接加入结果
   - 如果当前区间与新区间有重叠，则合并区间
   - 如果当前区间完全在新区间之后（当前区间的开始 > 新区间的结束），直接加入结果
3. **区间合并**：当发现重叠时，将新区间扩展为 `[min(新区间开始, 当前区间开始), max(新区间结束, 当前区间结束)]`
4. **处理剩余区间**：合并完成后，将剩余的所有区间加入结果

**关键点**：
- 利用已排序的性质，只需要一次遍历
- 合并区间时需要考虑新区间可能跨越多个原区间的情况
- 使用标志位来跟踪是否已经开始合并过程

### 思路 1：代码

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # 1. 添加所有在新区间之前的区间
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # 2. 合并与新区间重叠的区间
        while i < n and intervals[i][0] \le newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # 3. 添加合并后的新区间
        result.append(newInterval)
        
        # 4. 添加剩余的区间
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是原区间列表的长度。我们只需要遍历一次原区间列表。
- **空间复杂度**：$O(1)$，除了返回结果外，只使用了常数额外空间。
