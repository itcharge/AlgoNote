class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sectionSort(self, head: ListNode):
        node_i = head
        # node_i 为当前未排序链表的第一个链节点
        while node_i and node_i.next:
            # min_node 为未排序链表中的值最小节点
            min_node = node_i
            node_j = node_i.next
            while node_j:
                if node_j.val < min_node.val:
                    min_node = node_j
                node_j = node_j.next
            # 交换值最小节点与未排序链表中第一个节点的值
            if node_i != min_node:
                node_i.val, min_node.val = min_node.val, node_i.val
            node_i = node_i.next
        
        return head
    
    def sortLinkedList(self, head: ListNode):
        return self.sectionSort(head)