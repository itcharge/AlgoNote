# [0987. 二叉树的垂序遍历](https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/)

- 标签：树、深度优先搜索、广度优先搜索、哈希表、二叉树、排序
- 难度：困难

## 题目链接

- [0987. 二叉树的垂序遍历 - 力扣](https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/)

## 题目大意

**描述**：

给定二叉树的根结点 $root$ ，请你设计算法计算二叉树的「垂序遍历」序列。

对位于 $(row, col)$ 的每个结点而言，其左右子结点分别位于 $(row + 1, col - 1)$ 和 $(row + 1, col + 1)$。树的根结点位于 $(0, 0)$。

二叉树的「垂序遍历」从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。

**要求**：

返回二叉树的「垂序遍历」序列。

**说明**：

- 树中结点数目总数在范围 $[1, 10^{3}]$ 内。
- $0 \le Node.val \le 10^{3}$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/01/29/vtree1.jpg)

```python
输入：root = [3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
解释：
列 -1 ：只有结点 9 在此列中。
列  0 ：只有结点 3 和 15 在此列中，按从上到下顺序。
列  1 ：只有结点 20 在此列中。
列  2 ：只有结点 7 在此列中。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/01/29/vtree2.jpg)

```python
输入：root = [1,2,3,4,5,6,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
列 -2 ：只有结点 4 在此列中。
列 -1 ：只有结点 2 在此列中。
列  0 ：结点 1 、5 和 6 都在此列中。
          1 在上面，所以它出现在前面。
          5 和 6 位置都是 (2, 0) ，所以按值从小到大排序，5 在 6 的前面。
列  1 ：只有结点 3 在此列中。
列  2 ：只有结点 7 在此列中。
```

## 解题思路

### 思路 1：深度优先搜索 + 排序

使用深度优先搜索遍历二叉树，记录每个节点的位置 $(row, col)$ 和值，然后按照题目要求排序。

1. 使用 DFS 遍历二叉树，记录每个节点的 $(col, row, val)$。
2. 按照以下规则排序：
   - 首先按列 $col$ 从小到大排序。
   - 列相同时，按行 $row$ 从小到大排序。
   - 行和列都相同时，按值 $val$ 从小到大排序。
3. 将排序后的节点按列分组，返回结果。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []  # 存储 (col, row, val)
        
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        
        # 按照 col, row, val 排序
        nodes.sort()
        
        # 按列分组
        result = []
        prev_col = float('-inf')
        
        for col, row, val in nodes:
            if col != prev_col:
                result.append([])
                prev_col = col
            result[-1].append(val)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是二叉树的节点数量。需要遍历所有节点并排序。
- **空间复杂度**：$O(n)$，需要存储所有节点的位置信息。
