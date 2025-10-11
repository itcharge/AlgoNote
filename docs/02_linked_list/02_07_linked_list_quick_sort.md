## 1. 链表快速排序基本思想

> **链表快速排序基本思想**：
> 
> 通过选择基准值（pivot）将链表分割为两部分，使得左部分所有节点的值都小于基准值，右部分所有节点的值都大于等于基准值，然后递归地对左右两部分进行排序，最终实现整个链表的有序排列。

链表快速排序的核心思想是**分治策略**，具体算法步骤如下：

1. **选择基准值**：从链表中选择一个基准值 `pivot`，通常选择头节点的值作为基准值。
2. **分割链表**：通过快慢指针（`node_i`、`node_j`）遍历链表，将链表分割为两部分：
   - 左部分：所有节点值都小于基准值
   - 右部分：所有节点值都大于等于基准值
3. **递归排序**：对分割后的左右两部分分别递归执行快速排序
4. **合并结果**：当子链表长度小于等于1时，递归结束，最终得到有序链表

## 2. 链表快速排序实现代码

```python
class Solution:
    def partition(self, left: ListNode, right: ListNode):
        """
        分割函数：将链表分割为两部分
        left: 左边界节点（包含）
        right: 右边界节点（不包含）
        返回：基准值节点的最终位置
        """
        # 边界条件：区间没有元素或者只有一个元素，直接返回第一个节点
        if left == right or left.next == right:
            return left
        
        # 选择头节点为基准节点
        pivot = left.val
        
        # 使用快慢指针进行分割
        # node_i: 指向小于基准值的最后一个节点
        # node_j: 遍历指针，寻找小于基准值的节点
        node_i, node_j = left, left.next
        
        while node_j != right:
            # 发现一个小于基准值的元素
            if node_j.val < pivot:
                # 将 node_i 向右移动一位
                node_i = node_i.next
                # 交换 node_i 和 node_j 的值，保证 node_i 之前的节点都小于基准值
                node_i.val, node_j.val = node_j.val, node_i.val
            node_j = node_j.next
        
        # 将基准节点放到正确位置上（node_i 位置）
        node_i.val, left.val = left.val, node_i.val
        return node_i
        
    def quickSort(self, left: ListNode, right: ListNode):
        """
        快速排序主函数
        left: 左边界节点（包含）
        right: 右边界节点（不包含）
        """
        # 递归终止条件：区间长度小于等于 1
        if left == right or left.next == right:
            return left
        
        # 分割链表，获取基准值位置
        pi = self.partition(left, right)
        
        # 递归排序左半部分
        self.quickSort(left, pi)
        # 递归排序右半部分
        self.quickSort(pi.next, right)
        
        return left

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        链表排序入口函数
        """
        # 边界条件检查
        if not head or not head.next:
            return head
        
        # 调用快速排序
        return self.quickSort(head, None)
```

## 3. 链表快速排序算法复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n \log n)$ | 每次等分为两半，递归层数约 $\log n$ |
| **最坏时间复杂度** | $O(n^2)$ | 已有序/逆序或重复值多，划分极端不均 |
| **平均时间复杂度** | $O(n \log n)$ | 期望情况下划分较均匀 |
| **空间复杂度** | $O(\log n)$ | 递归调用栈深度（原地就地分区，无额外数组） |
| **稳定性** | 不稳定 | 相等节点的相对顺序可能改变 |

## 4. 总结

链表快速排序通过分治与就地分区实现排序，平均效率高，但极端情况下退化明显，且不稳定。

- **优点**：平均时间复杂度 $O(n\log n)$，就地分区、空间开销小
- **缺点**：最坏时间复杂度 $O(n^2)$，不稳定，对枢轴选择敏感

## 练习题目

- [0148. 排序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/sort-list.md)（链表快速排序会超时，仅做练习）

- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)