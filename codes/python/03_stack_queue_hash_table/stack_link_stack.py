class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    # 初始化空栈
    def __init__(self):
        self.top = None
    
    # 判断栈是否为空
    def is_empty(self):
        return self.top == None
    
    # 入栈操作
    def push(self, value):
        cur = Node(value)
        cur.next = self.top
        self.top = cur
    
    # 出栈操作
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            cur = self.top
            self.top = self.top.next
            del cur
    
    # 获取栈顶元素
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self.top.value
        
    
stack = Stack()

for i in range(5):
    stack.push(i)
    
for i in range(3):
    stack.pop()
    
print(stack.peek())