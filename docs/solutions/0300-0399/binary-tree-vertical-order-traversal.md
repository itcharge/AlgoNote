# [0314. 二叉树的垂直遍历](https://leetcode.cn/problems/binary-tree-vertical-order-traversal/)

- 标签：树、深度优先搜索、广度优先搜索、哈希表、二叉树、排序
- 难度：中等

## 题目链接

- [0314. 二叉树的垂直遍历 - 力扣](https://leetcode.cn/problems/binary-tree-vertical-order-traversal/)

## 题目大意

**描述**：

给定一个二叉树的根结点 $root$。

**要求**：

返回其结点按垂直方向（从上到下，逐列）遍历的结果。

**说明**：

- 如果两个结点在同一行和列，那么顺序则为「从左到右」。
- 树中结点的数目在范围 $[0, 10^{3}]$ 内。
- $-10^{3} \le Node.val \le 10^{3}$。

**示例**：

- 示例 1：

![](https://pic.leetcode.cn/1727276130-UOKFsu-image.png)

```python
输入：root = [3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
```

- 示例 2：

![](https://pic.leetcode.cn/1727276212-bzuKab-image.png)

```python
输入：root = [3,9,8,4,0,1,7]
输出：[[4],[9],[3,0,1],[8],[7]]
```

## 解题思路

### 思路 1：BFS + 哈希表

二叉树的垂直遍历问题可以通过 BFS（广度优先搜索）结合哈希表来解决。我们需要为每个节点分配一个列坐标，然后按照列坐标对节点进行分组。

**问题分析**：

对于二叉树中的每个节点，我们需要：

- 为根节点分配列坐标 $0$。
- 左子节点的列坐标为父节点列坐标 $-1$。
- 右子节点的列坐标为父节点列坐标 $+1$。
- 使用 BFS 保证同一列中节点的从上到下顺序。
- 使用哈希表按列坐标分组存储节点值。

**算法步骤**：

1. **初始化**：如果根节点为空，返回空列表。创建队列存储 `(节点, 列坐标)` 元组，创建哈希表存储每列的节点值列表。
2. **BFS 遍历**：从根节点开始，将根节点和列坐标 $0$ 加入队列。
3. **处理节点**：对于队列中的每个节点，将其值加入对应列的列表中，然后处理其左右子节点。
4. **更新坐标**：左子节点列坐标 $-1$，右子节点列坐标 $+1$。
5. **排序输出**：按照列坐标从小到大排序，返回每列的节点值列表。

**关键变量**：

- $col$：节点的列坐标，根节点为 $0$。
- $queue$：BFS 队列，存储 `(节点, 列坐标)` 元组。
- $column\_table$：哈希表，键为列坐标，值为该列的节点值列表。
- $min\_col$ 和 $max\_col$：记录最小和最大列坐标，用于最终排序。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 如果根节点为空，返回空列表
        if not root:
            return []
        
        # 使用队列进行 BFS，存储 (节点, 列坐标) 元组
        queue = [(root, 0)]
        # 哈希表存储每列的节点值列表
        column_table = {}
        # 记录最小和最大列坐标
        min_col = 0
        max_col = 0
        
        # BFS 遍历
        while queue:
            node, col = queue.pop(0)
            
            # 将节点值加入对应列的列表
            if col not in column_table:
                column_table[col] = []
            column_table[col].append(node.val)
            
            # 更新列坐标范围
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            # 处理左子节点，列坐标 -1
            if node.left:
                queue.append((node.left, col - 1))
            
            # 处理右子节点，列坐标 +1
            if node.right:
                queue.append((node.right, col + 1))
        
        # 按照列坐标从小到大排序，构建结果列表
        result = []
        for col in range(min_col, max_col + 1):
            if col in column_table:
                result.append(column_table[col])
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是树中节点的数量。BFS 遍历需要 $O(n)$ 时间，最后按列坐标排序需要 $O(k \log k)$ 时间，其中 $k$ 是列的数量，最坏情况下 $k = n$，因此总时间复杂度为 $O(n \log n)$。
- **空间复杂度**：$O(n)$，队列和哈希表最多存储 $n$ 个节点，递归调用栈的深度最多为 $O(n)$。
