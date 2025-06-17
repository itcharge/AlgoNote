# [0435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/)

- 标签：贪心、数组、动态规划、排序
- 难度：中等

## 题目链接

- [0435. 无重叠区间 - 力扣](https://leetcode.cn/problems/non-overlapping-intervals/)

## 题目大意

**描述**：给定一个区间的集合 `intervals`，其中 `intervals[i] = [starti, endi]`。从集合中移除部分区间，使得剩下的区间互不重叠。

**要求**：返回需要移除区间的最小数量。

**说明**：

- $1 \le intervals.length \le 10^5$。
- $intervals[i].length == 2$。
- $-5 * 10^4 \le starti < endi \le 5 * 10^4$。

**示例**：

- 示例 1：

```python
输入：intervals = [[1,2],[2,3],[3,4],[1,3]]
输出：1
解释：移除 [1,3] 后，剩下的区间没有重叠。
```

- 示例 2：

```python
输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
```

## 解题思路

### 思路 1：贪心算法

这道题我们可以转换一下思路。原题要求保证移除区间最少，使得剩下的区间互不重叠。换个角度就是：「如何使得剩下互不重叠区间的数目最多」。那么答案就变为了：「总区间个数 - 不重叠区间的最多个数」。我们的问题也变成了求所有区间中不重叠区间的最多个数。

从贪心算法的角度来考虑，我们应该将区间按照结束时间排序。每次选择结束时间最早的区间，然后再在剩下的时间内选出最多的区间。

我们用贪心三部曲来解决这道题。

1. **转换问题**：将原问题转变为，当选择结束时间最早的区间之后，再在剩下的时间内选出最多的区间（子问题）。
2. **贪心选择性质**：每次选择时，选择结束时间最早的区间。这样选出来的区间一定是原问题最优解的区间之一。
3. **最优子结构性质**：在上面的贪心策略下，贪心选择当前时间最早的区间 + 剩下的时间内选出最多区间的子问题最优解，就是全局最优解。也就是说在贪心选择的方案下，能够使所有区间中不重叠区间的个数最多。

使用贪心算法的代码解决步骤描述如下：

1. 将区间集合按照结束坐标升序排列，然后维护两个变量，一个是当前不重叠区间的结束时间 `end_pos`，另一个是不重叠区间的个数 `count`。初始情况下，结束坐标 `end_pos` 为第一个区间的结束坐标，`count` 为 `1`。
2. 依次遍历每段区间。对于每段区间：`intervals[i]`：
   1. 如果 `end_pos <= intervals[i][0]`，即 `end_pos` 小于等于区间起始位置，则说明出现了不重叠区间，令不重叠区间数 `count` 加 `1`，`end_pos` 更新为新区间的结束位置。
3. 最终返回「总区间个数 - 不重叠区间的最多个数」即 `len(intervals) - count` 作为答案。

### 思路 1：代码

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        end_pos = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if end_pos <= intervals[i][0]:
                count += 1
                end_pos = intervals[i][1]

        return len(intervals) - count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 是区间的数量。
- **空间复杂度**：$O(\log n)$。
