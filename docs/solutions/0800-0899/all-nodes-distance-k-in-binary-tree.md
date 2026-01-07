# [0863. 二叉树中所有距离为 K 的结点](https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/)

- 标签：树、深度优先搜索、广度优先搜索、哈希表、二叉树
- 难度：中等

## 题目链接

- [0863. 二叉树中所有距离为 K 的结点 - 力扣](https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/)

## 题目大意

**描述**：

给定一个二叉树（具有根结点 $root$）， 一个目标结点 $target$，和一个整数值 $k$。

**要求**：

返回到目标结点 $target$ 距离为 $k$ 的所有结点的值的数组。

答案可以以「任何顺序」返回。

**说明**：

- 节点数在 $[1, 500]$ 范围内。
- $0 \le Node.val \le 500$。
- $Node.val$ 中所有值「不同」。
- 目标结点 $target$ 是树上的结点。
- $0 \le k \le 10^{3}$。

**示例**：

- 示例 1：

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

```python
输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
输出：[7,4,1]
解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1
```

- 示例 2：

```python
输入: root = [1], target = 1, k = 3
输出: []
```

## 解题思路

### 思路 1：DFS + BFS

这道题要求找到二叉树中距离目标节点 $target$ 为 $k$ 的所有节点。由于二叉树只能从父节点访问子节点，无法直接从子节点访问父节点，因此需要先建立父节点的映射关系。

算法步骤：

1. 使用 DFS 遍历整棵树，建立每个节点到其父节点的映射关系。
2. 从目标节点 $target$ 开始，使用 BFS 向四周扩散（左子节点、右子节点、父节点）。
3. 使用 $visited$ 集合记录已访问的节点，避免重复访问。
4. 当扩散距离达到 $k$ 时，返回当前层的所有节点值。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import deque, defaultdict
        
        # 建立父节点映射
        parent = defaultdict(lambda: None)
        
        def dfs(node, par=None):
            """DFS 遍历，建立父节点映射"""
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        
        # 建立父节点映射
        dfs(root)
        
        # BFS 从 target 开始扩散
        queue = deque([target])
        visited = {target}
        distance = 0
        
        while queue:
            # 如果距离达到 k，返回当前层的所有节点值
            if distance == k:
                return [node.val for node in queue]
            
            # 遍历当前层
            for _ in range(len(queue)):
                node = queue.popleft()
                
                # 向左子节点扩散
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                
                # 向右子节点扩散
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                
                # 向父节点扩散
                if parent[node] and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])
            
            distance += 1
        
        return []
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数。需要遍历整棵树建立父节点映射，然后进行 BFS。
- **空间复杂度**：$O(n)$，需要存储父节点映射和 BFS 队列。
