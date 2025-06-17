class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    # 根据 data 初始化一个新链表
    def create(self, data):
        if not data:
            return
        self.head = ListNode(data[0])
        cur = self.head
        for i in range(1, len(data)):
            node = ListNode(data[i])
            cur.next = node
            cur = cur.next
    
    # 获取线性链表长度
    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next 
        return count
    
    # 查找元素：在链表中查找值为 val 的元素
    def find(self, val):
        cur = self.head
        while cur:
            if val == cur.val:
                return cur
            cur = cur.next
        
        return None
    
    # 链表头部插入元素
    def insertFront(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
    
    # 链表尾部插入元素
    def insertRear(self, val):
        node = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    
    # 链表中间插入元素
    def insertInside(self, index, val):
        count = 0
        cur = self.head
        while cur and count < index - 1:
            count += 1
            cur = cur.next
            
        if not cur:
            return 'Error'
        
        node = ListNode(val)
        node.next = cur.next
        cur.next = node
        
    # 改变元素：将链表中第 i 个元素值改为 val
    def change(self, index, val):
        count = 0
        cur = self.head
        while cur and count < index:
            count += 1
            cur = cur.next
        
        if not cur:
            return 'Error'
        
        cur.val = val
    
    # 链表头部删除元素
    def removeFront(self):
        if self.head:
            self.head = self.head.next
            
    # 链表尾部删除元素
    def removeRear(self):
        if not self.head or not self.head.next:
            return 'Error'
        
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
        
    # 链表中间删除元素
    def removeInside(self, index):
        count = 0
        cur = self.head
        
        while cur.next and count < index - 1:
            count += 1
            cur = cur.next
        
        if not cur:
            return 'Error'
        
        del_node = cur.next
        cur.next = del_node.next