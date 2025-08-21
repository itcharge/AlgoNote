## 1. 链表归并算法基本思想

> **链表归并排序基本思想**：
> 
> **采用分治策略，将链表递归分割为更小的子链表，然后两两归并得到有序链表**。

链表归并排序的算法步骤如下：


1. **分割阶段**：找到链表的中间节点，将链表从中间断开，并递归进行分割。
    1. 使用快慢指针法，`fast = head.next`、`slow = head`，让 `fast` 每次移动 2 步，`slow` 移动 1 步，当 `fast` 到达链表末尾时，`slow` 即为链表的中间节点。
    2. 从中间位置将链表分为左右两个子链表 `left_head` 和 `right_head`，并从中间位置断开，即 `slow.next = None`。
    3. 对左右两个子链表分别进行递归分割，直到每个子链表中只包含一个节点。
2. **归并阶段**：将递归分割后的子链表进行两两归并，完成一遍归并后每个子链表长度加倍。重复进行归并操作，直到得到完整的排序链表。
    1. 使用哑节点 `dummy_head` 构造一个头节点，并使用 `cur` 指向 `dummy_head` 用于遍历。
    2. 比较两个子链表头节点 `left` 和 `right` 的值大小。将较小的头节点加入到合并后的链表中，并向后移动该链表的头节点指针。
    3. 重复上一步操作，直到其中一个子链表为空。
    4. 将剩余非空的子链表直接连接到合并后的链表末尾。
    5. 返回哑节点的下一个节点 `dummy_head.next` 作为合并后的头节点。

## 2. 链表归并排序实现代码

```python
class Solution:
    def merge(self, left, right):
        # 归并阶段
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
        # 分割阶段
        if not head or not head.next:
            return head
        
        # 快慢指针找到中间节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # 断开左右子链表
        left_head, right_head = head, slow.next 
        slow.next = None
        
        # 归并操作
        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
```

## 3. 链表归并排序算法复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n \log n)$ | 每次二分出约 $\log n$ 层；每层线性合并 $n$ 个节点 |
| **最坏时间复杂度** | $O(n \log n)$ | 任何输入都经历 $\log n$ 层 × 每层 $O(n)$ 合并 |
| **平均时间复杂度** | $O(n \log n)$ | 期望同上：$\log n$ 层 × 每层 $O(n)$ |
| **空间复杂度** | $O(\log n)$ | 递归需要约 $\log n$ 层调用栈（迭代自底向上可降到 $O(1)$） |
| **稳定性** | ✅ 稳定 | 归并时相等元素优先取左侧，原相对顺序保留 |

## 4. 总结

链表归并排序采用分治策略，将链表递归拆分后再两两归并得到有序链表，整体效率高且稳定。

**优点**：时间复杂度 $O(n\log n)$，稳定排序，适合大规模链表；无需随机访问，天然适配链表结构
**缺点**：递归实现需要 $O(\log n)$ 栈空间，实现相对复杂，常数因子较高

## 练习题目

- [0148. 排序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/sort-list.md)
- [0021. 合并两个有序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/merge-two-sorted-lists.md)
- [0023. 合并 K 个升序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/merge-k-sorted-lists.md)

- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)