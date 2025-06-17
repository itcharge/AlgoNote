# [LCR 031. LRU 缓存](https://leetcode.cn/problems/OrIXps/)

- 标签：设计、哈希表、链表、双向链表
- 难度：中等

## 题目链接

- [LCR 031. LRU 缓存 - 力扣](https://leetcode.cn/problems/OrIXps/)

## 题目大意

要求：实现一个 `LRU（最近最少使用）缓存机制`，并且在 `O(1)` 时间复杂度内完成 `get`、`put` 操作。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以正整数作为容量 `capacity` 初始化 LRU 缓存。
- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1`。
- `void put(int key, int value)` 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

## 解题思路

LRU（最近最少使用缓存）是一种常用的页面置换算法，选择最近最久未使用的页面予以淘汰。LRU 更新和插入新页面都发生在链表首，删除页面都发生在链表尾。

## 代码

```python
class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.move_node(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.move_node(node)
            return
        if len(self.hashmap) == self.capacity:
            self.hashmap.pop(self.head.next.key)
            self.remove_node(self.head.next)

        node = Node(key=key, val=value)
        self.hashmap[key] = node
        self.add_node(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def add_node(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node


    def move_node(self, node):
        self.remove_node(node)
        self.add_node(node)
```

