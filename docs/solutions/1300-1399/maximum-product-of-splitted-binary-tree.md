# [1339. 分裂二叉树的最大乘积](https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [1339. 分裂二叉树的最大乘积 - 力扣](https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/)

## 题目大意

**描述**：给定一棵二叉树 $root$，删除一条边将树分成两棵子树，求两棵子树的和之积的最大值。

**说明**：
- 节点数 $[2, 5 \times 10^4]$。
- 节点值 $\ge 1$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/02/sample_1_1699.png)

```python
输入：root = [1,2,3,4,5,6]
输出：110
解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/02/sample_2_1699.png)

```python
输入：root = [1,null,2,3,4,null,null,5,6]
输出：90
解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）
```


## 解题思路

### 思路 1：DFS

#### 1. 核心思想

先计算整棵树的总和 $total$。再 DFS 遍历每个节点，计算以该节点为根的子树和 $sub\_sum$，另一部分和为 $total - sub\_sum$，乘积为 $sub\_sum \times (total - sub\_sum)$。

#### 2. 具体步骤

**第 1 步**：DFS 计算 $total$。

**第 2 步**：第二次 DFS，对每个节点计算子树和并更新最大乘积。

### 思路 1：代码

```python
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9 + 7
        total = 0

        def sum_dfs(node):
            nonlocal total
            if not node:
                return 0
            left = sum_dfs(node.left)
            right = sum_dfs(node.right)
            total += node.val
            return node.val + left + right

        sum_dfs(root)
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            sub = node.val + left + right
            self.ans = max(self.ans, sub * (total - sub))
            return sub

        dfs(root)
        return self.ans % mod
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(h)$。
