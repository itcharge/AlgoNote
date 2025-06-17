# [0406. 根据身高重建队列](https://leetcode.cn/problems/queue-reconstruction-by-height/)

- 标签：贪心、树状数组、线段树、数组、排序
- 难度：中等

## 题目链接

- [0406. 根据身高重建队列 - 力扣](https://leetcode.cn/problems/queue-reconstruction-by-height/)

## 题目大意

n 个人打乱顺序排成一排，给定一个数组 people 表示队列中人的属性（顺序是打乱的）。其中 $people[i] = [h_i, k_i]$ 表示第 i 个人的身高为 $h_i$，前面正好有 $k_i$ 个身高大于或等于 $h_i$ 的人。

现在重新构造并返回输入数组 people 所表示的队列 queue。其中 $queue[j] = [h_j, k_j]$ 是队列中第 j 个人的信息，表示为身高为 $h_j$，前面正好有 $k_j$ 个身高大于或等于 $h_j$​ 的人。

## 解题思路

这道题目有两个维度，身高 $h_j$ 和满足条件的数量 $k_j$。进行排序的时候如果同时考虑两个维度条件，就有点复杂了。我们可以考虑固定一个维度，先排好序，再考虑另一个维度的要求。

我们可以先确定身高维度。将数组按身高从高到低进行排序，身高相同的则按照 k 值升序排列。这样排序之后可以确定目前对于第 j 个人来说，前面的 j - 1 个人肯定比他都高。

然后建立一个包含 n 个位置的空队列 queue，按照上边排好的顺序遍历，依次将其插入到第 $k_j$​ 位置上。最后返回新的队列。

## 代码

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        people.sort(key = lambda x: (-x[0], x[1]))
        for p in people:
            queue.insert(p[1], p)
        return queue
```

