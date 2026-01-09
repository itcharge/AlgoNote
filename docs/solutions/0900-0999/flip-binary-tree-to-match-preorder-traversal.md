# [0971. 翻转二叉树以匹配先序遍历](https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0971. 翻转二叉树以匹配先序遍历 - 力扣](https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/)

## 题目大意

**描述**：

给定一棵二叉树的根节点 $root$，树中有 $n$ 个节点，每个节点都有一个不同于其他节点且处于 1 到 $n$ 之间的值。

另给你一个由 $n$ 个值组成的行程序列 $voyage$，表示「预期」的二叉树「先序遍历」结果。

通过交换节点的左右子树，可以「翻转」该二叉树中的任意节点。例，翻转节点 1 的效果如下：

![](https://assets.leetcode.com/uploads/2021/02/15/fliptree.jpg)

请翻转「最少」的树中节点，使二叉树的「先序遍历」与预期的遍历行程 $voyage$ 相匹配。

**要求**：

如果可以，则返回「翻转的」所有节点的值的列表。你可以按任何顺序返回答案。如果不能，则返回列表 $[-1]$。

**说明**：

- 树中的节点数目为 n。
- $n == voyage.length$。
- $1 \le n \le 10^{3}$。
- $1 \le Node.val, voyage[i] \le n$。
- 树中的所有值 互不相同。
- voyage 中的所有值 互不相同。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2019/01/02/1219-01.png)

```python
输入：root = [1,2], voyage = [2,1]
输出：[-1]
解释：翻转节点无法令先序遍历匹配预期行程。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2019/01/02/1219-02.png)

```python
输入：root = [1,2,3], voyage = [1,3,2]
输出：[1]
解释：交换节点 2 和 3 来翻转节点 1 ，先序遍历可以匹配预期行程。
```

## 解题思路

### 思路 1：深度优先搜索（DFS）

#### 思路

这道题要求翻转二叉树的某些节点，使得先序遍历结果与给定的 $voyage$ 匹配。

我们可以使用深度优先搜索，同时维护一个指针 $index$ 指向 $voyage$ 中当前应该匹配的位置：

1. **基本情况**：如果当前节点为空，返回 `True`。
2. **检查值**：如果当前节点的值与 $voyage[index]$ 不匹配，返回 `False`。
3. **递归处理**：
   - 如果左子节点存在且值与 $voyage[index + 1]$ 匹配，按正常顺序遍历（先左后右）。
   - 否则，需要翻转当前节点（先右后左），并记录当前节点的值。
4. 如果任何一步失败，返回 `[-1]`。

#### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.flipped = []  # 记录翻转的节点
        self.index = 0  # 当前匹配的位置
        
        def dfs(node):
            if not node:
                return True
            
            # 检查当前节点的值是否匹配
            if node.val != voyage[self.index]:
                return False
            
            self.index += 1
            
            # 如果左子节点存在且值不匹配，需要翻转
            if node.left and node.left.val != voyage[self.index]:
                # 记录翻转的节点
                self.flipped.append(node.val)
                # 先遍历右子树，再遍历左子树
                return dfs(node.right) and dfs(node.left)
            
            # 正常顺序：先左后右
            return dfs(node.left) and dfs(node.right)
        
        # 如果匹配失败，返回 [-1]
        if dfs(root):
            return self.flipped
        else:
            return [-1]
```

#### 复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树中节点的数量。每个节点最多被访问一次。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度。递归调用栈的深度最多为树的高度。
