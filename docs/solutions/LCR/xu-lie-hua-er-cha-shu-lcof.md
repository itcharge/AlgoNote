# [LCR 156. 序列化与反序列化二叉树](https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/)

- 标签：树、深度优先搜索、广度优先搜索、设计、字符串、二叉树
- 难度：困难

## 题目链接

- [LCR 156. 序列化与反序列化二叉树 - 力扣](https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/)

## 题目大意

给定一棵二叉树的根节点 `root`。

要求：设计一个算法，来实现二叉树的序列化与反序列化。

## 解题思路

1. 序列化：将二叉树转为字符串数据表示

按照前序递归遍历二叉树，并将根节点跟左右子树的值链接起来（中间用 `,` 隔开）。

注意：如果遇到空节点，则标记为 'None'，这样在反序列化时才能唯一确定一棵二叉树。

2. 反序列化：将字符串数据转为二叉树结构

先将字符串按 `,` 分割成数组。然后递归处理每一个元素。

- 从数组左侧取出一个元素。
  - 如果当前元素为 'None'，则返回 None。
  - 如果当前元素不为空，则新建一个二叉树节点作为根节点，保存值为当前元素值。并递归遍历左右子树，不断重复从数组中取出元素，进行判断。
  - 最后返回当前根节点。

## 代码

```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(datalist):
            val = datalist.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = dfs(datalist)
            root.right = dfs(datalist)
            return root

        datalist = data.split(',')
        return dfs(datalist)
```

