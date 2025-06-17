# [LCR 153. 二叉树中和为目标值的路径](https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

- 标签：树、深度优先搜索、回溯、二叉树
- 难度：中等

## 题目链接

- [LCR 153. 二叉树中和为目标值的路径 - 力扣](https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

## 题目大意

给定一棵二叉树的根节点 `root` 和一个整数 `target`。

要求：打印出二叉树中各节点的值的和为 `target` 的所有路径。从根节点开始往下一直到叶节点所经过的节点形成一条路径。

## 解题思路

回溯求解。在回溯的同时，记录下当前路径。同时维护 `target`，每遍历到一个节点，就减去该节点值。如果遇到叶子节点，并且 `target == 0` 时，将当前路径加入答案数组中。然后递归遍历左右子树，并回退当前节点，继续遍历。

## 代码

```python
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(root: TreeNode, target: int):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0:
                res.append(path[:])
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()
        dfs(root, target)
        return res

```

