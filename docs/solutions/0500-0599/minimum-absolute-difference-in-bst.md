# [0530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)

- 标签：树、深度优先搜索、广度优先搜索、二叉搜索树、二叉树
- 难度：

## 题目链接

- [0530. 二叉搜索树的最小绝对差 - 力扣](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)

## 题目大意

**描述**：给定一个二叉搜索树的根节点 $root$。

**要求**：返回树中任意两不同节点值之间的最小差值。

**说明**：

- **差值**：是一个正数，其数值等于两值之差的绝对值。
- 树中节点的数目范围是 $[2, 10^4]$。
- $0 \le Node.val \le 10^5$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)

```python
输入：root = [4,2,6,1,3]
输出：1
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)

```python
输入：root = [1,0,48,null,null,12,49]
输出：1
```

## 解题思路

### 思路 1：中序遍历

先来看二叉搜索树的定义：

- 若左子树不为空，则左子树上所有节点值均小于它的根节点值；
- 若右子树不为空，则右子树上所有节点值均大于它的根节点值；
- 任意节点的左、右子树也分别为二叉搜索树。

题目要求二叉搜索树上任意两节点的差的绝对值的最小值。

二叉树的中序遍历顺序是：左 -> 根 -> 右，二叉搜索树的中序遍历最终得到就是一个升序数组。而升序数组中绝对值差的最小值就是比较相邻两节点差值的绝对值，找出其中最小值。

那么我们就可以先对二叉搜索树进行中序遍历，并保存中序遍历的结果。然后再比较相邻节点差值的最小值，从而找出最小值。

### 思路 1：代码

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder = self.inorderTraversal(root)
        ans = float('inf')
        for i in range(1, len(inorder)):
            ans = min(ans, abs(inorder[i - 1] - inorder[i]))

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为二叉搜索树中的节点数量。
- **空间复杂度**：$O(n)$。

