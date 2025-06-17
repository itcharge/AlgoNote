# [LCR 123. 图书整理 I](https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)

- 标签：栈、递归、链表、双指针
- 难度：简单

## 题目链接

- [LCR 123. 图书整理 I - 力扣](https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)

## 题目大意

给定一个链表的头节点 `head`。

要求：从尾到头反过来返回每个节点的值（用数组返回）。

## 解题思路

- 定义数组 `res`，从头到尾遍历链表。
- 将每个节点值存入数组中。
- 直接返回倒序数组。

## 代码

```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
```

