# [0669. 修剪二叉搜索树](https://leetcode.cn/problems/trim-a-binary-search-tree/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：中等

## 题目链接

- [0669. 修剪二叉搜索树 - 力扣](https://leetcode.cn/problems/trim-a-binary-search-tree/)

## 题目大意

给定一棵二叉搜索树的根节点 `root`，同时给定最小边界 `low` 和最大边界 `high`。通过修建二叉搜索树，使得所有节点值都在 `[low, high]` 中。修剪树不应该改变保留在树中的元素的相对结构（即如果没有移除节点，则该节点的父节点关系、子节点关系都应当保留）。

现在要求返回修建过后的二叉树的根节点。

## 解题思路

递归修剪，函数返回值为修剪之后的树。

- 如果当前根节点为空，则直接返回 None。
- 如果当前根节点的值小于 `low`，则该节点左子树全部都小于最小边界，则删除左子树，然后递归遍历右子树，在右子树中寻找符合条件的节点。
- 如果当前根节点的值大于 `hight`，则该节点右子树全部都大于最大边界，则删除右子树，然后递归遍历左子树，在左子树中寻找符合条件的节点。
- 如果在最小边界和最大边界的区间内，则分别从左右子树寻找符合条件的节点作为根的左右子树。

## 代码

```python
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right
        if root.val > high:
            left = self.trimBST(root.left, low, high)
            return left

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
```

