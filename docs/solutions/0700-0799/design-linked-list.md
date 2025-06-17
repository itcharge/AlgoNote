# [0707. 设计链表](https://leetcode.cn/problems/design-linked-list/)

- 标签：设计、链表
- 难度：中等

## 题目链接

- [0707. 设计链表 - 力扣](https://leetcode.cn/problems/design-linked-list/)

## 题目大意

**要求**：设计实现一个链表，需要支持以下操作：

- `get(index)`：获取链表中第 `index` 个节点的值。如果索引无效，则返回 `-1`。
- `addAtHead(val)`：在链表的第一个元素之前添加一个值为 `val` 的节点。插入后，新节点将成为链表的第一个节点。
- `addAtTail(val)`：将值为 `val` 的节点追加到链表的最后一个元素。
- `addAtIndex(index, val)`：在链表中的第 `index` 个节点之前添加值为 `val`  的节点。如果 `index` 等于链表的长度，则该节点将附加到链表的末尾。如果 `index` 大于链表长度，则不会插入节点。如果 `index` 小于 `0`，则在头部插入节点。
- `deleteAtIndex(index)`：如果索引 `index` 有效，则删除链表中的第 `index` 个节点。

**说明**：

- 所有`val`值都在 $[1, 1000]$ 之内。
- 操作次数将在 $[1, 1000]$ 之内。
- 请不要使用内置的 `LinkedList` 库。

**示例**：

- 示例 1：

```python
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   // 链表变为 1 -> 2 -> 3
linkedList.get(1);            // 返回 2
linkedList.deleteAtIndex(1);  // 现在链表是 1-> 3
linkedList.get(1);            // 返回 3
```

## 解题思路

### 思路 1：单链表

新建一个带有 `val` 值 和 `next` 指针的链表节点类， 然后按照要求对节点进行操作。

### 思路 1：代码

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0)


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        if index < 0:
            index = 0

        self.size += 1
        pre = self.head
        for _ in range(index):
            pre = pre.next

        add_node = ListNode(val)
        add_node.next = pre.next
        pre.next = add_node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        pre = self.head
        for _ in range(index):
            pre = pre.next

        pre.next = pre.next.next
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `addAtHead(val)`：$O(1)$。
  - `get(index)`、`addAtTail(val)`、`del eteAtIndex(index)`：$O(k)$。$k$ 指的是元素的索引。
  - `addAtIndex(index, val)`：$O(n)$。$n$ 指的是链表的元素个数。

- **空间复杂度**：$O(1)$。

### 思路 2：双链表

新建一个带有 `val` 值和 `next` 指针、`prev` 指针的链表节点类，然后按照要求对节点进行操作。

### 思路 2：代码

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        if index < 0:
            index = 0

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next
        else:
            next = self.tail
            for _ in range(self.size - index):
                next = next.prev
            prev = next.prev

        self.size += 1
        add_node = ListNode(val)
        add_node.prev = prev
        add_node.next = next
        prev.next = add_node
        next.prev = add_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next.next
        else:
            next = self.tail
            for _ in range(self.size - index - 1):
                next = next.prev
            prev = next.prev.prev

        self.size -= 1
        prev.next = next
        next.prev = prev
```

### 思路 2：复杂度分析

- **时间复杂度**：
  - `addAtHead(val)`、`addAtTail(val)`：$O(1)$。
  - `get(index)`、`addAtIndex(index, val)`、`del eteAtIndex(index)`：$O(min(k, n - k))$。$n$ 指的是链表的元素个数，$k$ 指的是元素的索引。
- **空间复杂度**：$O(1)$。

