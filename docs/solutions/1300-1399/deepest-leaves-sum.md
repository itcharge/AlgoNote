# [1302. 层数最深叶子节点的和](https://leetcode.cn/problems/deepest-leaves-sum/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [1302. 层数最深叶子节点的和 - 力扣](https://leetcode.cn/problems/deepest-leaves-sum/)

## 题目大意

**描述**：给定一棵二叉树的根节点 $root$。

**要求**：返回所有最深叶子节点值之和。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/12/28/1483_ex1.png)

```python
输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
```

- 示例 2：

```python
输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：19
```


## 解题思路

### 思路 1：BFS 层序遍历

#### 1. 核心思想

层序遍历二叉树，最后一层的所有节点之和就是答案。可以用 BFS 逐层遍历，保留每层的和。

#### 2. 具体步骤

**第 1 步**：队列初始化为 $root$。

**第 2 步**：BFS 循环：
- 记录当前层的节点数和 $level\_sum$。
- 将当前层的所有子节点加入队列。
- 遍历完一层后，更新 $ans = level\_sum$。

**第 3 步**：循环结束返回 $ans$。

### 思路 1：代码

```python
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans = level_sum
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
