# [LCR 078. 合并 K 个升序链表](https://leetcode.cn/problems/vvXgSW/)

- 标签：链表、分治、堆（优先队列）、归并排序
- 难度：困难

## 题目链接

- [LCR 078. 合并 K 个升序链表 - 力扣](https://leetcode.cn/problems/vvXgSW/)

## 题目大意

给定一个链表数组 `lists`，每个链表都已经按照升序排列。

要求：将所有链表合并到一个升序链表中，返回合并后的链表。

## 解题思路

分而治之的思想。将链表数组不断二分，转为规模为二分之一的子问题，然后再进行归并排序。

## 代码

```python
class Solution:
    def merge_sort(self, lists: List[ListNode], left: int, right: int) -> ListNode:
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        node_left = self.merge_sort(lists, left, mid)
        node_right = self.merge_sort(lists, mid + 1, right)
        return self.merge(node_left, node_right)

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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        size = len(lists)
        return self.merge_sort(lists, 0, size - 1)
```

