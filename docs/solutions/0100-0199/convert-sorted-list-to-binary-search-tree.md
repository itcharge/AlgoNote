# [0109. 有序链表转换二叉搜索树](https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/)

- 标签：树、二叉搜索树、链表、分治、二叉树
- 难度：中等

## 题目链接

- [0109. 有序链表转换二叉搜索树 - 力扣](https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/)

## 题目大意

**描述**：

给定一个单链表的头节点 $head$，其中的元素按升序排序。

**要求**：

将其转换为平衡二叉搜索树。

**说明**：

- $head$ 中的节点数在 $[0, 2 \times 10^{4}]$ 范围内。
- $-10^{5} \le Node.val \le 10^{5}$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)

```python
输入: head = [-10,-3,0,5,9]
输出: [0,-3,9,-10,null,5]
解释: 一个可能的答案是 [0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
```

- 示例 2：

```python
输入: head = []
输出: []
```

## 解题思路

### 思路 1：分治法 + 快慢指针

由于链表是有序的，我们可以使用分治法来构建平衡二叉搜索树。关键是要找到链表的中间节点作为根节点，然后递归构建左右子树。

**算法步骤**：

1. **找到中间节点**：使用快慢指针找到链表的中间节点 $mid$，将链表分为两部分。
2. **构建根节点**：以中间节点的值创建根节点 $root$。
3. **递归构建左子树**：对中间节点左侧的链表递归构建左子树。
4. **递归构建右子树**：对中间节点右侧的链表递归构建右子树。
5. **返回根节点**：返回构建好的二叉搜索树根节点。

**关键点**：

- 使用快慢指针找到中间节点，时间复杂度为 $O(n)$。
- 需要断开链表，避免在递归过程中重复处理节点。
- 分治法确保左右子树节点数量平衡，从而构建平衡二叉搜索树。

### 思路 1：代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 递归终止条件：空链表
        if not head:
            return None
        
        # 找到中间节点
        mid = self.findMiddle(head)
        
        # 创建根节点
        root = TreeNode(mid.val)
        
        # 如果只有一个节点，直接返回
        if head == mid:
            return root
        
        # 递归构建左子树
        root.left = self.sortedListToBST(head)
        
        # 递归构建右子树
        root.right = self.sortedListToBST(mid.next)
        
        return root
    
    def findMiddle(self, head: ListNode) -> ListNode:
        """
        使用快慢指针找到链表的中间节点
        同时断开链表，避免重复处理
        """
        prev = None  # 慢指针的前一个节点
        slow = head  # 慢指针
        fast = head  # 快指针
        
        # 快指针每次走两步，慢指针每次走一步
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # 断开链表，避免重复处理
        if prev:
            prev.next = None
        
        return slow
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是链表的长度。每次递归都需要 $O(n)$ 时间找到中间节点，递归深度为 $O(\log n)$，所以总时间复杂度为 $O(n \log n)$。
- **空间复杂度**：$O(\log n)$，其中 $n$ 是链表的长度。递归调用栈的深度为 $O(\log n)$。
