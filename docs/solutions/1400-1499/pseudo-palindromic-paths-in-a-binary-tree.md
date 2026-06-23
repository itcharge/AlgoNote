# [1457. 二叉树中的伪回文路径](https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/)

- 标签：位运算、树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [1457. 二叉树中的伪回文路径 - 力扣](https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/)

## 题目大意

**描述**：给定一棵二叉树 $root$，节点值为 $1$ ~ $9$。

**要求**：返回从根到叶节点的所有路径中，能重排为回文串的路径数。

**说明**：
- 回文重排条件：路径中最多只有一种数字出现奇数次。
- 节点数 $[1, 10^5]$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/23/palindromic_paths_1.png)

```python
输入：root = [2,3,1,3,1,null,1]
输出：2 
解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
     在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/23/palindromic_paths_2.png)

```python
输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1 
解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
     这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
```

## 解题思路

### 思路 1：位运算 + DFS

#### 1. 核心思想

回文重排的充要条件：出现奇数次的数字不超过 $1$ 个。

用位掩码 $mask$ 表示数字出现次数的奇偶性：第 $i$ 位为 $1$ 表示数字 $i$ 出现奇数次。

DFS 遍历时，每遇到一个节点值 $val$，翻转 $mask$ 的第 $val$ 位。到达叶节点时，检查 $mask$ 中 $1$ 的个数是否 $\le 1$。

#### 2. 具体步骤

**第 1 步**：定义递归函数 $dfs(node, mask)$：
- 翻转当前节点值的对应位：$mask \oplus= 1 << val$。
- 如果是叶节点（左右子均为空）：
  - 如果 $mask$ 中 $1$ 的个数 $\le 1$（即 $mask \& (mask-1) == 0$），返回 $1$。
  - 否则返回 $0$。
- 递归左右子树，累加结果。

**第 2 步**：从根开始 $dfs(root, 0)$。

#### 3. 举例说明

以二叉树 `[2,3,1,3,1,null,1]` 为例：

```
     2
   /   \
  3     1
 / \     \
3   1     1
```

根到叶路径：
- $2→3→3$：$mask$ 的位：$2(1\text{次}=\text{奇}), 3(2\text{次}=\text{偶})$ → $1$ 个奇数位，回文 ✓
- $2→3→1$：$2(\text{奇}),3(\text{奇}),1(\text{奇})$ → $3$ 个奇数位，非回文
- $2→1→1$：$2(\text{奇}),1(2\text{次}=\text{偶})$ → $1$ 个奇数位，回文 ✓

结果：$2$。

### 思路 1：代码

```python
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mask):
            if not node:
                return 0
            mask ^= 1 << node.val
            if not node.left and not node.right:
                # 检查 mask 中 1 的个数是否 <= 1
                return 1 if mask & (mask - 1) == 0 else 0
            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root, 0)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个节点访问一次。
- **空间复杂度**：$O(h)$，递归栈深度。
