# [LCR 148. 验证图书取出顺序](https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

- 标签：栈、数组、模拟
- 难度：中等

## 题目链接

- [LCR 148. 验证图书取出顺序 - 力扣](https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

## 题目大意

给定连个整数序列 `pushed` 和 `popped`，其中 `pushed` 表示栈的压入顺序。

要求：判断第二个序列 `popped` 是否为栈的压出序列。

## 解题思路

借助一个栈来模拟压入、压出的操作。检测最后是否能模拟成功。

## 代码

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for item in pushed:
            stack.append(item)
            while(stack and stack[-1] == popped[index]):
                stack.pop()
                index += 1

        return len(stack) == 0
```

