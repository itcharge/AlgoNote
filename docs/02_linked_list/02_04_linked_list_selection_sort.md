## 1. 链表选择排序算法思想

> **链表选择排序基本思想**：
> 
> 在未排序部分中找到最小元素，然后将其放到已排序部分的末尾。

## 2. 链表选择排序算法步骤

1. **初始化**：使用两个指针 `node_i` 和 `node_j`。`node_i` 指向当前未排序部分的第一个节点，同时也用于控制外循环。

2. **寻找最小值**：在未排序部分中，使用 `min_node` 记录值最小的节点。初始时假设 `node_i` 为最小值节点。

3. **比较交换**：遍历未排序部分，比较每个节点的值。如果发现更小的值，则更新 `min_node`。

4. **交换操作**：一趟排序结束后，如果 `min_node` 不等于 `node_i`，则交换两个节点的值。

5. **移动指针**：将 `node_i` 向右移动一位，继续处理剩余未排序部分。

6. **终止条件**：当 `node_i` 为 `None` 或 `node_i.next` 为 `None` 时，排序完成。

## 3. 链表选择排序实现代码

```python
class Solution:
    def selectionSort(self, head: ListNode):
        node_i = head
        
        # 外层循环：遍历每个节点
        while node_i and node_i.next:
            # 假设当前节点为最小值节点
            min_node = node_i
            node_j = node_i.next
            
            # 内层循环：在未排序部分寻找最小值
            while node_j:
                if node_j.val < min_node.val:
                    min_node = node_j
                node_j = node_j.next
            
            # 如果找到更小的值，则交换
            if node_i != min_node:
                node_i.val, min_node.val = min_node.val, node_i.val
            
            # 移动到下一个节点
            node_i = node_i.next
        
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.selectionSort(head)
```

## 4. 链表选择排序算法复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n^2)$ | 无论初始顺序如何，都需 $O(n^2)$ 次比较 |
| **最坏时间复杂度** | $O(n^2)$ | 无论初始顺序如何，都需 $O(n^2)$ 次比较 |
| **平均时间复杂度** | $O(n^2)$ | 比较次数与数据状态无关 |
| **空间复杂度** | $O(1)$ | 原地排序，仅使用常数额外空间 |
| **稳定性** | 不稳定 | 可能改变相等节点的相对次序 |

**适用场景**：

- **小规模数据**：节点数量较少的场景（如 < 100）
- **对空间复杂度严格**：仅使用常数额外空间的需求
- **交换代价高的场景**：选择排序交换次数少（最多 \(n-1\) 次）


## 5. 总结

链表中的选择排序是一种简单直观的链表排序算法，通过在未排序部分中选择最小节点并将其放到已排序部分的末尾来完成排序。虽然实现简单，但效率较低。

- **优点**：实现简单，空间复杂度低，交换次数少
- **缺点**：时间复杂度高，不稳定，不适合大规模数据

## 练习题目

- [0148. 排序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/sort-list.md)（链表选择排序会超时，仅做练习）

- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)