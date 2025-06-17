# [0539. 最小时间差](https://leetcode.cn/problems/minimum-time-difference/)

- 标签：数组、数学、字符串、排序
- 难度：中等

## 题目链接

- [0539. 最小时间差 - 力扣](https://leetcode.cn/problems/minimum-time-difference/)

## 题目大意

给定一个 24 小时制形式（小时:分钟 "HH:MM"）的时间列表 `timePoints`。

要求：找出列表中任意两个时间的最小时间差并以分钟数表示。

## 解题思路

- 遍历时间列表 `timePoints`，将每个时间转换为以分钟计算的整数形式，比如时间 `14:20`，将其转换为 `14 * 60 + 20 = 860`，存放到新的时间列表 `times` 中。
- 为了处理最早时间、最晚时间之间的时间间隔，我们将 `times` 中最小时间添加到列表末尾一起进行排序。
- 然后将新的时间列表 `times` 按照升序排列。
- 遍历排好序的事件列表 `times` ，找出相邻两个时间的最小间隔值即可。

## 代码

```python
class Solution:
    def changeTime(self, timePoint: str):
        hours, minutes = timePoint.split(':')
        return int(hours) * 60 + int(minutes)

    def findMinDifference(self, timePoints: List[str]) -> int:
        if not timePoints or len(timePoints) > 24 * 60:
            return 0

        times = sorted(self.changeTime(time) for time in timePoints)
        times.append(times[0] + 24 * 60)
        res = times[-1]
        for i in range(1, len(times)):
            res = min(res, times[i] - times[i - 1])
        return res
```

