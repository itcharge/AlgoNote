# [0100. 相同的树](https://leetcode.cn/problems/same-tree/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0100. 相同的树 - 力扣](https://leetcode.cn/problems/same-tree/)

## 题目大意

**描述**：给定两个二叉树的根节点 $p$ 和 $q$。

**要求**：判断这两棵树是否相同。

**说明**：

- **两棵树相同的定义**：结构上相同；节点具有相同的值。
- 两棵树上的节点数目都在范围 $[0, 100]$ 内。
- $-10^4 \le Node.val \le 10^4$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```python
输入：p = [1,2,3], q = [1,2,3]
输出：True
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```python
输入：p = [1,2], q = [1,null,2]
输出：False
```

## 解题思路

### 思路 1：递归

1. 先判断两棵树的根节点是否相同。
2. 然后再递归地判断左右子树是否相同。

### 思路 1：代码

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(min(m, n))$，其中 $m$、$n$ 分别为两棵树中的节点数量。
- **空间复杂度**：$O(min(m, n))$。
