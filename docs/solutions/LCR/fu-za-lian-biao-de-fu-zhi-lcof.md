# [LCR 154. 复杂链表的复制](https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/)

- 标签：哈希表、链表
- 难度：中等

## 题目链接

- [LCR 154. 复杂链表的复制 - 力扣](https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/)

## 题目大意

给定一个链表，每个节点除了 `next` 指针之后，还包含一个随机指针 `random`，该指针可以指向链表中的任何节点或者空节点。

要求：将该链表进行深拷贝。

## 解题思路

遍历链表，利用哈希表，以旧节点：新节点为映射关系，将节点关系存储下来。

再次遍历链表，将新链表的 `next` 和 `random` 指针设置好。

## 代码

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node_dict = dict()
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            node_dict[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                node_dict[curr].next = node_dict[curr.next]
            if curr.random:
                node_dict[curr].random = node_dict[curr.random]
            curr = curr.next
        return node_dict[head]
```

