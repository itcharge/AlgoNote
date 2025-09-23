## 1. 链表简介

### 1.1 链表定义

> **链表（Linked List）**：一种线性表数据结构，通过一组任意（可连续或不连续）的存储单元，存储同类型数据。

简而言之，**链表** 是线性表的链式存储实现。

以单链表为例，其结构如下图：

![链表](https://qcdn.itcharge.cn/images/202405092229936.png)

如上图所示，链表通过指针将一组任意的存储单元串联起来。每个数据元素及其所在的存储单元构成一个「链节点」。为了将所有节点连接成链，每个链节点除了存放数据元素本身，还需要额外存储一个指向其直接后继节点的指针，称为「后继指针 $next$」。

在链表结构中，数据元素之间的逻辑顺序由指针维护。虽然逻辑上相邻的数据元素在物理内存中可以相邻，也可以完全不相邻，因此链表在物理存储上的分布是非连续、随机的。

链表的优缺点如下：

- **优点**：链表无需预先分配存储空间，按需动态申请，能够有效避免空间浪费；在插入、删除等操作上，链表通常比数组更高效，尤其是在需要频繁修改数据结构时表现突出。

- **缺点**：链表除了存储数据本身外，还需额外存储指针信息，因此整体空间开销大于数组；同时，链表不支持随机访问，查找元素时需要从头遍历，效率较低。

下面介绍除单链表外的其他链表类型。

### 1.2 双向链表

> **双向链表（Doubly Linked List）**：链表的一种，也称为双链表。每个节点包含两个指针，分别指向其直接前驱和直接后继节点。

- **双向链表的特点**：可以从任意节点高效地访问其前驱和后继节点，支持双向遍历，插入和删除操作更加灵活。

![双向链表](https://qcdn.itcharge.cn/images/202405092230869.png)

### 1.3 循环链表

> **循环链表（Circular Linked List）**：一种特殊的链表结构，其最后一个节点的指针指向头节点，从而使整个链表首尾相连，形成一个闭环。

- **循环链表的特点**：无论从哪个节点出发，都可以遍历到链表中的任意节点，实现了节点间的循环访问。

![循环链表](https://qcdn.itcharge.cn/images/202405092230094.png)

下面我们将以最基础的「单链表」为例，详细讲解链表的基本操作。

## 2. 链表的基本操作

在数据结构中，常见的基本操作包括增、删、改、查四类，链表的操作同样主要围绕这四个方面展开。下面我们详细介绍链表的基本操作。

### 2.1 链表的结构定义

链表由若干链节点通过 $next$ 指针依次连接而成。通常我们会先定义一个简单的「链节点类」，再基于此实现完整的「链表类」。

- **链节点类（ListNode）**：包含成员变量 $val$（存储数据元素的值）和 $next$（指向下一个节点的指针）。

- **链表类（LinkedList）**：包含一个链节点变量 $head$，用于表示链表的头节点。

创建空链表时，只需将头节点 $head$ 设为「空指针」。在 Python 中可用 $None$ 表示，其他语言中常用 $NULL$、$nil$、$0$ 等。

**链节点与链表结构的代码实现如下：**

```python
# 链节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 节点的值
        self.next = next    # 指向下一个节点

class LinkedList:
    def __init__(self):
        self.head = None    # 链表头指针，初始为 None
```

### 2.2 创建链表

> **创建链表**：根据给定的线性表数据，依次生成链表节点，并将它们顺序连接起来，构成完整的链表。

具体步骤如下：
1. 取出线性表的第 $1$ 个元素，创建链表头节点。
2. 依次遍历剩余元素，每获取一个数据元素，就新建一个节点，并将其连接到当前链表的尾部。
3. 所有元素插入完成后，返回头节点。

**创建链表** 的实现代码如下：

```python
# 根据 data 列表初始化一个新链表
def create(self, data):
    if not data:
        # 如果输入数据为空，直接返回，不创建链表
        return
    # 创建头节点，并将 head 指向头节点
    self.head = ListNode(data[0])
    cur = self.head  # cur 用于指向当前链表的尾节点
    # 依次遍历 data 中剩余的元素，逐个创建新节点并连接到链表尾部
    for i in range(1, len(data)):
        node = ListNode(data[i])  # 创建新节点
        cur.next = node           # 将新节点连接到当前尾节点
        cur = cur.next            # cur 指向新的尾节点，准备连接下一个节点
```

「创建链表」的操作需要遍历所有数据元素，时间复杂度为 $O(n)$，其中 $n$ 为线性表的长度。

### 2.3 链表长度

> **链表长度**：通过一个指针变量 $cur$ 沿着链表的 $next$ 指针逐个遍历节点，并用计数器 $count$ 统计节点数量，最终得到链表长度。

具体步骤如下：
1. 令指针 $cur$ 指向链表头节点（第 $1$ 个节点）。
2. 沿着 $next$ 指针遍历链表，每访问一个节点，计数器 $count$ 加 $1$。
3. 当 $cur$ 变为 $None$（即遍历到链表末尾）时，遍历结束，此时 $count$ 即为链表长度，返回该值。

**「求链表长度」** 的实现代码如下：

```python
# 获取线性链表长度
def length(self):
    count = 0                # 初始化计数器，记录节点个数
    cur = self.head          # 从链表头节点开始遍历
    while cur:               # 只要当前节点不为 None，就继续遍历
        count += 1           # 每遍历到一个节点，计数器加 1
        cur = cur.next       # 指针后移，指向下一个节点
    return count             # 返回计数器的值，即链表长度
```

「求链表长度」的操作需要遍历链表的所有节点，操作次数为 $n$，因此时间复杂度为 $O(n)$，其中 $n$ 为链表长度。

### 2.4 查找节点

> **链表中查找值为 $val$ 的节点**：从头节点 $head$ 开始，依次遍历链表，查找值等于 $val$ 的节点。如果找到，返回该节点；否则返回 $None$。

具体步骤如下：

1. 定义指针变量 $cur$，初始指向链表的头节点。
2. 沿着链表的 $next$ 指针依次遍历每个节点：
   - 如果当前节点 $cur$ 的值等于 $val$，则查找成功，返回该节点。
   - 否则，$cur$ 指向下一个节点，继续查找。
3. 如果遍历完整个链表仍未找到，说明链表中不存在值为 $val$ 的节点，返回 $None$。

**「链表中查找值为 $val$ 的节点」** 的实现代码如下：

```python
# 链表中查找值为 val 的节点
def find(self, val):
    cur = self.head  # 从链表头节点开始遍历
    while cur:  # 只要当前节点不为 None，就继续遍历
        if val == cur.val:  # 如果当前节点的值等于目标值，查找成功
            return cur      # 返回当前节点
        cur = cur.next      # 指针后移，指向下一个节点

    # 遍历完整个链表都没有找到目标值，返回 None
    return None
```

「链表中查找值为 $val$ 的节点」需要遍历链表的所有节点，因此其时间复杂度为 $O(n)$，其中 $n$ 表示链表的长度。

### 2.5 插入节点

- **插入节点**：在链表的第 $i$ 个位置前插入一个值为 $val$ 的新节点。

具体步骤如下：

1. 定义指针变量 $cur$，初始指向链表头节点，同时定义计数器 $count$，初始值为 $0$。
2. 沿着链表的 $next$ 指针遍历，$cur$ 每指向一个节点，$count$ 加 $1$。
3. 当 $count$ 等于 $index - 1$ 时，$cur$ 正好指向第 $index - 1$ 个节点（即新节点的前驱节点），此时停止遍历。
4. 创建一个新节点 $node$，其值为 $val$。
5. 将 $node.next$ 指向 $cur.next$，即新节点的后继为原本的第 $index$ 个节点。
6. 将 $cur.next$ 指向 $node$，完成插入操作。

> 注意：如果 $index = 1$，即在头节点前插入，需要特殊处理（如使用虚拟头节点或单独判断）。

![插入节点](https://qcdn.itcharge.cn/images/202405092232900.png)

**「插入节点」** 的实现代码如下：

```python
# 插入节点
def insertInside(self, index, val):
    # 头部插入（index == 1）
    if index == 1:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        return

    count = 0
    cur = self.head
    # 遍历链表，找到第 index - 1 个节点（即新节点的前驱节点）
    while cur and count < index - 1:
        cur = cur.next
        count += 1

    # 如果遍历到链表末尾还没找到前驱节点，说明 index 越界，插入失败
    if not cur:
        return 'Error'

    node = ListNode(val)
    # 尾部插入（index 指向最后一个节点的下一个位置）
    if cur.next is None:
        cur.next = node
    else:
        node.next = cur.next
        cur.next = node
```

「插入节点」操作需要将指针 $cur$ 从链表头部遍历到第 $i$ 个节点的前一个位置，平均时间复杂度为 $O(n)$，因此整体的时间复杂度为 $O(n)$。

### 2.6 改变节点

> **将链表中第 $i$ 个节点的值修改为 $val$**：只需遍历到第 $i$ 个节点，然后直接修改该节点的值。具体步骤如下：
>
1. 定义指针变量 $cur$ 指向链表头节点，并设置计数器 $count$，初始为 $0$。
2. 沿着 $next$ 指针遍历链表，每遍历一个节点，$count$ 加 $1$。
3. 当 $count$ 等于 $index$ 时，$cur$ 正好指向第 $i$ 个节点，停止遍历。
4. 直接将 $cur$ 的值设为 $val$。

**「将链表中第 $i$ 个节点的值修改为 $val$」** 的实现代码如下：

```python
# 改变元素：将链表中第 i 个元素值改为 val
def change(self, index, val):
    # 初始化计数器 count 和指针 cur，cur 指向链表头节点
    count = 0
    cur = self.head
    # 遍历链表，直到找到第 index 个节点
    while cur and count < index:
        count += 1
        cur = cur.next
        
    # 如果 cur 为空，说明 index 越界，返回错误
    if not cur:
        return 'Error'

    # 修改第 index 个节点的值为 val
    cur.val = val
```

要将链表中第 $i$ 个节点的值修改为 $val$，需要从链表头节点出发，遍历到第 $i$ 个节点，然后进行赋值操作。由于遍历链表的时间复杂度为 $O(n)$，因此该操作的整体时间复杂度为 $O(n)$。

### 2.7 删除元素

> **删除元素**：删除链表中第 $i$ 个节点。

具体步骤如下：

1. 使用指针变量 $cur$ 遍历至第 $i - 1$ 个节点（即待删除节点的前驱）。
2. 将 $cur$ 的 $next$ 指针指向第 $i$ 个节点的下一个节点，从而跳过并移除第 $i$ 个节点。

![删除元素](https://qcdn.itcharge.cn/images/202405092233332.png)

**「删除元素」** 的实现代码如下：

```python
# 链表删除元素
def removeInside(self, index):
    # 初始化计数器 count 和指针 cur，cur 指向链表头节点
    count = 0
    cur = self.head

    # 遍历链表，cur 移动到第 index - 1 个节点（即待删除节点的前驱）
    while cur.next and count < index - 1:
        count += 1
        cur = cur.next

    # 如果 cur 为空，说明 index 越界，返回错误
    if not cur:
        return 'Error'

    # del_node 指向待删除的节点
    del_node = cur.next
    # 将 cur 的 next 指针指向 del_node 的下一个节点，实现删除
    cur.next = del_node.next
```

「删除元素」操作需要将指针 $cur$ 从链表头节点遍历至第 $i$ 个节点的前一个节点，因此其时间复杂度为 $O(n)$。

## 3. 总结

### 3.1 链表特点

链表是一种**链式存储**的线性表数据结构，具有以下核心特征：

- **存储方式**：通过指针连接任意存储单元，物理存储非连续
- **节点结构**：每个节点包含数据域和指针域
- **访问方式**：只能顺序访问，不支持随机访问

### 3.2 链表类型

| 类型 | 特点 | 适用场景 |
|------|------|----------|
| **单链表** | 每个节点只有一个后继指针 | 基础链表操作 |
| **双向链表** | 每个节点有前驱和后继指针 | 需要双向遍历 |
| **循环链表** | 尾节点指向头节点形成环 | 循环访问场景 |

### 3.3 基本操作复杂度

| 操作 | 时间复杂度 | 空间复杂度 | 说明 |
|------|------------|------------|------|
| **查找** | $O(n)$ | $O(1)$ | 需要遍历到目标位置 |
| **插入** | $O(n)$ | $O(1)$ | 找到插入位置后操作简单 |
| **删除** | $O(n)$ | $O(1)$ | 找到删除位置后操作简单 |
| **修改** | $O(n)$ | $O(1)$ | 需要遍历到目标位置 |

### 3.4 链表 vs 数组

| 特性 | 链表 | 数组 |
|------|------|------|
| **存储方式** | 链式存储，非连续 | 顺序存储，连续 |
| **随机访问** | 不支持，$O(n)$ | 支持，$O(1)$ |
| **插入删除** | 高效，$O(1)$（已知位置） | 需要移动元素，$O(n)$ |
| **空间开销** | 额外指针开销 | 无额外开销 |
| **内存分配** | 动态分配 | 静态分配 |

### 3.5 应用场景

- **频繁插入删除**：链表在插入删除操作上比数组更高效
- **动态内存管理**：适合内存大小不确定的场景
- **实现其他数据结构**：栈、队列、哈希表等的基础
- **算法优化**：某些算法中链表结构能提供更好的性能

## 练习题目

- [0707. 设计链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/design-linked-list.md)
- [0206. 反转链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/reverse-linked-list.md)
- [0203. 移除链表元素](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/remove-linked-list-elements.md)
- [0328. 奇偶链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/odd-even-linked-list.md)
- [0234. 回文链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/palindrome-linked-list.md)
- [0138. 随机链表的复制](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/copy-list-with-random-pointer.md)

- [链表基础题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E5%9F%BA%E7%A1%80%E9%A2%98%E7%9B%AE)

## 参考资料

- 【文章】[链表理论基础 - 代码随想录](https://programmercarl.com/链表理论基础.html#链表理论基础)
- 【文章】[什么是链表 - 漫画算法 - 小灰的算法之旅 - 力扣](https://leetcode.cn/leetbook/read/journey-of-algorithm/5ozchs/)
- 【文章】[链表 - 数据结构与算法之美 - 极客时间](https://time.geekbang.org/column/article/41013)
- 【书籍】数据结构教程 第 2 版 - 唐发根 著
- 【书籍】数据结构与算法 Python 语言描述 - 裘宗燕 著
