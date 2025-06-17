# [0622. 设计循环队列](https://leetcode.cn/problems/design-circular-queue/)

- 标签：设计、队列、数组、链表
- 难度：中等

## 题目链接

- [0622. 设计循环队列 - 力扣](https://leetcode.cn/problems/design-circular-queue/)

## 题目大意

**要求**：设计实现一个循环队列，支持以下操作：

- `MyCircularQueue(k)`: 构造器，设置队列长度为 `k`。
- `Front`: 从队首获取元素。如果队列为空，返回 `-1`。
- `Rear`: 获取队尾元素。如果队列为空，返回 `-1`。
- `enQueue(value)`: 向循环队列插入一个元素。如果成功插入则返回真。
- `deQueue()`: 从循环队列中删除一个元素。如果成功删除则返回真。
- `isEmpty()`: 检查循环队列是否为空。
- `isFull()`: 检查循环队列是否已满。

**说明**：

- 所有的值都在 `0` 至 `1000` 的范围内。
- 操作数将在 `1` 至 `1000` 的范围内。
- 请不要使用内置的队列库。

**示例**：

- 示例 1：

```python
MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
```

## 解题思路

这道题可以使用数组，也可以使用链表来实现循环队列。

### 思路 1：使用数组模拟

建立一个容量为 `k + 1` 的数组 `queue`。并保存队头指针 `front`、队尾指针 `rear`，队列容量 `capacity` 为 `k + 1`（这里之所以用了 `k + 1` 的容量，是为了判断空和满，需要空出一个）。

然后实现循环队列的各个接口：

1. `MyCircularQueue(k)`: 
   1. 将数组 `queue` 初始化大小为 `k + 1` 的数组。
   2. `front`、`rear` 初始化为 `0`。
2. `Front`: 
   1. 先检测队列是否为空。如果队列为空，返回 `-1`。
   2. 如果不为空，则返回队头元素。
3. `Rear`: 
   1. 先检测队列是否为空。如果队列为空，返回 `-1`。
   2. 如果不为空，则返回队尾元素。
4. `enQueue(value)`: 
   1. 如果队列已满，则无法插入，返回 `False`。
   2. 如果队列未满，则将队尾指针 `rear` 向右循环移动一位，并进行插入操作。然后返回 `True`。
5. `deQueue()`: 
   1. 如果队列为空，则无法删除，返回 `False`。
   2. 如果队列不空，则将队头指针 `front` 指向元素赋值为 `None`，并将 `front` 向右循环移动一位。然后返回 `True`。
6. `isEmpty()`: 如果 `rear` 等于 `front`，则说明队列为空，返回 `True`。否则，队列不为空，返回 `False`。
7. `isFull()`: 如果 `(rear + 1) % capacity` 等于 `front`，则说明队列已满，返回 `True`。否则，队列未满，返回 `False`。

### 思路 1：代码

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k + 1
        self.queue = [0 for _ in range(k + 1)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.front + 1)  % self.capacity]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。初始化和每项操作的时间复杂度均为 $O(1)$。
- **空间复杂度**：$O(k)$。其中 $k$ 为给定队列的元素数目。

