# [0621. 任务调度器](https://leetcode.cn/problems/task-scheduler/)

- 标签：贪心、数组、哈希表、计数、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0621. 任务调度器 - 力扣](https://leetcode.cn/problems/task-scheduler/)

## 题目大意

给定一个字符数组 tasks 表示 CPU 需要执行的任务列表。tasks 中每个字母表示一种不同种类的任务。任务可以按任意顺序执行，并且每个任务执行时间为 1 个单位时间。在任何一个单位时间，CPU 可以完成一个任务，或者也可以处于待命状态。

但是两个相同种类的任务之间需要 n 个单位时间的冷却时间，所以不能在连续的 n 个单位时间内执行相同的任务。

要求计算出完成 tasks 中所有任务所需要的「最短时间」。

## 解题思路

因为相同种类的任务之间最少需要 n 个单位时间间隔，所以为了最短时间，应该优先考虑任务出现此次最多的任务。

先找出出现次数最多的任务，然后中间间隔的单位来安排别的任务，或者处于待命状态。

然后将第二出现次数最多的任务，按照 n 个时间间隔安排起来。如果第二出现次数最多的任务跟第一出现次数最多的任务出现次数相同，则最短时间就会加一。

最后我们会发现：最短时间跟出现次数最多的任务正相关。

假设出现次数最多的任务为 "A"。与 "A" 出现次数相同的任务数为 count。则：

- `最短时间 = （A 出现次数 - 1）* （n + 1）+ count`。

最后还应该比较一下总的任务个数跟计算出的最短时间答案。如果最短时间比总的任务个数还少，说明间隔中放不下所有的任务，会有任务「溢出」。则应该将多余任务插入间隔中，则答案应为总的任务个数。

## 代码

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 记录每个任务出现的次数
        tasks_counts = [0 for _ in range(26)]
        for i in range(len(tasks)):
            num = ord(tasks[i]) - ord('A')
            tasks_counts[num] += 1
        max_task_count = max(tasks_counts)
        # 统计多少个出现最多次的任务
        count = 0
        for task_count in tasks_counts:
            if task_count == max_task_count:
               count += 1

        # 如果结果比任务数量少，则返回总任务数
        return max((max_task_count - 1) * (n + 1) + count, len(tasks))
```

