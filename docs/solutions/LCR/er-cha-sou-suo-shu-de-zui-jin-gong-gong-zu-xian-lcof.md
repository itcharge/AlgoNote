# [LCR 193. 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：简单

## 题目链接

- [LCR 193. 二叉搜索树的最近公共祖先 - 力扣](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

## 题目大意

给定一棵二叉搜索树的根节点 `root` 和两个指定节点 `p`、`q`。

要求：找到该树中两个指定节点 `p`、`q` 的最近公共祖先。

- 祖先：若节点 `p` 在节点 `node` 的左子树或右子树中，或者 `p == node`，则称 `node` 是 `p` 的祖先。
- 最近公共祖先：对于树的两个节点 `p`、`q`，最近公共祖先表示为一个节点 `lca_node`，满足 `lca_node` 是 `p`、`q` 的祖先且 `lca_node` 的深度尽可能大（一个节点也可以是自己的祖先）

## 解题思路

对于节点 `p`、节点 `q`，最近公共祖先就是从根节点分别到它们路径上的分岔点，也是路径中最后一个相同的节点，现在我们的问题就是求这个分岔点。

使用递归遍历查找最近公共祖先。

- 从根节点开始遍历；
  - 如果当前节点的值大于 `p`、`q` 的值，说明 `p` 和 `q`  应该在当前节点的左子树，因此将当前节点移动到它的左子节点，继续遍历；
  - 如果当前节点的值小于 `p`、`q` 的值，说明 `p` 和 `q`  应该在当前节点的右子树，因此将当前节点移动到它的右子节点，继续遍历；
  - 如果当前节点不满足上面两种情况，则说明 `p` 和 `q` 分别在当前节点的左右子树上，则当前节点就是分岔点，直接返回该节点即可。

## 代码

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if ancestor.val > p.val and ancestor.val > q.val:
                ancestor = ancestor.left
            elif ancestor.val < p.val and ancestor.val < q.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
```

