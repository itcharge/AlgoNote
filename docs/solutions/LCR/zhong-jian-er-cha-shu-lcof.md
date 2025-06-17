# [LCR 124. 推理二叉树](https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/)

- 标签：树、数组、哈希表、分治、二叉树
- 难度：中等

## 题目链接

- [LCR 124. 推理二叉树 - 力扣](https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/)

## 题目大意

给定一棵二叉树的前序遍历结果和中序遍历结果。

要求：构建该二叉树，并返回其根节点。假设树中没有重复的元素。

## 解题思路

前序遍历的顺序是：根 -> 左 -> 右。中序遍历的顺序是：左 -> 根 -> 右。根据前序遍历的顺序，可以找到根节点位置。然后在中序遍历的结果中可以找到对应的根节点位置，就可以从根节点位置将二叉树分割成左子树、右子树。同时能得到左右子树的节点个数。此时构建当前节点，并递归建立左右子树，在左右子树对应位置继续递归遍历进行上述步骤，直到节点为空，具体操作步骤如下：

- 从前序遍历顺序中当前根节点的位置在 `postorder[0]`。
- 通过在中序遍历中查找上一步根节点对应的位置 `inorder[k]`，从而将二叉树的左右子树分隔开，并得到左右子树节点的个数。
- 从上一步得到的左右子树个数将前序遍历结果中的左右子树分开。
- 构建当前节点，并递归建立左右子树，在左右子树对应位置继续递归遍历并执行上述三步，直到节点为空。

## 代码

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def createTree(preorder, inorder, n):
            if n == 0:
                return None
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            node = TreeNode(inorder[k])
            node.left = createTree(preorder[1: k + 1], inorder[0: k], k)
            node.right = createTree(preorder[k + 1:], inorder[k + 1:], n - k - 1)
            return node

        return createTree(preorder, inorder, len(inorder))
```

