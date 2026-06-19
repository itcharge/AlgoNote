# [1373. 二叉搜索子树的最大键值和](https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/)

- 标签：树、深度优先搜索、二叉搜索树、动态规划、二叉树
- 难度：困难

## 题目链接

- [1373. 二叉搜索子树的最大键值和 - 力扣](https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/)

## 题目大意

**描述**：给定一棵二叉树 $root$。

**要求**：返回所有 BST 子树（以某节点为根的子树是 BST）中节点值之和的最大值。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/07/sample_1_1709.png)

```python
输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
输出：20
解释：键值为 3 的子树是和最大的二叉搜索树。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/07/sample_2_1709.png)

```python
输入：root = [4,3,null,1,2]
输出：2
解释：键值为 2 的单节点子树是和最大的二叉搜索树。
```


## 解题思路

### 思路 1：后序遍历

#### 1. 核心思想

后序遍历时向父节点返回四个信息：当前子树是否是 BST、子树的最小值、最大值、节点和。父节点根据左右子树的信息判断以自己为根的子树是否为 BST。

#### 2. 具体步骤

**第 1 步**：定义 $dfs(node)$ 返回 $(is\_bst, min\_val, max\_val, sum)$。

**第 2 步**：如果左右子树都是 BST 且 $node.val > left.max$ 且 $node.val < right.min$，则当前子树也是 BST，更新答案。

### 思路 1：代码

```python
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            left_is_bst, left_min, left_max, left_sum = dfs(node.left)
            right_is_bst, right_min, right_max, right_sum = dfs(node.right)
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                total = left_sum + node.val + right_sum
                self.ans = max(self.ans, total)
                return (True,
                        min(left_min, node.val),
                        max(right_max, node.val),
                        total)
            return (False, 0, 0, 0)

        dfs(root)
        return self.ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(h)$。
