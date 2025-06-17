# [LCR 143. 子结构判断](https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [LCR 143. 子结构判断 - 力扣](https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/)

## 题目大意

给定两棵二叉树的根节点 `A`、`B`。

要求：判断 `B` 是不是 `A` 的子结构。（空树不是任意一棵树的子结构）。

- `B` 是 `A` 的子结构：`A` 中有出现和 `B` 相同的结构和节点值。

## 解题思路

深度优先搜索。

- 先判断特例，如果 `A`、`B` 都为空树，则直接返回 `False`。
- 然后递归判断 `A`、`B` 是否相等。
    - 如果 `A`、`B` 相等，则返回 `True`。
    - 如果 `A`、`B` 不相等，则递归判断 `B` 是否是  `A` 的左子树的子结构，或者 `B` 是否是 `A` 的右子树的子结构，如果有一种满足，则返回 `True`，如果都不满足，则返回 `False`。

递归判断 `A`、`B` 是否相等的具体方法如下：

- 如果 `B` 为空树，则直接返回 `False`，因为空树不是任意一棵树的子结构。
- 如果 `A` 为空树或者 `A` 节点的值不等于 `B` 节点的值，则返回 `False`。
- 如果 `A`、`B` 都不为空，且节点值相同，则递归判断 `A` 的左子树和 `B` 的左子树是否相等，判断 `A` 的右子树和 `B` 的右子树是否相等。如果都相等，则返回 `True`，否则返回 `False`。

## 代码

```python
class Solution:
    def hasSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.hasSubStructure(A.left, B.left) and self.hasSubStructure(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        if self.hasSubStructure(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
```

