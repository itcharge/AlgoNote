# [0513. 找树左下角的值](https://leetcode.cn/problems/find-bottom-left-tree-value/)

- 标签：树、深度优先搜索、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0513. 找树左下角的值 - 力扣](https://leetcode.cn/problems/find-bottom-left-tree-value/)

## 题目大意

**描述**：给定一个二叉树的根节点 `root`。

**要求**：找出该二叉树 「最底层」的「最左边」节点的值。

**说明**：

- 假设二叉树中至少有一个节点。
- 二叉树的节点个数的范围是 $[1,10^4]$。
- $-2^{31} \le Node.val \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：[1,2,3,4,null,5,6,null,null,7]
输出：7
```

![](https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg)

## 解题思路

### 思路 1：层序遍历

这个问题可以拆分为两个问题：

1. 如何找到「最底层」。
2. 在「最底层」如何找到最左边的节点。

第一个问题，我们可以通过层序遍历直接确定最底层节点。而第二个问题可以通过改变层序遍历的左右节点访问顺序从而找到「最底层」的「最左边节点」。具体方法如下：

1. 对二叉树进行层序遍历。每层元素先访问右节点，再访问左节点。
2. 当遍历到最后一个元素时，此时最后一个元素就是「最底层」的「最左边」节点，即左下角的节点，将该节点的值返回即可。

### 思路 1：层序遍历代码

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

