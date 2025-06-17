# [LCR 041. 数据流中的移动平均值](https://leetcode.cn/problems/qIsx9U/)

- 标签：设计、队列、数组、数据流
- 难度：简单

## 题目链接

- [LCR 041. 数据流中的移动平均值 - 力扣](https://leetcode.cn/problems/qIsx9U/)

## 题目大意

**描述**：给定一个整数数据流和一个窗口大小 `size`。

**要求**：根据滑动窗口的大小，计算滑动窗口里所有数字的平均值。要求实现 `MovingAverage` 类：

- `MovingAverage(int size)`：用窗口大小 `size` 初始化对象。
- `double next(int val)`：成员函数 `next` 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 `size` 个值的移动平均值，即滑动窗口里所有数字的平均值。

**说明**：

- $1 \le size \le 1000$。
- $-10^5 \le val \le 10^5$。
- 最多调用 `next` 方法 $10^4$ 次。

**示例**：

- 示例 1：

```python
输入：
inputs = ["MovingAverage", "next", "next", "next", "next"]
inputs = [[3], [1], [10], [3], [5]]
输出：
[null, 1.0, 5.5, 4.66667, 6.0]

解释：
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // 返回 1.0 = 1 / 1
movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3
```

## 解题思路

### 思路 1：队列

1. 使用队列保存滑动窗口的元素，并记录对应窗口大小和元素和。
2. 当队列长度小于窗口大小的时候，直接向队列中添加元素，并记录当前窗口中的元素和。
3. 当队列长度等于窗口大小的时候，先将队列头部元素弹出，再添加元素，并记录当前窗口中的元素和。
4. 然后根据元素和和队列中元素个数计算出平均值。

### 思路 1：代码

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

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。初始化方法和每次调用 `next` 方法的时间复杂度都是 $O(1)$。
- **空间复杂度**：$O(size)$。其中 $size$ 就是给定的滑动窗口的大小。