# [0919. 完全二叉树插入器](https://leetcode.cn/problems/complete-binary-tree-inserter/)

- 标签：树、广度优先搜索、设计、二叉树
- 难度：中等

## 题目链接

- [0919. 完全二叉树插入器 - 力扣](https://leetcode.cn/problems/complete-binary-tree-inserter/)

## 题目大意

要求：设计一个用完全二叉树初始化的数据结构 `CBTInserter`，并支持以下几种操作：

- `CBTInserter(TreeNode root)` 使用根节点为 `root` 的给定树初始化该数据结构；
- `CBTInserter.insert(int v)`  向树中插入一个新节点，节点类型为 `TreeNode`，值为 `v`。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
- `CBTInserter.get_root()` 返回树的根节点。

## 解题思路

使用数组标记完全二叉树中节点的序号，初始化数组为 `[None]`。完全二叉树中节点的序号从 `1` 开始，对于序号为 `k` 的节点，其左子节点序号为 `2k`，右子节点的序号为 `2k + 1`，其父节点的序号为 `k // 2`。

然后在初始化和插入节点的同时，按顺序向数组中插入节点。

## 代码

```python
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.queue = [root]
        self.nodelist = [None]

        while self.queue:
            node = self.queue.pop(0)
            self.nodelist.append(node)
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)


    def insert(self, v: int) -> int:
        self.nodelist.append(TreeNode(v))
        index = len(self.nodelist) - 1
        father = self.nodelist[index // 2]
        if index % 2 == 0:
            father.left = self.nodelist[-1]
        else:
            father.right = self.nodelist[-1]
        return father.val


    def get_root(self) -> TreeNode:
        return self.nodelist[1]
```

