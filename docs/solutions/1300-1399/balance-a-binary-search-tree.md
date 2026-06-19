# [1382. 将二叉搜索树变平衡](https://leetcode.cn/problems/balance-a-binary-search-tree/)

- 标签：贪心、树、深度优先搜索、二叉搜索树、分治、二叉树
- 难度：中等

## 题目链接

- [1382. 将二叉搜索树变平衡 - 力扣](https://leetcode.cn/problems/balance-a-binary-search-tree/)

## 题目大意

**描述**：给定一棵二叉搜索树 $root$。

**要求**：将其调整为一棵平衡二叉搜索树（左右子树高度差不超过 $1$），返回任意一棵合法结果。

**说明**：
- 节点数在 $[1, 10^4]$ 范围内。
- 节点值唯一。

**示例**：
- 示例：
```python
输入：root = [1,null,2,null,3,null,4]
输出：[2,1,3,null,null,null,4]
```

## 解题思路

### 思路 1：中序遍历 + 递归构建

#### 1. 核心思想

BST 的中序遍历结果是严格递增的序列。利用这个性质：
1. 中序遍历原 BST，得到有序数组。
2. 用有序数组递归构建平衡 BST：每次取中间元素作为根节点，左半部分构建左子树，右半部分构建右子树。

#### 2. 具体步骤

**第 1 步**：中序遍历，收集节点值到 $vals$ 数组。

**第 2 步**：定义 $build(l, r)$ 构建子树：
- 如果 $l > r$，返回 $None$。
- $mid = (l + r) // 2$，创建值为 $vals[mid]$ 的节点。
- 左子树 = $build(l, mid-1)$，右子树 = $build(mid+1, r)$。
- 返回该节点。

**第 3 步**：调用 $build(0, len(vals)-1)$。

### 思路 1：代码

```python
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        # 中序遍历
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        # 递归构建平衡 BST
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(vals[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        return build(0, len(vals) - 1)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$，中序遍历 $O(n)$，构建 $O(n)$。
- **空间复杂度**：$O(n)$，存储中序序列和递归栈。
