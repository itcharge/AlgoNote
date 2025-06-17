# [0652. 寻找重复的子树](https://leetcode.cn/problems/find-duplicate-subtrees/)

- 标签：树、深度优先搜索、哈希表、二叉树
- 难度：中等

## 题目链接

- [0652. 寻找重复的子树 - 力扣](https://leetcode.cn/problems/find-duplicate-subtrees/)

## 题目大意

给定一个二叉树，返回所有重复的子树。对于重复的子树，只需返回其中任意一棵的根节点。

## 解题思路

对二叉树进行先序遍历，对遍历的所有的子树进行序列化处理，将序列化处理后的字符串作为哈希表的键，记录每棵子树出现的次数。

当出现第二次时，则说明该子树是重复的子树，将其加入答案数组。最后返回答案数组即可。

## 代码

```python
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        tree_dict = dict()
        res = []
        def preorder(node):
            if not node:
                return '#'
            sub_tree = str(node.val) + ',' + preorder(node.left) + ',' + preorder(node.right)
            if sub_tree in tree_dict:
                tree_dict[sub_tree] += 1
            else:
                tree_dict[sub_tree] = 1
            if tree_dict[sub_tree] == 2:
                res.append(node)
            return sub_tree
        preorder(root)
        return res
```

