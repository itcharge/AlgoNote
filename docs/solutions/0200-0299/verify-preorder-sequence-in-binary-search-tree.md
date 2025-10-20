# [0255. 验证二叉搜索树的前序遍历序列](https://leetcode.cn/problems/verify-preorder-sequence-in-binary-search-tree/)

- 标签：栈、树、二叉搜索树、递归、数组、二叉树、单调栈
- 难度：中等

## 题目链接

- [0255. 验证二叉搜索树的前序遍历序列 - 力扣](https://leetcode.cn/problems/verify-preorder-sequence-in-binary-search-tree/)

## 题目大意

**描述**：

给定一个「无重复元素」的整数数组 $preorder$。

**要求**：

如果它是以二叉搜索树的先序遍历排列，返回 $true$，否则返回 $false$。

**说明**：

- $1 \le preorder.length \le 10^{4}$。
- $1 \le preorder[i] \le 10^{4}$。
- $preorder$ 中 无重复元素。

- 进阶：能否使用恒定的空间复杂度来完成此题？

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/12/preorder-tree.jpg)

```python
输入: preorder = [5,2,1,3,6]
输出: true
```

- 示例 2：

```python
输入: preorder = [5,2,6,1,3]
输出: false
```

## 解题思路

### 思路 1：单调栈

核心思想是利用单调栈来模拟二叉搜索树的前序遍历过程。在二叉搜索树的前序遍历中，对于任意节点，其左子树的所有节点值都小于该节点值，右子树的所有节点值都大于该节点值。

算法步骤：

1. 使用单调栈维护一个递减序列，栈中存储的是当前路径上的节点值。
2. 维护一个变量 $lower\_bound$ 表示当前节点值的最小下界。
3. 遍历前序遍历序列 $preorder$：
   - 如果当前值 $preorder[i] < lower\_bound$，说明违反了二叉搜索树的性质，返回 $false$。
   - 如果当前值 $preorder[i] > preorder[i-1]$，说明进入了右子树，需要更新 $lower\_bound$。
   - 将当前值入栈，保持栈的单调递减性质。

具体实现：
- 设 $preorder[i]$ 为当前遍历的元素
- 如果 $preorder[i] < lower\_bound$，则返回 $false$
- 如果栈不为空且 $preorder[i] > stack[-1]$，则说明进入了右子树，需要弹出栈中所有小于 $preorder[i]$ 的元素，并更新 $lower\_bound$ 为最后一个被弹出的元素
- 将 $preorder[i]$ 入栈

### 思路 1：代码

```python
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # 单调栈方法：模拟二叉搜索树前序遍历
        if not preorder:
            return True
        
        stack = []  # 单调递减栈
        lower_bound = float('-inf')  # 当前节点值的最小下界
        
        for num in preorder:
            # 如果当前值小于下界，说明违反了 BST 性质
            if num < lower_bound:
                return False
            
            # 如果当前值大于栈顶元素，说明进入了右子树
            # 需要弹出所有小于当前值的元素，并更新下界
            while stack and num > stack[-1]:
                lower_bound = stack.pop()
            
            # 将当前值入栈
            stack.append(num)
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。每个元素最多入栈和出栈一次。
- **空间复杂度**：$O(n)$，最坏情况下栈的大小为 $n$。
