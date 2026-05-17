# [1206. 设计跳表](https://leetcode.cn/problems/design-skiplist/)

- 标签：设计、链表
- 难度：困难

## 题目链接

- [1206. 设计跳表 - 力扣](https://leetcode.cn/problems/design-skiplist/)

## 题目大意

**描述**：不使用任何库函数，设计一个跳表（Skiplist）。

跳表是在 $O(\log n)$ 时间内完成增加、删除、搜索操作的数据结构。跳表中有很多层，每一层是一个短的链表。

需要实现以下函数：
- `search(target)`：返回 $target$ 是否存在于跳表中。
- `add(num)`：插入一个元素到跳表。
- `erase(num)`：在跳表中删除一个值，如果 $num$ 不存在返回 `false`。如果存在多个 $num$，删除其中任意一个即可。

**说明**：

- $0 \le num, target \le 2 \times 10^{4}$。
- 调用 `search`, `add`, `erase` 操作次数不大于 $5 \times 10^{4}$。

**示例**：

- 示例 1：

```python
输入
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
输出
[null, null, null, null, false, null, true, false, true, false]

解释
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除
```

## 解题思路

### 思路 1：跳表实现

###### 1. 核心思想

跳表（Skiplist）可以理解为「带索引的链表」。普通链表的查找是 $O(n)$ 的，因为必须从头到尾逐个遍历。跳表通过在链表之上建立多层「索引」，让查找时可以跳过大量节点，达到 $O(\log n)$ 的效率。

可以这样形象地理解：
- **第 0 层**：一个包含所有元素的有序链表。
- **第 1 层**：在第 0 层的基础上，每隔一个节点抽出一个作为「快速通道」。
- **第 2 层**：在第 1 层的基础上，再隔一个抽一个。
- 依此类推，越往上节点越稀疏，查找时从顶层开始，快速定位到目标区间，然后向下层细化。

插入时，每个节点出现的层数是随机的（抛硬币），期望上每升高一层的概率为 $1/2$，所以 $n$ 个元素的期望层数为 $\log n$。

###### 2. 具体步骤

**第 1 步：设计节点结构**

每个节点 $Node$ 包含：
- $val$：节点存储的整数值。
- $next$：一个数组，$next[i]$ 表示该节点在第 $i$ 层的下一个节点指针。

**第 2 步：初始化跳表**

- 设置最大层数 $MAX\_LEVEL = 16$（对于 $5 \times 10^4$ 次操作足够了）。
- 创建头节点 $head$，值设为 $-1$，$next$ 数组长度为 $MAX\_LEVEL + 1$。
- 当前实际层数 $level = 0$。

**第 3 步：实现 search(target)**

从当前最高层向下查找：
- 从 $head$ 出发，在第 $i$ 层向右移动，直到下一个节点的值 $\ge target$。
- 然后下降到第 $i-1$ 层继续。
- 最终到达第 $0$ 层时，检查下一个节点是否为 $target$。

这个过程就像在图书馆的书架上找书：先在高层标牌上确定大致区域，再到具体书架上找。

**第 4 步：实现 add(num)**

- 从最高层开始，找到 $num$ 在每一层应该插入的位置，记录在 $update$ 数组中。
- 随机决定新节点的层数 $level$。
- 如果 $level > self.level$，需要将 $self.level+1$ 到 $level$ 层的 $update$ 设为 $head$，并更新 $self.level$。
- 创建新节点，从第 $0$ 层到第 $level$ 层分别插入（调整指针）。

**第 5 步：实现 erase(num)**

- 同样先找到 $num$ 在每一层的前驱节点，记录在 $update$ 中。
- 检查第 $0$ 层 $update[0]$ 的下一个节点是否为 $num$，如果不是则返回 $false$。
- 从第 $0$ 层开始向上，逐层删除 $num$（只需要调整前驱节点的 $next$ 指针指向 $num$ 的 $next$）。
- 如果某层 $update[i]$ 的下一个不是 $num$，说明更高层也没有了，直接跳出。
- 如果删除后最高层变为空，降低 $self.level$。

### 思路 1：代码

```python
import random

class Node:
    def __init__(self, val=-1, level=0):
        self.val = val
        # next[i] 表示该节点在第 i 层的下一个节点
        self.next = [None] * (level + 1)

class Skiplist:

    def __init__(self):
        # 最大层数，对于 5 * 10^4 次操作足够
        self.MAX_LEVEL = 16
        # 头节点，值设为 -1
        self.head = Node(-1, self.MAX_LEVEL)
        # 当前跳表的实际最大层数
        self.level = 0

    def _random_level(self):
        """随机决定新节点的层数，每升高一层的概率为 0.5"""
        level = 0
        while random.random() < 0.5 and level < self.MAX_LEVEL:
            level += 1
        return level

    def search(self, target: int) -> bool:
        cur = self.head
        # 从最高层开始逐层下降
        for i in range(self.level, -1, -1):
            # 在当前层向右移动，直到下一个节点值 >= target
            while cur.next[i] and cur.next[i].val < target:
                cur = cur.next[i]
        # 已经到达第 0 层，检查下一个节点
        cur = cur.next[0]
        return cur is not None and cur.val == target

    def add(self, num: int) -> None:
        # update[i] 记录第 i 层中 num 的前驱节点
        update = [self.head] * (self.MAX_LEVEL + 1)
        cur = self.head

        # 从最高层开始，找到每层 num 应该插入的位置
        for i in range(self.level, -1, -1):
            while cur.next[i] and cur.next[i].val < num:
                cur = cur.next[i]
            update[i] = cur

        # 随机决定新节点的层数
        level = self._random_level()
        if level > self.level:
            # 更高层的前驱设为 head
            for i in range(self.level + 1, level + 1):
                update[i] = self.head
            self.level = level

        # 创建新节点并插入到各层
        node = Node(num, level)
        for i in range(level + 1):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

    def erase(self, num: int) -> bool:
        # update[i] 记录第 i 层中 num 的前驱节点
        update = [self.head] * (self.MAX_LEVEL + 1)
        cur = self.head

        # 从最高层开始，找到每层 num 的前驱
        for i in range(self.level, -1, -1):
            while cur.next[i] and cur.next[i].val < num:
                cur = cur.next[i]
            update[i] = cur

        cur = cur.next[0]
        # 如果底层没有 num，说明 num 不存在
        if cur is None or cur.val != num:
            return False

        # 从各层中删除 cur
        for i in range(self.level + 1):
            if update[i].next[i] != cur:
                break
            update[i].next[i] = cur.next[i]

        # 如果最高层空了，降低层数
        while self.level > 0 and self.head.next[self.level] is None:
            self.level -= 1

        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$，其中 $n$ 是跳表中的元素个数。每次操作从最高层开始，每层跳过部分元素。期望时间复杂度为 $O(\log n)$，其中 $n$ 是元素个数。最坏情况下可能退化为 $O(n)$，但概率极低。
- **空间复杂度**：$O(n \log n)$，每个节点出现在多个层级中。期望空间复杂度为 $O(n)$ 乘以常数因子（每层期望节点数递减）。
