# [0381. O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/)

- 标签：设计、数组、哈希表、数学、随机化
- 难度：困难

## 题目链接

- [0381. O(1) 时间插入、删除和获取随机元素 - 允许重复 - 力扣](https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/)

## 题目大意

**描述**：

`RandomizedCollection` 是一种包含数字集合（可能是重复的）的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。

**要求**：

实现 `RandomizedCollection` 类:

- `RandomizedCollection()` 初始化空的 `RandomizedCollection` 对象。
- `bool insert(int val)` 将一个 $val$ 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 $true$，否则返回 $false$。
- `bool remove(int val)` 如果存在，从集合中移除一个 $val$ 项。如果该项存在，则返回 $true$，否则返回 $false$。注意，如果 $val$ 在集合中出现多次，我们只删除其中一个。
- `int getRandom()` 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量线性相关。

**说明**：

- 您必须实现类的函数，使每个函数的平均时间复杂度为 $O(1)$。
- 注意：生成测试用例时，只有在 `RandomizedCollection` 中至少有一项时，才会调用 `getRandom`。
- $-2^{31} \le val \le 2^{31} - 1$。
- `insert`, `remove` 和 `getRandom` 最多总共被调用 $2 \times 10^{5}$ 次。
- 当调用 `getRandom` 时，数据结构中至少有一个元素。

**示例**：

- 示例 1：

```python
输入
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
输出
[null, true, false, true, 2, true, 1]

解释
RandomizedCollection collection = new RandomizedCollection();// 初始化一个空的集合。
collection.insert(1);   // 返回 true，因为集合不包含 1。
                        // 将 1 插入到集合中。
collection.insert(1);   // 返回 false，因为集合包含 1。
                        // 将另一个 1 插入到集合中。集合现在包含 [1,1]。
collection.insert(2);   // 返回 true，因为集合不包含 2。
                        // 将 2 插入到集合中。集合现在包含 [1,1,2]。
collection.getRandom(); // getRandom 应当:
                        // 有 2/3 的概率返回 1,
                        // 1/3 的概率返回 2。
collection.remove(1);   // 返回 true，因为集合包含 1。
                        // 从集合中移除 1。集合现在包含 [1,2]。
collection.getRandom(); // getRandom 应该返回 1 或 2，两者的可能性相同。
```

## 解题思路

### 思路 1：数组 + 哈希表

这道题的核心思想是：**使用数组存储所有元素，用哈希表记录每个值在数组中的索引位置，通过交换数组末尾元素来实现 O(1) 删除**。

解题步骤：

1. **数据结构设计**：
   - 使用数组 $nums$ 存储所有元素，支持 $O(1)$ 随机访问。
   - 使用哈希表 $indices$ 记录每个值在数组中的所有索引位置，其中 $indices[val]$ 是一个集合，存储值 $val$ 在数组中的所有索引。

2. **插入操作**：
   - 将新元素 $val$ 添加到数组末尾，时间复杂度 $O(1)$。
   - 在哈希表中记录该元素的索引位置，时间复杂度 $O(1)$。
   - 返回该值是否首次出现（即哈希表中该值的集合是否为空）。

3. **删除操作**：
   - 从哈希表中获取要删除值 $val$ 的任意一个索引位置 $index$。
   - 将数组末尾元素 $last\_val$ 移动到位置 $index$，实现 $O(1)$ 删除。
   - 更新哈希表中 $last\_val$ 的索引信息。
   - 从哈希表中移除 $val$ 的索引记录。

4. **随机获取操作**：
   - 从数组中随机选择一个索引，返回对应元素，时间复杂度 $O(1)$。

**关键点**：

- 删除时通过交换数组末尾元素避免移动其他元素，保证 $O(1)$ 时间复杂度。
- 哈希表使用集合存储索引，支持快速查找和删除任意索引。
- 需要同时维护数组和哈希表的一致性。

**算法正确性**：

设数组长度为 $n$，哈希表 $indices$ 中每个值的索引集合大小之和等于 $n$。删除操作通过交换末尾元素保持数组连续性，哈希表正确维护每个值的索引信息，确保所有操作的正确性。

### 思路 1：代码

```python
import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        """
        初始化 RandomizedCollection 对象
        - nums: 存储所有元素的数组
        - indices: 哈希表，记录每个值在数组中的所有索引位置
        """
        self.nums = []  # 存储所有元素的数组
        self.indices = defaultdict(set)  # 值 -> 索引集合的映射

    def insert(self, val: int) -> bool:
        """
        插入元素 val 到集合中
        
        Args:
            val: 要插入的值
            
        Returns:
            bool: 如果该值不存在则返回 True，否则返回 False
        """
        # 将元素添加到数组末尾
        self.nums.append(val)
        # 记录该元素在数组中的索引位置
        self.indices[val].add(len(self.nums) - 1)
        # 返回该值是否首次出现
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        """
        从集合中移除一个 val 元素
        
        Args:
            val: 要删除的值
            
        Returns:
            bool: 如果该值存在则返回 True，否则返回 False
        """
        # 如果该值不存在，返回 False
        if not self.indices[val]:
            return False
        
        # 获取要删除元素的索引位置
        index = self.indices[val].pop()
        # 获取数组末尾元素
        last_val = self.nums[-1]
        
        # 如果删除的不是最后一个元素，需要交换
        if index != len(self.nums) - 1:
            # 将末尾元素移动到要删除的位置
            self.nums[index] = last_val
            # 更新末尾元素的索引信息
            self.indices[last_val].discard(len(self.nums) - 1)
            self.indices[last_val].add(index)
        
        # 删除数组末尾元素
        self.nums.pop()
        # 如果删除后该值的索引集合为空，从哈希表中移除
        if not self.indices[val]:
            del self.indices[val]
        
        return True

    def getRandom(self) -> int:
        """
        从当前集合中随机返回一个元素
        
        Returns:
            int: 随机选择的元素
        """
        # 从数组中随机选择一个索引，返回对应元素
        # 注意：根据题目要求，调用此方法时集合中至少有一个元素
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `insert(val)`：$O(1)$，数组末尾插入和哈希表操作都是常数时间。
  - `remove(val)`：$O(1)$，通过交换末尾元素实现常数时间删除。
  - `getRandom()`：$O(1)$，随机选择数组中的元素。
- **空间复杂度**：$O(n)$，其中 $n$ 是集合中元素的总数。需要 $O(n)$ 空间存储数组和哈希表。
