## 1. 链表快速排序算法描述

1. 从链表中找到一个基准值 `pivot`，这里以头节点为基准值。
2. 然后通过快慢指针 `node_i`、`node_j` 在链表中移动，使得 `node_i` 之前的节点值都小于基准值，`node_i` 之后的节点值都大于基准值。从而把数组拆分为左右两个部分。
3. 再对左右两个部分分别重复第二步，直到各个部分只有一个节点，则排序结束。

## 2. 链表快速排序实现代码

```python
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
                # 因为 node_i 之前节点都小于基准值，所以先将 node_i 向右移动一位（此时 node_i 节点值大于等于基准节点值）
                node_i = node_i.next
                # 将小于基准值的元素 node_j 与当前 node_i 换位，换位后可以保证 node_i 之前的节点都小于基准节点值
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        return self.quickSort(head, None)
```

## 3. 链表快速排序算法复杂度分析

- **时间复杂度**：$O(n \times \log_2n)$。
- **空间复杂度**：$O(1)$。

## 练习题目

- [链表排序题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)