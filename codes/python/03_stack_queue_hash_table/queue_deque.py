class Node:
    """双向链表节点"""
    def __init__(self, value):
        self.value = value     # 节点值
        self.prev = None       # 指向前一个节点的指针
        self.next = None       # 指向后一个节点的指针

class Deque:
    """双向队列实现 - 链式存储"""
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

class ArrayDeque:
    """双向队列实现 - 顺序存储"""
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

# 测试代码
if __name__ == "__main__":
    print("=== 链式存储双向队列测试 ===")
    deque = Deque()
    
    # 测试队尾入队
    deque.push_back(1)
    deque.push_back(2)
    deque.push_back(3)
    print(f"队尾入队后，队列大小: {deque.get_size()}")
    print(f"队头元素: {deque.peek_front()}")
    print(f"队尾元素: {deque.peek_back()}")
    
    # 测试队头入队
    deque.push_front(0)
    print(f"队头入队后，队列大小: {deque.get_size()}")
    print(f"队头元素: {deque.peek_front()}")
    print(f"队尾元素: {deque.peek_back()}")
    
    # 测试出队操作
    print(f"队头出队: {deque.pop_front()}")
    print(f"队尾出队: {deque.pop_back()}")
    print(f"出队后，队列大小: {deque.get_size()}")
    
    print("\n=== 顺序存储双向队列测试 ===")
    array_deque = ArrayDeque(capacity=5)
    
    # 测试队尾入队
    array_deque.push_back(1)
    array_deque.push_back(2)
    array_deque.push_back(3)
    print(f"队尾入队后，队列大小: {array_deque.get_size()}")
    print(f"队头元素: {array_deque.peek_front()}")
    print(f"队尾元素: {array_deque.peek_back()}")
    
    # 测试队头入队
    array_deque.push_front(0)
    print(f"队头入队后，队列大小: {array_deque.get_size()}")
    print(f"队头元素: {array_deque.peek_front()}")
    print(f"队尾元素: {array_deque.peek_back()}")
    
    # 测试出队操作
    print(f"队头出队: {array_deque.pop_front()}")
    print(f"队尾出队: {array_deque.pop_back()}")
    print(f"出队后，队列大小: {array_deque.get_size()}")
    
    # 测试循环队列特性
    print("\n=== 循环队列特性测试 ===")
    array_deque.push_back(4)
    array_deque.push_back(5)
    array_deque.push_front(6)
    print(f"队列大小: {array_deque.get_size()}")
    print(f"是否已满: {array_deque.is_full()}")
    
    # 清空队列
    while not array_deque.is_empty():
        print(f"出队: {array_deque.pop_front()}")
    
    print(f"队列是否为空: {array_deque.is_empty()}")
