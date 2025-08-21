

## 1. 链表插入排序基本思想

> **链表插入排序基本思想**：
> 
> 将链表分为已排序部分和未排序部分，逐个将未排序部分的节点插入到已排序部分的正确位置**。

链表插入排序的算法步骤如下：

1. **初始化**：
   - 创建哑节点 `dummy_head`，指向链表头 `head`
   - 设置 `sorted_tail` 为已排序部分的尾节点，初始为 `head`
   - 设置 `cur` 为当前待插入节点，初始为 `head.next`

2. **插入过程**：
   - 如果 `cur.val >= sorted_tail.val`：说明 `cur` 已经在正确位置，将 `sorted_tail` 后移
   - 如果 `cur.val < sorted_tail.val`：需要将 `cur` 插入到已排序部分的合适位置
     - 初始化 `prev = dummy_head`，用于在已排序部分中寻找插入位置
     - 使用 `while prev.next.val <= cur.val` 循环，让 `prev` 移动到第一个大于 `cur.val` 的节点的前一个位置
     - 执行插入操作：
       - `sorted_tail.next = cur.next`：从原位置移除 `cur`
       - `cur.next = prev.next`：`cur` 指向 `prev` 的下一个节点
       - `prev.next = cur`：`prev` 指向 `cur`，完成插入

3. **更新指针**：
   - 更新 `cur` 为下一个待插入节点：`cur = sorted_tail.next`
   - 重复步骤2，直到所有节点都处理完毕

### 关键理解：
- 已排序部分始终是有序的
- 每次插入后，已排序部分长度+1，未排序部分长度-1
- 插入操作需要维护链表的前后连接关系
- **`prev` 的作用**：在已排序部分中寻找插入位置，它始终指向要插入位置的前一个节点
- **`prev` 的移动规律**：通过 `prev.next.val <= cur.val` 的条件，`prev` 会移动到第一个大于 `cur.val` 的节点的前一个位置

## 2. 链表插入排序实现代码

```python
class Solution:
    def insertionSort(self, head: ListNode):
        if not head or not head.next:
            return head
        
        # 创建哑节点，简化边界情况处理
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        # sorted_tail: 已排序部分的尾节点
        # cur: 当前待插入的节点
        sorted_tail = head
        cur = head.next 
        
        while cur:
            if sorted_tail.val <= cur.val:
                # cur 已经在正确位置，扩展已排序部分
                sorted_tail = sorted_tail.next 
            else:
                # 需要插入 cur 到已排序部分的合适位置
                prev = dummy_head
                # 找到插入位置：第一个大于 cur.val 的节点的前一个位置
                while prev.next.val <= cur.val:
                    prev = prev.next
                
                # 执行插入操作
                sorted_tail.next = cur.next  # 从原位置移除 cur
                cur.next = prev.next         # cur 指向下一个节点
                prev.next = cur              # 前一个节点指向 cur
            
            # 移动到下一个待插入节点
            cur = sorted_tail.next 
        
        return dummy_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.insertionSort(head)
```

## 3. 链表插入排序算法复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n)$ | 链表基本有序，仅线性扫描与少量移动 |
| **最坏时间复杂度** | $O(n^2)$ | 链表逆序，每次插入需线性查找插入位置 |
| **平均时间复杂度** | $O(n^2)$ | 一般情况下多次线性插入 |
| **空间复杂度** | $O(1)$ | 原地排序，仅使用常数个指针变量 |
| **稳定性** | ✅ 稳定 | 相等节点的相对次序保持不变 |

**适用场景**：
- 链表长度较小（通常 < 1000）
- 链表基本有序的情况
- 需要稳定排序的场景
- 作为教学或理解插入排序原理的练习

## 4. 总结

链表插入排序通过将未排序节点插入到已排序部分的正确位置完成排序。对近乎有序的链表表现较好，但总体效率不高。

**优点**：实现简单，稳定排序，空间复杂度低，适合近乎有序数据
**缺点**：平均/最坏时间复杂度高，不适合大规模数据

## 练习题目

- [0148. 排序链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/sort-list.md)(链表插入排序会超时，仅做练习)
- [0147. 对链表进行插入排序](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/insertion-sort-list.md)

- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)