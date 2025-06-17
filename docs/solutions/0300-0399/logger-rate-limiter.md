# [0359. 日志速率限制器](https://leetcode.cn/problems/logger-rate-limiter/)

- 标签：设计、哈希表
- 难度：简单

## 题目链接

- [0359. 日志速率限制器 - 力扣](https://leetcode.cn/problems/logger-rate-limiter/)

## 题目大意

设计一个日志系统，可以流式接受消息和消息的时间戳。每条不重复的信息最多每 10 秒打印一次。即如果在时间 t 打印了 A 信息，则直到 t+10 的时间，才能再次打印这条信息。

要求实现 Logger 类：

- `def __init__(self):` 初始化 logger 对象
- `def shouldPrintMessage(self, timestamp: int, message: str) -> bool:`
  - 如果该条消息 message 在给定时间戳 timestamp 能够打印出来，则返回 True，否则返回 False。

## 解题思路

初始化一个哈希表，用来存储消息 message 最后一次打印的时间戳。

当新的消息到达是，先判断之前是否出现过相同的消息，如果未出现则可打印，存储时间戳，并返回 True。

如果出现过，且上一次相同的消息在 10 秒之前打印的，则该消息也可打印，更新时间戳，并返回 True。

如果上一次相同的消息是在 10 秒内打印的，则该信息不可打印，直接返回 False。

## 代码

```python
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_dict = dict()


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.msg_dict:
            self.msg_dict[message] = timestamp
            return True
        if timestamp - self.msg_dict[message] >= 10:
            self.msg_dict[message] = timestamp
            return True
        else:
            return False
```

