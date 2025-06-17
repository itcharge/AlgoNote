# [LCR 142. 训练计划 IV](https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)

- 标签：递归、链表
- 难度：简单

## 题目链接

- [LCR 142. 训练计划 IV - 力扣](https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)

## 题目大意

给定两个升序链表。

要求：将其合并为一个升序链表。

## 解题思路

利用归并排序的思想。

创建一个新的链表节点作为头节点（记得保存），然后判断 l1和 l2 头节点的值，将较小值的节点添加到新的链表中。

当一个节点添加到新的链表中之后，将对应的 l1 或 l2 链表向后移动一位。

然后继续判断当前 l1 节点和当前 l2 节点的值，继续将较小值的节点添加到新的链表中，然后将对应的链表向后移动一位。

这样，当 l1 或 l2 遍历到最后，最多有一个链表还有节点未遍历，则直接将该节点链接到新的链表尾部即可。

## 代码

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = ListNode(-1)

        curr = newHead
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 is not None else l2

        return newHead.next
```

