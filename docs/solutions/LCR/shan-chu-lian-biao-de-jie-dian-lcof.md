# [LCR 136. 删除链表的节点](https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

- 标签：链表
- 难度：简单

## 题目链接

- [LCR 136. 删除链表的节点 - 力扣](https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

## 题目大意

给定一个链表。

要求：删除链表中值为 `val` 的节点，并返回新的链表头节点。

## 解题思路

用两个指针 `prev` 和 `curr`。`prev` 指向前一节点和当前节点，`curr` 指向当前节点。从前向后遍历链表，遇到值为 `val` 的节点时，将 `prev` 指向当前节点的下一个节点，继续递归遍历。遇不到则更新 `prev` 指针，并继续遍历。

需要注意的是要删除的节点可能包含了头节点。我们可以考虑在遍历之前，新建一个头节点，让其指向原来的头节点。这样，最终如果删除的是头节点，则删除原头节点即可。返回结果的时候，可以直接返回新建头节点的下一位节点。

## 代码

```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(0, head)
        newHead.next = head

        prev, curr = newHead, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return newHead.next
```

