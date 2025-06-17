#!/usr/bin/env python3

class Stack:
    # 初始化空栈
    def __init__(self, size=100):
        self.stack = []
        self.size = size
        self.top = -1
        
    # 判断栈是否为空
    def is_empty(self):
        return self.top == -1
    
    # 判断栈是否已满
    def is_full(self):
        return self.top + 1 == self.size
    
    # 入栈操作
    def push(self, value):
        if self.is_full():
            raise Exception('Stack is full')
        else:
            self.stack.append(value)
            self.top += 1
    
    # 出栈操作
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            self.top -= 1
            self.stack.pop()
    
    # 获取栈顶元素
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self.stack[self.top]
        
    

    

S = Stack(10)
for i in range(5):
    S.push(i)

for i in range(3):
    S.pop()
    
print(S.peek())