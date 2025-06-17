

## 1. 链表插入排序算法描述

1. 先使用哑节点 `dummy_head` 构造一个指向 `head` 的指针，使得可以从 `head` 开始遍历。
2. 维护 `sorted_list` 为链表的已排序部分的最后一个节点，初始时，`sorted_list = head`。
3. 维护 `prev` 为插入元素位置的前一个节点，维护 `cur` 为待插入元素。初始时，`prev = head`，`cur = head.next`。
4. 比较 `sorted_list` 和 `cur` 的节点值。

    - 如果 `sorted_list.val <= cur.val`，说明 `cur` 应该插入到 `sorted_list` 之后，则将 `sorted_list` 后移一位。
    - 如果 `sorted_list.val > cur.val`，说明 `cur` 应该插入到 `head` 与 `sorted_list` 之间。则使用 `prev` 从 `head` 开始遍历，直到找到插入 `cur` 的位置的前一个节点位置。然后将 `cur` 插入。

5. 令 `cur = sorted_list.next`，此时 `cur` 为下一个待插入元素。
6. 重复 4、5 步骤，直到 `cur` 遍历结束为空。返回 `dummy_head` 的下一个节点。

## 2. 链表插入排序实现代码

```python
class Solution:
    def insertionSort(self, head: ListNode):
        if not head or not head.next:
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
                prev.next = cur
            cur = sorted_list.next 
        
        return dummy_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.insertionSort(head)
```

## 3. 链表插入排序算法复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(1)$。

## 练习题目

- [链表排序题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)