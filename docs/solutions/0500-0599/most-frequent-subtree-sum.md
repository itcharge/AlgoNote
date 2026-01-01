# [0508. 出现次数最多的子树元素和](https://leetcode.cn/problems/most-frequent-subtree-sum/)

- 标签：树、深度优先搜索、哈希表、二叉树
- 难度：中等

## 题目链接

- [0508. 出现次数最多的子树元素和 - 力扣](https://leetcode.cn/problems/most-frequent-subtree-sum/)

## 题目大意

**描述**：

给定一个二叉树的根结点 $root$。

**要求**：

返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

**说明**：

- 一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
- 节点数在 $[1, 10^{4}]$ 范围内。
- $-10^{5} \le Node.val \le 10^{5}$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg)

```python
输入: root = [5,2,-3]
输出: [2,-3,4]
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg)

```python
输入: root = [5,2,-5]
输出: [2]
```

## 解题思路

### 思路 1：递归 + 哈希表

对于每个节点，我们需要计算以该节点为根的子树元素和。使用后序遍历（DFS）：
1. 递归计算左右子树的元素和
2. 当前节点的子树元素和 = $node.val + left\_sum + right\_sum$
3. 使用哈希表统计每个子树元素和出现的次数
4. 遍历完成后，找到出现次数最多的子树元素和

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_count = defaultdict(int)
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # 递归计算左右子树的元素和
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            # 当前节点的子树元素和
            subtree_sum = node.val + left_sum + right_sum
            
            # 统计子树元素和的出现次数
            sum_count[subtree_sum] += 1
            
            return subtree_sum
        
        dfs(root)
        
        # 找到出现次数最多的子树元素和
        if not sum_count:
            return []
        
        max_count = max(sum_count.values())
        return [sum_val for sum_val, count in sum_count.items() if count == max_count]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树的节点数，需要遍历每个节点一次。
- **空间复杂度**：$O(n)$，递归栈的深度最多为 $n$，哈希表最多存储 $n$ 个不同的子树元素和。
