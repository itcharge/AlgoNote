# [1325. 删除给定值的叶子节点](https://leetcode.cn/problems/delete-leaves-with-a-given-value/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [1325. 删除给定值的叶子节点 - 力扣](https://leetcode.cn/problems/delete-leaves-with-a-given-value/)

## 题目大意

**描述**：给定一棵二叉树 $root$ 和一个整数 $target$。重复删除所有值为 $target$ 的叶子节点，直到没有这样的叶子节点为止。

**要求**：返回删除后的二叉树。

**说明**：删除一个叶子节点后，它的父节点可能变成新的叶子节点，如果父节点的值也是 $target$，也要删除。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/16/sample_1_1684.png)

```python
输入：root = [1,2,3,2,null,2,4], target = 2
输出：[1,null,3,null,4]
解释：
上面左边的图中，绿色节点为叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。
有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/16/sample_2_1684.png)

```python
输入：root = [1,3,3,3,2], target = 3
输出：[1,3,null,null,2]
```


## 解题思路

### 思路 1：后序遍历

#### 1. 核心思想

后序遍历天然适合这种问题：先处理左右子树，再处理当前节点。如果当前节点是叶子节点且值为 $target$，将其删除（返回 $None$）。

#### 2. 具体步骤

**第 1 步**：定义递归函数 $remove(node)$：
- 如果 $node$ 为空，返回 $None$。
- 递归删除左子树。
- 递归删除右子树。
- 如果 $node$ 左右子树为空且 $node.val == target$，返回 $None$。
- 否则返回 $node$。

**第 2 步**：返回 $remove(root)$。

### 思路 1：代码

```python
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(h)$，$h$ 是树高。
