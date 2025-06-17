# [LCR 022. 环形链表 II](https://leetcode.cn/problems/c32eOV/)

- 标签：哈希表、链表、双指针
- 难度：中等

## 题目链接

- [LCR 022. 环形链表 II - 力扣](https://leetcode.cn/problems/c32eOV/)

## 题目大意

给定一个链表的头节点 `head`。

要求：判断链表中是否有环，如果有环则返回入环的第一个节点，无环则返回 `None`。

## 解题思路

利用两个指针，一个慢指针每次前进一步，快指针每次前进两步（两步或多步效果是等价的）。如果两个指针在链表头节点以外的某一节点相遇（即相等）了，那么说明链表有环，否则，如果（快指针）到达了某个没有后继指针的节点时，那么说明没环。

如果有环，则再定义一个指针，和慢指针一起每次移动一步，两个指针相遇的位置即为入口节点。

这是因为：假设入环位置为 A，快慢指针在在 B 点相遇，则相遇时慢指针走了 a + b 步，快指针走了 $a + n(b+c) + b$ 步。

$2(a + b) = a + n(b + c) + b$。可以推出：$a = c + (n-1)(b + c)$。

我们可以发现：从相遇点到入环点的距离 $c$ 加上 $n-1$ 圈的环长 $b + c$ 刚好等于从链表头部到入环点的距离。

## 代码

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        ans = head
        while ans != slow:
            ans, slow = ans.next, slow.next
        return ans    
```

