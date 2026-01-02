# [0623. 在二叉树中增加一行](https://leetcode.cn/problems/add-one-row-to-tree/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0623. 在二叉树中增加一行 - 力扣](https://leetcode.cn/problems/add-one-row-to-tree/)

## 题目大意

**描述**：

给定一个二叉树的根 $root$ 和两个整数 $val$ 和 $depth$。

**要求**：

在给定的深度 $depth$ 处添加一个值为 $val$ 的节点行。

注意，根节点 $root$ 位于深度 1。

**说明**：

- 加法规则如下:
   - 给定整数 $depth$，对于深度为 $depth - 1$ 的每个非空树节点 $cur$ ，创建两个值为 $val$ 的树节点作为 $cur$ 的左子树根和右子树根。
   - $cur$ 原来的左子树应该是新的左子树根的左子树。
   - $cur$ 原来的右子树应该是新的右子树根的右子树。
   - 如果 $depth == 1$ 意味着 $depth - 1$ 根本没有深度，那么创建一个树节点，值 $val$ 作为整个原始树的新根，而原始树就是新根的左子树。
- 节点数在 $[1, 10^{4}]$ 范围内。
- 树的深度在 $[1, 10^{4}]$ 范围内。
- $-10^{3} \le Node.val \le 10^{3}$。
- $-10^{5} \le val \le 10^{5}$。
- $1 \le depth \le the depth of tree + 1$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg)

```python
输入: root = [4,2,6,3,1,5], val = 1, depth = 2
输出: [4,1,1,2,null,null,6,3,1,5]
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg)

```python
输入: root = [4,2,null,3,1], val = 1, depth = 3
输出:  [4,2,null,1,1,3,null,null,1]
```

## 解题思路

### 思路 1：广度优先搜索

#### 思路 1：算法描述

这道题目要求在二叉树的指定深度 $depth$ 处添加一行值为 $val$ 的节点。

我们可以使用广度优先搜索（BFS）来找到深度为 $depth - 1$ 的所有节点，然后为这些节点添加新的左右子节点。

特殊情况：如果 $depth = 1$，则需要创建一个新的根节点，原来的树作为新根节点的左子树。

具体步骤如下：

1. 如果 $depth = 1$，创建一个新的根节点，值为 $val$，原来的根节点作为新根节点的左子节点，返回新根节点。
2. 使用 BFS 遍历二叉树，找到深度为 $depth - 1$ 的所有节点。
3. 对于深度为 $depth - 1$ 的每个节点 $node$：
   - 创建两个新节点 $left\_node$ 和 $right\_node$，值都为 $val$。
   - 将 $node$ 的原左子节点作为 $left\_node$ 的左子节点。
   - 将 $node$ 的原右子节点作为 $right\_node$ 的右子节点。
   - 将 $left\_node$ 和 $right\_node$ 分别设置为 $node$ 的左右子节点。
4. 返回根节点。

#### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # 特殊情况：在根节点前添加一行
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        # 使用 BFS 找到深度为 depth - 1 的所有节点
        queue = [root]
        current_depth = 1
        
        while queue and current_depth < depth - 1:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            current_depth += 1
        
        # 为深度为 depth - 1 的所有节点添加新的左右子节点
        for node in queue:
            # 创建新的左子节点
            left_node = TreeNode(val)
            left_node.left = node.left
            node.left = left_node
            
            # 创建新的右子节点
            right_node = TreeNode(val)
            right_node.right = node.right
            node.right = right_node
        
        return root
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数。最坏情况下需要遍历所有节点。
- **空间复杂度**：$O(n)$。队列中最多存储 $n$ 个节点。
