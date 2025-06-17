# [0814. 二叉树剪枝](https://leetcode.cn/problems/binary-tree-pruning/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0814. 二叉树剪枝 - 力扣](https://leetcode.cn/problems/binary-tree-pruning/)

## 题目大意

给定一棵二叉树的根节点 `root`，树的每个节点值要么是 `0`，要么是 `1`。

要求：剪除该二叉树中所有节点值为 `0` 的子树。

- 节点 `node` 的子树为： `node` 本身，以及所有 `node` 的后代。

## 解题思路

定义辅助方法 `containsOnlyZero(root)` 递归判断以 `root` 为根的子树中是否只包含 `0`。如果子树中只包含 `0`，则返回 `True`。如果子树中含有 `1`，则返回 `False`。当 `root` 为空时，也返回 `True`。

然后递归遍历二叉树，判断当前节点 `root` 是否只包含 `0`。如果只包含 `0`，则将其置空，返回 `None`。否则递归遍历左右子树，并设置对应的左右指针。

最后返回根节点 `root`。

## 代码

```python
class Solution:
    def containsOnlyZero(self, root: TreeNode):
        if not root:
            return True
        if root.val == 1:
            return False
        return self.containsOnlyZero(root.left) and self.containsOnlyZero(root.right)

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        if self.containsOnlyZero(root):
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root
```

