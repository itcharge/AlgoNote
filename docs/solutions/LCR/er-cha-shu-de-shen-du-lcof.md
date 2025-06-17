# [LCR 175. 计算二叉树的深度](https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [LCR 175. 计算二叉树的深度 - 力扣](https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/)

## 题目大意

给定一个二叉树的根节点 `root`。

要求：找出树的深度。

- 深度：从根节点到叶节点一次经过的节点形成一条路径，最长路径的长度为树的深度。

## 解题思路

递归遍历，先递归遍历左右子树，返回左右子树的高度，则当前节点的高度为左右子树最大深度 + 1。即 `max(left_height, right_height) + 1`。

## 代码

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
```

