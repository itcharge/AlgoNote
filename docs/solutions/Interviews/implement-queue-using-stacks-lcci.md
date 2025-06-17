# [面试题 03.04. 化栈为队](https://leetcode.cn/problems/implement-queue-using-stacks-lcci/)

- 标签：栈、设计、队列
- 难度：简单

## 题目链接

- [面试题 03.04. 化栈为队 - 力扣](https://leetcode.cn/problems/implement-queue-using-stacks-lcci/)

## 题目大意

要求：实现一个 MyQueue 类，要求仅使用两个栈实现先入先出队列。

## 解题思路

使用两个栈，`inStack` 用于输入，`outStack` 用于输出。

- `push` 操作：将元素压入 `inStack` 中。
- `pop` 操作：如果 `outStack` 输出栈为空，将 `inStack` 输入栈元素依次取出，按顺序压入 `outStack` 栈。这样 `outStack` 栈的元素顺序和之前 `inStack` 元素顺序相反，`outStack` 顶层元素就是要取出的队头元素，将其移出，并返回该元素。如果 `outStack` 输出栈不为空，则直接取出顶层元素。
- `peek` 操作：和 `pop` 操作类似，只不过最后一步不需要取出顶层元素，直接将其返回即可。
- `empty` 操作：如果 `inStack` 和 `outStack` 都为空，则队列为空，否则队列不为空。

## 代码

```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        self.outStack.pop()
        return top


    def peek(self) -> int:
        """
        Get the front element.
        """
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        return top


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.outStack) == 0 and len(self.inStack) == 0
```

