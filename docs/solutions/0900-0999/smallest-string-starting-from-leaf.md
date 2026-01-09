# [0988. 从叶结点开始的最小字符串](https://leetcode.cn/problems/smallest-string-starting-from-leaf/)

- 标签：树、深度优先搜索、字符串、回溯、二叉树
- 难度：中等

## 题目链接

- [0988. 从叶结点开始的最小字符串 - 力扣](https://leetcode.cn/problems/smallest-string-starting-from-leaf/)

## 题目大意

**描述**：

给定一颗根结点为 $root$ 的二叉树，树中的每一个结点都有一个 $[0, 25]$ 范围内的值，分别代表字母 `'a'` 到 `'z'`。

**要求**：

返回「按字典序最小」的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

**说明**：

- 注意：字符串中任何较短的前缀在「字典序上」都是「较小」的：
   - 例如，在字典序上 `"ab"` 比 `"aba"` 要小。叶结点是指没有子结点的结点。
- 节点的叶节点是没有子节点的节点。
- 给定树的结点数在 $[1, 8500]$ 范围内。
- $0 \le Node.val \le 25$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/02/tree1.png)

```python
输入：root = [0,1,2,3,4,3,4]
输出："dba"
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2019/01/30/tree2.png)

```python
输入：root = [25,1,3,1,3,0,2]
输出："adz"
```

## 解题思路

### 思路 1：深度优先搜索

使用 DFS 遍历二叉树，从叶子节点到根节点构建字符串，然后比较所有路径的字典序。

1. **DFS 遍历**：从根节点开始，递归遍历到叶子节点。
2. **构建字符串**：在递归过程中，将节点值转换为字符并拼接。
3. **叶子节点判断**：当到达叶子节点时，将当前路径（反转后）与最小字符串比较。
4. **字典序比较**：使用 Python 的字符串比较功能，更新最小字符串。

**注意**：由于是从叶子到根，需要在递归返回时构建字符串，或者在递归过程中构建后反转。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result = None
        
        def dfs(node, path):
            if not node:
                return
            
            # 将当前节点值转换为字符并添加到路径
            path = chr(ord('a') + node.val) + path
            
            # 如果是叶子节点，更新结果
            if not node.left and not node.right:
                if self.result is None or path < self.result:
                    self.result = path
                return
            
            # 递归遍历左右子树
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
        
        dfs(root, "")
        return self.result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是树中节点的数量。需要遍历所有节点，每次字符串拼接需要 $O(n)$ 时间。
- **空间复杂度**：$O(n)$，递归栈的深度最多为树的高度，字符串长度最多为 $n$。
