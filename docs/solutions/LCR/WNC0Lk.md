# [LCR 046. 二叉树的右视图](https://leetcode.cn/problems/WNC0Lk/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [LCR 046. 二叉树的右视图 - 力扣](https://leetcode.cn/problems/WNC0Lk/)

## 题目大意

给定一棵二叉树的根节点 `root`。

要求：按照从顶部到底部的顺序，返回从右侧能看到的节点值。

## 解题思路

二叉树的层次遍历，不过遍历每层节点的时候，只需要将最后一个节点加入结果数组即可。

## 代码

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        order = []
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if i == size - 1:
                order.append(curr.val)
        return order
```

