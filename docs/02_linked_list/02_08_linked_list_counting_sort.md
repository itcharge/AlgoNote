## 1. 链表计数排序算法描述

    1. 使用 `cur` 指针遍历一遍链表。找出链表中最大值 `list_max` 和最小值 `list_min`。
    2. 使用数组 `counts` 存储节点出现次数。
    3. 再次使用 `cur` 指针遍历一遍链表。将链表中每个值为 `cur.val` 的节点出现次数，存入数组对应第 `cur.val - list_min` 项中。
    4. 反向填充目标链表：
       1. 建立一个哑节点 `dummy_head`，作为链表的头节点。使用 `cur` 指针指向 `dummy_head`。
       2. 从小到大遍历一遍数组 `counts`。对于每个 `counts[i] != 0` 的元素建立一个链节点，值为 `i + list_min`，将其插入到 `cur.next` 上。并向右移动 `cur`。同时 `counts[i] -= 1`。直到 `counts[i] == 0` 后继续向后遍历数组 `counts`。
    5. 将哑节点 `dummy_dead` 的下一个链节点 `dummy_head.next` 作为新链表的头节点返回。

## 2. 链表计数排序代码实现

  ```python
class Solution:
    def countingSort(self, head: ListNode):
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.countingSort(head)
  ```

## 3. 链表计数排序算法复杂度分析

  - **时间复杂度**：$O(n + k)$，其中 $k$ 代表待排序链表中所有元素的值域。
  - **空间复杂度**：$O(k)$。

