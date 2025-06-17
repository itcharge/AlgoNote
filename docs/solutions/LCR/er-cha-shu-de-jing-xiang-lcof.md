# [LCR 144. 翻转二叉树](https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [LCR 144. 翻转二叉树 - 力扣](https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/)

## 题目大意

给定一个二叉树的根节点 `root`。

要求：将其进行左右翻转。

## 解题思路

从根节点开始遍历，然后从叶子节点向上递归交换左右子树位置。

## 代码

```python
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left = right
        root.right = left
        return root
```

