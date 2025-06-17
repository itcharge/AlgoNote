# [0257. 二叉树的所有路径](https://leetcode.cn/problems/binary-tree-paths/)

- 标签：树、深度优先搜索、字符串、回溯、二叉树
- 难度：简单

## 题目链接

- [0257. 二叉树的所有路径 - 力扣](https://leetcode.cn/problems/binary-tree-paths/)

## 题目大意

给定一个二叉树，返回所有从根节点到叶子节点的路径。

## 解题思路

深度优先搜索。在递归遍历时，需考虑当前节点和左右孩子节点。

- 如果当前节点不是叶子节点，则当前拼接路径中加入该点，并继续递归遍历。
- 如果当前节点是叶子节点，则当前拼接路径中加入该点，并将当前路径加入答案数组。

## 代码

```python
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def dfs(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                res.append(path)
            elif not root.right:
                dfs(root.left, path + "->")
            elif not root.left:
                dfs(root.right, path + "->")
            else:
                dfs(root.left, path + "->")
                dfs(root.right, path + "->")
        dfs(root, "")
        return res
```

