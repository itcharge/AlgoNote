## 1. 链表基数排序算法描述

1. 使用 `cur` 指针遍历链表，获取节点值位数最长的位数 `size`。
2. 从个位到高位遍历位数。因为 `0` ~ `9` 共有 `10` 位数字，所以建立 `10` 个桶。
3. 以每个节点对应位数上的数字为索引，将节点值放入到对应桶中。
4. 建立一个哑节点 `dummy_head`，作为链表的头节点。使用 `cur` 指针指向 `dummy_head`。
5. 将桶中元素依次取出，并根据元素值建立链表节点，并插入到新的链表后面。从而生成新的链表。
6. 之后依次以十位，百位，…，直到最大值元素的最高位处值为索引，放入到对应桶中，并生成新的链表，最终完成排序。
7. 将哑节点 `dummy_dead` 的下一个链节点 `dummy_head.next` 作为新链表的头节点返回。

## 2. 链表基数排序代码实现

```python
class Solution:
    def radixSort(self, head: ListNode):       
        # 计算位数最长的位数
        size = 0
        cur = head
        while cur:
            val_len = len(str(cur.val))
            if val_len > size:
                size = val_len
            cur = cur.next
        
        # 从个位到高位遍历位数
        for i in range(size):
            buckets = [[] for _ in range(10)]
            cur = head
            while cur:
                # 以每个节点对应位数上的数字为索引，将节点值放入到对应桶中
                buckets[cur.val // (10 ** i) % 10].append(cur.val)
                cur = cur.next
            
            # 生成新的链表
            dummy_head = ListNode(-1)
            cur = dummy_head
            for bucket in buckets:
                for num in bucket:
                    cur.next = ListNode(num)
                    cur = cur.next
            head = dummy_head.next
            
        return head
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.radixSort(head)
```

## 3. 链表基数排序算法复杂度分析

- **时间复杂度**：$O(n \times k)$。其中 $n$ 是待排序元素的个数，$k$ 是数字位数。$k$ 的大小取决于数字位的选择（十进制位、二进制位）和待排序元素所属数据类型全集的大小。
- **空间复杂度**：$O(n + k)$。

## 练习题目

- [链表排序题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)