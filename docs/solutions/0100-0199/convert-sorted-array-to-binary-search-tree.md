# [0108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/)

- 标签：树、二叉搜索树、数组、分治、二叉树
- 难度：简单

## 题目链接

- [0108. 将有序数组转换为二叉搜索树 - 力扣](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/)

## 题目大意

**描述**：给定一个升序的有序数组 `nums`。

**要求**：将其转换为一棵高度平衡的二叉搜索树。

**说明**：

- $1 \le nums.length \le 10^4$。
- $-10^4 \le nums[i] \le 10^4$。
- `nums` 按严格递增顺序排列。

**示例**：

- 示例 1：

![img](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

```python
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案
```

- 示例 2：

![img](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

```python
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
```

## 解题思路

### 思路 1：递归遍历

直观上，如果把数组的中间元素当做根，那么数组左侧元素都小于根节点，右侧元素都大于根节点，且左右两侧元素个数相同，或最多相差 $1$ 个。那么构建的树高度差也不会超过 $1$。

所以猜想出：如果左右子树越平均，树就越平衡。这样我们就可以每次取中间元素作为当前的根节点，两侧的元素作为左右子树递归建树，左侧区间 $[L, mid - 1]$ 作为左子树，右侧区间 $[mid + 1, R]$ 作为右子树。

### 思路 1：代码

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return 
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(nums) - 1)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是数组的长度。
- **空间复杂度**：$O(n)$。