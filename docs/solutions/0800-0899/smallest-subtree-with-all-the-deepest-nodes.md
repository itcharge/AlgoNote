# [0865. 具有所有最深节点的最小子树](https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/)

- 标签：树、深度优先搜索、广度优先搜索、哈希表、二叉树
- 难度：中等

## 题目链接

- [0865. 具有所有最深节点的最小子树 - 力扣](https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/)

## 题目大意

**描述**：

给定一个根为 $root$ 的二叉树，每个节点的深度是「该节点到根的最短距离」。

**要求**：

返回包含原始树中所有「最深节点」的「最小子树」。

**说明**：

- 如果一个节点在「整个树」的任意节点之间具有最大的深度，则该节点是「最深的」。
- 一个节点的「子树」是该节点加上它的所有后代的集合。
- 树中节点的数量在 $[1, 500]$ 范围内。
- $0 \le Node.val \le 500$。
- 每个节点的值都是「独一无二」的。

- 注意：本题与力扣 1123 重复：https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves [https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/]

**示例**：

- 示例 1：

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png)

```python
输入：root = [3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：
我们返回值为 2 的节点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的节点。
注意，节点 5、3 和 2 包含树中最深的节点，但节点 2 的子树最小，因此我们返回它。
```

- 示例 2：

```python
输入：root = [1]
输出：[1]
解释：根节点是树中最深的节点。
```

## 解题思路

### 思路 1:DFS

对于每个节点，我们需要知道:

1. 左子树的最大深度
2. 右子树的最大深度

如果左右子树的最大深度相同，说明当前节点就是包含所有最深节点的最小子树的根。

递归函数返回：(节点, 深度)，表示以当前节点为根的子树中，包含所有最深节点的最小子树的根节点和深度。

### 思路 1:代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            # 返回 (包含所有最深节点的最小子树根节点, 深度)
            if not node:
                return None, 0
            
            # 递归处理左右子树
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            
            # 如果左右子树深度相同,当前节点就是答案
            if left_depth == right_depth:
                return node, left_depth + 1
            # 如果左子树更深,答案在左子树中
            elif left_depth > right_depth:
                return left_node, left_depth + 1
            # 如果右子树更深,答案在右子树中
            else:
                return right_node, right_depth + 1
        
        return dfs(root)[0]
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n)$,其中 $n$ 是树中节点的数量。需要遍历每个节点一次。
- **空间复杂度**:$O(h)$,其中 $h$ 是树的高度。递归栈的深度为树的高度。
