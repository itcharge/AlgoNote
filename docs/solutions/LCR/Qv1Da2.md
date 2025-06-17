# [LCR 028. 扁平化多级双向链表](https://leetcode.cn/problems/Qv1Da2/)

- 标签：深度优先搜索、链表、双向链表
- 难度：中等

## 题目链接

- [LCR 028. 扁平化多级双向链表 - 力扣](https://leetcode.cn/problems/Qv1Da2/)

## 题目大意

给定一个带子链表指针 `child` 的双向链表。

要求：将 `child` 的子链表进行扁平化处理，使所有节点出现在单级双向链表中。

扁平化处理如下：

```
原链表：
1---2---3---4---5---6--NULL
        |
        7---8---9---10--NULL
            |
            11--12--NULL
扁平化之后：
1---2---3---7---8---11---12---9---10---4---5---6--NULL
```

## 解题思路

递归处理多层链表的扁平化。遍历链表，找到 `child` 非空的节点， 将其子链表链接到当前节点的 `next` 位置（自身扁平化处理）。然后继续向后遍历，不断找到 `child` 节点，并进行链接。直到处理到尾部位置。

## 代码

```python
class Solution:
    def dfs(self, node: 'Node'):
        # 找到链表的尾节点或 child 链表不为空的节点
        while node.next and not node.child:
            node = node.next
        tail = None
        if node.child:
            # 如果 child 链表不为空，将 child 链表扁平化
            tail = self.dfs(node.child)

            # 将扁平化的 child 链表链接在该节点之后
            temp = node.next
            node.next = node.child
            node.next.prev = node
            node.child = None
            tail.next = temp
            if temp:
                temp.prev = tail
            # 链接之后，从 child 链表的尾节点继续向后处理链表
            return self.dfs(tail)
        # child 链表为空，则该节点是尾节点，直接返回
        return node

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.dfs(head)
        return head
```

