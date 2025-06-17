# [LCR 147. 最小栈](https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/)

- 标签：栈、设计
- 难度：简单

## 题目链接

- [LCR 147. 最小栈 - 力扣](https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/)

## 题目大意

要求：设计一个「栈」，实现  `push` ，`pop` ，`top` ，`min` 操作，并且操作时间复杂度都是 `O(1)`。

## 解题思路

使用一个栈，栈元素中除了保存当前值之外，再保存一个当前最小值。

-  `push` 操作：如果栈不为空，则判断当前值与栈顶元素所保存的最小值，并更新当前最小值，将新元素保存到栈中。
-  `pop`操作：正常出栈
-  `top` 操作：返回栈顶元素保存的值。
-  `min` 操作：返回栈顶元素保存的最小值。

## 代码

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    class Node:
        def __init__(self, x):
            self.val = x
            self.min = x

    def push(self, x: int) -> None:
        node = self.Node(x)
        if len(self.stack) == 0:
            self.stack.append(node)
        else:
            topNode = self.stack[-1]
            if node.min > topNode.min:
                node.min = topNode.min

            self.stack.append(node)


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1].val


    def min(self) -> int:
        return self.stack[-1].min
```

