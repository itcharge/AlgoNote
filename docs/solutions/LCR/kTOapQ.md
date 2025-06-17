# [LCR 055. 二叉搜索树迭代器](https://leetcode.cn/problems/kTOapQ/)

- 标签：栈、树、设计、二叉搜索树、二叉树、迭代器
- 难度：中等

## 题目链接

- [LCR 055. 二叉搜索树迭代器 - 力扣](https://leetcode.cn/problems/kTOapQ/)

## 题目大意

要求：实现一个二叉搜索树的迭代器 `BSTIterator`。表示一个按中序遍历二叉搜索树（BST）的迭代器：

- `def __init__(self, root: TreeNode):`：初始化 `BSTIterator` 类的一个对象，会给出二叉搜索树的根节点。
- `def hasNext(self) -> bool:`：如果向右指针遍历存在数字，则返回 `True`，否则返回 `False`。
- `def next(self) -> int:`：将指针向右移动，返回指针处的数字。

## 解题思路

中序遍历的顺序是：左、根、右。我们使用一个栈来保存节点，以便于迭代的时候取出对应节点。

- 初始的遍历当前节点的左子树，将其路径上的节点存储到栈中。
- 调用 next 方法的时候，从栈顶取出节点，因为之前已经将路径上的左子树全部存入了栈中，所以此时该节点的左子树为空，这时候取出节点右子树，再将右子树的左子树进行递归遍历，并将其路径上的节点存储到栈中。
- 调用 hasNext 的方法的时候，直接判断栈中是否有值即可。

## 代码

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.in_order(root)


    def in_order(self, node):
        while node:
            self.stack.append(node)
            node = node.left


    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.in_order(node.right)
        return node.val


    def hasNext(self) -> bool:
        return len(self.stack) != 0
```

