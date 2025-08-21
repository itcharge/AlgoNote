## 1. 链表基数排序算法思想

> **基数排序算法思想**：
> 
> 从最低位（个位）开始，按照每一位的数字将节点分配到对应的桶中，然后按顺序重新连接


## 2. 链表基数排序算法步骤

1. **确定最大位数**：遍历链表找出最大数字的位数。
2. **按位排序**：从个位开始，依次处理每一位。
3. **分配桶**：根据当前位的数字（0-9）将节点分配到 10 个桶中。
4. **重新连接**：按桶的顺序重新连接链表。
5. **重复处理**：处理完所有位后完成排序。

## 3. 链表基数排序代码实现

```python
class Solution:
    def radixSort(self, head: ListNode):       
        # 1. 计算最大数字的位数
        size = 0
        cur = head
        while cur:
            val_len = len(str(cur.val))
            size = max(size, val_len)
            cur = cur.next
        
        # 2. 从个位到最高位依次排序
        for i in range(size):
            # 创建 10 个桶（对应数字 0-9）
            buckets = [[] for _ in range(10)]
            cur = head
            
            # 3. 按当前位数字分配到对应桶
            while cur:
                # 获取第 i 位数字：先除以 10^i，再对 10 取余
                digit = (cur.val // (10 ** i)) % 10
                buckets[digit].append(cur.val)
                cur = cur.next
            
            # 4. 按桶的顺序重新构建链表
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

## 4. 链表基数排序算法分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n \times k)$ | 每一位都需遍历所有节点，总共 $k$ 位，每位操作 $O(n)$，整体 $O(nk)$ |
| **最坏时间复杂度** | $O(n \times k)$ | 同上；与初始顺序无关 |
| **平均时间复杂度** | $O(n \times k)$ | 同上；$n$ 为节点数，$k$ 为最大位数 |
| **空间复杂度** | $O(n + k)$ | 需要 $n$ 个临时节点/数组及 $k$ 个桶 |
| **稳定性** | ✅ 稳定 | 按桶顺序收集，保持相等值相对次序 |

## 5. 总结

链表基数排序按位进行「分桶 + 收集」，在位数较小、整数键的场景下效率稳定。

**优点**：时间复杂度与数据有序度无关，稳定排序，适合固定位数整数
**缺点**：空间开销较高，仅适用于整数或可映射到位的键

## 练习题目

- [链表排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)