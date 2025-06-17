# [面试题 04.05. 合法二叉搜索树](https://leetcode.cn/problems/legal-binary-search-tree-lcci/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：中等

## 题目链接

- [面试题 04.05. 合法二叉搜索树 - 力扣](https://leetcode.cn/problems/legal-binary-search-tree-lcci/)

## 题目大意

给定一个二叉树的根节点 `root`。

要求：检查该二叉树是否为二叉搜索树。

二叉搜索树特征：

- 节点的左子树只包含小于当前节点的数。
- 节点的右子树只包含大于当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

## 解题思路

根据题意进行递归遍历即可。前序、中序、后序遍历都可以。

以前序遍历为例，递归函数为：`preorderTraversal(root, min_v, max_v)`

前序遍历时，先判断根节点的值是否在 `(min_v, max_v)` 之间。如果不在则直接返回 `False`。在区间内，则继续递归检测左右子树是否满足，都满足才是一棵二叉搜索树。

递归遍历左子树的时候，要将上界 `max_v` 改为左子树的根节点值，因为左子树上所有节点的值均小于根节点的值。同理，遍历右子树的时候，要将下界 `min_v` 改为右子树的根节点值，因为右子树上所有节点的值均大于根节点。

## 代码

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def preorderTraversal(root, min_v, max_v):
            if root == None:
                return True
            if root.val >= max_v or root.val <= min_v:
                return False
            return preorderTraversal(root.left, min_v, root.val) and preorderTraversal(root.right, root.val, max_v)

        return preorderTraversal(root, float('-inf'), float('inf'))
```

