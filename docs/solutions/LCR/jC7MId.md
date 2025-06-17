# [LCR 051. 二叉树中的最大路径和](https://leetcode.cn/problems/jC7MId/)

- 标签：树、深度优先搜索、动态规划、二叉树
- 难度：困难

## 题目链接

- [LCR 051. 二叉树中的最大路径和 - 力扣](https://leetcode.cn/problems/jC7MId/)

## 题目大意

给定一个二叉树的根节点 `root`。

要求：返回其最大路径和。

- 路径：从树中的任意节点出发，沿父节点——子节点连接，到达任意节点的序列。同一个节点在一条路径序列中至多出现一次。该路径至少包含一个节点，且不一定经过根节点。
- 路径和：路径中各节点值的总和。

## 解题思路

深度优先搜索遍历二叉树。递归的同时，维护一个最大路径和变量。定义函数 `dfs(self, root)` 计算二叉树中以该节点为根节点，并且经过该节点的最大贡献值。

计算的结果可能的情况有 2 种：

- 经过空节点的最大贡献值等于 `0`。

- 经过非空节点的最大贡献值等于 当前节点值 + 左右子节点的最大贡献值中较大的一个。

在递归时，我们先计算左右子节点的最大贡献值，再更新维护当前最大路径和变量。

最终 `max_sum` 即为答案。

## 代码

```python
class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def dfs(self, root):
        if not root:
            return 0
        left_max = max(self.dfs(root.left), 0)
        right_max = max(self.dfs(root.right), 0)
        self.max_sum = max(self.max_sum, root.val + left_max + right_max)
        return root.val + max(left_max, right_max)

    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_sum
```

