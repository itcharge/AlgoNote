# [0933. 最近的请求次数](https://leetcode.cn/problems/number-of-recent-calls/)

- 标签：设计、队列、数据流
- 难度：简单

## 题目链接

- [0933. 最近的请求次数 - 力扣](https://leetcode.cn/problems/number-of-recent-calls/)

## 题目大意

要求：实现一个用来计算特定时间范围内的最近请求的 `RecentCounter` 类：

- `RecentCounter()` 初始化计数器，请求数为 0 。
- `int ping(int t)` 在时间 `t` 时添加一个新请求，其中 `t` 表示以毫秒为单位的某个时间，并返回在 `[t-3000, t]` 内发生的请求数。

## 解题思路

使用一个队列，用于存储 `[t - 3000, t]` 范围内的请求。

获取请求数时，将队首所有小于 `t - 3000` 时间的请求将其从队列中移除，然后返回队列的长度即可。

## 代码

```python
class RecentCounter:

    def __init__(self):
        self.queue = []


    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)
```

