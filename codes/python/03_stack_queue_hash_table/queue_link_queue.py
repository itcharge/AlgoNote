class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    # 初始化空队列
    def __init__(self):
        head = Node(0)
        self.front = head
        self.rear = head
    
    # 判断队列是否为空
    def is_empty(self):
        return self.front == self.rear
    
    # 入队操作
    def enqueue(self, value):
        node = Node(value)
        self.rear.next = node
        self.rear = node
    
    # 出队操作
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            node = self.front.next
            self.front.next = node.next
            if self.rear == node:
                self.rear = self.front
            value = node.value
            del node
            return value
            
    # 获取队头元素
    def front_value(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            return self.front.next.value
        
    # 获取队尾元素
    def rear_value(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            return self.rear.value
        
    
queue = Queue()

queue.enqueue(1)
print(queue.front_value())
print(queue.rear_value())
queue.dequeue()
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
print(queue.front_value())
print(queue.rear_value())
queue.dequeue()
print(queue.front_value())
print(queue.rear_value())
