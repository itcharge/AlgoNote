class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def bubbleSort(self, head: ListNode):
        node_i = head
        tail = None
        # 外层循环次数为 链表长度 次
        while node_i:
            node_j = head
            while node_j and node_j.next != tail:
                if node_j.val > node_j.next.val:
                    # 交换两个节点的值
                    node_j.val, node_j.next.val = node_j.next.val, node_j.val
                node_j = node_j.next
            # 尾指针向前移动 1 位，此时尾指针右侧为排好序的链表
            tail = node_j
            node_i = node_i.next
            
        return head
    
    def sortLinkedList(self, head: ListNode):
        return self.bubbleSort(head)