# [LCR 025. 两数相加 II](https://leetcode.cn/problems/lMSNwu/)

- 标签：栈、链表、数学
- 难度：中等

## 题目链接

- [LCR 025. 两数相加 II - 力扣](https://leetcode.cn/problems/lMSNwu/)

## 题目大意

给定两个非空链表的头节点 `l1` 和 `l2` 来代表两个非负整数。数字最高位位于链表开始位置。每个节点只储存一位数字。除了数字 `0` 之外，这两个链表代表的数字都不会以 `0` 开头。

要求：将这两个数相加会返回一个新的链表。

## 解题思路

链表中最高位位于链表开始位置，最低位位于链表结束位置。这与我们做加法的数位顺序是相反的。为了将链表逆序，从而从低位开始处理数位，我们可以借用两个栈：将链表中所有数字分别压入两个栈中，再依次取出相加。

同时，在相加的时候，还要考虑进位问题。具体步骤如下：

- 将链表 `l1` 中所有节点值压入 `stack1` 栈中，再将链表 `l2` 中所有节点值压入 `stack2` 栈中。
- 使用 `res` 存储新的结果链表，一开始指向 `None`，`carry` 记录进位。
- 如果 `stack1` 或 `stack2` 不为空，或着进位 `carry` 不为 `0`，则：
  - 从 `stack1` 中取出栈顶元素 `num1`，如果 `stack1` 为空，则 `num1 = 0`。
  - 从 `stack2` 中取出栈顶元素 `num2`，如果 `stack2` 为空，则 `num2 = 0`。
  - 计算相加结果，并计算进位。
  - 建立新节点，存储进位后余下的值，并令其指向 `res`。
  - `res` 指向新节点，继续判断。
- 如果 `stack1`、`stack2` 都为空，并且进位 `carry` 为 `0`，则输出 `res`。

## 代码

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        res = None
        carry = 0
        while stack1 or stack2 or carry != 0:
            num1 = stack1.pop() if stack1 else 0
            num2 = stack2.pop() if stack2 else 0
            cur_sum = num1 + num2 + carry
            carry = cur_sum // 10
            cur_sum %= 10
            cur_node = ListNode(cur_sum)
            cur_node.next = res
            res = cur_node
        return res
```

