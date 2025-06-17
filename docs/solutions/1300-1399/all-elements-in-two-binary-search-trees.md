# [1305. 两棵二叉搜索树中的所有元素](https://leetcode.cn/problems/all-elements-in-two-binary-search-trees/)

- 标签：树、深度优先搜索、二叉搜索树、二叉树、排序
- 难度：中等

## 题目链接

- [1305. 两棵二叉搜索树中的所有元素 - 力扣](https://leetcode.cn/problems/all-elements-in-two-binary-search-trees/)

## 题目大意

**描述**：给定两棵二叉搜索树的根节点 $root1$ 和 $root2$。

**要求**：返回一个列表，其中包含两棵树中所有整数并按升序排序。

**说明**：

- 每棵树的节点数在 $[0, 5000]$ 范围内。
- $-10^5 \le Node.val \le 10^5$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/29/q2-e1.png)

```python
输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
```

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/29/q2-e5-.png)

```python
输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
```

## 解题思路

### 思路 1：二叉树的中序遍历 + 快慢指针

根据二叉搜索树的特性，如果我们以中序遍历的方式遍历整个二叉搜索树时，就会得到一个有序递增列表。我们按照这样的方式分别对两个二叉搜索树进行中序遍历，就得到了两个有序数组，那么问题就变成了：两个有序数组的合并问题。

两个有序数组的合并可以参考归并排序中的归并过程，使用快慢指针将两个有序数组合并为一个有序数组。

具体步骤如下：

1. 分别使用中序遍历的方式遍历两个二叉搜索树，得到两个有序数组 $nums1$、$nums2$。
2. 使用两个指针 $index1$、$index2$ 分别指向两个有序数组的开始位置。
3. 比较两个指针指向的元素，将两个有序数组中较小元素依次存入结果数组 $nums$ 中，并将指针移动到下一个位置。
4. 重复步骤 $3$，直到某一指针到达数组末尾。
5. 将另一个数组中的剩余元素依次存入结果数组 $nums$ 中。
6. 返回结果数组 $nums$。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nums1 = self.inorderTraversal(root1)
        nums2 = self.inorderTraversal(root2)
        nums = []
        index1, index2 = 0, 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                nums.append(nums1[index1])
                index1 += 1
            else:
                nums.append(nums2[index2])
                index2 += 1
        
        while index1 < len(nums1):
            nums.append(nums1[index1])
            index1 += 1
    
        while index2 < len(nums2):
            nums.append(nums2[index2])
            index2 += 1
        
        return nums
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 和 $m$ 分别为两棵二叉搜索树的节点个数。
- **空间复杂度**：$O(n + m)$。
