## 1. 双向队列简介

> **双向队列（Deque，Double-Ended Queue）**：一种线性表数据结构，允许在队列的两端进行插入和删除操作，既可以从队头入队/出队，也可以从队尾入队/出队。

### 1.1 基本概念

双向队列可以看作是栈和队列的结合体，具有以下特点：

- **队头（front）**：队列的前端，可以进行插入和删除操作
- **队尾（rear）**：队列的后端，也可以进行插入和删除操作
- **空队列**：没有任何数据元素的双向队列

### 1.2 核心特性

双向队列的操作遵循 **双端操作** 的原则：
- 可以在队列的两端进行插入和删除操作
- 既具有栈的"后进先出"特性，又具有队列的"先进先出"特性
- 提供了比普通队列更灵活的操作方式

### 1.3 基本操作

双向队列支持以下基本操作：

- **队头入队（push_front）**：在队头插入元素
- **队头出队（pop_front）**：从队头删除并返回元素
- **队尾入队（push_back）**：在队尾插入元素
- **队尾出队（pop_back）**：从队尾删除并返回元素
- **查看队头元素（peek_front）**：查看队头元素但不删除
- **查看队尾元素（peek_back）**：查看队尾元素但不删除


## 2. 双向队列的实现方式

双向队列可以通过 **顺序存储** 和 **链式存储** 两种方式实现。由于双向队列需要在两端进行操作，链式存储通常更加高效和灵活。

### 2.1 链式存储双向队列

链式存储是双向队列最常用的实现方式，使用双向链表结构，每个节点都有指向前后节点的指针。

#### 2.1.1 链式存储双向队列的基本描述

我们使用双向链表实现双向队列：

- **节点结构**：每个节点包含数据域和两个指针域（prev 和 next）
- **头尾指针**：维护指向队头节点和队尾节点的指针
- **哨兵节点**：可以使用哨兵节点简化边界处理

#### 2.1.2 链式存储双向队列的实现代码

```python
class Node:
    """双向链表节点"""
    def __init__(self, value):
        self.value = value     # 节点值
        self.prev = None       # 指向前一个节点的指针
        self.next = None       # 指向后一个节点的指针

class Deque:
    """双向队列实现"""
    def __init__(self):
        """初始化空双向队列"""
        # 创建哨兵节点
        self.head = Node(0)    # 头哨兵节点
        self.tail = Node(0)    # 尾哨兵节点
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0          # 队列大小
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.size == 0
    
    def get_size(self):
        """获取队列大小"""
        return self.size
    
    def push_front(self, value):
        """队头入队"""
        new_node = Node(value)
        # 在头哨兵节点后插入新节点
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
    
    def push_back(self, value):
        """队尾入队"""
        new_node = Node(value)
        # 在尾哨兵节点前插入新节点
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
    
    def pop_front(self):
        """队头出队"""
        if self.is_empty():
            raise Exception('Deque is empty')
        
        # 删除头哨兵节点后的第一个节点
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        self.size -= 1
        return node.value
    
    def pop_back(self):
        """队尾出队"""
        if self.is_empty():
            raise Exception('Deque is empty')
        
        # 删除尾哨兵节点前的第一个节点
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        self.size -= 1
        return node.value
    
    def peek_front(self):
        """查看队头元素"""
        if self.is_empty():
            raise Exception('Deque is empty')
        return self.head.next.value
    
    def peek_back(self):
        """查看队尾元素"""
        if self.is_empty():
            raise Exception('Deque is empty')
        return self.tail.prev.value
```

- **时间复杂度**：所有操作均为 O(1)

### 2.2 顺序存储双向队列

顺序存储双向队列可以使用数组实现，但需要处理循环队列的问题以避免"假溢出"。

#### 2.2.1 顺序存储双向队列的基本描述


使用循环数组实现双向队列：

- **数组结构**：使用固定大小的数组存储元素
- **头尾指针**：维护队头和队尾的位置
- **循环处理**：通过取模运算实现循环队列

#### 2.2.2 顺序存储双向队列的实现代码

```python
class Deque:
    """顺序存储双向队列实现"""
    def __init__(self, capacity=100):
        """初始化双向队列"""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0        # 队头指针
        self.rear = 0         # 队尾指针
        self.size = 0         # 队列大小
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.size == 0
    
    def is_full(self):
        """判断队列是否已满"""
        return self.size == self.capacity
    
    def get_size(self):
        """获取队列大小"""
        return self.size
    
    def push_front(self, value):
        """队头入队"""
        if self.is_full():
            raise Exception('Deque is full')
        
        # 队头指针向前移动
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1
    
    def push_back(self, value):
        """队尾入队"""
        if self.is_full():
            raise Exception('Deque is full')
        
        self.queue[self.rear] = value
        # 队尾指针向后移动
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    def pop_front(self):
        """队头出队"""
        if self.is_empty():
            raise Exception('Deque is empty')
        
        value = self.queue[self.front]
        # 队头指针向后移动
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def pop_back(self):
        """队尾出队"""
        if self.is_empty():
            raise Exception('Deque is empty')
        
        # 队尾指针向前移动
        self.rear = (self.rear - 1) % self.capacity
        value = self.queue[self.rear]
        self.size -= 1
        return value
    
    def peek_front(self):
        """查看队头元素"""
        if self.is_empty():
            raise Exception('Deque is empty')
        return self.queue[self.front]
    
    def peek_back(self):
        """查看队尾元素"""
        if self.is_empty():
            raise Exception('Deque is empty')
        return self.queue[(self.rear - 1) % self.capacity]
```

