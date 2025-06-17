# [LCR 045. 找树左下角的值](https://leetcode.cn/problems/LwUNpT/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [LCR 045. 找树左下角的值 - 力扣](https://leetcode.cn/problems/LwUNpT/)

## 题目大意

给定一个二叉树的根节点 `root`。

要求：找出该二叉树 「最底层」的「最左边」节点的值。

## 解题思路

这个问题拆开来看，一是如何找到「最底层」，而是在「最底层」如何找到最左边的节点。

通过层序遍历，我们可以直接确定最底层节点。而「最底层」的「最左边」节点可以改变层序遍历的左右节点访问顺序。

每层元素先访问右节点，在访问左节点，则最后一个遍历的元素就是「最底层」的「最左边」节点，即左下角的节点，返回该点对应的值即可。

## 代码

```python
import collections

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
        return cur.val
```

