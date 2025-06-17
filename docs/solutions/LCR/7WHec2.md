# [LCR 077. 排序链表](https://leetcode.cn/problems/7WHec2/)

- 标签：链表、双指针、分治、排序、归并排序
- 难度：中等

## 题目链接

- [LCR 077. 排序链表 - 力扣](https://leetcode.cn/problems/7WHec2/)

## 题目大意

给定链表的头节点 `head`。

要求：按照升序排列并返回排序后的链表。

## 解题思路

归并排序。

1. 利用快慢指针找到链表的中点，以中点为界限将链表拆分成两个子链表。
2. 然后对两个子链表分别递归排序。
3. 将排序后的子链表进行归并排序，得到完整的排序后的链表。

## 代码

```python
class Solution:
    def merge_sort(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return self.merge(self.merge_sort(head, mid), self.merge_sort(mid, tail))

    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        root = ListNode(-1)
        cur = root
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        if a:
            cur.next = a
        if b:
            cur.next = b
        return root.next

    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort(head, None)
```

