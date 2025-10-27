# [0460. LFU 缓存](https://leetcode.cn/problems/lfu-cache/)

- 标签：设计、哈希表、链表、双向链表
- 难度：困难

## 题目链接

- [0460. LFU 缓存 - 力扣](https://leetcode.cn/problems/lfu-cache/)

## 题目大意

**要求**：

请你为「[最不经常使用（LFU）](https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E7%AE%97%E6%B3%95)」缓存算法设计并实现数据结构。

实现 `LFUCache` 类：

- `LFUCache(int capacity)` - 用数据结构的容量 $capacity$ 初始化对象。
- `int get(int key)` - 如果键 $key$ 存在于缓存中，则获取键的值，否则返回 $-1$。
- `void put(int key, int value)` - 如果键 $key$ 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 $capacity$ 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除「最久未使用」的键。

为了确定最不常使用的键，可以为缓存中的每个键维护一个「使用计数器」。使用计数最小的键是最久未使用的键。

当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 `put` 操作)。对缓存中的键执行 `get` 或 `put` 操作，使用计数器的值将会递增。

函数 `get` 和 `put` 必须以 $O(1)$ 的平均时间复杂度运行。

**说明**：

- $1 \le capacity \le 10^{4}$。
- $0 \le key \le 10^{5}$。
- $0 \le value \le 10^{9}$。
- 最多调用 $2 \times 10^{5}$ 次 `get` 和 `put` 方法。

**示例**：

- 示例 1：

```python
输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
// cnt(x) = 键 x 的使用计数
// cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // 返回 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // 返回 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3
```

## 解题思路

### 思路 1：双层双向链表 + 哈希表

LFU Cache 的核心在于既要维护频率信息，又要维护相同频率下的 LRU 顺序。

我们可以使用以下数据结构：

- 使用一个哈希表 $node\_dict$ 存储键值对 $(key, node)$，用于 $O(1)$ 时间访问节点
- 使用一个哈希表 $freq\_dict$ 存储频率到双向链表的映射 $freq \rightarrow DoublyLinkedList$
- 每个节点包含 $key$、$value$、$freq$（频率）、$prev$、$next$ 指针
- 每个频率对应一个双向链表，链表内部按照 LRU 规则排序（头部是最新访问，尾部是最久未访问）

算法步骤：

1. `get(key)` 操作：
   - 如果 $key$ 不在 $node\_dict$ 中，返回 $-1$
   - 如果 $key$ 存在，从原来的频率链表中移除，频率加 $1$，插入到新频率链表中，更新 $node\_dict$
   - 更新最小频率 $min\_freq$（如果原来的最小频率链表为空）

2. `put(key, value)` 操作：
   - 如果 $key$ 已存在，更新其 $value$，并执行一次 $get$ 操作来更新频率
   - 如果 $key$ 不存在：
     - 如果容量已满，删除 $freq\_dict[min\_freq]$ 链表尾部的节点
     - 创建新节点，频率为 $1$，插入到频率为 $1$ 的链表中
     - 更新 $min\_freq = 1$

### 思路 1：代码

```python
class Node:
    def __init__(self, key=0, value=0, freq=0):
        self.key = key
        self.value = value
        self.freq = freq  # 使用频率
        self.prev = None  # 前驱节点
        self.next = None  # 后继节点


class DoublyLinkedList:
    """双向链表，用于维护相同频率的节点"""
    def __init__(self):
        # 创建虚拟头尾节点
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0  # 当前链表大小
    
    def add_node_to_head(self, node):
        """在链表头部添加节点"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove_node(self, node):
        """删除指定节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_tail(self):
        """删除链表尾部节点（最久未使用）"""
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0  # 最小频率
        self.node_dict = {}  # 存储键值对：key -> node
        self.freq_dict = {}  # 存储频率到双向链表的映射：freq -> DoublyLinkedList

    def get(self, key: int) -> int:
        # 如果 key 不存在，返回 -1
        if key not in self.node_dict:
            return -1
        
        node = self.node_dict[key]
        # 从原来频率的链表中移除
        self.freq_dict[node.freq].remove_node(node)
        
        # 如果移除后，该频率链表为空且是最小频率，更新 min_freq
        if self.freq_dict[node.freq].size == 0 and self.min_freq == node.freq:
            self.min_freq += 1
        
        # 频率加 1
        node.freq += 1
        
        # 将节点插入到新频率链表的头部
        if node.freq not in self.freq_dict:
            self.freq_dict[node.freq] = DoublyLinkedList()
        self.freq_dict[node.freq].add_node_to_head(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        # 如果 key 已存在，更新 value 并执行 get 操作来更新频率
        if key in self.node_dict:
            node = self.node_dict[key]
            node.value = value
            self.get(key)  # 触发频率更新
            return
        
        # 如果 key 不存在，需要插入新节点
        # 如果容量已满，需要删除最少使用的节点
        if len(self.node_dict) >= self.capacity:
            # 删除 min_freq 链表尾部的节点
            tail_node = self.freq_dict[self.min_freq].remove_tail()
            del self.node_dict[tail_node.key]
        
        # 创建新节点，频率为 1
        node = Node(key, value, freq=1)
        self.node_dict[key] = node
        
        # 插入到频率为 1 的链表头部
        if 1 not in self.freq_dict:
            self.freq_dict[1] = DoublyLinkedList()
        self.freq_dict[1].add_node_to_head(node)
        
        # 更新最小频率为 1
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。所有操作（`get` 和 `put`）的平均时间复杂度都是 $O(1)$，因为都是通过哈希表访问节点，通过双向链表进行插入和删除。
- **空间复杂度**：$O(capacity)$。其中 $capacity$ 是缓存的容量。哈希表的空间复杂度为 $O(capacity)$，双向链表节点数为 $O(capacity)$。
