# [0700. 二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/)

- 标签：树、二叉搜索树、二叉树
- 难度：简单

## 题目链接

- [0700. 二叉搜索树中的搜索 - 力扣](https://leetcode.cn/problems/search-in-a-binary-search-tree/)

## 题目大意

**描述**：给定一个二叉搜索树和一个值 `val`。

**要求**：在二叉搜索树中查找节点值等于 `val` 的节点，并返回该节点。

**说明**：

- 数中节点数在 $[1, 5000]$ 范围内。
- $1 \le Node.val \le 10^7$。
- `root` 是二叉搜索树。
- $1 \le val \le 10^7$。

**示例**：

- 示例 1：

![img](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)

```python
输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg)

```python
输入：root = [4,2,7,1,3], val = 5
输出：[]
```

## 解题思路

### 思路 1：递归

1. 从根节点 `root` 开始向下递归遍历。
   1. 如果 `val` 等于当前节点的值，即 `val == root.val`，则返回 `root`；
   2. 如果 `val` 小于当前节点的值 ，即 `val < root.val`，则递归遍历左子树，继续查找；
   3. 如果 `val` 大于当前节点的值 ，即 `val > root.val`，则递归遍历右子树，继续查找。
2. 如果遍历到最后也没有找到，则返回空节点。

### 思路 1：代码

```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是二叉搜索树的节点数。
- **空间复杂度**：$O(n)$。