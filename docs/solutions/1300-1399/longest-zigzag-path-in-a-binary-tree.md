# [1372. 二叉树中的最长交错路径](https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/)

- 标签：树、深度优先搜索、动态规划、二叉树
- 难度：中等

## 题目链接

- [1372. 二叉树中的最长交错路径 - 力扣](https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/)

## 题目大意

**描述**：给定一棵二叉树 $root$。交错路径定义为从某个节点开始，每一步都改变方向（左→右→左→右 或 右→左→右→左）的路径。

**要求**：返回最长交错路径的长度（边的数量）。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/07/sample_1_1702.png)

```python
输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
输出：3
解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/07/sample_2_1702.png)

```python
输入：root = [1,1,1,null,1,null,null,1,1,null,1]
输出：4
解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。
```


## 解题思路

### 思路 1：DFS 传递方向

#### 1. 核心思想

递归遍历时传递当前方向和当前交错路径长度。对每个节点，尝试向相反方向延伸，或从该节点重新开始。

#### 2. 具体步骤

**第 1 步**：定义 $dfs(node, direction, length)$：
- $direction = 0$ 表示从上一步是左→当前，$1$ 表示右→当前。
- 如果往相反方向走（如当前是左子节点，下一步向右子节点），长度 $+1$。
- 如果往相同方向走，则重新开始（长度置为 $1$）。

### 思路 1：代码

```python
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, direction, length):
            """direction: 0=从左来, 1=从右来"""
            self.ans = max(self.ans, length)
            if node.left:
                if direction == 1:  # 上一步从右来，这步走左是交错
                    dfs(node.left, 0, length + 1)
                else:
                    dfs(node.left, 0, 1)
            if node.right:
                if direction == 0:  # 上一步从左来，这步走右是交错
                    dfs(node.right, 1, length + 1)
                else:
                    dfs(node.right, 1, 1)

        dfs(root, 0, 0)
        return self.ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(h)$。
