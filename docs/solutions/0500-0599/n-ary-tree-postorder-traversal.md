# [0590. N 叉树的后序遍历](https://leetcode.cn/problems/n-ary-tree-postorder-traversal/)

- 标签：栈、树、深度优先搜索
- 难度：简单

## 题目链接

- [0590. N 叉树的后序遍历 - 力扣](https://leetcode.cn/problems/n-ary-tree-postorder-traversal/)

## 题目大意

给定一个 N 叉树的根节点 `root`。

要求：返回其节点值的后序遍历。

## 解题思路

N 叉树的后序遍历顺序为：子节点顺序递归遍历 -> 根节点。

一个取巧的方法是先按照：根节点 -> 子节点逆序递归遍历 的顺序将遍历顺序存储到答案数组。

然后再将其进行翻转就变为了后序遍历顺序。具体操作如下：

- 用栈保存根节点 `root`。然后遍历栈。
- 循环判断栈是否为空。
- 如果栈不为空，取出栈顶节点，将节点值加入答案数组。
- 顺序遍历栈顶节点的子节点，将其依次放入栈中（顺序遍历保证取出顺序为逆序）。
- 然后继续第 2 ~ 4 步，直到栈为空。

最后将答案数组逆序返回。

## 代码

```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        stack = []
        if not root:
            return res

        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)

        return res[::-1]
```

