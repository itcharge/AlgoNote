# [0951. 翻转等价二叉树](https://leetcode.cn/problems/flip-equivalent-binary-trees/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0951. 翻转等价二叉树 - 力扣](https://leetcode.cn/problems/flip-equivalent-binary-trees/)

## 题目大意

**描述**：

我们可以为二叉树 $T$ 定义一个「翻转操作」，如下所示：选择任意节点，然后交换它的左子树和右子树。

只要经过一定次数的翻转操作后，能使 $X$ 等于 $Y$，我们就称二叉树 $X$ 翻转「等价」于二叉树 $Y$。

这些树由根节点 $root1$ 和 $root2$ 给出。

**要求**：

如果两个二叉树是否是翻转「等价」的树，则返回 true，否则返回 false。

**说明**：

- 每棵树节点数在 $[0, 10^{3}]$ 范围内。
- 每棵树中的每个值都是唯一的、在 $[0, 99]$ 范围内的整数。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png)

```python
输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
输出：true
解释：我们翻转值为 1，3 以及 5 的三个节点。
```

- 示例 2：

```python
输入: root1 = [], root2 = []
输出: true
```

## 解题思路

### 思路 1：深度优先搜索（DFS）

#### 思路

这道题要求判断两棵二叉树是否翻转等价。翻转等价的定义是：通过若干次翻转操作（交换左右子树），可以使两棵树相同。

我们可以使用递归的方式判断：

1. **基本情况**：
   - 如果两个节点都为空，返回 `True`。
   - 如果只有一个节点为空，或者两个节点的值不同，返回 `False`。
2. **递归情况**：对于两个节点，有两种可能：
   - **不翻转**：左子树对应左子树，右子树对应右子树。
   - **翻转**：左子树对应右子树，右子树对应左子树。
   - 只要其中一种情况成立，就返回 `True`。

#### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 基本情况：两个节点都为空
        if not root1 and not root2:
            return True
        
        # 只有一个节点为空，或者值不同
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # 递归判断：不翻转或翻转
        # 不翻转：左对左，右对右
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        # 翻转：左对右，右对左
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        
        return no_flip or flip
```

#### 复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树中节点的数量。每个节点最多被访问一次。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度。递归调用栈的深度最多为树的高度。
