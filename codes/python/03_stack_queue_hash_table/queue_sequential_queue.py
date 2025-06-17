class Queue:
    # 初始化空队列
    def __init__(self, size=100):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.front = -1
        self.rear = -1
        
    # 判断队列是否为空
    def is_empty(self):
        return self.front == self.rear
    
    # 判断队列是否已满
    def is_full(self):
        return self.rear + 1 == self.size
    
    # 入队操作
    def enqueue(self, value):
        if self.is_full():
            raise Exception('Queue is full')
        else:
            self.rear += 1
            self.queue[self.rear] = value
            
    # 出队操作
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            self.queue[self.front] = None
            self.front += 1
            return self.queue[self.front]
        
    # 获取队头元素
    def front_value(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            return self.queue[self.front + 1]
    
    # 获取队尾元素
    def rear_value(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            return self.queue[self.rear]
        
        
        
        
queue = Queue(size=2)

queue.enqueue(1)
print(queue.front_value())
print(queue.rear_value())
#queue.dequeue()
queue.enqueue(2)
queue.enqueue(3)
#queue.dequeue()
print(queue.front_value())
print(queue.rear_value())
#queue.dequeue()
#print(queue.front_value())
#print(queue.rear_value())
    