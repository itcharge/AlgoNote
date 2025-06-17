# [0144. 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

- 标签：栈、树、深度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0144. 二叉树的前序遍历 - 力扣](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

## 题目大意

**描述**：给定一个二叉树的根节点 `root`。

**要求**：返回该二叉树的前序遍历结果。

**说明**：

- 树中节点数目在范围 $[0, 100]$ 内。
- $-100 \le Node.val \le 100$。

**示例**：

- 示例 1：

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```python
输入：root = [1,null,2,3]
输出：[1,2,3]
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

```python
输入：root = [1,null,2]
输出：[1,2]
```

## 解题思路

### 思路 1：递归遍历

二叉树的前序遍历递归实现步骤为：

1. 判断二叉树是否为空，为空则直接返回。
2. 先访问根节点。
3. 然后递归遍历左子树。
4. 最后递归遍历右子树。

### 思路 1：代码

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是二叉树的节点数目。
- **空间复杂度**：$O(n)$。

### 思路 2：模拟栈迭代遍历

二叉树的前序遍历递归实现的过程，实际上就是调用系统栈的过程。我们也可以使用一个显式栈 `stack` 来模拟递归的过程。

前序遍历的顺序为：根节点 - 左子树 - 右子树，而根据栈的「先入后出」特点，所以入栈的顺序应该为：先放入右子树，再放入左子树。这样可以保证最终为前序遍历顺序。 

二叉树的前序遍历显式栈实现步骤如下：

1. 判断二叉树是否为空，为空则直接返回。
2. 初始化维护一个栈，将根节点入栈。
3. 当栈不为空时：
   1. 弹出栈顶元素 `node`，并访问该元素。
   2. 如果 `node` 的右子树不为空，则将 `node` 的右子树入栈。
   3. 如果 `node` 的左子树不为空，则将 `node` 的左子树入栈。

### 思路 2：代码

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                        # 二叉树为空直接返回
            return []
            
        res = []
        stack = [root]

        while stack:                        # 栈不为空
            node = stack.pop()              # 弹出根节点
            res.append(node.val)            # 访问根节点
            if node.right:
                stack.append(node.right)    # 右子树入栈
            if node.left:
                stack.append(node.left)     # 左子树入栈

        return res
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是二叉树的节点数目。
- **空间复杂度**：$O(n)$。