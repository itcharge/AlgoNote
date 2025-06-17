# [1008. 前序遍历构造二叉搜索树](https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/)

- 标签：栈、树、二叉搜索树、数组、二叉树、单调栈
- 难度：中等

## 题目链接

- [1008. 前序遍历构造二叉搜索树 - 力扣](https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/)

## 题目大意

给定一棵二叉搜索树的前序遍历结果 `preorder`。

要求：返回与给定前序遍历 `preorder` 相匹配的二叉搜索树的根节点。题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。

## 解题思路

二叉搜索树的中序遍历是升序序列。而题目又给了我们二叉搜索树的前序遍历，那么通过对前序遍历结果的排序，我们也可以得到二叉搜索树的中序遍历结果。这样就能根据二叉树的前序、中序遍历序列构造二叉树了。就变成了了「[0105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)」题。

此外，我们还有另一种方法求解。前序遍历的顺序是：根 -> 左 -> 右。并且在二叉搜索树中，左子树的值小于根节点，右子树的值大于根节点。

根据以上性质，我们可以递归地构造二叉搜索树。

首先，以前序遍历的开始位置元素构造为根节点。从开始位置的下一个位置开始，找到序列中第一个大于等于根节点值的位置 `mid`。该位置左侧的值都小于根节点，右侧的值都大于等于根节点。以此位置为中心，递归的构造左子树和右子树。

最后再将根节点进行返回。

## 代码

```python
class Solution:
    def buildTree(self, preorder, start, end):
        if start == end:
            return None
        root = preorder[start]
        mid = start + 1
        while mid < end and preorder[mid] < root:
            mid += 1
        node = TreeNode(root)
        node.left = self.buildTree(preorder, start + 1, mid)
        node.right = self.buildTree(preorder, mid, end)
        return node

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.buildTree(preorder, 0, len(preorder))
```

