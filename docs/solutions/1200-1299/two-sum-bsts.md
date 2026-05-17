# [1214. 查找两棵二叉搜索树之和](https://leetcode.cn/problems/two-sum-bsts/)

- 标签：栈、树、深度优先搜索、二叉搜索树、双指针、二分查找
- 难度：中等

## 题目链接

- [1214. 查找两棵二叉搜索树之和 - 力扣](https://leetcode.cn/problems/two-sum-bsts/)

## 题目大意

**描述**：给定两棵二叉搜索树 $root1$ 和 $root2$，以及一个整数 $target$。

**要求**：判断是否存在两个节点（分别来自两棵不同的树），使得它们的节点值之和等于 $target$。

**说明**：

- 每棵树节点数在 $[1, 5000]$ 范围内。
- $-10^{9} \le Node.val, target \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：root1 = [2,1,4], root2 = [1,0,3], target = 5
输出：true
解释：root1 的 2 加上 root2 的 3 等于 5。
```

- 示例 2：

```python
输入：root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
输出：false
```

## 解题思路

### 思路 1：哈希集合

#### 1. 核心思想

最直接的方法：遍历一棵树，将所有节点值存入哈希集合，然后遍历另一棵树，检查 $target - val$ 是否在哈希集合中。

#### 2. 具体步骤

**第 1 步**：遍历 $root1$，将所有节点值存入集合 $values$。

**第 2 步**：遍历 $root2$，对于每个节点 $val$，检查 $target - val$ 是否在 $values$ 中。如果在，返回 $True$。

**第 3 步**：遍历结束返回 $False$。

### 思路 1：代码

```python
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        # 遍历 root1，将值存入集合
        values = set()

        def dfs(node):
            if not node:
                return
            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root1)

        # 遍历 root2，检查是否存在互补值
        def check(node):
            if not node:
                return False
            if target - node.val in values:
                return True
            return check(node.left) or check(node.right)

        return check(root2)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n_1 + n_2)$，其中 $n_1$、$n_2$ 分别是两棵树的节点数。
- **空间复杂度**：$O(n_1)$，存储第一棵树的节点值。

### 思路 2：中序遍历 + 双指针

#### 1. 核心思想

利用 BST 的中序遍历是有序数组这一性质。将两棵 BST 中序遍历得到两个有序数组，然后用双指针判断是否存在和为 $target$ 的两个数。

#### 2. 代码

```python
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def inorder(node, arr):
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)

        arr1, arr2 = [], []
        inorder(root1, arr1)
        inorder(root2, arr2)

        # 双指针
        i, j = 0, len(arr2) - 1
        while i < len(arr1) and j >= 0:
            s = arr1[i] + arr2[j]
            if s == target:
                return True
            elif s < target:
                i += 1
            else:
                j -= 1
        return False
```

#### 3. 复杂度分析

- **时间复杂度**：$O(n_1 + n_2)$，中序遍历和双指针遍历都是线性时间。
- **空间复杂度**：$O(n_1 + n_2)$，需要存储两个有序数组。

思路 1 更直观，思路 2 利用了 BST 有序性，在面试中可能更具区分度。
