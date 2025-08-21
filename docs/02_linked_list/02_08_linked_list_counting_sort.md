## 1. 链表计数排序基本思想

> **计数排序（Counting Sort）基本思想**：
> 
> 统计每个元素在序列中出现的次数，然后根据统计结果将元素放回正确的位置。

对于链表结构，计数排序的基本思想是：
1. **统计阶段**：遍历链表，统计每个数值出现的次数
2. **重构阶段**：根据统计结果，重新构建有序链表



## 2. 链表计数排序算法步骤


1. **初始化阶段**
   - 使用 `cur` 指针遍历一遍链表
   - 找出链表中最大值 `list_max` 和最小值 `list_min`
   - 计算数值范围：`size = list_max - list_min + 1`

2. **计数统计阶段**
   - 创建大小为 `size` 的计数数组 `counts`，初始化为 0
   - 再次遍历链表，统计每个数值出现的次数
   - 将计数结果存储在 `counts[cur.val - list_min]` 中

3. **重构链表阶段**
   - 建立哑节点 `dummy_head` 作为新链表的头节点
   - 使用 `cur` 指针指向 `dummy_head`
   - 从小到大遍历计数数组 `counts`
   - 对于每个非零计数，创建相应数量的节点，值为 `i + list_min`
   - 将新节点插入到当前指针位置，并移动指针


## 3. 链表计数排序代码实现

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def countingSort(self, head: ListNode) -> ListNode:
        # 边界条件检查
        if not head or not head.next:
            return head
        
        # 步骤1: 找出链表中最大值和最小值
        list_min, list_max = float('inf'), float('-inf')
        cur = head
        while cur:
            if cur.val < list_min:
                list_min = cur.val
            if cur.val > list_max:
                list_max = cur.val
            cur = cur.next
        
        # 计算数值范围
        size = list_max - list_min + 1
        
        # 步骤2: 创建计数数组并统计每个数值的出现次数
        counts = [0 for _ in range(size)]
        cur = head
        while cur:
            # 将数值映射到计数数组的索引
            index = cur.val - list_min
            counts[index] += 1
            cur = cur.next
        
        # 步骤3: 重构有序链表
        dummy_head = ListNode(-1)  # 哑节点，简化头节点操作
        cur = dummy_head
        
        # 遍历计数数组，按顺序重构链表
        for i in range(size):
            # 对于每个非零计数，创建相应数量的节点
            while counts[i] > 0:
                # 创建新节点，值为 i + list_min
                new_node = ListNode(i + list_min)
                cur.next = new_node
                cur = cur.next
                counts[i] -= 1
        
        return dummy_head.next

    def sortList(self, head: ListNode) -> ListNode:
        """
        排序链表的主函数
        
        Args:
            head: 待排序链表的头节点
            
        Returns:
            排序后的链表头节点
        """
        return self.countingSort(head)
```

## 4. 链表计数排序算法分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n + k)$ | 遍历链表 n 次 + 遍历计数数组 k 次 |
| **最坏时间复杂度** | $O(n + k)$ | 与初始顺序无关，始终为 n + k |
| **平均时间复杂度** | $O(n + k)$ | 其中 n 为链表长度，k 为值域大小（max - min + 1） |
| **空间复杂度** | $O(k)$ | 需要大小为 k 的计数数组 |
| **稳定性** | ✅ 稳定 | 重构按数值顺序写回，保留相对次序 |

## 5. 总结

链表计数排序通过「统计次数 + 重构链表」完成排序，在值域小且为整数的场景下接近线性时间。

**优点**：时间近线性（当 k 较小）、实现简单、稳定排序
**缺点**：额外空间 $O(k)$，对值域敏感，不适合大值域或稀疏分布

## 练习题目

- [0148. 排序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/sort-list.md)

- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)
