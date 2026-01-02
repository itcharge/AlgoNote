# [0606. 根据二叉树创建字符串](https://leetcode.cn/problems/construct-string-from-binary-tree/)

- 标签：树、深度优先搜索、字符串、二叉树
- 难度：中等

## 题目链接

- [0606. 根据二叉树创建字符串 - 力扣](https://leetcode.cn/problems/construct-string-from-binary-tree/)

## 题目大意

**描述**：

给定二叉树的根节点 $root$。

**要求**：

采用前序遍历的方式，将二叉树转化为一个由括号和整数组成的字符串，返回构造出的字符串。

空节点使用一对空括号对 `"()"` 表示，转化后需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

**说明**：

- 树中节点的数目范围是 $[1, 10^{4}]$。
- $-10^{3} \le Node.val \le 10^{3}$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/05/03/cons1-tree.jpg)

```python
输入：root = [1,2,3,4]
输出："1(2(4))(3)"
解释：初步转化后得到 "1(2(4)())(3()())" ，但省略所有不必要的空括号对后，字符串应该是"1(2(4))(3)" 。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/05/03/cons2-tree.jpg)

```python
输入：root = [1,2,3,null,4]
输出："1(2()(4))(3)"
解释：和第一个示例类似，但是无法省略第一个空括号对，否则会破坏输入与输出一一映射的关系。
```

## 解题思路

### 思路 1：深度优先搜索

#### 思路 1：算法描述

这道题目要求将二叉树转化为一个由括号和整数组成的字符串，采用前序遍历的方式。

我们可以使用深度优先搜索（DFS）来递归构造字符串。需要注意的是，要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

具体规则如下：

1. 如果节点有左子树，则需要在左子树的字符串外加上括号。
2. 如果节点有右子树，则需要在右子树的字符串外加上括号。
3. 如果节点没有左子树但有右子树，则需要在左子树的位置加上空括号 `"()"`。
4. 如果节点既没有左子树也没有右子树，则不需要加括号。

#### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        # 只有根节点
        if not root.left and not root.right:
            return str(root.val)
        
        # 有左子树，没有右子树
        if root.left and not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        
        # 有右子树（无论是否有左子树）
        return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数。需要遍历所有节点。
- **空间复杂度**：$O(n)$。递归调用栈的深度最多为 $n$。
