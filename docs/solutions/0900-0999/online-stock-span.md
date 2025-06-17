# [0901. 股票价格跨度](https://leetcode.cn/problems/online-stock-span/)

- 标签：栈、设计、数据流、单调栈
- 难度：中等

## 题目链接

- [0901. 股票价格跨度 - 力扣](https://leetcode.cn/problems/online-stock-span/)

## 题目大意

要求：编写一个 `StockSpanner` 类，用于收集某些股票的每日报价，并返回该股票当日价格的跨度。

- 今天股票价格的跨度：股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如：如果未来 7 天股票的价格是 `[100, 80, 60, 70, 60, 75, 85]`，那么股票跨度将是 `[1, 1, 1, 2, 1, 4, 6]`。

## 解题思路

「求解小于或等于今天价格的最大连续日」等价于「求出左侧第一个比当前股票价格大的股票，并计算距离」。求出左侧第一个比当前股票价格大的股票我们可以使用「单调递减栈」来做。具体步骤如下：

- 初始化方法：初始化一个空栈，即 `self.stack = []`

- 求解今天股票价格的跨度：

  - 初始化跨度 `span` 为 `1`。
  - 如果今日股票价格 `price` 大于等于栈顶元素 `self.stack[-1][0]`，则：
    - 将其弹出，即 `top = self.stack.pop()`。
    - 跨度累加上弹出栈顶元素的跨度，即 `span += top[1]`。
    - 继续判断，直到遇到一个今日股票价格 `price` 小于栈顶元素的元素位置，再将 `[price, span]` 压入栈中。
  - 如果今日股票价格 `price` 小于栈顶元素 `self.stack[-1][0]`，则直接将 `[price, span]` 压入栈中。

  - 最后输出今天股票价格的跨度 `span`。    

## 代码

```python
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            top = self.stack.pop()
            span += top[1]
        self.stack.append([price, span])
        return span
```

