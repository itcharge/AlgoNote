# [面试题 04.02. 最小高度树](https://leetcode.cn/problems/minimum-height-tree-lcci/)

- 标签：树、二叉搜索树、数组、分治、二叉树
- 难度：简单

## 题目链接

- [面试题 04.02. 最小高度树 - 力扣](https://leetcode.cn/problems/minimum-height-tree-lcci/)

## 题目大意

给定一个升序的有序数组 `nums`。

要求：创建一棵高度最小的二叉搜索树（高度平衡的二叉搜索树）。

## 解题思路

直观上，如果把数组的中间元素当做根，那么数组左侧元素都小于根节点，右侧元素都大于根节点，且左右两侧元素个数相同，或最多相差 `1` 个。那么构建的树高度差也不会超过 `1`。所以猜想出：如果左右子树约平均，树就越平衡。这样我们就可以每次取中间元素作为当前的根节点，两侧的元素作为左右子树递归建树，左侧区间 `[L, mid - 1]` 作为左子树，右侧区间 `[mid + 1, R]` 作为右子树。

## 代码

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        size = len(nums)
        if size == 0:
            return None
        mid = size // 2
        root = TreeNode(nums[mid])
        root.left = Solution.sortedArrayToBST(self, nums[:mid])
        root.right = Solution.sortedArrayToBST(self, nums[mid + 1:])
        return root
```

