# [LCR 174. 寻找二叉搜索树中的目标节点](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：简单

## 题目链接

- [LCR 174. 寻找二叉搜索树中的目标节点 - 力扣](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

## 题目大意

**描述**：给定一棵二叉搜索树的根节点 $root$，以及一个整数 $k$。

**要求**：找出二叉搜索树书第 $k$ 大的节点。

**说明**：

- 

**示例**：

- 示例 1：

![](https://pic.leetcode.cn/1695101634-kzHKZW-image.png)

```python
输入：root = [7, 3, 9, 1, 5], cnt = 2
       7
      / \
     3   9
    / \
   1   5
输出：7
```

- 示例 2：

![](https://pic.leetcode.cn/1695101636-ESZtLa-image.png)

```python
输入: root = [10, 5, 15, 2, 7, null, 20, 1, null, 6, 8], cnt = 4
       10
      / \
     5   15
    / \    \
   2   7    20
  /   / \ 
 1   6   8
输出: 8
```

## 解题思路

### 思路 1：遍历

已知中序遍历「左 -> 根 -> 右」能得到递增序列。逆中序遍历「右 -> 根 -> 左」可以得到递减序列。

则根据「右 -> 根 -> 左」递归遍历 k 次，找到第 $k$ 个节点位置，并记录答案。

### 思路 1：代码

```python
class Solution:
    res = 0
    k = 0
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        if self.k == 0:
            return
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.dfs(root.left)

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        self.k = k
        self.dfs(root)
        return self.res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为树中节点数量。
- **空间复杂度**：$O(n)$。

