# [0563. 二叉树的坡度](https://leetcode.cn/problems/binary-tree-tilt/)

- 标签：树、深度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0563. 二叉树的坡度 - 力扣](https://leetcode.cn/problems/binary-tree-tilt/)

## 题目大意

**描述**：

给定一个二叉树的根节点 $root$。

**要求**：

计算并返回「整个树」的坡度。


**说明**：

- 一个树的「节点的坡度」定义为：该节点左子树的节点之和和右子树节点之和的「差的绝对值」。如果没有左子树的话，左子树的节点之和为 $0$；没有右子树的话也是一样。空结点的坡度是 $0$。
- 「整个树」的坡度就是其所有节点的坡度之和。
- 树中节点数目的范围在 $[0, 10^{4}]$ 内。
- $-10^{3} \le Node.val \le 10^{3}$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/10/20/tilt1.jpg)

```python
输入：root = [1,2,3]
输出：1
解释：
节点 2 的坡度：|0-0| = 0（没有子节点）
节点 3 的坡度：|0-0| = 0（没有子节点）
节点 1 的坡度：|2-3| = 1（左子树就是左子节点，所以和是 2 ；右子树就是右子节点，所以和是 3 ）
坡度总和：0 + 0 + 1 = 1
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/10/20/tilt2.jpg)

```python
输入：root = [4,2,9,3,5,null,7]
输出：15
解释：
节点 3 的坡度：|0-0| = 0（没有子节点）
节点 5 的坡度：|0-0| = 0（没有子节点）
节点 7 的坡度：|0-0| = 0（没有子节点）
节点 2 的坡度：|3-5| = 2（左子树就是左子节点，所以和是 3 ；右子树就是右子节点，所以和是 5 ）
节点 9 的坡度：|0-7| = 7（没有左子树，所以和是 0 ；右子树正好是右子节点，所以和是 7 ）
节点 4 的坡度：|(3+5+2)-(9+7)| = |10-16| = 6（左子树值为 3、5 和 2 ，和是 10 ；右子树值为 9 和 7 ，和是 16 ）
坡度总和：0 + 0 + 0 + 2 + 7 + 6 = 15
```

## 解题思路

### 思路 1：递归计算

对于每个节点，我们需要：

1. 计算左子树所有节点的和 $left\_sum$。
2. 计算右子树所有节点的和 $right\_sum$。
3. 计算该节点的坡度 $|left\_sum - right\_sum|$。
4. 返回该节点及其子树的总和 $node.val + left\_sum + right\_sum$。

使用后序遍历（DFS），在遍历过程中：

- 递归计算左右子树的和
- 计算当前节点的坡度并累加到总坡度中
- 返回当前子树的和

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal total_tilt
            if not node:
                return 0
            
            # 递归计算左右子树的和
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            # 计算当前节点的坡度并累加
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt
            
            # 返回当前子树的和
            return node.val + left_sum + right_sum
        
        dfs(root)
        return total_tilt
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树的节点数，需要遍历每个节点一次。
- **空间复杂度**：$O(h)$，其中 $h$ 是树的高度，递归栈的深度最多为 $h$。
