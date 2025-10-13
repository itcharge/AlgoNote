# [0993. 二叉树的堂兄弟节点](https://leetcode.cn/problems/cousins-in-binary-tree/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0993. 二叉树的堂兄弟节点 - 力扣](https://leetcode.cn/problems/cousins-in-binary-tree/)

## 题目大意

给定一个二叉树，和两个值 x，y。从二叉树中找出 x 和 y 对应的节点 node_x，node_y。如果两个节点是堂兄弟节点，则返回 True，否则返回 False。

- 堂兄弟节点：两个节点的深度相同，父节点不同。

## 解题思路

广度优先搜索或者深度优先搜索都可。以深度优先搜索为例，递归遍历查找节点值为 x，y 的两个节点。在递归的同时，需要传入递归函数当前节点的深度和父节点信息。如果找到对应的节点，则保存两节点对应深度和父节点信息。最后判断两个节点是否是深度相同，父节点不同。如果是，则返回 True，不是则返回 False。

## 代码

```python
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depths = [0, 0]
        parents = [None, None]

        def dfs(node, depth, parent):
            if not node:
                return
            if node.val == x:
                depths[0] = depth
                parents[0] = parent
            elif node.val == y:
                depths[1] = depth
                parents[1] = parent
            dfs(node.left, depth+1, node)
            dfs(node.right, depth+1, node)

        dfs(root, 0, None)
        return depths[0] == depths[1] and parents[0] != parents[1]
```

