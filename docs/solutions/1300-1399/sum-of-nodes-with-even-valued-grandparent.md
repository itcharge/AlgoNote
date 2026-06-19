# [1315. 祖父节点值为偶数的节点和](https://leetcode.cn/problems/sum-of-nodes-with-even-valued-grandparent/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [1315. 祖父节点值为偶数的节点和 - 力扣](https://leetcode.cn/problems/sum-of-nodes-with-even-valued-grandparent/)

## 题目大意

**描述**：给定一棵二叉树 $root$。

**要求**：返回所有祖父节点值为偶数的节点值之和。如果不存在这样的节点，返回 $0$。

**说明**：
- 祖父节点：父节点的父节点。
- 节点值的范围：$1 \le val \le 100$。
- 节点数范围：$[1, 10^4]$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/10/1473_ex1.png)

```python
输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：18
解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
```

- 示例 2：

```python
输入：
输出：
```


## 解题思路

### 思路 1：DFS 传递祖父和父节点信息

#### 1. 核心思想

深度优先遍历二叉树，在递归过程中同时传递祖父节点和父节点的值。当遍历到当前节点时，检查祖父节点值是否为偶数，如果是则累加当前节点值。

#### 2. 具体步骤

**第 1 步**：定义递归函数 $dfs(node, parent, grandparent)$：
- 如果 $node$ 为空，返回。
- 如果 $grandparent$ 存在且值为偶数，将 $node.val$ 加入答案。
- 递归左子：$dfs(node.left, node, parent)$。
- 递归右子：$dfs(node.right, node, parent)$。

**第 2 步**：从根节点开始调用，根节点没有父节点和祖父节点，传入 $None$。

**第 3 步**：返回累加和。

#### 3. 举例说明

以二叉树 `[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]` 为例：

```
        6 (偶数)
       / \
      7   8 (偶数)
     / \ / \
    2  7 1  3
   /  / \
  9  1   4
        /
       5
```

遍历过程：
- 根节点 $6$：祖父为 None，跳过
- 节点 $7$：祖父 None，跳过
- 节点 $8$：祖父 None，跳过
- 节点 $2$：祖父 $6$ 为偶数 → 累加 $2$
- 节点 $7$（左7的子节点）：祖父 $6$ 为偶数 → 累加 $7$
- 节点 $1$（8的左子）：祖父 $6$ 为偶数 → 累加 $1$
- 节点 $3$（8的右子）：祖父 $6$ 为偶数 → 累加 $3$
- 节点 $9$：祖父 $7$ 为奇数 → 跳过
- 节点 $1$（7的右子）：祖父 $7$ 为奇数 → 跳过
- 节点 $4$：祖父 $7$ 为奇数 → 跳过
- 节点 $5$：祖父 $7$ 为奇数 → 跳过

总和 = $2 + 7 + 1 + 3 = 13$。

### 思路 1：代码

```python
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, parent, grandparent):
            if not node:
                return
            # 如果祖父节点存在且值为偶数，累加当前节点值
            if grandparent is not None and grandparent.val % 2 == 0:
                self.ans += node.val
            # 递归：当前节点成为下一层的父节点，父节点成为下一层的祖父节点
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

        dfs(root, None, None)
        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个节点遍历一次。
- **空间复杂度**：$O(h)$，递归栈深度 $h$ 等于树的高度。

---

### 思路 2：BFS 层序遍历

也可以用 BFS 实现。层序遍历时，每遇到一个值为偶数的节点，就将其孙节点的值加入总和。

```python
from collections import deque

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([root])

        while q:
            node = q.popleft()
            if node.val % 2 == 0:
                # 偶数节点，累加其孙节点值
                if node.left:
                    if node.left.left:
                        ans += node.left.left.val
                    if node.left.right:
                        ans += node.left.right.val
                if node.right:
                    if node.right.left:
                        ans += node.right.left.val
                    if node.right.right:
                        ans += node.right.right.val
            # 入队子节点继续遍历
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans
```

BFS 思路：遇到偶数节点时检查其孙子节点。两种方法时间空间复杂度一致，DFS 的递归传参更简洁。
