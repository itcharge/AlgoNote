# [0156. 上下翻转二叉树](https://leetcode.cn/problems/binary-tree-upside-down/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0156. 上下翻转二叉树 - 力扣](https://leetcode.cn/problems/binary-tree-upside-down/)

## 题目大意

**描述**：

给定一个二叉树的根节点 $root$。

**要求**：

将此二叉树上下翻转，并返回新的根节点。

你可以按下面的步骤翻转一棵二叉树：

1. 原来的左子节点变成新的根节点
2. 原来的根节点变成新的右子节点
3. 原来的右子节点变成新的左子节点

![](https://assets.leetcode.com/uploads/2020/08/29/main.jpg)

上面的步骤逐层进行。题目数据保证每个右节点都有一个同级节点（即共享同一父节点的左节点）且不存在子节点。

**说明**：

- 树中节点数目在范围 $[0, 10]$ 内。
- $1 \le Node.val \le 10$。
- 树中的每个右节点都有一个同级节点（即共享同一父节点的左节点）。
- 树中的每个右节点都没有子节点。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/08/29/updown.jpg)

```python
输入：root = [1,2,3,4,5]
输出：[4,5,2,null,null,3,1]
```

- 示例 2：

```python
输入：root = []
输出：[]
```

## 解题思路

### 思路 1：递归

根据题目描述，我们需要将二叉树进行上下翻转。观察翻转规则：

1. 原来的左子节点变成新的根节点
2. 原来的根节点变成新的右子节点  
3. 原来的右子节点变成新的左子节点

这是一个递归问题，我们可以采用以下策略：

1. **递归终止条件**：如果当前节点 $root$ 为空或者没有左子节点，直接返回当前节点。
2. **递归处理**：对左子树进行翻转，得到新的根节点 $new\_root$。
3. **重新连接**：
   - 将原根节点 $root$ 作为新根节点 $new\_root$ 的右子节点
   - 将原右子节点 $root.right$ 作为新根节点 $new\_root$ 的左子节点
   - 将原根节点 $root$ 的左右子节点设为 $null$，避免循环引用

**关键点**：
- 翻转后的新根节点是原树最左边的叶子节点
- 需要保存原根节点和右子节点，用于重新连接
- 翻转是逐层进行的，每层都遵循相同的翻转规则

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归终止条件：空节点或没有左子节点
        if not root or not root.left:
            return root
        
        # 保存原根节点和右子节点
        original_root = root
        original_right = root.right
        
        # 递归处理左子树，得到新的根节点
        new_root = self.upsideDownBinaryTree(root.left)
        
        # 重新连接节点
        # 原左子节点（现在是新根节点）的左子节点指向原右子节点
        root.left.left = original_right
        # 原左子节点（现在是新根节点）的右子节点指向原根节点
        root.left.right = original_root
        
        # 将原根节点的左右子节点设为 None，避免循环引用
        original_root.left = None
        original_root.right = None
        
        return new_root
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(h)$，其中 $h$ 是树的高度。我们需要递归到树的最左边叶子节点，递归深度等于树的高度。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度。递归调用栈的深度等于树的高度。
