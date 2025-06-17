# [0653. 两数之和 IV - 输入二叉搜索树](https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/)

- 标签：树、深度优先搜索、广度优先搜索、二叉搜索树、哈希表、双指针、二叉树
- 难度：简单

## 题目链接

- [0653. 两数之和 IV - 输入二叉搜索树 - 力扣](https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/)

## 题目大意

给定一个二叉搜索树的根节点 `root` 和一个整数 `k`。

要求：判断该二叉搜索树是否存在两个节点值的和等于 `k`。如果存在，则返回 `True`，不存在则返回 `False`。

## 解题思路

二叉搜索树中序遍历的结果是从小到大排序，所以我们可以先对二叉搜索树进行中序遍历，将中序遍历结果存储到列表中。再使用左右指针查找节点值和为 `k` 的两个节点。

## 代码

```python
class Solution:
    def inOrder(self, root, nums):
        if not root:
            return
        self.inOrder(root.left, nums)
        nums.append(root.val)
        self.inOrder(root.right, nums)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        self.inOrder(root, nums)
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                return True
            elif sum < k:
                left += 1
            else:
                right -= 1
        return False
```

