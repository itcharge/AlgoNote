# [0706. 设计哈希映射](https://leetcode.cn/problems/design-hashmap/)

- 标签：设计、数组、哈希表、链表、哈希函数
- 难度：简单

## 题目链接

- [0706. 设计哈希映射 - 力扣](https://leetcode.cn/problems/design-hashmap/)

## 题目大意

**要求**：不使用任何内建的哈希表库设计一个哈希映射（`HashMap`）。

需要满足以下操作：

- `MyHashMap()` 用空映射初始化对象。
- `void put(int key, int value) 向 HashMap` 插入一个键值对 `(key, value)` 。如果 `key` 已经存在于映射中，则更新其对应的值 `value`。
- `int get(int key)` 返回特定的 `key` 所映射的 `value`；如果映射中不包含 `key` 的映射，返回 `-1`。
- `void remove(key)` 如果映射中存在 key 的映射，则移除 `key` 和它所对应的 `value` 。

**说明**：

- $0 \le key, value \le 10^6$。
- 最多调用 $10^4$ 次 `put`、`get` 和 `remove` 方法。

**示例**：

- 示例 1：

```python
输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]

解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
```

## 解题思路

### 思路 1：链地址法

和 [0705. 设计哈希集合](https://leetcode.cn/problems/design-hashset/) 类似。这里我们使用「链地址法」来解决哈希冲突。即利用「数组 + 链表」的方式实现哈希集合。

1. 定义哈希表长度 `buckets` 为 `1003`。
2. 定义一个一维长度为 `buckets` 的二维数组 `table`。其中第一维度用于计算哈希函数，为关键字 `key` 分桶。第二个维度用于存放 `key` 和对应的 `value`。第二维度的数组会根据 `key` 值动态增长，用数组模拟真正的链表。
3. 定义一个 `hash(key)` 的方法，将 `key` 转换为对应的地址 `hash_key`。
4. 进行 `put` 操作时，根据 `hash(key)` 方法，获取对应的地址 `hash_key`。然后遍历 `hash_key` 对应的数组元素，查找与 `key` 值一样的元素。
   1. 如果找到与 `key` 值相同的元素，则更改该元素对应的 `value` 值。
   2. 如果没找到与 `key` 值相同的元素，则在第二维数组 `table[hask_key]` 中增加元素，元素为 `(key, value)` 组成的元组。

5. 进行 `get` 操作跟 `put` 操作差不多。根据 `hash(key)` 方法，获取对应的地址 `hash_key`。然后遍历 `hash_key` 对应的数组元素，查找与 `key` 值一样的元素。
   1. 如果找到与 `key` 值相同的元素，则返回该元素对应的 `value`。
   2. 如果没找到与 `key` 值相同的元素，则返回 `-1`。

### 思路 1：代码

```python
class MyHashMap:

    def __init__(self):
        self.buckets = 1003
        self.table = [[] for _ in range(self.buckets)]


    def hash(self, key):
        return key % self.buckets


    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        for item in self.table[hash_key]:
            if key == item[0]:
                item[1] = value
                return
        self.table[hash_key].append([key, value])


    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        for item in self.table[hash_key]:
            if key == item[0]:
                return item[1]
        return -1


    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        for i, item in enumerate(self.table[hash_key]):
            if key == item[0]:
                self.table[hash_key].pop(i)
                return
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\frac{n}{b})$。其中 $n$ 为哈希表中元素数量，$b$ 为链表的数量。
- **空间复杂度**：$O(n + b)$。