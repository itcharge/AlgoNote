# [LCR 053. 二叉搜索树中的中序后继](https://leetcode.cn/problems/P5rCT8/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：中等

## 题目链接

- [LCR 053. 二叉搜索树中的中序后继 - 力扣](https://leetcode.cn/problems/P5rCT8/)

## 题目大意

给定一棵二叉搜索树的根节点 `root` 和其中一个节点 `p`。

要求：找到该节点在树中的中序后继，即按照中序遍历的顺序节点 `p` 的下一个节点。

## 解题思路

递归遍历，具体步骤如下：

- 如果 `root.val` 小于等于 `p.val`，则直接从 `root` 的右子树递归查找比 `p.val` 大的节点，从而找到中序后继。
- 如果 `root.val` 大于 `p.val`，则 `root` 有可能是中序后继，也有可能是 `root` 的左子树。则从 `root` 的左子树递归查找更接近（更小的）。如果查找的值为 `None`，则当前 `root` 就是中序后继，否则继续递归查找，从而找到中序后继。

## 代码 

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not p or not root:
            return None

        if root.val <= p.val:
            node = self.inorderSuccessor(root.right, p)
        else:
            node = self.inorderSuccessor(root.left, p)
            if not node:
                node = root
        return node
```

