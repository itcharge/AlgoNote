# [LCR 176. 判断是否为平衡二叉树](https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/)

- 标签：树、深度优先搜索、二叉树
- 难度：简单

## 题目链接

- [LCR 176. 判断是否为平衡二叉树 - 力扣](https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/)

## 题目大意

给定一棵二叉树的根节点 `root`。

要求：判断该树是不是平衡二叉树。如果是平衡二叉树，返回 `True`，否则，返回 `False`。

- 平衡二叉树：任意节点的左右子树深度不超过 `1`。

## 解题思路

递归遍历二叉树。先递归遍历左右子树，判断左右子树是否平衡，再判断以当前节点为根节点的左右子树是否平衡。

如果遍历的子树是平衡的，则返回它的高度，否则返回 `-1`。

只要出现不平衡的子树，则该二叉树一定不是平衡二叉树。

## 代码

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if root == None:
                return False
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
```

