# [LCR 152. 验证二叉搜索树的后序遍历序列](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

- 标签：栈、树、二叉搜索树、递归、二叉树、单调栈
- 难度：中等

## 题目链接

- [LCR 152. 验证二叉搜索树的后序遍历序列 - 力扣](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

## 题目大意

**描述**：给定一个整数数组 $postorder$。数组的任意两个数字都互不相同。

**要求**：判断该数组是不是某二叉搜索树的后序遍历结果。如果是，则返回 `True`，否则返回 `False`。

**说明**：

- 数组长度 <= 1000。
- $postorder$ 中无重复数字。

**示例**：

- 示例 1：

![](https://pic.leetcode.cn/1694762751-fwHhWX-%E5%89%91%E6%8C%8733%E7%A4%BA%E4%BE%8B1.png)

```python
输入: postorder = [4,9,6,9,8]
输出: false 
解释：从上图可以看出这不是一颗二叉搜索树
```

- 示例 2：

![](https://pic.leetcode.cn/1694762510-vVpTic-%E5%89%91%E6%8C%8733.png)

```python
输入: postorder = [4,6,5,9,8]
输出: true 
解释：可构建的二叉搜索树如上图
```

## 解题思路

### 思路 1：递归分治

后序遍历的顺序为：左 -> 右 -> 根。而二叉搜索树的定义是：左子树所有节点值 < 根节点值，右子树所有节点值 > 根节点值。

所以，可以把数组最右侧元素作为二叉搜索树的根节点值。然后判断数组的左右两侧是否符合左侧值都小于该节点值，右侧值都大于该节点值。如果不满足，则说明不是某二叉搜索树的后序遍历结果。

找到左右分界线位置，然后递归左右数组继续查找。

终止条件为数组 开始位置 > 结束位置，此时该树的子节点数目小于等于 $1$，直接返回 `True` 即可。

### 思路 1：代码

```python
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def verify(left, right):
            if left >= right:
                return True
            index = left
            while postorder[index] < postorder[right]:
                index += 1
            mid = index
            while postorder[index] > postorder[right]:
                index += 1

            return index == right and verify(left, mid - 1) and verify(mid, right - 1)
        if len(postorder) <= 2:
            return True
        return verify(0, len(postorder) - 1)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(n)$。



