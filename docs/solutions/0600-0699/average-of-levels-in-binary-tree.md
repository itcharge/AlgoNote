# [0637. 二叉树的层平均值](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [0637. 二叉树的层平均值 - 力扣](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)

## 题目大意

**描述**：

给定一个非空二叉树的根节点 $root$。

**要求**：

 以数组的形式返回每一层节点的平均值。与实际答案相差 $10^{-5}$ 以内的答案可以被接受。

**说明**：

- 树中节点数量在 $[1, 10^{4}]$ 范围内。
- $-2^{31} \le Node.val \le 2^{31} - 1$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

```python
输入：root = [3,9,20,null,null,15,7]
输出：[3.00000,14.50000,11.00000]
解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 [3, 14.5, 11] 。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)

```python
输入：root = [3,9,20,15,7]
输出：[3.00000,14.50000,11.00000]
```

## 解题思路

### 思路 1：广度优先搜索

#### 思路 1：算法描述

这道题目要求返回二叉树每一层节点的平均值。我们可以使用广度优先搜索（BFS）来层序遍历二叉树。

具体步骤如下：

1. 初始化结果数组 $ans$ 和队列 $queue$，将根节点加入队列。
2. 当队列不为空时，执行以下操作：
   - 记录当前层的节点数量 $size$。
   - 初始化当前层的节点值之和 $level\_sum = 0$。
   - 遍历当前层的所有节点：
     - 从队列中取出节点，将其值加到 $level\_sum$ 中。
     - 如果节点有左子节点，将左子节点加入队列。
     - 如果节点有右子节点，将右子节点加入队列。
   - 计算当前层的平均值 $level\_sum / size$，加入结果数组 $ans$。
3. 返回结果数组 $ans$。

#### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        ans = []
        queue = [root]
        
        while queue:
            size = len(queue)  # 当前层的节点数量
            level_sum = 0      # 当前层的节点值之和
            
            # 遍历当前层的所有节点
            for _ in range(size):
                node = queue.pop(0)
                level_sum += node.val
                
                # 将下一层的节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 计算当前层的平均值
            ans.append(level_sum / size)
        
        return ans
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是二叉树的节点数。需要遍历所有节点。
- **空间复杂度**：$O(n)$。队列中最多存储 $n$ 个节点。
