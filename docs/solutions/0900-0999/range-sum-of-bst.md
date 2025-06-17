# [0938. 二叉搜索树的范围和](https://leetcode.cn/problems/range-sum-of-bst/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：简单

## 题目链接

- [0938. 二叉搜索树的范围和 - 力扣](https://leetcode.cn/problems/range-sum-of-bst/)

## 题目大意

给定一个二叉搜索树，和一个范围 [low, high]。求范围 [low, high] 之间所有节点的值的和。

## 解题思路

二叉搜索树的定义：

- 若左子树不为空，则左子树上所有节点值均小于它的根节点值；
- 若右子树不为空，则右子树上所有节点值均大于它的根节点值；
- 任意节点的左、右子树也分别为二叉搜索树。

这道题求解 [low, high] 之间所有节点的值的和，需要递归求解。

- 当前节点为 None 时返回 0；
- 当前节点值 val > high 时，则返回左子树之和；
- 当前节点值 val < low 时，则返回右子树之和；
- 当前节点 val <= high，且 val >= low 时，则返回当前节点值 + 左子树之和 + 右子树之和。

## 代码

```python
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
```

