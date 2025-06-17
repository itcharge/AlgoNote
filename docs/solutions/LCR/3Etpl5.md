# [LCR 049. 求根节点到叶节点数字之和](https://leetcode.cn/problems/3Etpl5/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [LCR 049. 求根节点到叶节点数字之和 - 力扣](https://leetcode.cn/problems/3Etpl5/)

## 题目大意

给定一个二叉树的根节点 `root`，树中每个节点都存放有一个 `0` 到 `9` 之间的数字。每条从根节点到叶节点的路径都代表一个数字。例如，从根节点到叶节点的路径是 `1` -> `2` -> `3`，表示数字 `123`。

要求：计算从根节点到叶节点生成的所有数字的和。

## 解题思路

使用深度优先搜索，记录下路径上所有节点构成的数字，使用 `pretotal` 保存下当前路径上构成的数字。如果遇到叶节点直接返回当前数字，否则递归遍历左右子树，并累加对应结果。

## 代码

```python
class Solution:
    def dfs(self, root, pretotal):
        if not root:
            return 0
        total = pretotal * 10 + root.val
        if not root.left and not root.right:
            return total
        return self.dfs(root.left, total) + self.dfs(root.right, total)

    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
```

