# [0272. 最接近的二叉搜索树值 II](https://leetcode.cn/problems/closest-binary-search-tree-value-ii/)

- 标签：栈、树、深度优先搜索、二叉搜索树、双指针、二叉树、堆（优先队列）
- 难度：困难

## 题目链接

- [0272. 最接近的二叉搜索树值 II - 力扣](https://leetcode.cn/problems/closest-binary-search-tree-value-ii/)

## 题目大意

**描述**：

给定二叉搜索树的根 $root$ 、一个目标值 $target$ 和一个整数 $k$。

**要求**：

返回 BST 中最接近目标的 $k$ 个值。你可以按任意顺序返回答案。

**说明**：

- 题目保证该二叉搜索树中只会存在一种 $k$ 个值集合最接近 $target$。
- 二叉树的节点总数为 n。
- $1 \le k \le n \le 10^{4}$。
- $0 \le Node.val \le 10^{9}$。
- $-10^{9} \le target \le 10^{9}$。

- 进阶：假设该二叉搜索树是平衡的，请问您是否能在小于 O(n)（ n = total nodes ）的时间复杂度内解决该问题呢？

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg)

```python
输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2
输出: [4,3]
```

- 示例 2：

```python
输入: root = [1], target = 0.000000, k = 1
输出: [1]
```

## 解题思路

### 思路 1：中序遍历 + 排序

这是一个典型的二叉搜索树问题。我们需要找到 BST 中最接近目标值 $target$ 的 $k$ 个值。

我们可以使用中序遍历 + 排序的方法来解决这个问题：

1. **中序遍历**：由于 BST 的中序遍历结果是有序的，我们可以先通过中序遍历得到所有节点的值，存储在数组 $values$ 中。
2. **按距离排序**：将所有节点值按照与 $target$ 的距离进行排序，选择距离最小的 $k$ 个值。
3. **算法步骤**：
   - 对 BST 进行中序遍历，得到有序数组 $values$。
   - 创建一个包含节点值和距离的列表 $distances$，其中每个元素为 $(|value - target|, value)$。
   - 对 $distances$ 按照距离进行排序。
   - 取前 $k$ 个元素的值作为结果。

### 思路 1：代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        values = []  # 存储中序遍历的结果
        
        def inorder(node):
            """中序遍历 BST，得到有序数组"""
            if not node:
                return
            inorder(node.left)   # 遍历左子树
            values.append(node.val)  # 访问根节点
            inorder(node.right)  # 遍历右子树
        
        inorder(root)  # 执行中序遍历
        
        # 创建距离列表，每个元素为 (距离, 值)
        distances = []
        for value in values:
            distance = abs(value - target)
            distances.append((distance, value))
        
        # 按距离排序，取前 k 个值
        distances.sort()
        result = [distances[i][1] for i in range(k)]
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是 BST 中节点的数量。需要遍历所有节点进行中序遍历，然后对距离进行排序。
- **空间复杂度**：$O(n)$，需要存储中序遍历的结果数组、距离列表，以及递归调用栈的空间。
