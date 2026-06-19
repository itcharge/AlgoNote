# [1379. 找出克隆二叉树中的相同节点](https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [1379. 找出克隆二叉树中的相同节点 - 力扣](https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)

## 题目大意

**描述**：给定两棵二叉树 $original$ 和 $cloned$，$cloned$ 是 $original$ 的克隆（结构和值相同）。给定一个 $target$ 节点（在 $original$ 中）。

**要求**：返回 $cloned$ 中与 $target$ 对应的节点。

**说明**：
- 树中节点值唯一。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/02/21/e1.png)

```python
输入: tree = [7,4,3,null,null,6,19], target = 3
输出: 3
解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点（其他示例类似）。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/02/21/e2.png)

```python
输入: tree = [7], target =  7
输出: 7
```


## 解题思路

### 思路 1：DFS

#### 1. 核心思想

同时遍历 $original$ 和 $cloned$，对应位置保持同步。当在 $original$ 中找到 $target$ 时，返回 $cloned$ 中的对应节点。

#### 2. 代码

```python
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original is target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        return self.getTargetCopy(original.right, cloned.right, target)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(h)$。
