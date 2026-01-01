# [0559. N 叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/)

- 标签：树、深度优先搜索、广度优先搜索
- 难度：简单

## 题目链接

- [0559. N 叉树的最大深度 - 力扣](https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/)

## 题目大意

**描述**：

给定一个 N 叉树。

**要求**：

找到其最大深度。

**说明**：

- 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
- N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
- 树的深度不会超过 $10^{3}$。
- 树的节点数目位于 $[0, 10^{4}]$ 之间。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```python
输入：root = [1,null,3,2,4,null,5,6]
输出：3
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```python
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：5
```

## 解题思路

### 思路 1：递归（深度优先搜索）

对于 N 叉树，最大深度等于根节点到最远叶子节点的路径长度。

使用递归方法：

- 如果节点为空，返回深度 $0$。
- 否则，递归计算所有子节点的最大深度 $max\_child\_depth$。
- 当前节点的深度为 $1 + max\_child\_depth$。

### 思路 1：代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        # 如果没有子节点，深度为 1
        if not root.children:
            return 1
        
        # 递归计算所有子节点的最大深度
        max_child_depth = 0
        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))
        
        # 当前节点深度 = 1 + 子节点最大深度
        return 1 + max_child_depth
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树的节点数，需要遍历每个节点一次。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度，递归栈的深度最多为 $h$。
