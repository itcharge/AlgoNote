# [0641. 设计循环双端队列](https://leetcode.cn/problems/design-circular-deque/)

- 标签：设计、队列、数组、链表
- 难度：中等

## 题目链接

- [0641. 设计循环双端队列 - 力扣](https://leetcode.cn/problems/design-circular-deque/)

## 题目大意

**描述**：

设计实现双端队列。

**要求**：

实现 MyCircularDeque 类:

- `MyCircularDeque(int k)`：构造函数,双端队列最大为 $k$。
- `boolean insertFront()`：将一个元素添加到双端队列头部。 如果操作成功返回 true，否则返回 false。
- `boolean insertLast()`：将一个元素添加到双端队列尾部。如果操作成功返回 true，否则返回 false。
- `boolean deleteFront()`：从双端队列头部删除一个元素。 如果操作成功返回 true，否则返回 false。
- `boolean deleteLast()`：从双端队列尾部删除一个元素。如果操作成功返回 true，否则返回 false。
- `int getFront()`：从双端队列头部获得一个元素。如果双端队列为空，返回 $-1$。
- `int getRear()`：获得双端队列的最后一个元素。 如果双端队列为空，返回 $-1$。
- `boolean isEmpty()`：若双端队列为空，则返回 true，否则返回 false。
- `boolean isFull()`：若双端队列满了，则返回 true，否则返回 false。

**说明**：

- $1 \le k \le 10^{3}$。
- $0 \le value \le 10^{3}$。
- `insertFront`, `insertLast`, `deleteFront`, `deleteLast`, `getFront`, `getRear`, `isEmpty`, `isFull`  调用次数不大于 $2000$ 次。

**示例**：

- 示例 1：

```python
输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]

解释
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4
```

## 解题思路

### 思路 1：数组实现循环双端队列

#### 思路 1：算法描述

这道题目要求设计实现一个循环双端队列。我们可以使用数组来实现。

需要维护以下变量：

- $queue$：存储队列元素的数组，长度为 $k + 1$（多一个空间用于区分队列满和队列空）。
- $front$：队首指针，指向队首元素。
- $rear$：队尾指针，指向队尾元素的下一个位置。
- $capacity$：队列的容量，为 $k + 1$。

各个操作的实现：

1. **insertFront**：在队首插入元素。将 $front$ 向前移动一位（循环），然后在 $front$ 位置插入元素。
2. **insertLast**：在队尾插入元素。在 $rear$ 位置插入元素，然后将 $rear$ 向后移动一位（循环）。
3. **deleteFront**：删除队首元素。将 $front$ 向后移动一位（循环）。
4. **deleteLast**：删除队尾元素。将 $rear$ 向前移动一位（循环）。
5. **getFront**：获取队首元素。返回 $queue[front]$。
6. **getRear**：获取队尾元素。返回 $queue[(rear - 1 + capacity) \% capacity]$。
7. **isEmpty**：判断队列是否为空。当 $front = rear$ 时，队列为空。
8. **isFull**：判断队列是否已满。当 $(rear + 1) \% capacity = front$ 时，队列已满。

#### 思路 1：代码

```python
class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k + 1  # 多一个空间用于区分队列满和队列空
        self.queue = [0] * self.capacity
        self.front = 0  # 队首指针
        self.rear = 0   # 队尾指针

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # 将 front 向前移动一位（循环）
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        # 将 rear 向后移动一位（循环）
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # 将 front 向后移动一位（循环）
        self.front = (self.front + 1) % self.capacity
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # 将 rear 向前移动一位（循环）
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # 队尾元素在 rear 的前一个位置
        return self.queue[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

#### 思路 1：复杂度分析

- **时间复杂度**：所有操作的时间复杂度均为 $O(1)$。
- **空间复杂度**：$O(k)$。需要使用长度为 $k + 1$ 的数组存储队列元素。
