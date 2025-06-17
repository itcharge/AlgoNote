# [LCR 149. 彩灯装饰记录 I](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

- 标签：树、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [LCR 149. 彩灯装饰记录 I - 力扣](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

## 题目大意

给定一棵二叉树的根节点 `root`。

要求：从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

## 解题思路

广度优先搜索。

具体步骤如下：

- 根节点入队。
- 当队列不为空时，求出当前队列长度 $s_i$。
    - 依次从队列中取出这 $s_i$ 个元素，将其加入答案数组，并将其左右子节点入队，然后继续迭代。
- 当队列为空时，结束。

## 代码

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        order = []
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                order.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return order
```

