# [1367. 二叉树中的链表](https://leetcode.cn/problems/linked-list-in-binary-tree/)

- 标签：树、深度优先搜索、链表、二叉树
- 难度：中等

## 题目链接

- [1367. 二叉树中的链表 - 力扣](https://leetcode.cn/problems/linked-list-in-binary-tree/)

## 题目大意

**描述**：给定一棵二叉树 $root$ 和一个链表 $head$。

**要求**：判断链表中所有节点是否在二叉树中构成一条向下的路径（从某个节点开始，一直往子节点走）。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/29/sample_1_1720.png)

```python
输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
解释：树中蓝色的节点构成了与链表对应的子路径。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/29/sample_2_1720.png)

```python
输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
```


## 解题思路

### 思路 1：双重 DFS

#### 1. 核心思想

枚举二叉树中的每个节点作为起点，从该起点开始尝试匹配链表。如果匹配成功，返回 $True$。

#### 2. 具体步骤

**第 1 步**：定义 $dfs(tree\_node, list\_node)$，检查从 $tree\_node$ 开始是否能匹配从 $list\_node$ 开始的链表：
- 如果 $list\_node$ 为空，匹配成功。
- 如果 $tree\_node$ 为空，匹配失败。
- 如果值不相等，匹配失败。
- 否则递归检查左子树或右子树与链表的下一节点。

**第 2 步**：主函数 $isSubPath$ 遍历每个树节点作为起点。

### 思路 1：代码

```python
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(tree_node, list_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            if tree_node.val != list_node.val:
                return False
            return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)

        if not root:
            return False
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \times m)$，$n$ 是树节点数，$m$ 是链表长度。最坏情况每个节点都作为起点匹配。
- **空间复杂度**：$O(h)$，递归栈深度。
