# [面试题 02.02. 返回倒数第 k 个节点](https://leetcode.cn/problems/kth-node-from-end-of-list-lcci/)

- 标签：链表、双指针
- 难度：简单

## 题目链接

- [面试题 02.02. 返回倒数第 k 个节点 - 力扣](https://leetcode.cn/problems/kth-node-from-end-of-list-lcci/)

## 题目大意

给定一个链表的头节点 `head`，以及一个整数 `k`。

要求：返回链表的倒数第 `k` 个节点的值。

## 解题思路

常规思路是遍历一遍链表，求出链表长度，再遍历一遍到对应位置，返回该位置上的节点。

如果用一次遍历实现的话，可以使用快慢指针。让快指针先走 `k` 步，然后快慢指针、慢指针再同时走，每次一步，这样等快指针遍历到链表尾部的时候，慢指针就刚好遍历到了倒数第 `k` 个节点位置。返回该该位置上的节点即可。

## 代码

```python
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        slow = head
        fast = head
        for _ in range(k):
            if fast == None:
                return fast
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val
```

