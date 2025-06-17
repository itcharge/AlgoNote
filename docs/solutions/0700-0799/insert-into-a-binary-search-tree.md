# [0701. 二叉搜索树中的插入操作](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

- 标签：树、二叉搜索树、二叉树
- 难度：中等

## 题目链接

- [0701. 二叉搜索树中的插入操作 - 力扣](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

## 题目大意

**描述**：给定一个二叉搜索树的根节点和要插入树中的值 `val`。

**要求**：将 `val` 插入到二叉搜索树中，返回新的二叉搜索树的根节点。

**说明**：

- 树中的节点数将在 $[0, 10^4]$ 的范围内。
- $-10^8 \le Node.val \le 10^8$
- 所有值 `Node.val` 是独一无二的。
- $-10^8 \le val \le 10^8$。
- **保证** $val$ 在原始 BST 中不存在。

**示例**：

- 示例 1：

```python
输入：root = [4,2,7,1,3], val = 5
输出：[4,2,7,1,3,5]
解释：另一个满足题目要求可以通过的树是：
```

- 示例 2：

```python
输入：root = [40,20,60,10,30,50,70], val = 25
输出：[40,20,60,10,30,50,70,null,null,25]
```

## 解题思路

### 思路 1：递归

已知搜索二叉树的性质：

- 左子树上任意节点值均小于根节点，即 `root.left.val < root.val`。
- 右子树上任意节点值均大于根节点，即 `root.left.val > root.val`。

那么根据 `val` 和当前节点的大小关系，则可以确定将 `val` 插入到当前节点的哪个子树上。具体步骤如下：

1. 从根节点 `root` 开始向下递归遍历。根据 `val` 值和当前子树节点 `cur` 的大小关系：
   1. 如果 `val < cur.val`，则应在当前节点的左子树继续遍历判断。
      1. 如果左子树为空，则新建节点，赋值为 `val`。链接到该子树的父节点上。并停止遍历。
      2. 如果左子树不为空，则继续向左子树移动。
   2. 如果 `val >= cur.val`，则应在当前节点的右子树继续遍历判断。
      1. 如果右子树为空，则新建节点，赋值为 `val`。链接到该子树的父节点上。并停止遍历。
      2. 如果右子树不为空，则继续向左子树移动。
2. 遍历完返回根节点 `root`。

### 思路 1：代码

```python
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        cur = root
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
        return root
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是二叉搜索树的节点数。
- **空间复杂度**：$O(n)$。