# [0105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

- 标签：树、数组、哈希表、分治、二叉树
- 难度：中等

## 题目链接

- [0105. 从前序与中序遍历序列构造二叉树 - 力扣](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## 题目大意

**描述**：给定一棵二叉树的前序遍历结果 `preorder` 和中序遍历结果 `inorder`。

**要求**：构造出该二叉树并返回其根节点。

**说明**：

- $1 \le preorder.length \le 3000$。
- $inorder.length == preorder.length$。
- $-3000 \le preorder[i], inorder[i] \le 3000$。
- $preorder$ 和 $inorder$ 均无重复元素。
- $inorder$ 均出现在 $preorder$。
- $preorder$ 保证为二叉树的前序遍历序列。
- $inorder$ 保证为二叉树的中序遍历序列。

**示例**：

- 示例 1：

![img](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```python
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
```

- 示例 2：

```python
输入: preorder = [-1], inorder = [-1]
输出: [-1]
```

## 解题思路

### 思路 1：递归遍历

前序遍历的顺序是：根 -> 左 -> 右。中序遍历的顺序是：左 -> 根 -> 右。根据前序遍历的顺序，可以找到根节点位置。然后在中序遍历的结果中可以找到对应的根节点位置，就可以从根节点位置将二叉树分割成左子树、右子树。同时能得到左右子树的节点个数。此时构建当前节点，并递归建立左右子树，在左右子树对应位置继续递归遍历进行上述步骤，直到节点为空，具体操作步骤如下：

1. 从前序遍历顺序中当前根节点的位置在 $postorder[0]$。
2. 通过在中序遍历中查找上一步根节点对应的位置 $inorder[k]$，从而将二叉树的左右子树分隔开，并得到左右子树节点的个数。
3. 从上一步得到的左右子树个数将前序遍历结果中的左右子树分开。
4. 构建当前节点，并递归建立左右子树，在左右子树对应位置继续递归遍历并执行上述三步，直到节点为空。

### 思路 1：代码

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def createTree(preorder, inorder, n):
            if n == 0:
                return None
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            node = TreeNode(inorder[k])
            node.left = createTree(preorder[1: k+1], inorder[0: k], k)
            node.right = createTree(preorder[k+1:], inorder[k+1:], n-k-1)
            return node
        return createTree(preorder, inorder, len(inorder))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是二叉树的节点数目。每次递归都需要在中序遍历数组 `inorder` 中查找根节点的位置，最坏情况下需要遍历整个数组，因此每一层递归的查找操作为 $O(n)$，而递归总共 $n$ 层，所以总时间复杂度为 $O(n^2)$。  
- **空间复杂度**：$O(n^2)$。递归过程中每次切片会新建子数组，最坏情况下每层递归都要复制 $O(n)$ 大小的数组，共 $O(n)$ 层，因此总空间复杂度为 $O(n^2)$。如果不考虑切片额外空间，仅考虑递归栈，则为 $O(n)$。

### 思路 2：递归遍历 + 哈希表

在思路 1 中，每次递归都需要在中序遍历数组 $inorder$ 中查找根节点的位置，这导致了 $O(n)$ 的查找时间。我们可以使用哈希表来优化这个过程，将中序遍历数组中每个元素的值与其索引位置建立映射关系，这样查找根节点位置的时间复杂度就可以优化到 $O(1)$。

具体操作步骤如下：

1. 首先遍历中序遍历数组，将每个元素的值与其索引位置建立映射关系，存储在哈希表中。
2. 从前序遍历顺序中当前根节点的位置在 $preorder[0]$。
3. 通过哈希表查找根节点在中序遍历中的位置 $inorder[k]$，从而将二叉树的左右子树分隔开，并得到左右子树节点的个数。
4. 从上一步得到的左右子树个数将前序遍历结果中的左右子树分开。
5. 构建当前节点，并递归建立左右子树，在左右子树对应位置继续递归遍历并执行上述步骤，直到节点为空。

### 思路 2：代码

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 构建中序遍历数组中元素值与索引的映射关系
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def createTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历的第一个节点就是根节点
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)
            
            # 在中序遍历中找到根节点的位置
            root_index = inorder_map[root_val]
            
            # 计算左子树的节点个数
            left_size = root_index - inorder_left
            
            # 递归构建左子树
            root.left = createTree(preorder_left + 1, preorder_left + left_size, 
                                 inorder_left, root_index - 1)
            
            # 递归构建右子树
            root.right = createTree(preorder_left + left_size + 1, preorder_right, 
                                  root_index + 1, inorder_right)
            
            return root
        
        return createTree(0, len(preorder) - 1, 0, len(inorder) - 1)
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数目。每个节点都会被访问一次，且通过哈希表查找根节点位置的时间复杂度为 $O(1)$，因此总时间复杂度为 $O(n)$。
- **空间复杂度**：$O(n)$。哈希表需要 $O(n)$ 的空间存储中序遍历数组中元素值与索引的映射关系，递归栈的深度为 $O(h)$，其中 $h$ 是二叉树的高度。在最坏情况下，二叉树退化为链表，此时 $h = n$，所以总空间复杂度为 $O(n)$。
