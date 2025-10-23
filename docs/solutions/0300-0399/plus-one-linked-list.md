# [0369. 给单链表加一](https://leetcode.cn/problems/plus-one-linked-list/)

- 标签：链表、数学
- 难度：中等

## 题目链接

- [0369. 给单链表加一 - 力扣](https://leetcode.cn/problems/plus-one-linked-list/)

## 题目大意

**描述**：

给定一个用链表表示的非负整数。

**要求**：

将这个整数再加上 $1$。

**说明**：

- 这些数字的存储是这样的：最高位有效的数字位于链表的首位 $head$。
- 链表中的节点数在 $[1, 10^{3}]$ 的范围内。
- $0 \le Node.val \le 9$。
- 由链表表示的数字不包含前导零，除了零本身。

**示例**：

- 示例 1：

```python
输入: head = [1,2,3]
输出: [1,2,4]
```

- 示例 2：

```python
输入: head = [0]
输出: [1]
```

## 解题思路

### 思路 1：递归 + 进位处理

使用递归的方式从链表末尾开始处理，模拟加 $1$ 的进位过程。从最后一个节点开始，如果当前节点值为 $9$，则需要进位，将当前节点设为 $0$ 并继续向前处理；否则直接加 $1$ 并返回。

具体步骤：

1. **递归终止条件**：当到达链表末尾（$head$ 为 $None$）时，返回进位标志 $1$。

2. **递归处理**：
   - 递归处理下一个节点，得到进位标志 $carry$。
   - 如果 $carry = 1$：
     - 如果当前节点值为 $9$，则设为 $0$，继续向前进位。
     - 否则当前节点值加 $1$，进位结束。
   - 如果 $carry = 0$，则不需要处理，直接返回。

3. **处理最高位进位**：如果最高位也需要进位（即原数字全为 $9$），则创建新节点作为新的头节点。

### 思路 1：代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            """递归处理链表加 1，返回是否需要进位"""
            if not node:
                # 到达链表末尾，返回进位 1
                return 1
            
            # 递归处理下一个节点
            carry = dfs(node.next)
            
            if carry == 1:
                if node.val == 9:
                    # 当前节点为 9，需要进位
                    node.val = 0
                    return 1
                else:
                    # 当前节点不为 9，直接加 1
                    node.val += 1
                    return 0
            
            # 不需要进位
            return 0
        
        # 递归处理整个链表
        carry = dfs(head)
        
        # 如果最高位也需要进位，创建新的头节点
        if carry == 1:
            new_head = ListNode(1)
            new_head.next = head
            return new_head
        
        return head
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是链表的长度。需要遍历链表一次。
- **空间复杂度**：$O(n)$，其中 $n$ 是链表的长度。递归调用栈的深度为链表长度。
