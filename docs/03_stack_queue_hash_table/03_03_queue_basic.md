## 1. 队列简介

> **队列（Queue）**：一种线性表数据结构，遵循「先进先出（FIFO）」原则，只允许在一端插入元素（队尾），在另一端删除元素（队头）。

### 1.1 基本概念

- **队尾（rear）**：允许插入元素的一端
- **队头（front）**：允许删除元素的一端
- **空队**：没有任何数据元素的队列

### 1.2 核心特性

队列的操作遵循 **先进先出（FIFO）** 的原则：
- 最先进入队列的元素，最先被取出。
- 类似于排队买票，先到的人先买票，后到的人只能排在队尾等待。

### 1.3 基本操作

- **入队（enqueue）**：在队尾插入元素
- **出队（dequeue）**：从队头删除元素

下图展示了队列结构和操作方式。

![队列结构](https://qcdn.itcharge.cn/images/202405092254785.png)

## 2. 队列的实现方式

与线性表类似，队列常见的存储方式有两种：**顺序存储** 和 **链式存储**。

- **顺序存储队列**：使用一段连续的存储空间（如数组），依次存放队列中从队头到队尾的元素。通过指针 $front$ 标记队头元素的位置，$rear$ 标记队尾元素的位置。
- **链式存储队列**：采用单链表实现，元素按插入顺序依次链接。$front$ 指向链表的头节点（即队头元素），$rear$ 指向链表的尾节点（即队尾元素）。

需要注意的是，$front$ 和 $rear$ 的具体指向方式可能因实现细节而异。为简化算法或代码，有时 $front$ 会指向队头元素的前一个位置，$rear$ 也可能指向队尾元素的下一个位置。具体以实际实现为准。

### 2.1 顺序存储队列

队列最常见的实现方式是利用数组来构建顺序存储结构。在 Python 中，可以直接使用列表（list）来实现顺序存储队列。

#### 2.1.1 顺序存储队列的基本描述

![顺序存储队列](https://qcdn.itcharge.cn/images/202405092254909.png)

为简化实现，我们约定：队头指针 $self.front$ 指向队头元素的前一个位置，队尾指针 $self.rear$ 指向队尾元素所在位置。

- **初始化空队列**：创建空队列 $self.queue$，设置队列容量 $self.size$，并令 $self.front = self.rear = -1$。
- **判断队列是否为空**：如果 $self.front$ 与 $self.rear$ 相等，则队列为空。
- **判断队列是否已满**：如果 $self.rear == self.size - 1$，则队列已满。
- **入队操作**：先判断队列是否已满，如果未满，则 $self.rear$ 右移一位，将新元素赋值到 $self.queue[self.rear]$。
- **出队操作**：先判断队列是否为空，如果不为空，则 $self.front$ 右移一位，返回 $self.queue[self.front]$。
- **获取队头元素**：先判断队列是否为空，如果不为空，则返回 $self.queue[self.front + 1]$。
- **获取队尾元素**：先判断队列是否为空，如果不为空，则返回 $self.queue[self.rear]$。

#### 2.1.2 顺序存储队列的实现代码

```python
class Queue:
    """
    顺序存储队列实现（非循环队列）
    front 指向队头元素的前一个位置，rear 指向队尾元素所在位置
    """
    def __init__(self, size=100):
        """
        初始化空队列
        :param size: 队列最大容量
        """
        self.size = size
        self.queue = [None for _ in range(size)]  # 存储队列元素的数组
        self.front = -1  # 队头指针，指向队头元素的前一个位置
        self.rear = -1   # 队尾指针，指向队尾元素所在位置

    def is_empty(self):
        """
        判断队列是否为空
        :return: 如果队列为空返回 True，否则返回 False
        """
        return self.front == self.rear

    def is_full(self):
        """
        判断队列是否已满
        :return: 如果队列已满返回 True，否则返回 False
        """
        return self.rear + 1 == self.size

    def enqueue(self, value):
        """
        入队操作：在队尾插入元素
        :param value: 待插入的元素
        :raises Exception: 队列已满时抛出异常
        """
        if self.is_full():
            raise Exception('Queue is full')
        self.rear += 1
        self.queue[self.rear] = value

    def dequeue(self):
        """
        出队操作：从队头删除元素并返回
        :return: 队头元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        self.front += 1
        return self.queue[self.front]

    def front_value(self):
        """
        获取队头元素（不删除）
        :return: 队头元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[self.front + 1]

    def rear_value(self):
        """
        获取队尾元素（不删除）
        :return: 队尾元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[self.rear]
```

### 2.2 顺序存储循环队列

在上一节的顺序队列实现中，队列满时（$self.rear == self.size - 1$）就无法再插入新元素，即使前面有空位也无法利用，导致「假溢出」问题。

为解决这个问题，常用两种方法：

- **方法一：每次出队后整体前移元素**  
  
这样可以利用前面的空位，但每次出队都要移动所有元素，效率低，时间复杂度 $O(n)$，不推荐。

- **方法二：循环移动**  

将队列的首尾视为相连，通过取模运算实现指针的循环移动，从而充分利用存储空间。采用循环队列后，所有基本操作的时间复杂度均为 $O(1)$，高效且无「假溢出」问题。

循环队列的实现要点如下：

- 设 $self.size$ 为循环队列的最大容量，队头指针 $self.front$ 指向队头元素前一个位置，队尾指针 $self.rear$ 指向队尾元素。
- **入队**：$self.rear = (self.rear + 1) \mod self.size$，在新位置插入元素。
- **出队**：$self.front = (self.front + 1) \mod self.size$，并返回该位置元素。

> **注意**：  
> 初始化时 $self.front == self.rear$，表示队列为空。  
> 但队列满时也可能出现 $self.front == self.rear$，因此需要区分队空和队满。

常见区分队空和队满的方法：

- **方法 1**：增加计数变量 $self.count$，记录队列元素个数。
- **方法 2**：增加标记变量 $self.tag$，区分最近一次操作是入队还是出队。
- **方法 3（常用）**：特意空出一个位置，约定「队头指针在队尾指针的下一位置」为队满。即：
   - 队满：$(self.rear + 1) \mod self.size == self.front$
   - 队空：$self.front == self.rear$

#### 2.2.1 顺序存储循环队列的基本描述

以方法 3 为例，循环队列的操作如下：

- **初始化**：队列大小为 $self.size + 1$，$self.front = self.rear = 0$。
- **判空**：$self.front == self.rear$
- **判满**：$(self.rear + 1) \mod self.size == self.front$
- **入队**：判断队满，未满则 $self.rear$ 循环前进一位，插入元素。
- **出队**：判断队空，非空则 $self.front$ 循环前进一位，返回该元素。
- **获取队头元素**：$self.queue[(self.front + 1) \mod self.size]$
- **获取队尾元素**：$self.queue[self.rear]$

![顺序存储循环队列](https://qcdn.itcharge.cn/images/202405092254537.png)

#### 2.2.2 顺序存储循环队列的实现代码

```python
class Queue:
    """
    顺序存储循环队列实现
    front 指向队头元素的前一个位置，rear 指向队尾元素所在位置
    """
    def __init__(self, size=100):
        """
        初始化空队列
        :param size: 队列最大容量（实际可用容量为 size）
        """
        self.size = size + 1  # 实际分配空间多一个，用于区分队满和队空
        self.queue = [None for _ in range(self.size)]  # 存储队列元素
        self.front = 0  # 队头指针，指向队头元素的前一个位置
        self.rear = 0   # 队尾指针，指向队尾元素所在位置

    def is_empty(self):
        """
        判断队列是否为空
        :return: True 表示队列为空，False 表示非空
        """
        return self.front == self.rear

    def is_full(self):
        """
        判断队列是否已满
        :return: True 表示队列已满，False 表示未满
        """
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        """
        入队操作：在队尾插入元素
        :param value: 要插入的元素
        :raises Exception: 队列已满时抛出异常
        """
        if self.is_full():
            raise Exception('Queue is full')
        # rear 指针循环前进一位
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        """
        出队操作：从队头删除元素并返回
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        # front 指针循环前进一位
        self.front = (self.front + 1) % self.size
        value = self.queue[self.front]
        self.queue[self.front] = None  # 可选：清除引用，便于垃圾回收
        return value

    def front_value(self):
        """
        获取队头元素
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[(self.front + 1) % self.size]

    def rear_value(self):
        """
        获取队尾元素
        :return: 队尾元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[self.rear]
```

### 2.3 链式存储队列

当队列需要频繁插入和删除元素时，链式存储结构比顺序存储结构更高效。因此，队列常用链表实现。

链式队列的实现思路如下：

1. 用单链表表示队列，每个节点存储一个元素。
2. 用指针 $front$ 指向队头元素的前一个位置，$rear$ 指向队尾元素。
3. 只允许在队头删除元素（出队），在队尾插入元素（入队）。

#### 2.3.1 链式存储队列的基本描述

![链式存储队列](https://qcdn.itcharge.cn/images/202405092255125.png)

约定：$self.front$ 指向队头元素前一个位置，$self.rear$ 指向队尾元素。

- **初始化空队列**：创建头节点 $self.head$，令 $self.front = self.rear = self.head$。
- **队列判空**：如果 $self.front == self.rear$，队列为空。
- **入队**：新建节点，插入链表末尾，$self.rear$ 指向新节点。
- **出队**：如果队列为空则抛出异常，否则取 $self.front.next$ 的值，$self.front$ 前进一位。如果出队后 $self.front.next$ 为空，$self.rear = self.front$。
- **获取队头元素**：队列非空时，返回 $self.front.next.value$。
- **获取队尾元素**：队列非空时，返回 $self.rear.value$。

#### 2.3.2 链式存储队列的实现代码

```python
class Node:
    """
    链表节点类
    """
    def __init__(self, value):
        self.value = value  # 节点存储的值
        self.next = None    # 指向下一个节点的指针

class Queue:
    """
    链式队列实现
    """
    def __init__(self):
        """
        初始化空队列，创建一个头结点（哨兵节点），front和rear都指向头结点
        """
        head = Node(0)  # 哨兵节点，不存储有效数据
        self.front = head  # front指向队头元素的前一个节点
        self.rear = head   # rear指向队尾节点

    def is_empty(self):
        """
        判断队列是否为空
        :return: 如果队列为空返回 True，否则返回 False
        """
        return self.front == self.rear

    def enqueue(self, value):
        """
        入队操作，在队尾插入新节点
        :param value: 要插入的元素值
        """
        node = Node(value)         # 创建新节点
        self.rear.next = node      # 当前队尾节点的next指向新节点
        self.rear = node           # rear指针后移，指向新节点

    def dequeue(self):
        """
        出队操作，删除队头元素
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
            
        node = self.front.next         # 队头节点（第一个有效节点）
        self.front.next = node.next    # front的next指向下一个节点
        if self.rear == node:          # 如果出队后队列为空，rear回退到front
            self.rear = self.front
        value = node.value             # 取出队头元素的值
        del node                       # 释放节点（可省略，Python自动垃圾回收）
        return value

    def front_value(self):
        """
        获取队头元素的值
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
            
        return self.front.next.value   # front.next为队头节点

    def rear_value(self):
        """
        获取队尾元素的值
        :return: 队尾元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
            
        return self.rear.value         # rear为队尾节点
```

## 3. 队列的应用

队列作为最常用的基础数据结构之一，在算法和实际开发中有着极其广泛的应用。无论是生活中的排队买票、银行业务办理，还是计算机系统内部的任务调度，队列都扮演着不可或缺的角色。其在计算机领域的典型应用主要体现在以下两个方面：

1. **缓解主机与外部设备之间的速度差异**
   - 例如，主机输出数据的速度远快于打印机的打印速度。如果直接将数据传递给打印机，打印机无法及时处理，容易造成数据丢失。为此，通常会设置一个打印缓冲队列，将待打印的数据按顺序写入队列，打印机则按照先进先出的顺序依次取出数据进行打印。这样既保证了数据的有序输出，也提升了主机的工作效率。

2. **解决多用户环境下的系统资源竞争**
   - 在多终端的计算机系统中，多个用户可能同时请求使用 CPU。操作系统会根据请求到达的先后顺序，将这些请求排成一个队列，每次优先分配 CPU 给队头的用户。当该用户的程序运行结束或时间片用完后，将其移出队列，再将 CPU 分配给新的队头用户。这样既保证了多用户的公平性，也确保了 CPU 的高效利用。
   - 此外，像 Linux 的环形缓冲区、高性能队列 Disruptor，以及 iOS 多线程中的 GCD、NSOperationQueue 等，底层都大量采用了队列结构来实现高效的数据和任务管理。

## 练习题目

- [0622. 设计循环队列](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/design-circular-queue.md)
- [0346. 数据流中的移动平均值](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/moving-average-from-data-stream.md)
- [0225. 用队列实现栈](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/implement-stack-using-queues.md)

- [队列基础题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%98%9F%E5%88%97%E5%9F%BA%E7%A1%80%E9%A2%98%E7%9B%AE)

## 参考资料

- 【书籍】数据结构与算法 Python 语言描述 - 裘宗燕 著
- 【书籍】数据结构教程 第 3 版 - 唐发根 著
- 【书籍】大话数据结构 程杰 著
- 【文章】[数据结构之 python 实现队列的链式存储 - 不服输的南瓜的博客](https://blog.csdn.net/weixin_40283816/article/details/87952682)
- 【文章】[顺序存储的循环队列判空判满判长_- ccxcuixia](https://blog.csdn.net/baidu_41304382/article/details/108091899)
- 【文章】[队列 - 数据结构与算法之美 - 极客时间](https://time.geekbang.org/column/article/41330)