# [1110. 删点成林](https://leetcode.cn/problems/delete-nodes-and-return-forest/)

- 标签：树、深度优先搜索、数组、哈希表、二叉树
- 难度：中等

## 题目链接

- [1110. 删点成林 - 力扣](https://leetcode.cn/problems/delete-nodes-and-return-forest/)

## 题目大意

**描述**：给定二叉树的根节点 $root$，树上每个节点都有一个不同的值。

如果节点值在 $to\underline{\hspace{0.5em}}delete$ 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

**要求**：返回森林中的每棵树。你可以按任意顺序组织答案。

**说明**：

- 树中的节点数最大为 $1000$。
- 每个节点都有一个介于 $1$ 到 $1000$ 之间的值，且各不相同。
- $to\underline{\hspace{0.5em}}delete.length \le 1000$。
- $to\underline{\hspace{0.5em}}delete$ 包含一些从 $1$ 到 $1000$、各不相同的值。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/07/05/screen-shot-2019-07-01-at-53836-pm.png)

```python
输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]
```

- 示例 2：

```python
输入：root = [1,2,4,null,3], to_delete = [3]
输出：[[1,2,4]]
```

## 解题思路

### 思路 1：深度优先搜索

将待删除节点数组 $to\underline{\hspace{0.5em}}delete$ 转为集合 $deletes$，则每次能以  $O(1)$ 的时间复杂度判断节点值是否在待删除节点数组中。

如果当前节点值在待删除节点数组中，则删除当前节点后，我们还需要判断其左右子节点是否也在待删除节点数组中。

以此类推，还需要判断左右子节点的左右子节点。。。

因此，我们应该递归遍历处理完所有的左右子树，再判断当前节点的左右子节点是否在待删除节点数组中。如果在，则将其加入到答案数组中。

为此我们可以写一个深度优先搜索算法，具体步骤如下：

1. 如果当前根节点为空，则返回 `None`。
2. 递归遍历处理完当前根节点的左右子树，更新当前节点的左右子树（子节点被删除的情况下需要更新当前根节点的左右子树）。
3. 如果当前根节点值在待删除节点数组中：
   1. 如果当前根节点的左子树没有在被删除节点数组中，将左子树节点加入到答案数组中。
   2. 如果当前根节点的右子树没有在被删除节点数组中，将右子树节点加入到答案数组中。
   3. 返回 `None`，表示当前节点被删除。
4. 如果当前根节点值不在待删除节点数组中：
   1. 返回根节点，表示当前节点没有被删除。

### 思路 1：代码

```Python
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        deletes = set(to_delete)
        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in deletes:
                if root.left:
                    forest.append(root.left)
                if root.right:
                    forest.append(root.right)
                return None
            else:
                return root


        if dfs(root):
            forest.append(root)
        return forest
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为二叉树中节点个数。
- **空间复杂度**：$O(n)$。

