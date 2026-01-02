# [0671. 二叉树中第二小的节点](https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/)

- 标签：树、深度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0671. 二叉树中第二小的节点 - 力扣](https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/)

## 题目大意

**描述**：

给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 $2$ 或 $0$。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，即 $root.val = min(root.left.val, root.right.val)$ 总成立。

**要求**：

给出这样的一个二叉树，你需要输出所有节点中的「第二小的值」。

如果第二小的值不存在的话，输出 $-1$。

**说明**：

- 树中节点数目在范围 $[1, 25]$ 内。
- $1 \le Node.val \le 2^{31} - 1$。
- 对于树中每个节点 $root.val == min(root.left.val, root.right.val)$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg)

```python
输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg)

```python
输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。
```

## 解题思路

### 思路 1：深度优先搜索

根据题目描述，二叉树的特性是根节点的值等于两个子节点中较小的值。因此根节点一定是最小值。我们需要找到第二小的值。

1. 根节点的值 $root.val$ 是最小值。
2. 使用深度优先搜索遍历整棵树，寻找第一个大于 $root.val$ 的值。
3. 在遍历过程中：
   - 如果当前节点的值大于 $root.val$，说明找到了一个候选值，更新答案。
   - 如果当前节点的值等于 $root.val$，继续递归搜索其子树。
4. 如果没有找到第二小的值，返回 $-1$。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        min_val = root.val
        
        def dfs(node):
            if not node:
                return
            
            # 如果当前节点值大于最小值且小于当前答案，更新答案
            if min_val < node.val < self.ans:
                self.ans = node.val
            # 只有当节点值等于最小值时，才需要继续搜索其子树
            elif node.val == min_val:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        return self.ans if self.ans != float('inf') else -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数。最坏情况下需要遍历所有节点。
- **空间复杂度**：$O(h)$，其中 $h$ 是二叉树的高度。递归调用栈的深度最多为树的高度。
