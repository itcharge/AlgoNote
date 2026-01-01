# [0572. 另一棵树的子树](https://leetcode.cn/problems/subtree-of-another-tree/)

- 标签：树、深度优先搜索、二叉树、字符串匹配、哈希函数
- 难度：简单

## 题目链接

- [0572. 另一棵树的子树 - 力扣](https://leetcode.cn/problems/subtree-of-another-tree/)

## 题目大意

**描述**：

给定两棵二叉树 $root$ 和 $subRoot$ 。

**要求**：

检验 $root$ 中是否包含和 $subRoot$ 具有相同结构和节点值的子树。如果存在，返回 true；否则，返回 false。

**说明**：

- 二叉树 $tree$ 的一棵子树包括 $tree$ 的某个节点和这个节点的所有后代节点。$tree$ 也可以看做它自身的一棵子树。
- $root$ 树上的节点数量范围是 $[1, 2000]$。
- $subRoot 树上的节点数量范围是 [1, 10^{3}]$。
- $-10^{4} \le root.val \le 10^{4}$。
- $-10^{4} \le subRoot.val \le 10^{4}$。

**示例**：

- 示例 1：

![](https://pic.leetcode.cn/1724998676-cATjhe-image.png)

```python
输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
```

- 示例 2：

![](https://pic.leetcode.cn/1724998698-sEJWnq-image.png)

```python
输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
```

## 解题思路

### 思路 1：递归匹配

对于树 $root$ 中的每个节点，我们需要检查以该节点为根的子树是否与 $subRoot$ 相同。

定义两个辅助函数：

1. `isSameTree(p, q)`：判断两棵树是否完全相同。
2. `isSubtree(root, subRoot)`：判断 $subRoot$ 是否是 $root$ 的子树。

对于 `isSubtree`，如果当前 $root$ 为空，返回 `False`。否则：

- 检查以 $root$ 为根的树是否与 $subRoot$ 相同。
- 递归检查 $root$ 的左子树和右子树是否包含 $subRoot$。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 判断两棵树是否完全相同
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        # 如果 root 为空，返回 False
        if not root:
            return False
        
        # 检查当前节点为根的树是否与 subRoot 相同
        # 或者递归检查左右子树
        return isSameTree(root, subRoot) or \
               self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$，其中 $m$ 是 $root$ 的节点数，$n$ 是 $subRoot$ 的节点数。最坏情况下需要检查 $root$ 中的每个节点，每次检查需要 $O(n)$ 时间。
- **空间复杂度**：$O(m)$，递归栈的深度最多为 $m$。
