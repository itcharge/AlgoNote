# [0654. 最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/)

- 标签：栈、树、数组、分治、二叉树、单调栈
- 难度：中等

## 题目链接

- [0654. 最大二叉树 - 力扣](https://leetcode.cn/problems/maximum-binary-tree/)

## 题目大意

给定一个不含重复元素的整数数组 `nums`。一个以此数组构建的最大二叉树定义如下：

- 二叉树的根是数组中的最大元素。
- 左子树是通过数组中最大值左边部分构造出的最大二叉树。
- 右子树是通过数组中最大值右边部分构造出的最大二叉树。

要求通过给定的数组构建最大二叉树，并且输出这个树的根节点。

## 解题思路

根据题意可知，数组中最大元素位置为根节点，最大元素位置左右部分可分别作为左右子树。则我们可以通过递归的方式构建最大二叉树。

- 定义 left、right 分别表示当前数组的左右边界位置，定义 `max_value_index` 为当前数组中最大值位置。
- 遍历当前数组，找到最大值位置 `max_value_index`，并建立根节点 `root`，将数组 `nums` 分为 `[left, max_value_index]` 和 `[max_value_index, right]` 两部分，并分别递归建树。
- 将其赋值给 `root` 的左右子节点，最后返回 root 节点。

## 代码

```python
class Solution:
    def createBinaryTree(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        max_value_index = left
        for i in range(left + 1, right):
            if nums[i] > nums[max_value_index]:
                max_value_index = i

        root = TreeNode(nums[max_value_index])
        root.left = self.createBinaryTree(nums, left, max_value_index)
        root.right = self.createBinaryTree(nums, max_value_index + 1, right)

        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.createBinaryTree(nums, 0, len(nums))
```

