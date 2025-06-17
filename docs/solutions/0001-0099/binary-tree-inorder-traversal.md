# [0094. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

- 标签：栈、树、深度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0094. 二叉树的中序遍历 - 力扣](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

## 题目大意

**描述**：给定一个二叉树的根节点 `root`。

**要求**：返回该二叉树的中序遍历结果。

**说明**：

- 树中节点数目在范围 $[0, 100]$ 内。
- $-100 \le Node.val \le 100$。

**示例**：

- 示例 1：

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```python
输入：root = [1,null,2,3]
输出：[1,3,2]
```

- 示例 2：

```python
输入：root = []
输出：[]
```

## 解题思路

### 思路 1：递归遍历

二叉树的中序遍历递归实现步骤为：

1. 判断二叉树是否为空，为空则直接返回。
2. 先递归遍历左子树。
3. 然后访问根节点。
4. 最后递归遍历右子树。

### 思路 1：代码

```python
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
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是二叉树的节点数目。
- **空间复杂度**：$O(n)$。

### 思路 2：模拟栈迭代遍历

我们可以使用一个显式栈 $stack$ 来模拟二叉树的中序遍历递归的过程。

与前序遍历不同，访问根节点要放在左子树遍历完之后。因此我们需要保证：**在左子树访问之前，当前节点不能提前出栈**。

我们应该从根节点开始，循环遍历左子树，不断将当前子树的根节点放入栈中，直到当前节点无左子树时，从栈中弹出该节点并进行处理。

然后再访问该元素的右子树，并进行上述循环遍历左子树的操作。这样可以保证最终遍历顺序为中序遍历顺序。

二叉树的中序遍历显式栈实现步骤如下：

1. 判断二叉树是否为空，为空则直接返回。
2. 初始化维护一个空栈。
3. 当根节点或者栈不为空时：
   1. 如果当前节点不为空，则循环遍历左子树，并不断将当前子树的根节点入栈。
   1. 如果当前节点为空，说明当前节点无左子树，则弹出栈顶元素 $node$，并访问该元素，然后尝试访问该节点的右子树。

### 思路 2：代码

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                # 二叉树为空直接返回
            return []
        
        res = []
        stack = []

        while root or stack:        # 根节点或栈不为空
            while root:             
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left    # 找到最左侧节点
            
            node = stack.pop()      # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出
            res.append(node.val)    # 访问该节点
            root = node.right       # 尝试访问该节点的右子树
        return res
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是二叉树的节点数目。
- **空间复杂度**：$O(n)$。