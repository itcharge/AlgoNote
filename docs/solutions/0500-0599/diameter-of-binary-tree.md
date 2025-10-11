# [0543. 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)

- 标签：树、深度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0543. 二叉树的直径 - 力扣](https://leetcode.cn/problems/diameter-of-binary-tree/)

## 题目大意

**描述**：给一个二叉树的根节点 $root$。

**要求**：计算该二叉树的直径长度。

**说明**：

- **二叉树的直径长度**：二叉树中任意两个节点路径长度中的最大值。
- 两节点之间的路径长度是以它们之间边的数目表示。
- 这条路径可能穿过也可能不穿过根节点。

**示例**：

- 示例 1：

```python
给定二叉树：
          1
         / \
        2   3
       / \     
      4   5    
输出：3
解释：该二叉树的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
```

## 解题思路

### 思路 1：树形 DP + 深度优先搜索

这道题重点是理解直径长度的定义。「二叉树的直径长度」的定义为：二叉树中任意两个节点路径长度中的最大值。并且这条路径可能穿过也可能不穿过根节点。

对于根为 $root$ 的二叉树来说，其直径长度并不简单等于「左子树高度」加上「右子树高度」。

根据路径是否穿过根节点，我们可以将二叉树分为两种：

1. 直径长度所对应的路径穿过根节点。
2. 直径长度所对应的路径不穿过根节点。

我们来看下图中的两个例子。

![二叉树的直径](https://qcdn.itcharge.cn/images/20230427111005.png)

如图所示，左侧这棵二叉树就是一棵常见的平衡二叉树，其直径长度所对应的路径是穿过根节点的（$D\rightarrow B \rightarrow A \rightarrow C$）。这种情况下：$\text{二叉树的直径} = \text{左子树高度} + \text{右子树高度}$。

而右侧这棵特殊的二叉树，其直径长度所对应的路径是没有穿过根节点的（$F \rightarrow D \rightarrow B \rightarrow E \rightarrow G$）。这种情况下：$\text{二叉树的直径} = \text{所有子树中最大直径长度}$。

也就是说根为 $root$ 的二叉树的直径长度可能来自于  $\text{左子树高度} + \text{右子树高度}$，也可能来自于 $\text{子树中的最大直径}$，即 $\text{二叉树的直径} = max(\text{左子树高度} + \text{右子树高度}, \quad \text{所有子树中最大直径长度})$。

那么现在问题就变成为如何求「子树的高度」和「子树中的最大直径」。

1. 子树的高度：我们可以利用深度优先搜索方法，递归遍历左右子树，并分别返回左右子树的高度。
2. 子树中的最大直径：我们可以在递归求解子树高度的时候维护一个 $ans$ 变量，用于记录所有 $\text{左子树高度} + \text{右子树高度}$ 中的最大值。

最终 $ans$ 就是我们所求的该二叉树的最大直径，将其返回即可。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, node):
        if not node:
            return 0
        left_height = self.dfs(node.left)                     # 左子树高度
        right_height = self.dfs(node.right)                   # 右子树高度
        self.ans = max(self.ans, left_height + right_height)  # 维护所有路径中的最大直径
        return max(left_height, right_height) + 1             # 返回该节点的高度 = 左右子树最大高度 + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数目。
- **空间复杂度**：$O(n)$。递归函数需要用到栈空间，栈空间取决于递归深度，最坏情况下递归深度为 $n$，所以空间复杂度为 $O(n)$。

