# [0705. 设计哈希集合](https://leetcode.cn/problems/design-hashset/)

- 标签：设计、数组、哈希表、链表、哈希函数
- 难度：简单

## 题目链接

- [0705. 设计哈希集合 - 力扣](https://leetcode.cn/problems/design-hashset/)

## 题目大意

**要求**：不使用内建的哈希表库，自行实现一个哈希集合（HashSet）。

需要满足以下操作：

- `void add(key)` 向哈希集合中插入值 $key$。
- `bool contains(key)` 返回哈希集合中是否存在这个值 $key$。
- `void remove(key)` 将给定值 $key$ 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

**说明**：

- $0 \le key \le 10^6$。
- 最多调用 $10^4$ 次 `add`、`remove` 和 `contains`。

**示例**：

- 示例 1：

```python
输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）
```

## 解题思路

### 思路 1：数组 + 链表

定义一个一维长度为 $buckets$ 的二维数组 $table$。

第一维度用于计算哈希函数，为 $key$ 进行分桶。第二个维度用于寻找 $key$ 存放的具体位置。第二维度的数组会根据 $key$ 值动态增长，模拟真正的链表。

### 思路 1：代码

```python
class MyHashSet:

    def __init__(self):
        self.buckets = 1003
        self.table = [[] for _ in range(self.buckets)]

        
    def hash(self, key):
        return key % self.buckets

    
    def add(self, key: int) -> None:
        hash_key = self.hash(key)
        if key in self.table[hash_key]:
            return
        self.table[hash_key].append(key)


    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        if key not in self.table[hash_key]:
            return
        self.table[hash_key].remove(key)


    def contains(self, key: int) -> bool:
        hash_key = self.hash(key)
        return key in self.table[hash_key]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\frac{n}{m})$，其中 $n$ 为哈希表中的元素数量，$b$ 为 $table$ 的元素个数，也就是链表的数量。
- **空间复杂度**：$O(n + m)$。

