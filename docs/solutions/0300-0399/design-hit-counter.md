# [0362. 敲击计数器](https://leetcode.cn/problems/design-hit-counter/)

- 标签：设计、队列、数组、二分查找、数据流
- 难度：中等

## 题目链接

- [0362. 敲击计数器 - 力扣](https://leetcode.cn/problems/design-hit-counter/)

## 题目大意

**要求**：

设计一个敲击计数器，使它可以统计在过去 $5$ 分钟内被敲击次数（即过去 $300$ 秒）。

您的系统应该接受一个时间戳参数 $timestamp$ (单位为秒)，并且您可以假定对系统的调用是按时间顺序进行的(即 $timestamp$ 是单调递增的)。几次撞击可能同时发生。

实现 `HitCounter` 类:

- `HitCounter()` 初始化命中计数器系统。
- `void hit(int timestamp)` 记录在 $timestamp$ (单位为秒)发生的一次命中。在同一个 $timestamp$ 中可能会出现几个点击。
- `int getHits(int timestamp)` 返回 $timestamp$ 在过去 $5$ 分钟内(即过去 $300$ 秒)的命中次数。

**说明**：

- $1 \le timestamp \le 2 \times 10^{9}$。
- 所有对系统的调用都是按时间顺序进行的（即 timestamp 是单调递增的）。
- `hit` 和 `getHits` 最多被调用 $300$ 次。

- 进阶: 如果每秒的敲击次数是一个很大的数字，你的计数器可以应对吗？

**示例**：

- 示例 1：

```python
输入：
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
输出：
[null, null, null, null, 3, null, 4, 3]

解释：
HitCounter counter = new HitCounter();
counter.hit(1);// 在时刻 1 敲击一次。
counter.hit(2);// 在时刻 2 敲击一次。
counter.hit(3);// 在时刻 3 敲击一次。
counter.getHits(4);// 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
counter.hit(300);// 在时刻 300 敲击一次。
counter.getHits(300); // 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
counter.getHits(301); // 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
```

## 解题思路

### 思路 1：队列

使用队列来存储所有的敲击时间戳。对于每次 `hit` 操作，我们将时间戳加入队列。对于 `getHits` 操作，我们需要移除所有超过 $300$ 秒的时间戳，然后返回队列中剩余元素的个数。

具体步骤：

1. **初始化**：创建一个空队列 $queue$ 来存储时间戳。
2. **hit 操作**：将当前时间戳 $timestamp$ 加入队列。
3. **getHits 操作**：
   - 计算时间窗口的起始时间：$start\_time = timestamp - 300$。
   - 移除队列中所有小于等于 $start\_time$ 的时间戳。
   - 返回队列中剩余元素的个数。

这种方法简单直观，但每次 `getHits` 操作都需要遍历队列来移除过期的时间戳。

### 思路 1：代码

```python
from collections import deque

class HitCounter:

    def __init__(self):
        # 使用双端队列存储时间戳
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        # 将当前时间戳加入队列
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # 计算时间窗口的起始时间（过去 300 秒）
        start_time = timestamp - 300
        
        # 移除所有过期的时间戳
        while self.queue and self.queue[0] <= start_time:
            self.queue.popleft()
        
        # 返回队列中剩余元素的个数
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `hit` 操作：$O(1)$，只需要将元素加入队列。
  - `getHits` 操作：$O(k)$，其中 $k$ 是需要移除的过期时间戳数量。
- **空间复杂度**：$O(n)$，其中 $n$ 是在过去 $300$ 秒内的敲击次数。
