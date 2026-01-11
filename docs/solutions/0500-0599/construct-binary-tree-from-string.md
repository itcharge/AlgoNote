# [0536. 从字符串生成二叉树](https://leetcode.cn/problems/construct-binary-tree-from-string/)

- 标签：栈、树、深度优先搜索、字符串、二叉树
- 难度：中等

## 题目链接

- [0536. 从字符串生成二叉树 - 力扣](https://leetcode.cn/problems/construct-binary-tree-from-string/)

## 题目大意

**描述**：

给定一个包括括号和整数字符串 $s$，你需要根据字符串构造一棵二叉树。

输入的字符串代表一棵二叉树，字符串的格式如下：

- 二叉树的节点值用数字表示（可能是负数）
- 开头的整数：代表根的值。
- 整数后跟着 0、1 或 2 对括号。
- 括号内表示子树。
   - 左子树用一对括号 `()` 包裹。
   - 右子树也用一对括号 `()` 包裹。
   - 如果只有右子树没有左子树，左子树位置用空括号 `()` 表示。

**要求**：

返回构造的二叉树的根节点。

**说明**：

- $0 \le s.length \le 3 \times 10^4$。
- $s$ 只包含数字、`'('`、`')'` 和 `'-'`。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/09/02/butree.jpg)

```python
输入： s = "4(2(3)(1))(6(5))"
输出： [4,2,6,3,1,5]
解释：
    4
   / \
  2   6
 / \  /
3  1 5
```

- 示例 2：

```python
输入： s = "4(2(3)(1))(6(5)(7))"
输出： [4,2,6,3,1,5,7]
```

## 解题思路

### 思路 1：递归解析

使用递归的方式解析字符串：

**解题步骤**：

1. 首先解析当前节点的值（可能是多位数或负数）。
2. 如果遇到左括号 `'('`，说明有子树，递归解析。
3. 第一个括号内的是左子树，第二个括号内的是右子树。
4. 使用索引 $index$ 追踪当前解析位置。

关键是正确匹配括号，找到每个子树的范围。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        self.index = 0
        
        def parse():
            if self.index >= len(s):
                return None
            
            # 解析节点值（可能是负数或多位数）
            start = self.index
            if s[self.index] == '-':
                self.index += 1
            while self.index < len(s) and s[self.index].isdigit():
                self.index += 1
            
            val = int(s[start:self.index])
            node = TreeNode(val)
            
            # 解析左子树
            if self.index < len(s) and s[self.index] == '(':
                self.index += 1  # 跳过 '('
                node.left = parse()
                self.index += 1  # 跳过 ')'
            
            # 解析右子树
            if self.index < len(s) and s[self.index] == '(':
                self.index += 1  # 跳过 '('
                node.right = parse()
                self.index += 1  # 跳过 ')'
            
            return node
        
        return parse()
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度。每个字符最多被访问一次。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度，递归栈的深度。
