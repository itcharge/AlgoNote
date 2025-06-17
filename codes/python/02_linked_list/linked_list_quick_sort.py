class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, left: ListNode, right: ListNode):
        # 左闭右开，区间没有元素或者只有一个元素，直接返回第一个节点
        if left == right or left.next == right:
            return left
        # 选择头节点为基准节点
        pivot = left.val
        # 使用 node_i, node_j 双指针，保证 node_i 之前的节点值都小于基准节点值，node_i 与 node_j 之间的节点值都大于等于基准节点值
        node_i, node_j = left, left.next
        
        while node_j != right:
            # 发现一个小与基准值的元素
            if node_j.val < pivot:
                # node_i 之前节点都小于基准值，所以 node_i 向右移动一位（此时 node_i 节点值大于等于基准节点值）
                node_i = node_i.next
                # 将小于基准值的元素与当前 node_i 换位，换位后可以保证 node_i 之前的节点都小于基准节点值
                node_i.val, node_j.val = node_j.val, node_i.val
            node_j = node_j.next
        
        # 将基准节点放到正确位置上
        node_i.val, left.val = left.val, node_i.val
        return node_i
    
    def quickSort(self, left: ListNode, right: ListNode):
        if left == right or left.next == right:
            return left
        pi = self.partition(left, right)
        self.quickSort(left, pi)
        self.quickSort(pi.next, right)
        return left

    def sortLinkedList(self, head: ListNode):
        if not head or not head.next:
            return head
        return self.quickSort(head, None)