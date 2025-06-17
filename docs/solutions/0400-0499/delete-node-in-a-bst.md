# [0450. 删除二叉搜索树中的节点](https://leetcode.cn/problems/delete-node-in-a-bst/)

- 标签：树、二叉搜索树、二叉树
- 难度：中等

## 题目链接

- [0450. 删除二叉搜索树中的节点 - 力扣](https://leetcode.cn/problems/delete-node-in-a-bst/)

## 题目大意

**描述**：给定一个二叉搜索树的根节点 `root`，以及一个值 `key`。

**要求**：从二叉搜索树中删除 key 对应的节点。并保证删除后的树仍是二叉搜索树。要求算法时间复杂度为 $0(h)$，$h$ 为树的高度。最后返回二叉搜索树的根节点。

**说明**：

- 节点数的范围 $[0, 10^4]$。
- $-10^5 \le Node.val \le 10^5$。
- 节点值唯一。
- `root` 是合法的二叉搜索树。
- $-10^5 \le key \le 10^5$。

**示例**：

- 示例 1：

![img](https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg)

```python
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如上图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。
```

- 示例 2：

```python
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
```

## 解题思路

### 思路 1：递归

删除分两个步骤：查找和删除。查找通过递归查找，删除的话需要考虑情况。

1.  从根节点 `root` 开始，递归遍历搜索二叉树。
   1. 如果当前节点节点为空，返回当前节点。
   2. 如果当前节点值大于 `key`，则去左子树中搜索并删除，此时 `root.left` 也要跟着递归更新，递归完成后返回当前节点。
   3. 如果当前节点值小于 `key`，则去右子树中搜索并删除，此时 `root.right` 也要跟着递归更新，递归完成后返回当前节点。
   4. 如果当前节点值等于 `key`，则该节点就是待删除节点。
      1. 如果当前节点的左子树为空，则删除该节点之后，则右子树代替当前节点位置，返回右子树。
      2. 如果当前节点的右子树为空，则删除该节点之后，则左子树代替当前节点位置，返回左子树。
      3. 如果当前节点的左右子树都有，则将左子树转移到右子树最左侧的叶子节点位置上，然后右子树代替当前节点位置。返回右子树。

### 思路 1：代码

```python
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是二叉搜索树的节点数。
- **空间复杂度**：$O(n)$。
