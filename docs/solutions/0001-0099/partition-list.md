# [0086. 分隔链表](https://leetcode.cn/problems/partition-list/)

- 标签：链表、双指针
- 难度：中等

## 题目链接

- [0086. 分隔链表 - 力扣](https://leetcode.cn/problems/partition-list/)

## 题目大意

**描述**：

给定一个链表的头节点 $head$ 和一个特定值 $x$。

**要求**：

对链表进行分隔，使得所有「小于 $x$ 的节点」都出现在「大于或等于 $x$ 的节点」之前。 

**说明**：

- 链表中节点的数目在范围 [0, 200] 内。
- $-100 \le Node.val \le 100$。
- $-200 \le x \le 200$。
- 你应当保留两个分区中每个节点的初始相对位置。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)

```python
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
```

- 示例 2：

```python
输入：head = [2,1], x = 2
输出：[1,2]
```

## 解题思路

### 思路 1：双指针 + 虚拟头节点

**核心思想**：

使用两个虚拟头节点分别构建小于x的链表和大于等于x的链表，然后遍历原链表，根据节点值的大小分别连接到对应的链表中，最后将两个链表合并。

**算法步骤**：

1. **创建虚拟头节点**：创建两个虚拟头节点 $small\_dummy$ 和 $large\_dummy$，分别用于构建小于x和大于等于 $x$ 的链表。
2. **创建指针**：为两个链表分别创建尾指针 $small\_tail$ 和 $large\_tail$
3. **遍历原链表**：从头节点开始遍历原链表。
4. **分类连接**：
   - 如果当前节点值 < x，将其连接到 $small\_tail$ 后面，并更新 $small\_tail$。
   - 如果当前节点值 >= x，将其连接到 $large\_tail$ 后面，并更新 $large\_tail$。
5. **合并链表**：将 $small\_tail$ 的 $next$ 指向 $large\_dummy.next$，将 $large\_tail$ 的 $next$ 设为 $None$。
6. **返回结果**：返回 $small\_dummy.next$。

**关键点**：

- 使用虚拟头节点简化边界处理。
- 保持原链表中节点的相对位置。
- 最后需要将 $large\_tail.next$ 设为 $None$，避免形成环。

### 思路 1：代码

```python
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 创建两个虚拟头节点
        small_dummy = ListNode(0)  # 小于x的链表虚拟头
        large_dummy = ListNode(0)  # 大于等于x的链表虚拟头
        
        # 创建两个尾指针
        small_tail = small_dummy
        large_tail = large_dummy
        
        # 遍历原链表
        current = head
        while current:
            if current.val < x:
                # 小于x的节点连接到small链表
                small_tail.next = current
                small_tail = small_tail.next
            else:
                # 大于等于x的节点连接到large链表
                large_tail.next = current
                large_tail = large_tail.next
            
            # 移动到下一个节点
            current = current.next
        
        # 合并两个链表
        small_tail.next = large_dummy.next  # 连接两个链表
        large_tail.next = None  # 避免形成环
        
        # 返回结果
        return small_dummy.next
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是链表的长度。需要遍历链表一次，每个节点只访问一次。
- **空间复杂度**：$O(1)$，只使用了常数个额外的指针变量，没有使用额外的数据结构。
