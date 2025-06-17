# [0501. 二叉搜索树中的众数](https://leetcode.cn/problems/find-mode-in-binary-search-tree/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树
- 难度：简单

## 题目链接

- [0501. 二叉搜索树中的众数 - 力扣](https://leetcode.cn/problems/find-mode-in-binary-search-tree/)

## 题目大意

给定一个有相同值的二叉搜索树（BST），要求找出 BST 中所有众数（出现频率最高的元素）。

二叉搜索树定义：

- 若左子树不为空，则左子树上所有节点值均小于它的根节点值；
- 若右子树不为空，则右子树上所有节点值均大于它的根节点值；
- 任意节点的左、右子树也分别为二叉搜索树。

## 解题思路

中序递归遍历二叉搜索树所得到的结果是一个有序数组，所以问题就变为了如何统计有序数组的众数。

定义几个变量。`count` 用来统计当前元素值对应的节点个数，`max_count` 用来元素出现次数最多的次数。数组 `res` 用来存储所有众数结果（因为众数可能不止一个）。

因为中序递归遍历二叉树，比较的元素肯定是相邻节点，所以需要再使用一个变量 `pre` 来指向前一节点。下面就开始愉快的递归了。

- 如果当前节点为空，直接返回。
- 递归遍历左子树。
- 比较当前节点和前一节点：
  - 如果前一节点为空，则当前元素频率赋值为 1。
  - 如果前一节点值与当前节点值相同，则当前元素频率 + 1。
  - 如果前一节点值与当前节点值不同，则重新计算当前元素频率，将当前元素频率赋值为 1。
- 判断当前元素频率和最高频率关系：
  - 如果当前元素频率和最高频率值相等，则将对应元素值加入 res 数组。
  - 如果当前元素频率大于最高频率值，则更新最高频率值，并清空原 res 数组，将当前元素加入 res 数组。
- 递归遍历右子树。

最终得到的 res 数组即为所求的众数。

## 代码

```python
class Solution:
    res = []
    count = 0
    max_count = 0
    pre = None
    def search(self, cur: TreeNode):
        if not cur:
            return
        self.search(cur.left)
        if not self.pre:
            self.count = 1
        elif self.pre.val == cur.val:
            self.count += 1
        else:
            self.count = 1

        self.pre = cur

        if self.count == self.max_count:
            self.res.append(cur.val)
        elif self.count > self.max_count:
            self.max_count = self.count
            self.res.clear()
            self.res.append(cur.val)

        self.search(cur.right)
        return

    def findMode(self, root: TreeNode) -> List[int]:
        self.count = 0
        self.max_count = 0
        self.res.clear()
        self.pre = None
        self.search(root)
        return self.res
```

