# [LCR 151. 彩灯装饰记录 III](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

- 标签：树、广度优先搜索、二叉树
- 难度：中等

## 题目链接

- [LCR 151. 彩灯装饰记录 III - 力扣](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

## 题目大意

给定一个二叉树的根节点 `root`。

要求：返回其之字形层序遍历。

- 之字形层序遍历：从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行。

## 解题思路

广度优先搜索，在二叉树的层序遍历的基础上需要增加一些变化。

普通广度优先搜索只取一个元素，变化后的广度优先搜索每次取出第 i 层上所有元素。

新增一个变量 odd，用于判断当前层数是奇数层，还是偶数层。从而判断元素遍历方向。

存储每层元素的 level 列表改用双端队列，如果是奇数层，则从末尾添加元素。如果是偶数层，则从头部添加元素。

具体步骤如下：

- 根节点入队。
- 当队列不为空时，求出当前队列长度 $s_i$，并判断当前层数的奇偶性。
- 依次从队列中取出这 $s_i$ 个元素。
    - 如果为奇数层，如果是奇数层，则从 level 末尾添加元素。
    - 如果是偶数层，则从 level头部添加元素。
- 然后保存将其左右子节点入队，然后继续迭代。
- 当队列为空时，结束。

## 代码

```python
import collections

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        order = []
        odd = True
        while queue:
            level = collections.deque()
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if odd:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level:
                order.append(list(level))
            odd = not odd
        return order
```

