# [LCR 125. 图书整理 II](https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

- 标签：栈、设计、队列
- 难度：简单

## 题目链接

- [LCR 125. 图书整理 II - 力扣](https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

## 题目大意

要求：使用两个栈实现先入先出队列。需要实现对应的两个函数：

- `appendTail`：在队列尾部插入整数。
- `deleteHead`：在队列头部删除整数（如果队列中没有元素，`deleteHead` 返回 -1）。

## 解题思路

使用两个栈，inStack 用于输入，outStack 用于输出。

- `appendTail` 操作：将元素压入 inStack 中
- `deleteHead` 操作：
  - 先判断  `inStack` 和 `outStack` 是否都为空，如果都为空则说明队列中没有元素，直接返回 `-1`。
  - 如果 `outStack` 输出栈为空，将 `inStack` 输入栈元素依次取出，按顺序压入 `outStack` 栈。这样 `outStack` 栈的元素顺序和之前 `inStack` 元素顺序相反，`outStack` 顶层元素就是要取出的队头元素，将其移出，并返回该元素。如果 `outStack` 输出栈不为空，则直接取出顶层元素。

## 代码

```python
class CQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []


    def appendTail(self, value: int) -> None:
        self.inStack.append(value)


    def deleteHead(self) -> int:
        if len(self.outStack) == 0 and len(self.inStack) == 0:
            return -1
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        self.outStack.pop()
        return top
```

