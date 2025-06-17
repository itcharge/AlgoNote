class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSort(self, head: ListNode):
        if not head and not head.next:
            return head
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        sorted_list = head
        cur = head.next 
        
        while cur:
            if sorted_list.val <= cur.val:
                # 将 cur 插入到 sorted_list 之后
                sorted_list = sorted_list.next 
            else:
                prev = dummy_head
                while prev.next.val <= cur.val:
                    prev = prev.next
                # 将 cur 到链表中间
                sorted_list.next = cur.next
                cur.next = prev.next
                prev.next = curr
            cur = sorted_list.next 
        
        return dummy_head.next
    
    def sortLinkedList(self, head: ListNode):
        return self.insertionSort(head)