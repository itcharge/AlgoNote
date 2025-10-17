# [0146. LRU 缓存](https://leetcode.cn/problems/lru-cache/)

- 标签：设计、哈希表、链表、双向链表
- 难度：中等

## 题目链接

- [0146. LRU 缓存 - 力扣](https://leetcode.cn/problems/lru-cache/)

## 题目大意

**要求**：

设计并实现一个满足 LRU (最近最少使用) 缓存约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以 正整数 作为容量 $capacity$ 初始化 LRU 缓存
- `int get(int key)` 如果关键字 $key$ 存在于缓存中，则返回关键字的值，否则返回 $-1$。
- `void put(int key, int value)` 
   - 如果关键字 $key$ 已经存在，则变更其数据值 $value$；
   - 如果不存在，则向缓存中插入该组 $key-value$。
   - 如果插入操作导致关键字数量超过 $capacity$，则应该逐出最久未使用的关键字。

函数 `get` 和 `put` 必须以 $O(1)$ 的平均时间复杂度运行。

**说明**：

- $1 \le capacity \le 3000$。
- $0 \le key \le 10000$。
- $0 \le value \le 10^{5}$。
- 最多调用 $2 \times 10^{5}$ 次 `get` 和 `put`。

**示例**：

- 示例 1：

```python
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

## 解题思路

### 思路 1：双向链表 + 哈希表

LRU (Least Recently Used) 缓存的核心思想是：当缓存容量达到上限时，删除最久未使用的数据。

为了实现 $O(1)$ 时间复杂度的 `get` 和 `put` 操作，我们需要：

1. **哈希表**：用于快速查找节点，时间复杂度 $O(1)$。
2. **双向链表**：用于维护访问顺序，最近访问的节点在头部，最久未访问的节点在尾部。

**数据结构设计**：

- 使用双向链表节点存储 $key$ 和 $value$。
- 使用哈希表 $hash\_map$ 存储 $key$ 到节点的映射。
- 维护虚拟头节点 $head$ 和虚拟尾节点 $tail$，简化边界处理。

**核心操作**：

1. **访问节点**：将节点移动到链表头部。
2. **添加节点**：在链表头部添加新节点。
3. **删除节点**：从链表尾部删除最久未使用的节点。

### 思路 1：代码

```python
class ListNode:
    """双向链表节点"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # 哈希表：key -> 节点
        self.hash_map = {}
        # 虚拟头节点和尾节点
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_head(self, node):
        """将节点添加到链表头部"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """从链表中删除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self, node):
        """将节点移动到链表头部"""
        self._remove_node(node)
        self._add_to_head(node)
    
    def _remove_tail(self):
        """删除链表尾部节点"""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node

    def get(self, key: int) -> int:
        if key in self.hash_map:
            # 节点存在，移动到头部
            node = self.hash_map[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # 节点存在，更新值并移动到头部
            node = self.hash_map[key]
            node.value = value
            self._move_to_head(node)
        else:
            # 节点不存在，创建新节点
            new_node = ListNode(key, value)
            if self.size >= self.capacity:
                # 缓存已满，删除尾部节点
                tail_node = self._remove_tail()
                del self.hash_map[tail_node.key]
                self.size -= 1
            
            # 添加新节点到头部
            self.hash_map[key] = new_node
            self._add_to_head(new_node)
            self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `get(key)`：$O(1)$，哈希表查找 + 链表操作。
  - `put(key, value)`：$O(1)$，哈希表操作 + 链表操作。
- **空间复杂度**：$O(capacity)$，其中 $capacity$ 是缓存容量，哈希表和双向链表最多存储 $capacity$ 个节点。
