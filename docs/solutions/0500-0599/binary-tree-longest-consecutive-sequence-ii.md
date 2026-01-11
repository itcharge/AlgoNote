# [0549. 二叉树最长连续序列 II](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0549. 二叉树最长连续序列 II - 力扣](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/)

## 题目大意

**描述**：

给定一棵二叉树的根节点 $root$，返回树中最长连续序列路径的长度。

连续序列路径是指路径中相邻节点的值相差 1。路径可以是递增的或递减的，路径可以是从父节点到子节点，也可以是从子节点到父节点（即路径可以"拐弯"）。

- 例如，$[1,2,3,4]$ 和 $[4,3,2,1]$ 都被认为有效，但路径 $[1,2,4,3]$ 无效。

**要求**：

返回最长连续序列路径的长度。

**说明**：

- 树中节点数在范围 $[1, 3 \times 10^4]$ 内。
- $-3 \times 10^4 \le Node.val \le 3 \times 10^4$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/14/consec2-1-tree.jpg)

```python
输入: root = [1,2,3]
输出: 2
解释: 最长的连续路径是 [1, 2] 或者 [2, 1]。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/03/14/consec2-2-tree.jpg)

```python
输入: root = [2,1,3]
输出: 3
解释: 最长的连续路径是 [1, 2, 3] 或者 [3, 2, 1]。
```

## 解题思路

### 思路 1：后序遍历 + 动态规划

本题扩展了连续序列既可递增也可递减，且可以"拐弯"（以父节点为顶点的左右递增或递减链）。

**核心思路**：

- 对于每个节点，返回两个值：以该节点为根向下的最大递增长度和最大递减长度。
- 递归处理左右子树，根据子节点与当前节点的值关系更新递增/递减长度。
- 全局维护最大值：可以是左递增 + 右递减 + 1，或左递减 + 右递增 + 1。

假设以 $node$ 节点为根节点，则返回 $(inc, dec)$，分别为递增和递减的最大长度。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return (0, 0)  # (inc, dec)
            
            inc = dec = 1
            
            if node.left:
                l_inc, l_dec = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec = max(dec, l_dec + 1)
                elif node.val == node.left.val - 1:
                    inc = max(inc, l_inc + 1)
            
            if node.right:
                r_inc, r_dec = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, r_dec + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, r_inc + 1)
            
            # 以 node 为顶点合并（不重叠）
            self.ans = max(self.ans, inc + dec - 1)
            return inc, dec
        
        dfs(root)
        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是节点数。每个节点只遍历一次。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度，递归栈空间。
