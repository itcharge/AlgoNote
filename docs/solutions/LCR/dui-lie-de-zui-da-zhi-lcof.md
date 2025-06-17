# [LCR 184. 设计自助结算系统](https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/)

- 标签：设计、队列、单调队列
- 难度：中等

## 题目链接

- [LCR 184. 设计自助结算系统 - 力扣](https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/)

## 题目大意

要求：设计一个「队列」，实现 `max_value` 函数，可通过 `max_value` 得到大年队列的最大值。并且要求 `max_value`、`push_back`、`pop_front` 的均摊时间复杂度都是 `O(1)`。

## 解题思路

利用空间换时间，使用两个队列。其中一个为原始队列 `queue`，另一个为递减队列 `deque`，`deque` 用来保存队列的最大值，具体做法如下：

- `push_back` 操作：如果 `deque` 队尾元素小于即将入队的元素 `value`，则将小于 `value` 的元素全部出队，再将 `valuew` 入队。否则直接将 `value` 直接入队，这样 `deque` 队首元素保存的就是队列的最大值。
- `pop_front` 操作：先判断 `deque`、`queue` 是否为空，如果 `deque` 或者 `queue` 为空，则说明队列为空，直接返回 `-1`。如果都不为空，从 `queue` 中取出一个元素，并跟 `deque` 队首元素进行比较，如果两者相等则需要将 `deque` 队首元素弹出。
- `max_value` 操作：如果 `deque` 不为空，则返回 `deque` 队首元素。否则返回 `-1`。

## 代码

```python
import collections
import queue


class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = collections.deque()


    def max_value(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1


    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)


    def pop_front(self) -> int:
        if not self.deque or not self.queue:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans
```

