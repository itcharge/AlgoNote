# [0958. 二叉树的完全性检验](https://leetcode.cn/problems/check-completeness-of-a-binary-tree/)

- 标签：树、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0958. 二叉树的完全性检验 - 力扣](https://leetcode.cn/problems/check-completeness-of-a-binary-tree/)

## 题目大意

**描述**：给定一个二叉树的根节点 `root`。

**要求**：判断该二叉树是否是一个完全二叉树。

**说明**：

- **完全二叉树**：
- 树的结点数在范围 $[1, 100]$ 内。
- $1 \le Node.val \le 1000$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/complete-binary-tree-1.png)

```python
输入：root = [1,2,3,4,5,6]
输出：true
解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
```

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/complete-binary-tree-2.png)

```python
输入：root = [1,2,3,4,5,null,7]
输出：false
解释：值为 7 的结点没有尽可能靠向左侧。
```

## 解题思路

### 思路 1：广度优先搜索

对于一个完全二叉树，按照「层序遍历」的顺序进行广度优先搜索，在遇到第一个空节点之后，整个完全二叉树的遍历就已结束了。不应该在后续遍历过程中再次出现非空节点。

如果在遍历过程中在遇到第一个空节点之后，又出现了非空节点，则该二叉树不是完全二叉树。

利用这一点，我们可以在广度优先搜索的过程中，维护一个布尔变量 `is_empty` 用于标记是否遇见了空节点。

### 思路 1：代码

```python
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        queue = collections.deque([root])
        is_empty = False
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    is_empty = True
                else:
                    if is_empty:
                        return False
                    queue.append(cur.left)
                    queue.append(cur.right)
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为二叉树的节点数。
- **空间复杂度**：$O(n)$。
