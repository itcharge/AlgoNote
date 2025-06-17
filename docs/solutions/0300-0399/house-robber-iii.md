# [0337. 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/)

- 标签：树、深度优先搜索、动态规划、二叉树
- 难度：中等

## 题目链接

- [0337. 打家劫舍 III - 力扣](https://leetcode.cn/problems/house-robber-iii/)

## 题目大意

小偷发现了一个新的可行窃的地区，这个地区的形状是一棵二叉树。这个地区只有一个入口，称为「根」。除了「根」之外，每栋房子只有一个「父」房子与之相连。如果两个直接相连的房子在同一天被打劫，房屋将自动报警。

现在给定这个代表地区房间的二叉树，每个节点值代表该房间所拥有的金额。要求计算在不触动警报的情况下，小偷一晚上能盗取的最高金额。

## 解题思路

树形动态规划问题。

对于当前节点 `cur`，不能选择子节点，也不能选择父节点。所以对于一棵子树来说，有两种情况：

- 选择了根节点
- 没有选择根节点

### 1. 选择根节点

如果选择了根节点，则不能再选择左右儿子节点，这种情况下的最大值为：当前节点 + 左子树不选择根节点 + 右子树不选择根节点。

### 2. 不选择根节点

如果不选择根节点，则可以选择左右儿子节点，共四种可能：

- 左子树选择根节点 + 右子树选择根节点
- 左子树选择根节点 + 右子树不选根节点
- 左子树不选根节点 + 右子树选择根节点
- 左子树不选根节点 + 右子树不选根节点

选择其中最大值。

上述描述中，当前节点的选择来自于子节点信息的选择，然后逐层向上，直到根节点。所以我们使用「后序遍历」的方式进行递归遍历。

## 代码

```python
class Solution:
    def dfs(self, root: TreeNode):
        if not root:
            return [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        val_steal = root.val + left[1] + right[1]
        val_no_steal = max(left[0], left[1]) + max(right[0], right[1])
        return [val_steal, val_no_steal]
    def rob(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return max(res[0], res[1])
```

