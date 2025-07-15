# [面试题 02.05. 链表求和](https://leetcode.cn/problems/sum-lists-lcci/)

- 标签：递归、链表、数学
- 难度：中等

## 题目链接

- [面试题 02.05. 链表求和 - 力扣](https://leetcode.cn/problems/sum-lists-lcci/)

## 题目大意

给定两个非空的链表 `l1` 和 `l2`，表示两个非负整数，每位数字都是按照逆序的方式存储的，每个节点存储一位数字。

要求：计算两个整数的和，并逆序返回表示和的链表。

## 解题思路

模拟大数加法，按位相加，将结果添加到新链表上。需要注意进位和对 `10` 取余。

## 代码

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0

            sum = num1 + num2 + carry
            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

        return head.next
```

