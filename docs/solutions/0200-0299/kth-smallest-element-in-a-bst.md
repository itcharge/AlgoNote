# [0230. 二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：中等

## 题目链接

- [0230. 二叉搜索树中第 K 小的元素 - 力扣](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)

## 题目大意

**描述**：

给定一个二叉搜索树的根节点 $root$，和一个整数 $k$。

**要求**：

设计一个算法查找其中第 $k$ 小的元素（从 $1$ 开始计数）。

**说明**：

- 树中的节点数为 $n$。
- $1 \le k \le n \le 10^{4}$。
- $0 \le Node.val \le 10^{4}$。

- 进阶：如果二叉搜索树经常被修改（插入 / 删除操作）并且你需要频繁地查找第 $k$ 小的值，你将如何优化算法？

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```python
输入：root = [3,1,4,null,2], k = 1
输出：1
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```python
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
```

## 解题思路

### 思路 1：中序遍历

这是一个经典的二叉搜索树问题。由于二叉搜索树具有左子树所有节点值小于根节点值，右子树所有节点值大于根节点值的性质，我们可以利用中序遍历来获得升序排列的节点值。

核心思想是：

- 对二叉搜索树进行中序遍历（左子树 → 根节点 → 右子树）。
- 中序遍历的结果是升序排列的节点值序列。
- 遍历到第 $k$ 个节点时，返回该节点的值。

具体算法步骤：

1. 使用递归或迭代的方式进行中序遍历。
2. 维护一个计数器 $count$，记录当前访问的节点序号。
3. 当 $count = k$ 时，返回当前节点的值。
4. 由于只需要找到第 $k$ 小的元素，可以在找到后立即返回，不需要遍历完整棵树。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 使用中序遍历找到第k小的元素
        self.count = 0  # 计数器，记录当前访问的节点序号
        self.result = 0  # 存储结果
        
        def inorder_traversal(node):
            if not node:
                return
            
            # 遍历左子树
            inorder_traversal(node.left)
            
            # 访问根节点
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # 遍历右子树
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return self.result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(k)$，其中 $k$ 是题目给定的参数。最坏情况下需要遍历 $k$ 个节点才能找到第 $k$ 小的元素。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度。递归调用栈的深度等于树的高度，最坏情况下为 $O(n)$（树退化为链表）。
