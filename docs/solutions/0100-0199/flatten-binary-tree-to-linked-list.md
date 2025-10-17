# [0114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

- 标签：栈、树、深度优先搜索、链表、二叉树
- 难度：中等

## 题目链接

- [0114. 二叉树展开为链表 - 力扣](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

## 题目大意

**描述**：

给定二叉树的根结点 $root$。

**要求**：

请你将它展开为一个单链表：

- 展开后的单链表应该同样使用 $TreeNode$，其中 $right$ 子指针指向链表中下一个结点，而左子指针始终为 $null$。
- 展开后的单链表应该与二叉树先序遍历顺序相同。

**说明**：

- 树中结点数在范围 $[0, 2000]$ 内。
- $-10^{3} \le Node.val \le 10^{3}$。

- 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)

```python
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
```

- 示例 2：

```python
输入：root = []
输出：[]
```

## 解题思路

### 思路 1：递归 + 后序遍历

根据题目要求，我们需要将二叉树按照先序遍历的顺序展开为链表。观察先序遍历的特点：

1. 先访问根节点 $root$
2. 再访问左子树 $root.left$
3. 最后访问右子树 $root.right$

我们可以采用递归 + 后序遍历的方式来解决：

1. **递归终止条件**：如果当前节点 $root$ 为空，直接返回。
2. **递归处理**：先递归处理左子树和右子树，得到展开后的左子树和右子树。
3. **重新连接**：
   - 将展开后的左子树连接到当前节点的右子节点位置
   - 将当前节点的左子节点设为 $null$
   - 将展开后的右子树连接到左子树展开链表的末尾

**关键点**：

- 使用后序遍历确保在处理当前节点时，左右子树已经被展开
- 需要找到左子树展开链表的末尾节点，用于连接右子树
- 展开后的链表结构：$root \rightarrow left\_flattened \rightarrow right\_flattened$

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 递归终止条件：空节点直接返回
        if not root:
            return
        
        # 递归处理左右子树
        self.flatten(root.left)
        self.flatten(root.right)
        
        # 保存当前节点的右子树
        right_subtree = root.right
        
        # 将左子树移到右子树位置
        if root.left:
            root.right = root.left
            root.left = None
            
            # 找到左子树展开链表的末尾节点
            current = root.right
            while current.right:
                current = current.right
            
            # 将原右子树连接到左子树展开链表的末尾
            current.right = right_subtree
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数。我们需要访问每个节点一次，并且对于每个节点，我们可能需要遍历其左子树来找到末尾节点，但总体时间复杂度仍然是 $O(n)$。
- **空间复杂度**：$O(h)$，其中 $h$ 是二叉树的高度。递归调用栈的深度等于树的高度，最坏情况下为 $O(n)$（当树为链式结构时）。
