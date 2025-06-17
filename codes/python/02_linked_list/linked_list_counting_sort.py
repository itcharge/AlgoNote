class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def countingSort(self, head: ListNode):
        if not head:
            return head
        
        list_min, list_max = float('inf'), float('-inf')
        cur = head
        while cur:
            if cur.val < list_min:
                list_min = cur.val
            if cur.val > list_max:
                list_max = cur.val
            cur = cur.next
            
        size = list_max - list_min + 1
        counts = [0 for _ in range(size)]
        
        cur = head
        while cur:
            counts[cur.val - list_min] += 1
            cur = cur.next
            
        dummy_head = ListNode(-1)
        cur = dummy_head
        for i in range(size):
            while counts[i]:
                cur.next = ListNode(i + list_min)
                counts[i] -= 1
                cur = cur.next
        return dummy_head.next
            
    def sortLinkedList(self, head: ListNode):
        return self.countingSort(head, None)