# [0426. 将二叉搜索树转化为排序的双向链表](https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)

- 标签：栈、树、深度优先搜索、二叉搜索树、链表、二叉树、双向链表
- 难度：中等

## 题目链接

- [0426. 将二叉搜索树转化为排序的双向链表 - 力扣](https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)

## 题目大意

给定一棵二叉树的根节点 `root`。

要求：将这棵二叉树转换为一个已排序的双向循环链表。要求不能创建新的节点，只能调整树中节点指针的指向。

## 解题思路

通过中序递归遍历可以将二叉树升序排列输出。这道题需要在中序遍历的同时，将节点的左右指向进行改变。使用 `head`、`tail` 存放双向链表的头尾节点，然后从根节点开始，进行中序递归遍历。

具体做法如下：

- 如果当前节点为空，直接返回。
- 如果当前节点不为空：
  - 递归遍历左子树。
  - 如果尾节点不为空，则将尾节点与当前节点进行连接。
  - 如果尾节点为空，则初始化头节点。
  - 将当前节点标记为尾节点。
  - 递归遍历右子树。
- 最后将头节点和尾节点进行连接。

## 代码

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node: 'Node'):
            if not node:
                return

            dfs(node.left)
            if self.tail:
                self.tail.right = node
                node.left = self.tail
            else:
                self.head = node
            self.tail = node
            dfs(node.right)

        if not root:
            return None

        self.head, self.tail = None, None
        dfs(root)
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head
```

