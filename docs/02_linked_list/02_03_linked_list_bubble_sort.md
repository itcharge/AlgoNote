## 1. 链表冒泡排序算法思想

> **链表冒泡排序基本思想**：
> 
> **通过相邻节点比较和交换，将最大值逐步「冒泡」到链表末尾**。

与数组冒泡排序类似，但需要处理链表的指针操作。

## 2. 链表冒泡排序算法步骤

链表冒泡排序的算法步骤如下：

1. **外层循环**：控制排序轮数，每轮将当前最大值「冒泡」到末尾
2. **内层循环**：比较相邻节点，必要时交换值
3. **尾指针优化**：每轮结束后，末尾已排序部分不再参与比较

```
初始状态：head → 4 → 2 → 1 → 3 → null
         ↑
       node_i, node_j

第1轮内循环：
- 比较 4 和 2：4 > 2，交换 → 2 → 4 → 1 → 3 → null
- 比较 4 和 1：4 > 1，交换 → 2 → 1 → 4 → 3 → null  
- 比较 4 和 3：4 > 3，交换 → 2 → 1 → 3 → 4 → null

第1轮结束：tail 指向 4，4 已排好序
第2轮内循环：只在 2 → 1 → 3 范围内比较
...
```

## 3. 链表冒泡排序实现代码

```python
class Solution:
    def bubbleSort(self, head: ListNode):
        if not head or not head.next:
            return head
            
        # 外层循环：控制排序轮数
        node_i = head
        tail = None  # 尾指针，右侧为已排序部分
        
        while node_i:
            node_j = head  # 内层循环指针
            
            # 内层循环：比较相邻节点
            while node_j and node_j.next != tail:
                if node_j.val > node_j.next.val:
                    # 交换相邻节点的值
                    node_j.val, node_j.next.val = node_j.next.val, node_j.val
                node_j = node_j.next
            
            # 更新尾指针，右侧已排好序
            tail = node_j
            node_i = node_i.next
            
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.bubbleSort(head)
```

## 4. 链表冒泡排序算法分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n)$ | 链表已有序，配合「提前终止」优化仅需一趟 |
| **最坏时间复杂度** | $O(n^2)$ | 链表逆序，多轮遍历与相邻节点交换 |
| **平均时间复杂度** | $O(n^2)$ | 一般情况下需要二重循环比较交换 |
| **空间复杂度** | $O(1)$ | 原地排序，仅使用常数个指针变量 |
| **稳定性** | 稳定 | 相等元素的相对次序保持不变 |


**适用场景**：

- **小规模数据**：节点数量 < 100
- **教学演示**：理解排序算法原理
- **特殊要求**：需要稳定排序且空间受限

## 5. 总结

链表中的冒泡排序是最简单的链表排序之一，通过相邻节点比较交换实现排序。虽然实现简单，但效率较低。

- **优点**：实现简单，稳定排序，空间复杂度低
- **缺点**：时间复杂度高，交换次数多

## 练习题目

- [0148. 排序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/sort-list.md) (链表冒泡排序会超时，仅做练习)
- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)