# [0404. 左叶子之和](https://leetcode.cn/problems/sum-of-left-leaves/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0404. 左叶子之和 - 力扣](https://leetcode.cn/problems/sum-of-left-leaves/)

## 题目大意

给定一个二叉树，计算所有左叶子之和。

## 解题思路

深度优先搜索递归遍历二叉树，如果当前节点不为空，且左孩子节点不为空，且左孩子节点的左右孩子节点都为空，则该节点的左孩子节点为左叶子节点。将其值累加起来，即为答案。

## 代码

```python
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return None
            if node.left and not node.left.left and not node.left.right:
                self.ans += node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans
```

