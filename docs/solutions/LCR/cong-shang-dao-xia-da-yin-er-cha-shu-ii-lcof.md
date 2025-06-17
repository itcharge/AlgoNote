# [LCR 150. 彩灯装饰记录 II](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)

- 标签：树、广度优先搜索、二叉树
- 难度：简单

## 题目链接

- [LCR 150. 彩灯装饰记录 II - 力扣](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)

## 题目大意

给定一棵二叉树的根节点 `root`。

要求：从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

## 解题思路

广度优先搜索，需要增加一些变化。普通广度优先搜索只取一个元素，变化后的广度优先搜索每次取出第 i 层上所有元素。

具体步骤如下：

- 根节点入队。
- 当队列不为空时，求出当前队列长度 $s_i$。
    - 依次从队列中取出这 $s_i$ 个元素，并将其左右子节点入队，遍历完之后将这层节点数组加入答案数组中，然后继续迭代。
- 当队列为空时，结束。

## 代码

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        order = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level:
                order.append(level)
        return order
```

