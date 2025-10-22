# [0333. 最大二叉搜索子树](https://leetcode.cn/problems/largest-bst-subtree/)

- 标签：树、深度优先搜索、二叉搜索树、动态规划、二叉树
- 难度：中等

## 题目链接

- [0333. 最大二叉搜索子树 - 力扣](https://leetcode.cn/problems/largest-bst-subtree/)

## 题目大意

**描述**：

给定一个二叉树。

**要求**：

找到其中最大的二叉搜索树（BST）子树，并返回该子树的大小。其中，最大指的是子树节点数最多的。

**说明**：

- 二叉搜索树（BST）中的所有节点都具备以下属性：
   - 左子树的值小于其父（根）节点的值。
   - 右子树的值大于其父（根）节点的值。
- 注意：子树必须包含其所有后代。
- 树上节点数目的范围是 $[0, 10^{4}]$。
- $-10^{4} \le Node.val \le 10^{4}$。

- 进阶:  你能想出 $O(n)$ 时间复杂度的解法吗？

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/10/17/tmp.jpg)

```python
输入：root = [10,5,15,1,8,null,7]
输出：3
解释：本例中最大的 BST 子树是高亮显示的子树。返回值是子树的大小，即 3 。
```

- 示例 2：

```python
输入：root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
输出：2
```

## 解题思路

### 思路 1：深度优先搜索 + 自底向上验证

这道题的核心思想是：**自底向上递归验证每个子树是否为 BST，并记录最大 BST 子树的大小**。

解题步骤：

1. **定义递归函数**：设计一个递归函数 `dfs(node)`，返回一个四元组 $(is\_bst, min\_val, max\_val, size)$：
   - $is\_bst$：以 $node$ 为根的子树是否为 BST。
   - $min\_val$：子树中的最小值。
   - $max\_val$：子树中的最大值。
   - $size$：子树的大小（节点数）。

2. **递归终止条件**：当 $node$ 为空时，返回 $(True, +\infty, -\infty, 0)$。

3. **递归处理**：
   - 递归处理左右子树，得到 $(left\_is\_bst, left\_min, left\_max, left\_size)$ 和 $(right\_is\_bst, right\_min, right\_max, right\_size)$。
   - 当前子树为 BST 的条件：
     - 左右子树都是 BST。
     - $node.val > left\_max$（当前节点值大于左子树最大值）。
     - $node.val < right\_min$（当前节点值小于右子树最小值）。
   - 如果当前子树是 BST，更新全局最大 BST 大小。

4. **更新边界值**：
   - $min\_val = \min(node.val, left\_min)$。
   - $max\_val = \max(node.val, right\_max)$。
   - $size = left\_size + right\_size + 1$。

**关键点**：

- 使用 $+\infty$ 和 $-\infty$ 作为空节点的边界值，确保边界条件正确处理。
- 只有当左右子树都是 BST 且满足 BST 性质时，当前子树才是 BST。
- 在递归过程中实时更新全局最大 BST 大小。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_size = 0  # 记录最大BST子树的大小
        
        def dfs(node):
            """
            递归函数，返回 (is_bst, min_val, max_val, size)
            is_bst: 当前子树是否为BST
            min_val: 子树中的最小值
            max_val: 子树中的最大值
            size: 子树的大小
            """
            if not node:
                # 空节点：是BST，边界值为正负无穷，大小为0
                return True, float('inf'), float('-inf'), 0
            
            # 递归处理左右子树
            left_is_bst, left_min, left_max, left_size = dfs(node.left)
            right_is_bst, right_min, right_max, right_size = dfs(node.right)
            
            # 判断当前子树是否为BST
            if (left_is_bst and right_is_bst and 
                node.val > left_max and node.val < right_min):
                # 当前子树是BST，计算大小并更新全局最大值
                current_size = left_size + right_size + 1
                self.max_size = max(self.max_size, current_size)
                
                # 更新边界值
                min_val = min(node.val, left_min)
                max_val = max(node.val, right_max)
                
                return True, min_val, max_val, current_size
            else:
                # 当前子树不是BST，返回False和任意边界值
                return False, 0, 0, 0
        
        dfs(root)
        return self.max_size
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树中节点的数量。每个节点被访问一次，每次访问的时间复杂度为 $O(1)$。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度。递归调用栈的深度等于树的高度，最坏情况下为 $O(n)$（当树退化为链表时）。
