## 1. 链表归并排序算法描述

1. **分割环节**：找到链表中心链节点，从中心节点将链表断开，并递归进行分割。
    1. 使用快慢指针 `fast = head.next`、`slow = head`，让 `fast` 每次移动 `2` 步，`slow` 移动 `1` 步，移动到链表末尾，从而找到链表中心链节点，即 `slow`。
    2. 从中心位置将链表从中心位置分为左右两个链表 `left_head` 和 `right_head`，并从中心位置将其断开，即 `slow.next = None`。
    3. 对左右两个链表分别进行递归分割，直到每个链表中只包含一个链节点。
2. **归并环节**：将递归后的链表进行两两归并，完成一遍后每个子链表长度加倍。重复进行归并操作，直到得到完整的链表。
    1. 使用哑节点 `dummy_head` 构造一个头节点，并使用 `cur` 指向 `dummy_head` 用于遍历。
    2. 比较两个链表头节点 `left` 和 `right` 的值大小。将较小的头节点加入到合并后的链表中，并向后移动该链表的头节点指针。
    3. 然后重复上一步操作，直到两个链表中出现链表为空的情况。
    4. 将剩余链表插入到合并后的链表中。
    5. 将哑节点 `dummy_dead` 的下一个链节点 `dummy_head.next` 作为合并后的头节点返回。

## 2. 链表归并排序实现代码

```python
class Solution:
    def merge(self, left, right):
        # 归并环节
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
```

## 3. 链表归并排序算法复杂度分析

- **时间复杂度**：$O(n \times \log_2n)$。
- **空间复杂度**：$O(1)$。

## 练习题目

- [0148. 排序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/sort-list.md)
- [0021. 合并两个有序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/merge-two-sorted-lists.md)
- [0023. 合并 K 个升序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/merge-k-sorted-lists.md)

- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)