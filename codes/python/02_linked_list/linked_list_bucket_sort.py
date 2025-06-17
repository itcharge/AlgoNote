class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 将链表节点值 val 添加到对应桶 buckets[index] 中
    def insertion(self, buckets, index, val):
        if not buckets[index]:
            buckets[index] = ListNode(val)
            return
        
        node = ListNode(val)
        node.next = buckets[index]
        buckets[index] = node
        
    # 归并环节
    def merge(self, left, right):
        
        dummy_head = ListNode(-1)
        cur = dummy_head
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
            
        if left:
            cur.next = left
        elif right:
            cur.next = right
            
        return dummy_head.next
    
    # 归并排序
    def mergeSort(self, head: ListNode):
        # 分割环节
        if not head or not head.next:
            return head
        
        # 快慢指针找到中心链节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
        # 断开左右链节点
        left_head, right_head = head, slow.next 
        slow.next = None
        
        # 归并操作
        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))        
    
    def bucketSort(self, head: ListNode, bucket_size=5):
        if not head:
            return head
        
        # 找出链表中最大值 list_max 和最小值 list_min
        list_min, list_max = float('inf'), float('-inf')
        cur = head
        while cur:
            if cur.val < list_min:
                list_min = cur.val
            if cur.val > list_max:
                list_max = cur.val
            cur = cur.next
            
        # 计算桶的个数，并定义桶
        bucket_count = (list_max - list_min) // bucket_size + 1
        buckets = [None for _ in range(bucket_count)]
        
        # 将链表节点值依次添加到对应桶中
        cur = head
        while cur:
            index = (cur.val - list_min) // bucket_size
            self.insertion(buckets, index, cur.val)
            cur = cur.next
            
        dummy_head = ListNode(-1)
        cur = dummy_head
        # 将元素依次出桶，并拼接成有序链表
        for bucket_head in buckets:
            bucket_cur = self.mergeSort(bucket_head)
            while bucket_cur:
                cur.next = bucket_cur
                cur = cur.next
                bucket_cur = bucket_cur.next
                
        return dummy_head.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.bucketSort(head)