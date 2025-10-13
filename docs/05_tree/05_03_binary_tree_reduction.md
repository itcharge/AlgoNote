## 1. 二叉树的还原简介

> **二叉树的还原**：指通过已知的二叉树遍历序列，重建出原始的二叉树结构。

我们知道，对于一棵非空二叉树，其前序、中序、后序遍历序列都是唯一的。但反过来，如果只给出某一种遍历序列，是否能唯一确定这棵二叉树呢？答案是否定的。

### 1.1 单一遍历序列的还原能力

- **前序遍历**：第一个节点必为根节点，但无法区分后续节点属于左子树还是右子树，因此仅凭前序序列无法还原二叉树。
- **中序遍历**：虽然根节点能将中序序列分为左右子树，但无法确定根节点是谁，因此仅凭中序序列也无法还原二叉树。
- **后序遍历**：最后一个节点必为根节点，但同样无法判断其他节点的归属，仅凭后序序列也无法还原二叉树。

### 1.2 两种遍历序列的组合情况

- **前序 + 中序**：前序序列确定根节点，中序序列确定左右子树的范围。递归分割子序列，可以唯一还原原二叉树。
- **中序 + 后序**：后序序列确定根节点，中序序列确定左右子树的范围，方法与前序+中序类似，也能唯一还原二叉树。
- **中序 + 层序**：通过层序遍历确定每个子树的根节点，再结合中序遍历分割左右子树，也可以唯一还原二叉树。

### 1.3 不能唯一还原的特殊情况

- **前序 + 后序**：仅有前序和后序遍历序列时，无法唯一确定二叉树结构。因为缺少中序信息，无法区分左右子树的分界。例如，如果存在度为 $1$ 的节点，无法判断该节点是左子树还是右子树。
- **特殊说明**：只有当二叉树中每个节点的度均为 $2$ 或 $0$（即满二叉树）时，前序和后序遍历序列才能唯一确定二叉树。如果存在度为 $1$ 的节点，则无法唯一还原。

**结论**：

- 已知「前序+中序」、「中序+后序」、「中序+层序」任意一组遍历序列，可以唯一还原一棵二叉树。  
- 仅有「前序+后序」遍历序列，通常无法唯一还原二叉树，除非二叉树为满二叉树。

## 2. 利用前序与中序遍历序列重建二叉树

- **描述**：给定一棵二叉树的前序遍历序列和中序遍历序列。
- **目标**：重建出原始的二叉树结构。
- **说明**：树中所有节点值均不重复。

### 2.1 实现思路与步骤

前序遍历顺序为：根节点 → 左子树 → 右子树；  
中序遍历顺序为：左子树 → 根节点 → 右子树。

基于上述规律，可以通过以下方式递归重建二叉树：

1. 前序遍历序列的第一个元素即为当前子树的根节点。
2. 在中序遍历序列中查找该根节点的位置 $inorder[k]$，据此将中序序列分为左、右子树两部分，并确定左右子树的节点数量。
3. 利用左右子树节点数量，将前序遍历序列切分为左、右子树对应的部分。
4. 递归构建当前根节点的左、右子树，直到子树为空（序列长度为0）为止。

简要流程如下：

- 取前序序列首元素作为根节点。
- 在中序序列中定位根节点，分割出左、右子树的中序区间。
- 根据左子树节点数，切分前序序列为左、右子树区间。
- 递归处理左右子树，直至区间为空。

### 2.2 代码实现

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        根据前序遍历和中序遍历序列重建二叉树

        参数:
            preorder: List[int]，二叉树的前序遍历序列
            inorder: List[int]，二叉树的中序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(preorder, inorder, n):
            """
            递归构建二叉树

            参数:
                preorder: 当前子树的前序遍历序列
                inorder: 当前子树的中序遍历序列
                n: 当前子树的节点数
            返回:
                TreeNode，当前子树的根节点
            """
            if n == 0:
                return None  # 递归终止条件：子树节点数为 0
            # 在中序遍历中查找根节点位置
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            # 创建根节点
            node = TreeNode(inorder[k])
            # 递归构建左子树
            node.left = createTree(preorder[1: k + 1], inorder[0: k], k)
            # 递归构建右子树
            node.right = createTree(preorder[k + 1:], inorder[k + 1:], n - k - 1)
            return node

        # 从整棵树的前序和中序序列开始递归构建
        return createTree(preorder, inorder, len(inorder))
