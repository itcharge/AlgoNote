# [0589. N 叉树的前序遍历](https://leetcode.cn/problems/n-ary-tree-preorder-traversal/)

- 标签：栈、树、深度优先搜索
- 难度：简单

## 题目链接

- [0589. N 叉树的前序遍历 - 力扣](https://leetcode.cn/problems/n-ary-tree-preorder-traversal/)

## 题目大意

给定一棵 N 叉树的根节点 `root`。

要求：返回其节点值的前序遍历。

进阶：使用迭代法完成。

## 解题思路

递归法很好写。迭代法需要借助于栈。

- 用栈保存根节点 `root`。然后遍历栈。
- 循环判断栈是否为空。
- 如果栈不为空，取出栈顶节点，将节点值加入答案数组。
- 逆序遍历栈顶节点的子节点，将其依次放入栈中（逆序保证取出顺序为正）。
- 然后继续第 2 ~ 4 步，直到栈为空。

最后输出答案数组。

## 代码

```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = []
        if not root:
            return res
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            for i in range(len(node.children) - 1, -1, -1):
                if node.children[i]:
                    stack.append(node.children[i])
        return res
```

