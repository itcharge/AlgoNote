# [0617. 合并二叉树](https://leetcode.cn/problems/merge-two-binary-trees/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0617. 合并二叉树 - 力扣](https://leetcode.cn/problems/merge-two-binary-trees/)

## 题目大意

给定两个二叉树，将两个二叉树合并成一个新的二叉树。合并规则如下：

- 如果两个二叉树对应节点重叠，则将两个节点的值相加并作为新的二叉树节点。
- 如果两个二叉树对应节点其中一个为空，另一个不为空，则将不为空的节点左心新的二叉树节点。

最终返回新的二叉树的根节点。

## 解题思路

利用前序遍历二叉树，并按照规则递归建立二叉树。将其对应节点值相加或者取其中不为空的节点做为新节点。

## 代码

```python
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged

```

