# [LCR 029. 循环有序列表的插入](https://leetcode.cn/problems/4ueAj6/)

- 标签：链表
- 难度：中等

## 题目链接

- [LCR 029. 循环有序列表的插入 - 力扣](https://leetcode.cn/problems/4ueAj6/)

## 题目大意

给定循环升序链表中的一个节点 `head` 和一个整数 `insertVal`。

要求：将整数 `insertVal` 插入循环升序链表中，并且满足链表仍为循环升序链表。最终返回原先给定的节点。

## 解题思路

- 先判断所给节点 `head` 是否为空，为空直接创建一个值为 `insertVal` 的新节点，并指向自己，返回即可。

- 如果 `head` 不为空，把 `head` 赋值给 `node` ，方便最后返回原节点 `head`。
- 然后遍历 `node`，判断插入值 `insertVal` 与 `node.val` 和 `node.next.val` 的关系，找到插入位置，具体判断如下：
  - 如果新节点值在两个节点值中间， 即 `node.val <= insertVal <= node.next.val`。则说明新节点值在最大值最小值中间，应将新节点插入到当前位置，则应将 `insertVal` 插入到这个位置。
  - 如果新节点值比当前节点值和当前节点下一节点值都大，并且当前节点值比当前节点值的下一节点值大，即 `node.next.val < node.val <= insertVal`，则说明 `insertVal` 比链表最大值都大，应插入最大值后边。
  - 如果新节点值比当前节点值和当前节点下一节点值都小，并且当前节点值比当前节点值的下一节点值大，即 `insertVal < node.next.val < node.val`，则说明 `insertVal` 比链表中最小值都小，应插入最小值前边。
- 找到插入位置后，跳出循环，在插入位置插入值为 `insertVal` 的新节点。

## 代码

```python
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        node = head
        while node.next != head:
            if node.val <= insertVal <= node.next.val:
                break
            elif node.next.val < node.val <= insertVal:
                break
            elif insertVal < node.next.val < node.val:
                break
            else:
                node = node.next

        insert_node = Node(insertVal)
        insert_node.next = node.next
        node.next = insert_node
        return head
```

