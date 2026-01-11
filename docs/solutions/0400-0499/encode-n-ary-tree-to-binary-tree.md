# [0431. 将 N 叉树编码为二叉树](https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree/)

- 标签：树、深度优先搜索、广度优先搜索、设计、二叉树
- 难度：困难

## 题目链接

- [0431. 将 N 叉树编码为二叉树 - 力扣](https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree/)

## 题目大意

**描述**：

给定一个 N 叉树的根节点 $root$。

**要求**：

设计一个算法将 N 叉树编码为二叉树，并能够将二叉树解码回 N 叉树。编码和解码算法的实现没有限制，只需要保证 N 叉树可以编码为二叉树并且能够解码回原来的 N 叉树。

**说明**：

- 一个 N 叉树是指每个节点都有不超过 N 个孩子节点的有根树。
- 一个二叉树是指每个节点都有不超过 2 个孩子节点的有根树。
- N 叉树的高度小于等于 $1000$。
- 节点总数在范围 $[0, 10^4]$ 内。

**示例**：

- 示例 1：

```python
输入：root = [1,null,3,2,4,null,5,6]
输出：[1,null,3,2,4,null,5,6]
解释：编码后再解码，得到原来的 N 叉树。
```

## 解题思路

### 思路 1：左孩子右兄弟表示法

将 N 叉树编码为二叉树，需要设计一种编码方式，使得可以唯一地还原。

**核心思路**：

- 使用"左孩子右兄弟"表示法：
  - 二叉树的左子节点：存储 N 叉树节点的第一个子节点。
  - 二叉树的右子节点：存储 N 叉树节点的下一个兄弟节点。

**编码步骤**：

1. 对于 N 叉树的每个节点：
   - 如果有子节点，将第一个子节点作为二叉树的左子节点。
   - 将所有兄弟节点用右子节点连接起来。
2. 递归处理所有节点。

**解码步骤**：

1. 二叉树的左子节点对应 N 叉树的第一个子节点。
2. 二叉树的右子节点对应 N 叉树的兄弟节点。
3. 递归还原所有节点。

### 思路 1：代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # 将 N 叉树编码为二叉树
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        
        # 创建二叉树根节点
        binary_root = TreeNode(root.val)
        
        # 如果有子节点
        if root.children:
            # 第一个子节点作为左子节点
            binary_root.left = self.encode(root.children[0])
            
            # 将兄弟节点用右子节点连接
            current = binary_root.left
            for i in range(1, len(root.children)):
                current.right = self.encode(root.children[i])
                current = current.right
        
        return binary_root
    
    # 将二叉树解码为 N 叉树
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None
        
        # 创建 N 叉树根节点
        root = Node(data.val, [])
        
        # 左子节点是第一个子节点
        current = data.left
        while current:
            # 递归解码子节点
            root.children.append(self.decode(current))
            # 右子节点是兄弟节点
            current = current.right
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是节点数。每个节点访问一次。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度，递归栈的深度。
