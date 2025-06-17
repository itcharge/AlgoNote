# [0222. 完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/)

- 标签：树、深度优先搜索、二分查找、二叉树
- 难度：中等

## 题目链接

- [0222. 完全二叉树的节点个数 - 力扣](https://leetcode.cn/problems/count-complete-tree-nodes/)

## 题目大意

给定一棵完全二叉树的根节点 `root`，返回该树的节点个数。

- 完全二叉树：除了最底层节点可能没有填满外，其余各层节点数都达到了最大值，并且最下面一层的节点都集中在盖层最左边的若干位置。若最底层在第 `h` 层，则该层包含 $1 \sim 2^h$ 个节点。

## 解题思路

根据题意可知公式：当前根节点的节点个数 = 左子树节点个数 + 右子树节点个数 + 1。

根据上述公式递归遍历左右子树节点，并返回左右子树节点数 + 1。

## 代码

```python
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

