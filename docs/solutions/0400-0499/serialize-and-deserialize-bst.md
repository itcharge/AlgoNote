# [0449. 序列化和反序列化二叉搜索树](https://leetcode.cn/problems/serialize-and-deserialize-bst/)

- 标签：树、深度优先搜索、广度优先搜索、设计、二叉搜索树、字符串、二叉树
- 难度：中等

## 题目链接

- [0449. 序列化和反序列化二叉搜索树 - 力扣](https://leetcode.cn/problems/serialize-and-deserialize-bst/)

## 题目大意

**描述**：

序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

**要求**：

设计一个算法来序列化和反序列化「二叉搜索树」。对序列化 / 反序列化算法的工作方式没有限制。 

您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
编码的字符串应尽可能紧凑。

**说明**：

- 树中节点数范围是 $[0, 10^{4}]$。
- $0 \le Node.val \le 10^{4}$。
- 题目数据保证输入的树是一棵二叉搜索树。

**示例**：

- 示例 1：

```python
输入：root = [2,1,3]
输出：[2,1,3]
```

- 示例 2：

```python
输入：root = []
输出：[]
```

## 解题思路

### 思路 1：前序遍历 + BST 特性

**核心思想**：利用二叉搜索树（BST）的特性，BST 中左子树所有节点值都小于根节点值，右子树所有节点值都大于根节点值。因此，可以通过前序遍历序列来唯一确定一棵 BST。

**算法步骤**：

1. **序列化**：
   - 使用前序遍历（根 -> 左 -> 右）访问 BST 的所有节点。
   - 将每个节点的值转换为字符串，用逗号 `','` 分隔。
   - 返回序列化后的字符串 $data$。

2. **反序列化**：
   - 将字符串 $data$ 按逗号分割，得到前序遍历数组 $values$。
   - 对于前序遍历的结果，第一个值是根节点 $root$。
   - 利用 BST 特性，找到第一个大于 $root$ 的值，该位置之前的元素属于左子树，之后的元素属于右子树。
   - 递归构建左子树和右子树。

**关键点**：BST 的前序遍历序列具有唯一性，第一个值确定根节点后，根据 BST 特性可以唯一确定左右子树的分界点。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # 存储序列化结果
        res = []
        
        def preorder(node):
            if not node:
                return
            # 前序遍历：先访问根节点
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        # 用逗号连接所有节点值
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        # 将字符串按逗号分割，转换为整数列表
        values = [int(val) for val in data.split(',')]
        
        def build_tree(preorder_values):
            if not preorder_values:
                return None
            
            # 第一个值是根节点
            root_val = preorder_values[0]
            root = TreeNode(root_val)
            
            # 找到第一个大于根节点的值，即右子树的起点
            i = 1
            while i < len(preorder_values) and preorder_values[i] < root_val:
                i += 1
            
            # 左子树：从位置 1 到 i-1
            root.left = build_tree(preorder_values[1:i])
            # 右子树：从位置 i 到末尾
            root.right = build_tree(preorder_values[i:])
            
            return root
        
        return build_tree(values)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是 BST 的节点数。序列化需要遍历所有节点，时间复杂度为 $O(n)$；反序列化时，每个节点需要处理一次，时间复杂度为 $O(n)$。
- **空间复杂度**：$O(n)$。递归调用栈的最大深度为 $O(n)$（最坏情况下是链状 BST），序列化字符串的空间为 $O(n)$。
