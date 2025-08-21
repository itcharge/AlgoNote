## 1. 链表桶排序算法思想

> **桶排序基本思想**：
> 
> 将数据分散到若干个有序的桶中，每个桶内再单独排序，最后按顺序合并所有桶。


## 2. 链表桶排序算法步骤

1. **确定数据范围**：遍历链表找出最大值和最小值。
2. **计算桶数量**：根据数据范围和桶大小确定桶的个数。
3. **分配元素到桶**：将每个元素放入对应的桶中。
4. **桶内排序**：对每个桶内的元素进行排序（使用归并排序等）。
5. **合并结果**：按桶的顺序将所有元素合并成有序链表。

## 3. 链表桶排序代码实现

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertion(self, buckets, index, val):
        """
        将元素插入到指定桶中（头插法）
        
        Args:
            buckets: 桶数组
            index: 桶的索引
            val: 要插入的值
        """
        if not buckets[index]:
            # 如果桶为空，直接创建新节点
            buckets[index] = ListNode(val)
            return
        
        # 头插法：新节点插入到桶的头部
        node = ListNode(val)
        node.next = buckets[index]
        buckets[index] = node
        
    def merge(self, left, right):
        """
        归并两个有序链表
        
        Args:
            left: 左链表头节点
            right: 右链表头节点
            
        Returns:
            合并后的有序链表头节点
        """
        dummy_head = ListNode(-1)  # 虚拟头节点
        cur = dummy_head
        
        # 比较两个链表的节点值，选择较小的加入结果链表
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
            
        # 处理剩余节点
        if left:
            cur.next = left
        elif right:
            cur.next = right
            
        return dummy_head.next
    
    def mergeSort(self, head):
        """
        对链表进行归并排序
        
        Args:
            head: 链表头节点
            
        Returns:
            排序后的链表头节点
        """
        # 递归终止条件：空链表或单节点
        if not head or not head.next:
            return head
        
        # 快慢指针找到链表中间位置
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
        # 分割链表为左右两部分
        left_head, right_head = head, slow.next 
        slow.next = None
        
        # 递归排序左右两部分，然后归并
        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))        
    
    def bucketSort(self, head, bucket_size=5):
        """
        链表桶排序主函数
        
        Args:
            head: 待排序的链表头节点
            bucket_size: 每个桶的大小，默认5
            
        Returns:
            排序后的链表头节点
        """
        if not head:
            return head
        
        # 第一步：找出链表中的最大值和最小值
        list_min, list_max = float('inf'), float('-inf')
        cur = head
        while cur:
            list_min = min(list_min, cur.val)
            list_max = max(list_max, cur.val)
            cur = cur.next
            
        # 第二步：计算桶的数量并初始化桶数组
        bucket_count = (list_max - list_min) // bucket_size + 1
        buckets = [None for _ in range(bucket_count)]
        
        # 第三步：将链表元素分配到对应的桶中
        cur = head
        while cur:
            # 计算元素应该放入哪个桶
            index = (cur.val - list_min) // bucket_size
            self.insertion(buckets, index, cur.val)
            cur = cur.next
            
        # 第四步：对每个桶内的元素排序，然后合并
        dummy_head = ListNode(-1)
        cur = dummy_head
        
        for bucket_head in buckets:
            if bucket_head:
                # 对桶内元素进行归并排序
                sorted_bucket = self.mergeSort(bucket_head)
                # 将排序后的桶内元素添加到结果链表
                while sorted_bucket:
                    cur.next = sorted_bucket
                    cur = cur.next
                    sorted_bucket = sorted_bucket.next
                
        return dummy_head.next
    
    def sortList(self, head):
        """
        排序链表接口函数
        
        Args:
            head: 待排序的链表头节点
            
        Returns:
            排序后的链表头节点
        """
        return self.bucketSort(head)
```

## 4. 链表桶排序算法复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n)$ | 元素均匀分布，各桶很少元素，桶内排序代价小 |
| **最坏时间复杂度** | $O(n^2)$ | 大量元素落入同一桶，桶内排序退化 |
| **平均时间复杂度** | $O(n + k)$ | 遍历元素 n 次 + 遍历 k 个桶（含桶内排序） |
| **空间复杂度** | $O(n + k)$ | 需要桶数组与桶内临时节点空间 |
| **稳定性** | ✅ 稳定 | 桶内使用稳定排序并按桶序合并，保留相对次序 |

## 5. 总结

链表桶排序将元素按值域分配到多个桶中，分别排序后再合并。适合值域已知且分布较均匀的场景。

**优点**：分布均匀且桶参数合理时可接近线性；可用稳定桶内排序；并行友好
**缺点**：对分布与桶大小/数量敏感；额外空间 $O(n+k)$；最坏情况可能退化

## 练习题目

- [0148. 排序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/sort-list.md)

- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)