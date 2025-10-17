# [0099. 恢复二叉搜索树](https://leetcode.cn/problems/recover-binary-search-tree/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：中等

## 题目链接

- [0099. 恢复二叉搜索树 - 力扣](https://leetcode.cn/problems/recover-binary-search-tree/)

## 题目大意

**描述**：

给你二叉搜索树的根节点 $root$，该树中恰好两个节点的值被错误地交换。

**要求**：

请在不改变其结构的情况下，恢复这棵树。

**说明**：

- 树上节点的数目在范围 $[2, 1000]$ 内。
- $-2^{31} \le Node.val \le 2^{31} - 1$。

- 进阶：使用 $O(n)$ 空间复杂度的解法很容易实现。你能想出一个只使用 $O(1)$ 空间的解决方案吗？

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg)

```python
输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg)

```python
输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
```

## 解题思路

### 思路 1：中序遍历 + 数组存储

**核心思想**：

利用二叉搜索树中序遍历得到有序序列的性质，通过中序遍历找到被错误交换的两个节点，然后交换它们的值。

**算法步骤**：

1. **中序遍历**：对二叉搜索树进行中序遍历，将遍历结果存储在数组 $nodes$ 中。
2. **查找错误节点**：遍历数组 $nodes$，找到第一个 $nodes[i] > nodes[i+1]$ 的位置，此时 $nodes[i]$ 是第一个错误节点。
3. **查找第二个错误节点**：继续遍历，找到最后一个 $nodes[j] < nodes[j-1]$ 的位置，此时 $nodes[j]$ 是第二个错误节点。
4. **交换节点值**：交换这两个节点的值。

**关键点**：

- 二叉搜索树的中序遍历结果应该是严格递增的序列。
- 当两个相邻节点被交换时，会出现两个逆序对：$(nodes[i], nodes[i+1])$ 和 $(nodes[j-1], nodes[j])$。
- 第一个错误节点是第一个逆序对中的较大值，第二个错误节点是最后一个逆序对中的较小值。
- 时间复杂度为 $O(n)$，空间复杂度为 $O(n)$。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 存储中序遍历的节点值
        nodes = []
        
        def inorder_traversal(node):
            """中序遍历，将节点值存储到数组中"""
            if not node:
                return
            inorder_traversal(node.left)
            nodes.append(node.val)
            inorder_traversal(node.right)
        
        # 执行中序遍历
        inorder_traversal(root)
        
        # 找到两个错误的位置
        first_error = -1  # 第一个错误节点的索引
        second_error = -1  # 第二个错误节点的索引
        
        # 找到第一个错误位置：nodes[i] > nodes[i+1]
        for i in range(len(nodes) - 1):
            if nodes[i] > nodes[i + 1]:
                first_error = i
                break
        
        # 找到第二个错误位置：从第一个错误位置之后开始找
        for i in range(first_error + 1, len(nodes) - 1):
            if nodes[i] > nodes[i + 1]:
                second_error = i + 1
                break
        
        # 如果只找到一个错误位置，说明两个错误节点相邻
        if second_error == -1:
            second_error = first_error + 1
        
        # 存储需要交换的两个值
        first_val = nodes[first_error]
        second_val = nodes[second_error]
        
        # 再次遍历树，交换这两个值
        def swap_values(node):
            """在树中找到并交换两个错误的值"""
            if not node:
                return
            swap_values(node.left)
            if node.val == first_val:
                node.val = second_val
            elif node.val == second_val:
                node.val = first_val
            swap_values(node.right)
        
        # 执行值交换
        swap_values(root)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树中节点的数量。需要执行两次完整的中序遍历：一次收集节点值，一次交换值。
- **空间复杂度**：$O(n)$，需要存储所有节点的值，以及递归调用栈的空间。
