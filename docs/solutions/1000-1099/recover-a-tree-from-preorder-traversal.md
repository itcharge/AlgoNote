# [1028. 从先序遍历还原二叉树](https://leetcode.cn/problems/recover-a-tree-from-preorder-traversal/)

- 标签：树、深度优先搜索、字符串、二叉树
- 难度：困难

## 题目链接

- [1028. 从先序遍历还原二叉树 - 力扣](https://leetcode.cn/problems/recover-a-tree-from-preorder-traversal/)

## 题目大意

对一棵二叉树进行深度优先搜索。在遍历的过程中，遇到节点，先输出与该节点深度相同数量的短线，再输出该节点的值。如果节点深度为 `D`，则子节点深度为 `D + 1`。根节点的深度为 `0`。如果节点只有一个子节点，则该子节点一定为左子节点。

现在给定深度优先搜索输出的字符串 `traversal`。

要求：还原二叉树，并返回其根节点 `root`。

## 解题思路

用栈存储需要构建子树的节点。并记录下上一节点深度和当前节点深度。

然后遍历深度优先搜索的输出字符串。

- 先将开始部分的数字作为根节点值，构建一个根节点 `root`，并将根节点插入到栈中。
- 如果遇到 `-`，则更新当前节点深度。

- 然后如果遇到数字，则将数字逐位转为整数。并且在最后进行判断。
  - 如果当前节点深度 > 前一节点深度：
    - 将栈顶节点出栈。
    - 构建一个新节点，值为当前整数。将新节点插入到栈顶节点的左子树上。
    - 将当前节点和新节点插入到栈中。
  - 如果当前节点深度 <= 前一节点深度：
    - 将当前节点深度个数的节点从栈中弹出。
    - 构建一个新节点，值为当前整数。并将新节点插入到最后弹出节点的右子树上。
    - 将当前节点和新节点插入到栈中。
- 最后输出根节点 `root`。

## 代码

```python
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []

        index, num = 0, 0
        pre_level, cur_level = 0, 0

        size = len(traversal)
        while index < size and traversal[index] != '-':
            num = num * 10 + ord(traversal[index]) - ord('0')
            index += 1

        root = TreeNode(num)
        stack.append(root)

        while index < size:
            if traversal[index] == '-':
                cur_level += 1
                index += 1
            else:
                num = 0
                while index < size and traversal[index] != '-':
                    num = num * 10 + ord(traversal[index]) - ord('0')
                    index += 1

                if cur_level > pre_level:
                    node = stack.pop()
                    node.left = TreeNode(num)
                    stack.append(node)
                    stack.append(node.left)
                    pre_level = cur_level
                    cur_level = 0
                else:
                    while len(stack) > cur_level:
                        stack.pop()
                    node = stack.pop()
                    node.right = TreeNode(num)
                    stack.append(node)
                    stack.append(node.right)
                    pre_level = cur_level
                    cur_level = 0
        return root
```

