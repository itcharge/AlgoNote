class Queue:
    # 初始化空队列
    def __init__(self, size=100):
        self.size = size + 1
        self.queue = [None for _ in range(size + 1)]
        self.front = 0
        self.rear = 0
        
    # 判断队列是否为空
    def is_empty(self):
        return self.front == self.rear
    
    # 判断队列是否已满
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    # 入队操作
    def enqueue(self, value):
        if self.is_full():
            raise Exception('Queue is full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            
    # 出队操作
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        
    # 获取队头元素
    def front_value(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            value = self.queue[(self.front + 1) % self.size]
            return value
        
    # 获取队尾元素
    def rear_value(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            value = self.queue[self.rear]
            return value
        
        
        
queue = Queue(size=2)

queue.enqueue(1)
#print(queue.front_value())
#print(queue.rear_value())
#queue.dequeue()
queue.enqueue(2)
queue.enqueue(3)
#queue.dequeue()
print(queue.front_value())
print(queue.rear_value())
#queue.dequeue()
#print(queue.front_value())
#print(queue.rear_value())