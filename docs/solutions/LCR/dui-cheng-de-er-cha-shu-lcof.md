# [LCR 145. 判断对称二叉树](https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [LCR 145. 判断对称二叉树 - 力扣](https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/)

## 题目大意

给定一个二叉树的根节点 `root`。

要求：检查这课二叉树是否是左右对称的。

## 解题思路

递归遍历左右子树， 然后判断当前节点的左右子节点。如果可以直接判断的情况，则跳出递归，直接返回结果。如果无法直接判断结果，则递归检测左右子树的外侧节点是否相等，同理再递归检测左右子树的内侧节点是否相等。

## 代码

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left: TreeNode, right: TreeNode):
        if not left and not right:
            return True
        elif not left and right:
            return False
        elif left and not right:
            return False
        elif left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)
```

