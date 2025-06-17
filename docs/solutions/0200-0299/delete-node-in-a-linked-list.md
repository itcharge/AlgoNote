# [0237. 删除链表中的节点](https://leetcode.cn/problems/delete-node-in-a-linked-list/)

- 标签：链表
- 难度：中等

## 题目链接

- [0237. 删除链表中的节点 - 力扣](https://leetcode.cn/problems/delete-node-in-a-linked-list/)

## 题目大意

删除链表的给定节点。

## 解题思路

直接将该节点的后续节点覆盖该节点即可。即让该节点的值等于下一节点值，并让其 next 指针指向下一节点的下一节点。

## 代码

```python
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```