- **时间复杂度**：所有操作均为 $O(1)$

### 2.3 两种实现方式对比

| 特性 | 链式存储 | 顺序存储 |
|------|----------|----------|
| 空间利用率 | 按需分配，无浪费 | 固定大小，可能浪费 |
| 扩容操作 | 无需扩容 | 需要重新分配空间 |
| 内存碎片 | 可能产生碎片 | 较少 |
| 实现复杂度 | 相对复杂 | 简单 |
| 缓存性能 | 较差 | 较好 |

## 3. 经典例题：设计循环双端队列

### 3.1 题目链接

- [641. 设计循环双端队列 - 力扣（LeetCode）](https://leetcode.cn/problems/design-circular-deque/)

### 3.2 题目大意

**描述**：设计实现双端队列。

**要求**：实现 `MyCircularDeque` 类：

- `MyCircularDeque(int k)`：构造函数，双端队列最大为 $k$。
- `boolean insertFront()`：将一个元素添加到双端队列头部。如果操作成功返回 $true$，否则返回 $false$。
- `boolean insertLast()`：将一个元素添加到双端队列尾部。如果操作成功返回 $true$，否则返回 $false$。
- `boolean deleteFront()`：从双端队列头部删除一个元素。如果操作成功返回 $true$，否则返回 $false$。
- `boolean deleteLast()`：从双端队列尾部删除一个元素。如果操作成功返回 $true$，否则返回 $false$。
- `int getFront()`：从双端队列头部获得一个元素。如果双端队列为空，返回 $-1$。
- `int getRear()`：获得双端队列的最后一个元素。如果双端队列为空，返回 $-1$。
- `boolean isEmpty()`：如果双端队列为空，则返回 $true$，否则返回 $false$。
- `boolean isFull()`：如果双端队列满了，则返回 $true$，否则返回 $false$。

### 3.3 解题思路

##### 思路 1：数组实现

使用数组实现循环双端队列，通过头尾指针和取模运算实现循环操作。

##### 思路 1：代码

```python
class MyCircularDeque:
    def __init__(self, k: int):
        """初始化双端队列"""
        self.capacity = k
        self.queue = [0] * k
        self.front = 0        # 队头指针
        self.rear = 0         # 队尾指针
        self.size = 0         # 队列大小

    def insertFront(self, value: int) -> bool:
        """在队头插入元素"""
        if self.isFull():
            return False
        
        # 队头指针向前移动
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """在队尾插入元素"""
        if self.isFull():
            return False
        
        self.queue[self.rear] = value
        # 队尾指针向后移动
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """删除队头元素"""
        if self.isEmpty():
            return False
        
        # 队头指针向后移动
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """删除队尾元素"""
        if self.isEmpty():
            return False
        
        # 队尾指针向前移动
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        """获取队头元素"""
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        """获取队尾元素"""
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """判断队列是否为空"""
        return self.size == 0

    def isFull(self) -> bool:
        """判断队列是否已满"""
        return self.size == self.capacity
```

##### 思路 1：复杂度分析

- **时间复杂度**：所有操作均为 $O(1)$
- **空间复杂度**：$O(k)$，其中 $k$ 为队列的容量，因为底层用定长数组实现

## 4. 总结

### 4.1 优点

- **操作灵活**：支持在队列两端进行插入和删除操作
- **效率高**：所有基本操作的时间复杂度均为 O(1)
- **功能强大**：可以模拟栈和队列的行为
- **应用广泛**：在滑动窗口、单调队列等算法中发挥重要作用

### 4.2 缺点

- **实现复杂**：相比普通队列，实现逻辑更加复杂
- **内存开销**：链式实现需要额外的指针空间
- **缓存性能**：链式实现在缓存性能上不如数组实现

### 4.3 适用场景

- **滑动窗口问题**：如滑动窗口最大值、最小值等
- **单调队列**：维护单调递增或递减序列
- **双端操作**：需要在序列两端频繁操作的场景
- **算法优化**：某些算法的时间复杂度优化

## 练习题目

- [0239. 滑动窗口最大值](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/sliding-window-maximum.md)
- [0641. 设计循环双端队列](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/design-circular-deque.md)
- [0862. 和至少为 K 的最短子数组](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0800-0899/shortest-subarray-with-sum-at-least-k.md)
- [0901. 股票价格跨度](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0900-0999/online-stock-span.md)

- [双向队列基础题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8F%8C%E5%90%91%E9%98%9F%E5%88%97%E5%9F%BA%E7%A1%80%E9%A2%98%E7%9B%AE)

## 参考资料

- 【书籍】数据结构与算法 Python 语言描述 - 裘宗燕 著
- 【书籍】数据结构教程 第 3 版 - 唐发根 著
- 【书籍】大话数据结构 程杰 著
- 【文章】[双端队列 - 数据结构与算法之美 - 极客时间](https://time.geekbang.org/column/article/41330)
- 【文章】[Python collections.deque 详解 - 菜鸟教程](https://www.runoob.com/python3/python3-collections-deque.html)
