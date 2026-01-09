# [0965. 单值二叉树](https://leetcode.cn/problems/univalued-binary-tree/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0965. 单值二叉树 - 力扣](https://leetcode.cn/problems/univalued-binary-tree/)

## 题目大意

**描述**：

给定一棵二叉树的根节点 $root$。如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

**要求**：

如果给定的树是单值二叉树，返回 true；否则返回 false。

**说明**：

- 给定树的节点数范围是 $[1, 10^{3}]$。
- 每个节点的值都是整数，范围为 $[0, 99]$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50104-pm.png)

```python
输入：[1,1,1,1,1,null,1]
输出：true
```

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50050-pm.png)

```python
输入：[2,2,2,5,2]
输出：false
```

## 解题思路

### 思路 1：深度优先搜索

使用深度优先搜索遍历整棵树，检查每个节点的值是否与根节点的值相同。

1. 如果当前节点为空，返回 $True$。
2. 如果当前节点的值与根节点的值不同，返回 $False$。
3. 递归检查左子树和右子树。
4. 只有当左右子树都是单值二叉树时，整棵树才是单值二叉树。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node, val):
            # 空节点返回 True
            if not node:
                return True
            # 当前节点值不等于目标值，返回 False
            if node.val != val:
                return False
            # 递归检查左右子树
            return dfs(node.left, val) and dfs(node.right, val)
        
        return dfs(root, root.val)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数量。需要遍历所有节点。
- **空间复杂度**：$O(h)$，其中 $h$ 是二叉树的高度。递归调用栈的深度为树的高度。
