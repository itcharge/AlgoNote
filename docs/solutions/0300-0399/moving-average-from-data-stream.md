# [0346. 数据流中的移动平均值](https://leetcode.cn/problems/moving-average-from-data-stream/)

- 标签：设计、队列、数组、数据流
- 难度：简单

## 题目链接

- [0346. 数据流中的移动平均值 - 力扣](https://leetcode.cn/problems/moving-average-from-data-stream/)

## 题目大意

给定一个整数 `val` 和一个窗口大小 `size`。

要求：根据滑动窗口的大小，计算滑动窗口里所有数字的平均值。要实现 `MovingAverage` 类：

- `MovingAverage(int size)` 用窗口大小 `size` 初始化对象。
- `double next(int val)` 成员函数 `next` 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 `size` 个值的移动平均值，即滑动窗口里所有数字的平均值。

## 解题思路

使用队列保存滑动窗口的元素，并记录对应窗口大小和元素和。

在小于窗口大小的时候，直接向队列中添加元素，并记录元素和。

在等于窗口大小的时候，先将队列头部元素弹出，再添加元素，并记录元素和。

然后根据元素和和队列中元素个数计算出平均值。

## 代码

```python
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size
        self.sum = 0


    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.queue.append(val)
        else:
            if self.queue:
                self.sum -= self.queue[0]
                self.queue.pop(0)
            self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)
```

