# [0630. 课程表 III](https://leetcode.cn/problems/course-schedule-iii/)

- 标签：贪心、数组、排序、堆（优先队列）
- 难度：困难

## 题目链接

- [0630. 课程表 III - 力扣](https://leetcode.cn/problems/course-schedule-iii/)

## 题目大意

**描述**：

这里有 $n$ 门不同的在线课程，按从 $1$ 到 $n$ 编号。给你一个数组 $courses$ ，其中 $courses[i] = [duration_i, lastDay_i]$ 表示第 $i$ 门课将会持续上 $durationi$ 天课，并且必须在不晚于 $lastDayi$ 的时候完成。

你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。

**要求**：

返回你最多可以修读的课程数目。

**说明**：

- $1 \le courses.length \le 10^{4}$。
- $1 \le duration_i, lastDay_i \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出：3
解释：
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
```

- 示例 2：

```python
输入：courses = [[1,2]]
输出：1
```

## 解题思路

### 思路 1：贪心 + 优先队列

#### 思路 1：算法描述

这道题目要求在不晚于截止日期的情况下，最多可以修读多少门课程。

我们可以使用贪心算法结合优先队列（最大堆）来解决这个问题。

基本思路：

1. 按照课程的截止日期从小到大排序。
2. 依次考虑每门课程，如果当前时间加上课程持续时间不超过截止日期，就选择这门课程。
3. 如果超过了截止日期，但当前课程的持续时间比已选课程中持续时间最长的课程短，就替换掉那门课程。

具体步骤如下：

1. 将课程按照截止日期从小到大排序。
2. 初始化当前时间 $time = 0$ 和最大堆 $heap$（存储已选课程的持续时间）。
3. 遍历排序后的课程：
   - 如果 $time + duration \le lastDay$，选择这门课程，将持续时间加入堆中，更新 $time$。
   - 否则，如果堆不为空且堆顶元素（最大持续时间）大于当前课程的持续时间，就替换掉堆顶课程。
4. 返回堆的大小，即最多可以修读的课程数。

#### 思路 1：代码

```python
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        import heapq
        
        # 按照截止日期从小到大排序
        courses.sort(key=lambda x: x[1])
        
        time = 0  # 当前时间
        heap = []  # 最大堆，存储已选课程的持续时间（取负数实现最大堆）
        
        for duration, lastDay in courses:
            # 如果可以在截止日期前完成这门课程
            if time + duration <= lastDay:
                time += duration
                heapq.heappush(heap, -duration)  # 加入堆中（取负数）
            # 如果不能完成，但当前课程的持续时间比已选课程中最长的短
            elif heap and -heap[0] > duration:
                # 替换掉持续时间最长的课程
                time += duration - (-heapq.heappop(heap))
                heapq.heappush(heap, -duration)
        
        return len(heap)
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是课程的数量。排序需要 $O(n \log n)$，每门课程最多进出堆一次，堆操作需要 $O(\log n)$。
- **空间复杂度**：$O(n)$。堆中最多存储 $n$ 门课程。
