# [LCR 044. 在每个树行中找最大值](https://leetcode.cn/problems/hPov7L/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [LCR 044. 在每个树行中找最大值 - 力扣](https://leetcode.cn/problems/hPov7L/)

## 题目大意

给定一棵二叉树的根节点 `root`。

要求：找出二叉树中每一层的最大值。

## 解题思路

利用队列进行层序遍历，并记录下每一层的最大值，将其存入答案数组中。

## 代码

```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        queue = []
        res = []
        if root:
            queue.append(root)
        while queue:
            max_level = float('-inf')
            size_level = len(queue)
            for i in range(size_level):
                node = queue.pop(0)
                max_level = max(max_level, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_level)
        return res
```

