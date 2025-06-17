## 1. 链表冒泡排序算法描述

1. 使用三个指针 `node_i`、`node_j` 和 `tail`。其中 `node_i` 用于控制外循环次数，循环次数为链节点个数（链表长度）。`node_j` 和 `tail` 用于控制内循环次数和循环结束位置。
2. 排序开始前，将 `node_i` 、`node_j` 置于头节点位置。`tail` 指向链表末尾，即 `None`。
3. 比较链表中相邻两个元素 `node_j.val` 与 `node_j.next.val` 的值大小，如果 `node_j.val > node_j.next.val`，则值相互交换。否则不发生交换。然后向右移动 `node_j` 指针，直到 `node_j.next == tail` 时停止。
4. 一次循环之后，将 `tail` 移动到 `node_j` 所在位置。相当于 `tail` 向左移动了一位。此时 `tail` 节点右侧为链表中最大的链节点。
5. 然后移动 `node_i` 节点，并将 `node_j` 置于头节点位置。然后重复第 3、4 步操作。
6. 直到 `node_i` 节点移动到链表末尾停止，排序结束。
7. 返回链表的头节点 `head`。

## 2. 链表冒泡排序算法实现代码

```python
class Solution:
    def bubbleSort(self, head: ListNode):
        node_i = head
        tail = None
        # 外层循环次数为 链表节点个数
        while node_i:
            node_j = head
            while node_j and node_j.next != tail:
                if node_j.val > node_j.next.val:
                    # 交换两个节点的值
                    node_j.val, node_j.next.val = node_j.next.val, node_j.val
                node_j = node_j.next
            # 尾指针向前移动 1 位，此时尾指针右侧为排好序的链表
            tail = node_j
            node_i = node_i.next
            
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.bubbleSort(head)
```

## 3. 链表冒泡排序算法复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(1)$。

## 4. 总结

链表冒泡排序使用三个指针进行操作。`node_i` 控制外层循环次数，`node_j` 和 `tail` 控制内层循环。每次比较相邻节点的值，需要交换时就交换。每次内循环结束后，最大的节点会移动到链表末尾。

这个算法的时间复杂度是 $O(n^2)$，因为需要进行两层循环。空间复杂度是 $O(1)$，因为只使用了固定数量的指针变量，没有使用额外空间。

链表冒泡排序适合小规模数据排序。对于大规模数据，其他排序算法可能更高效。实现时需要注意指针移动和节点交换的操作。

## 练习题目

- [链表排序题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)