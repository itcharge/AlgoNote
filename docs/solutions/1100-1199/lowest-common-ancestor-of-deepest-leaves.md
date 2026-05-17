# [1123. 最深叶节点的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/)

- 标签：树、深度优先搜索、广度优先搜索、哈希表、二叉树
- 难度：中等

## 题目链接

- [1123. 最深叶节点的最近公共祖先 - 力扣](https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/)

## 题目大意

**描述**：给定一棵二叉树的根节点 $root$。

**要求**：找出所有最深叶节点的最近公共祖先。

- **叶节点**：没有子节点的节点。
- **最近公共祖先**：离这些最深叶节点最近的那个祖先节点，而且是它们的公共祖先。

**说明**：

- 节点数 $[1, 10^3]$。
- $0 \le Node.val \le 10^3$。
- 每个节点值唯一。

**示例**：

```python
输入：root = [3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：最深叶节点是 7 和 4，它们的最近公共祖先是 2。
```

## 解题思路

### 思路 1：深度优先搜索

这道题可以递归来做。对于每个节点，我们需要知道：
1. 以它为根的子树的最大深度是多少。
2. 如果最深叶节点全部在它的左子树或右子树中，那么答案在那边。
3. 如果左右子树的最深深度相同，说明最深叶节点左右都有，当前节点就是它们的最近公共祖先。

用人话讲：从下往上递归，比较左右子树的深度。如果左边更深，答案在左边；右边更深，答案在右边；一样深，当前节点就是答案。

**步骤拆解：**

1. 定义递归函数 $dfs(node)$，返回两个值：$(深度, 最近公共祖先)$。

2. 递归处理左右子树，得到 $(left\_depth, left\_lca)$ 和 $(right\_depth, right\_lca)$。

3. 比较左右深度：
   - 左 > 右：最深叶节点全在左边，答案 = 左边的答案。
   - 左 < 右：最深叶节点全在右边，答案 = 右边的答案。
   - 左 == 右：左右都有最深叶节点，当前节点就是答案。

4. 返回结果时，深度要加 1（因为往父节点走了一层）。

### 思路 1：代码

```python
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            """返回 (当前子树的最大深度, 最深叶节点的最近公共祖先)"""
            if not node:
                return (0, None)
            
            # 递归处理左右子树
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            if left_depth > right_depth:
                # 最深叶节点全在左子树
                return (left_depth + 1, left_lca)
            elif left_depth < right_depth:
                # 最深叶节点全在右子树
                return (right_depth + 1, right_lca)
            else:
                # 左右深度相同，当前节点是最近公共祖先
                return (left_depth + 1, node)
        
        return dfs(root)[1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。每个节点访问一次。
- **空间复杂度**：$O(h)$，$h$ 是树的高度，代表递归栈的深度。
