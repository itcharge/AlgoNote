# [0437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [0437. 路径总和 III - 力扣](https://leetcode.cn/problems/path-sum-iii/)

## 题目大意

给定一个二叉树的根节点 `root`，和一个整数 `sum`。

要求：求出该二叉树里节点值之和等于 `sum` 的路径的数目。

- 路径：不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

## 解题思路

直观想法是：

以每一个节点 `node` 为起始节点，向下检测延伸的路径。递归遍历每一个节点所有可能的路径，然后将这些路径数目加起来即为答案。

但是这样会存在许多重复计算。我们可以定义节点的前缀和来减少重复计算。

- 节点的前缀和：从根节点到当前节点路径上所有节点的和。

有了节点的前缀和，我们就可以通过前缀和来计算两节点之间的路劲和。即：`则两节点之间的路径和 = 两节点之间的前缀和之差`。

为了计算符合要求的路径数量，我们用哈希表存储「前缀和的节点数量」。哈希表以「当前节点的前缀和」为键，以「该前缀和的节点数量」为值。这样就能通过哈希表直接计算出符合要求的路径数量，从而累加到答案上。

整个算法的具体步骤如下：

- 通过先序遍历方式递归遍历二叉树，计算每一个节点的前缀和 `cur_sum`。
- 从哈希表中取出 `cur_sum - sum` 的路径数量（也就是表示存在从前缀和为 `cur_sum - sum` 所对应的节点到前缀和为 `cur_sum` 所对应的节点的路径个数）累加到答案 `res` 中。
- 然后以「当前节点的前缀和」为键，以「该前缀和的节点数量」为值，存入哈希表中。
- 递归遍历二叉树，并累加答案值。
- 恢复哈希表「当前前缀和的节点数量」，返回答案。

## 代码

```python
class Solution:
    prefixsum_count = dict()

    def dfs(self, root, prefixsum_count, target_sum, cur_sum):
        if not root:
            return 0
        res = 0
        cur_sum += root.val
        res += prefixsum_count.get(cur_sum - target_sum, 0)
        prefixsum_count[cur_sum] = prefixsum_count.get(cur_sum, 0) + 1

        res += self.dfs(root.left, prefixsum_count, target_sum, cur_sum)
        res += self.dfs(root.right, prefixsum_count, target_sum, cur_sum)

        prefixsum_count[cur_sum] -= 1
        return res

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        prefixsum_count = dict()
        prefixsum_count[0] = 1
        return self.dfs(root, prefixsum_count, sum, 0)
```

