# [0432. 全 O(1) 的数据结构](https://leetcode.cn/problems/all-oone-data-structure/)

- 标签：设计、哈希表、链表、双向链表
- 难度：困难

## 题目链接

- [0432. 全 O(1) 的数据结构 - 力扣](https://leetcode.cn/problems/all-oone-data-structure/)

## 题目大意

**要求**：

设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。

实现 `AllOne` 类：

- `AllOne()` 初始化数据结构的对象。
- `inc(String key)` 字符串 $key$ 的计数增加 $1$。如果数据结构中尚不存在 $key$，那么插入计数为 $1$ 的 $key$ 。
- `dec(String key)` 字符串 $key$ 的计数减少 $1$。如果 $key$ 的计数在减少后为 $0$，那么需要将这个 $key$ 从数据结构中删除。测试用例保证：在减少计数前，$key$ 存在于数据结构中。
- `getMaxKey()` 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 `""`。
- `getMinKey()` 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 `""`。

**说明**：

- 注意：每个函数都应当满足 $O(1)$ 平均时间复杂度。
- $1 \le key.length \le 10$。
- $key$ 由小写英文字母组成。
- 测试用例保证：在每次调用 `dec` 时，数据结构中总存在 $key$。
- 最多调用 `inc`、`dec`、`getMaxKey` 和 `getMinKey` 方法 $5 \times 10^{4}$ 次。

**示例**：

- 示例 1：

```python
输入
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
输出
[null, null, null, "hello", "hello", null, "hello", "leet"]

解释
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "hello"
allOne.inc("leet");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "leet"
```

## 解题思路

### 思路 1：哈希表 + 双向链表

1. 我们需要设计一个数据结构，支持 $O(1)$ 时间复杂度的 `inc`、`dec`、`getMaxKey` 和 `getMinKey` 操作。
2. 使用哈希表 $key\_to\_node$ 存储每个字符串 $key$ 对应的节点，实现 $O(1)$ 的查找。
3. 使用双向链表维护计数有序的节点，每个节点存储相同计数的所有字符串。
4. 维护双向链表的头尾指针，头节点存储最小计数，尾节点存储最大计数。
5. 对于 `inc(key)` 操作：
   - 如果 $key$ 不存在，创建计数为 $1$ 的节点。
   - 如果 $key$ 存在，将其从当前计数节点移除，添加到计数 $+1$ 的节点中。
   - 如果当前计数节点为空，删除该节点。
6. 对于 `dec(key)` 操作：
   - 将 $key$ 从当前计数节点移除，添加到计数 $-1$ 的节点中。
   - 如果计数为 $0$，从哈希表中删除 $key$。
   - 如果当前计数节点为空，删除该节点。
7. `getMaxKey()` 和 `getMinKey()` 分别返回尾节点和头节点中的任意一个字符串。

### 思路 1：代码

```python
class Node:
    """双向链表节点"""
    def __init__(self, count=0):
        self.count = count  # 计数
        self.keys = set()   # 存储相同计数的所有字符串
        self.prev = None    # 前驱节点
        self.next = None    # 后继节点

class AllOne:
    def __init__(self):
        # 哈希表：key -> node
        self.key_to_node = {}
        # 双向链表头尾哨兵节点
        self.head = Node()  # 头节点（最小计数）
        self.tail = Node()  # 尾节点（最大计数）
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """增加 key 的计数"""
        if key in self.key_to_node:
            # key 已存在，移动到下一个计数节点
            node = self.key_to_node[key]
            self._move_key(key, node, node.count + 1)
        else:
            # key 不存在，创建计数为 1 的节点
            self._add_key(key, 1)

    def dec(self, key: str) -> None:
        """减少 key 的计数"""
        node = self.key_to_node[key]
        if node.count == 1:
            # 计数为 1，直接删除
            self._remove_key(key)
        else:
            # 移动到前一个计数节点
            self._move_key(key, node, node.count - 1)

    def getMaxKey(self) -> str:
        """返回计数最大的任意一个字符串"""
        if self.tail.prev == self.head:
            return ""
        # 返回尾节点的前一个节点中的任意一个字符串
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        """返回计数最小的任意一个字符串"""
        if self.head.next == self.tail:
            return ""
        # 返回头节点的下一个节点中的任意一个字符串
        return next(iter(self.head.next.keys))

    def _add_key(self, key: str, count: int) -> None:
        """添加新的 key"""
        # 查找或创建计数为 count 的节点
        if self.head.next != self.tail and self.head.next.count == count:
            # 头节点的下一个节点计数正好是 count
            node = self.head.next
        else:
            # 需要创建新节点
            node = Node(count)
            self._insert_after(self.head, node)
        
        # 将 key 添加到节点中
        node.keys.add(key)
        self.key_to_node[key] = node

    def _remove_key(self, key: str) -> None:
        """删除 key"""
        node = self.key_to_node[key]
        node.keys.remove(key)
        del self.key_to_node[key]
        
        # 如果节点为空，删除节点
        if not node.keys:
            self._remove_node(node)

    def _move_key(self, key: str, from_node: Node, to_count: int) -> None:
        """将 key 从一个计数节点移动到另一个计数节点"""
        # 从原节点移除
        from_node.keys.remove(key)
        
        # 查找或创建目标计数节点
        to_node = None
        if to_count == from_node.count + 1:
            # 移动到下一个节点
            if from_node.next != self.tail and from_node.next.count == to_count:
                to_node = from_node.next
            else:
                to_node = Node(to_count)
                self._insert_after(from_node, to_node)
        else:
            # 移动到前一个节点
            if from_node.prev != self.head and from_node.prev.count == to_count:
                to_node = from_node.prev
            else:
                to_node = Node(to_count)
                self._insert_after(from_node.prev, to_node)
        
        # 添加到目标节点
        to_node.keys.add(key)
        self.key_to_node[key] = to_node
        
        # 如果原节点为空，删除原节点
        if not from_node.keys:
            self._remove_node(from_node)

    def _insert_after(self, node: Node, new_node: Node) -> None:
        """在 node 后面插入 new_node"""
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove_node(self, node: Node) -> None:
        """删除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `inc(key)`：$O(1)$，哈希表查找和双向链表操作都是 $O(1)$。
  - `dec(key)`：$O(1)$，哈希表查找和双向链表操作都是 $O(1)$。
  - `getMaxKey()`：$O(1)$，直接访问尾节点的前一个节点。
  - `getMinKey()`：$O(1)$，直接访问头节点的下一个节点。
- **空间复杂度**：$O(n)$，其中 $n$ 是不同字符串的数量。哈希表和双向链表都需要 $O(n)$ 的空间。
