# [0872. 叶子相似的树](https://leetcode.cn/problems/leaf-similar-trees/)

- 标签：树、深度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0872. 叶子相似的树 - 力扣](https://leetcode.cn/problems/leaf-similar-trees/)

## 题目大意

将一棵二叉树树上所有的叶子，按照从左到右的顺序排列起来就形成了一个「叶值序列」。如果两棵二叉树的叶值序列是相同的，我们就认为它们是叶相似的。

现在给定两棵二叉树的根节点 `root1`、`root2`。如果两棵二叉是叶相似的，则返回 `True`，否则返回 `False`。

## 解题思路

分别 DFS 遍历两棵树，得到对应的叶值序列，判断两个叶值序列是否相等。

## 代码

```python
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode, res: List[int]):
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)

        res1 = []
        dfs(root1, res1)
        res2 = []
        dfs(root2, res2)
        return res1 == res2
```

