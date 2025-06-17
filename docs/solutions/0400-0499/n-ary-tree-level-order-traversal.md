# [0429. N 叉树的层序遍历](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/)

- 标签：树、广度优先搜索
- 难度：中等

## 题目链接

- [0429. N 叉树的层序遍历 - 力扣](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/)

## 题目大意

给定一个 N 叉树的根节点 `root`。

要求：返回其节点值的层序遍历（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔。

## 解题思路

和二叉树的层序遍历类似。广度优先搜索每次取出第 `i` 层上所有元素。具体步骤如下：

- 根节点入队。
- 当队列不为空时，求出当前队列长度 $size$。
  - 依次从队列中取出这 $size$ 个元素，并将元素值存入当前层级列表 `level` 中。
  - 将该层所有节点的所有孩子节点入队，遍历完之后将这层节点数组加入答案数组中，然后继续迭代。
- 当队列为空时，结束。

## 代码

```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = [root]
        
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                level.append(cur.val)
                for child in cur.children:
                    queue.append(child)
            ans.append(level)

        return ans
```