```

## 3. 利用中序与后序遍历序列重建二叉树

- **描述**：给定一棵二叉树的中序遍历序列和后序遍历序列。
- **目标**：重建出原始的二叉树结构。
- **说明**：树中所有节点值均不重复。

### 3.1 实现思路与步骤

- 中序遍历顺序：左子树 → 根节点 → 右子树
- 后序遍历顺序：左子树 → 右子树 → 根节点

利用后序遍历的最后一个元素可以确定当前子树的根节点。再在中序遍历序列中定位该根节点，从而划分出左、右子树的中序区间，并据此确定左右子树的节点数量。递归地对左右子树重复上述过程，直到区间为空。

具体步骤如下：

1. 后序遍历序列的最后一个元素 $postorder[n-1]$ 为当前子树的根节点。
2. 在中序遍历序列中查找该根节点的位置 $inorder[k]$，据此将中序序列分为左、右子树区间，并确定左右子树的节点数。
3. 利用左右子树的节点数，将后序遍历序列划分为左、右子树对应的区间。
4. 构建当前根节点，并递归构建其左、右子树，直到区间为空为止。

### 3.2 代码实现

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        根据中序遍历和后序遍历序列重建二叉树

        参数:
            inorder: List[int]，二叉树的中序遍历序列
            postorder: List[int]，二叉树的后序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(inorder, postorder, n):
            """
            递归构建二叉树

            参数:
                inorder: 当前子树的中序遍历序列
                postorder: 当前子树的后序遍历序列
                n: 当前子树的节点数
            返回:
                TreeNode，当前子树的根节点
            """
            if n == 0:
                return None  # 递归终止条件：子树节点数为0，返回空节点

            # 后序遍历的最后一个元素为当前子树的根节点
            root_val = postorder[n - 1]
            # 在中序遍历中查找根节点的位置
            k = 0
            while inorder[k] != root_val:
                k += 1

            # 创建根节点
            node = TreeNode(root_val)
            # 递归构建左子树
            # 左子树的中序区间：inorder[0:k]
            # 左子树的后序区间：postorder[0:k]
            node.left = createTree(inorder[0:k], postorder[0:k], k)
            # 递归构建右子树
            # 右子树的中序区间：inorder[k+1:n]
            # 右子树的后序区间：postorder[k:n-1]
            node.right = createTree(inorder[k+1:n], postorder[k:n-1], n - k - 1)
            return node

        # 从整棵树的中序和后序序列开始递归构建
        return createTree(inorder, postorder, len(postorder))
```

## 4. 利用前序与后序遍历序列构造二叉树

如前所述，**仅通过二叉树的前序和后序遍历序列，无法唯一确定一棵二叉树。** 但如果不要求唯一性，只需构造出任意一棵符合条件的二叉树，是可以实现的。

- **描述**：给定一棵二叉树的前序遍历和后序遍历序列。
- **目标**：重建并返回该二叉树。
- **说明**：假设树中节点值各不相同。如果存在多个可行答案，返回其中任意一个即可。

### 4.1 实现思路与步骤

我们可以假定前序遍历序列的第二个元素为左子树的根节点，进而递归划分左右子树。具体步骤如下：

1. 前序遍历的第一个元素 $preorder[0]$ 是当前子树的根节点。
2. 前序遍历的第二个元素 $preorder[1]$ 是左子树的根节点。我们在后序遍历中查找该节点的位置 $postorder[k]$，该位置左侧为左子树，右侧为右子树。
3. 由 $k$ 可确定左子树的节点数量，从而划分前序和后序序列的左右子树部分。
4. 递归构建当前节点的左、右子树，直到子树为空。

### 4.2 代码实现

```python
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        根据前序和后序遍历序列构造二叉树（不唯一）
        参数:
            preorder: List[int]，二叉树的前序遍历序列
            postorder: List[int]，二叉树的后序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(preorder, postorder, n):
            if n == 0:
                return None  # 递归终止条件：子树节点数为0，返回空节点
            # 前序遍历的第一个元素为当前子树的根节点
            root_val = preorder[0]
            node = TreeNode(root_val)
            if n == 1:
                return node  # 只有一个节点，直接返回
            # 前序遍历的第二个元素为左子树的根节点
            left_root_val = preorder[1]
            # 在后序遍历中查找左子树根节点的位置
            k = 0
            while postorder[k] != left_root_val:
                k += 1
            # k 为左子树在 postorder 中的结尾索引，左子树节点数为 k+1
            # 划分左右子树的前序和后序区间
            # 左子树：preorder[1:k+2], postorder[0:k+1]
            # 右子树：preorder[k+2:], postorder[k+1:n-1]
            node.left = createTree(preorder[1:k+2], postorder[0:k+1], k+1)
            node.right = createTree(preorder[k+2:], postorder[k+1:n-1], n-k-1)
            return node
        # 从整棵树的前序和后序序列开始递归构建
        return createTree(preorder, postorder, len(preorder))
```

## 5. 总结

### 5.1 核心要点

二叉树的还原是数据结构中的重要问题，其核心在于 **利用遍历序列的特性来重建树结构**。

**关键规律**：

- **前序遍历**：根节点 → 左子树 → 右子树
- **中序遍历**：左子树 → 根节点 → 右子树  
- **后序遍历**：左子树 → 右子树 → 根节点

### 5.2 还原能力对比

| 遍历序列组合 | 能否唯一还原 | 说明 |
|-------------|-------------|------|
| 前序 + 中序 | 可以 | 前序确定根，中序确定左右子树范围 |
| 中序 + 后序 | 可以 | 后序确定根，中序确定左右子树范围 |
| 中序 + 层序 | 可以 | 层序确定根，中序确定左右子树范围 |
| 前序 + 后序 | 不能 | 缺少中序信息，无法区分左右子树 |


二叉树的还原是理解树结构遍历特性的重要应用，掌握「前序+中序」和「中序+后序」的还原方法，就能解决大部分二叉树构造问题。

## 练习题目

- [0105. 从前序与中序遍历序列构造二叉树](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/construct-binary-tree-from-preorder-and-inorder-traversal.md)
- [0106. 从中序与后序遍历序列构造二叉树](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/construct-binary-tree-from-inorder-and-postorder-traversal.md)
- [0889. 根据前序和后序遍历构造二叉树](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0800-0899/construct-binary-tree-from-preorder-and-postorder-traversal.md)

- [二叉树的还原题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%BF%98%E5%8E%9F%E9%A2%98%E7%9B%AE)

## 参考资料

1. 【书籍】数据结构教程 第 3 版 - 唐发根 著
2. 【书籍】算法训练营 陈小玉 著
3. 【博文】[二叉树的构造系列 - 知乎](https://zhuanlan.zhihu.com/p/346336665)
4. 【评论】[889. 根据前序和后序遍历构造二叉树 - 力扣)](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/comments/)