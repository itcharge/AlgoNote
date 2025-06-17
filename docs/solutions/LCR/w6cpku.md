# [LCR 054. 把二叉搜索树转换为累加树](https://leetcode.cn/problems/w6cpku/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：中等

## 题目链接

- [LCR 054. 把二叉搜索树转换为累加树 - 力扣](https://leetcode.cn/problems/w6cpku/)

## 题目大意

给定一棵二叉搜索树（BST）的根节点 `root`，且二叉搜索树的节点值各不相同。要求将其转化为「累加树」，使其每个节点 `node` 的新值等于原树中大于或等于 `node.val` 的值之和。

二叉搜索树的定义：

- 若左子树不为空，则左子树上所有节点值均小于它的根节点值；
- 若右子树不为空，则右子树上所有节点值均大于它的根节点值；
- 任意节点的左、右子树也分别为二叉搜索树。

## 解题思路

题目要求将每个节点的值修改为原来的节点值加上大于它的节点值之和。已知二叉搜索树的中序遍历可以得到一个升序数组。

题目就可以变为：修改升序数组中每个节点值为末尾元素累加和。由于末尾元素累加和的求和过程和遍历顺序相反，所以我们可以考虑换种思路。

二叉搜索树的中序遍历顺序为：左 -> 根 -> 右，从而可以得到一个升序数组，那么我们将左右反着遍历，即顺序为：右 -> 根 -> 左，就可以得到一个降序数组，这样就可以在遍历的同时求前缀和。

当然我们在计算前缀和的时候，需要用到前一个节点的值，所以需要用变量 `pre` 存储前一节点的值。

## 代码

```python
class Solution:
    pre = 0

    def createBinaryTree(self, root: TreeNode):
        if not root:
            return
        self.createBinaryTree(root.right)
        root.val += self.pre
        self.pre = root.val
        self.createBinaryTree(root.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.pre = 0
        self.createBinaryTree(root)
        return root
```

