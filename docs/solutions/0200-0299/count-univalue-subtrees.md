# [0250. 统计同值子树](https://leetcode.cn/problems/count-univalue-subtrees/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0250. 统计同值子树 - 力扣](https://leetcode.cn/problems/count-univalue-subtrees/)

## 题目大意

**描述**：

给定一个二叉树。

**要求**：

统计该二叉树数值相同的「子树」个数。

**说明**：

- 同值子树：指该子树的所有节点都拥有相同的数值。
- $树中节点的编号在 $[0, 10^{3}]$ 范围内。
- $-10^{3} \le Node.val \le 10^{3}$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/08/21/unival_e1.jpg)

```python
输入：root = [5,1,5,5,5,null,5]
输出：4
```

- 示例 2：

```python
输入：root = []
输出：0
```

## 解题思路

### 思路 1：深度优先搜索

这是一个典型的树遍历问题。我们需要统计所有同值子树的个数。

**算法步骤**：

1. **定义递归函数**：$is\_unival(node)$ 判断以 $node$ 为根的子树是否为同值子树，同时统计同值子树个数。

2. **递归终止条件**：
   - 如果 $node$ 为空，返回 $True$（空树视为同值子树）。
   - 如果 $node$ 是叶子节点，返回 $True$（单个节点是同值子树）。

3. **递归处理**：
   - 递归检查左子树 $left\_is\_unival = is\_unival(node.left)$。
   - 递归检查右子树 $right\_is\_unival = is\_unival(node.right)$。
   - 如果左右子树都是同值子树，且它们的值都等于当前节点值，则当前子树也是同值子树。

4. **统计计数**：如果当前子树是同值子树，则计数器 $count$ 加 $1$。

**关键点**：

- 使用后序遍历（左右根）确保先处理子节点再处理父节点。
- 空树和叶子节点都视为同值子树。
- 需要同时检查子树是否为同值以及值是否相等。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0  # 统计同值子树个数
        
        def is_unival(node):
            """
            判断以 node 为根的子树是否为同值子树
            返回: (是否为同值子树, 子树的值)
            """
            # 空节点视为同值子树
            if not node:
                return True, None
            
            # 叶子节点是同值子树
            if not node.left and not node.right:
                self.count += 1
                return True, node.val
            
            # 递归检查左右子树
            left_is_unival, left_val = is_unival(node.left)
            right_is_unival, right_val = is_unival(node.right)
            
            # 判断当前子树是否为同值子树
            is_current_unival = True
            
            # 如果左子树存在且不是同值子树，或者值不相等
            if node.left and (not left_is_unival or left_val != node.val):
                is_current_unival = False
            
            # 如果右子树存在且不是同值子树，或者值不相等
            if node.right and (not right_is_unival or right_val != node.val):
                is_current_unival = False
            
            # 如果当前子树是同值子树，计数加1
            if is_current_unival:
                self.count += 1
            
            return is_current_unival, node.val
        
        is_unival(root)
        return self.count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树中节点的个数。每个节点都会被访问一次。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度。递归调用栈的深度等于树的高度，最坏情况下（树退化为链表）为 $O(n)$。
