# [1120. 子树的最大平均值](https://leetcode.cn/problems/maximum-average-subtree/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [1120. 子树的最大平均值 - 力扣](https://leetcode.cn/problems/maximum-average-subtree/)

## 题目大意

**描述**：给定一棵二叉树的根节点 $root$。

**要求**：找出所有子树中，平均值最大的那个，返回这个最大平均值。

子树指某个节点及其所有后代节点构成的集合。平均值 = 节点值总和 ÷ 节点个数。

**说明**：

- 节点数 $1$ 到 $5000$。
- 节点值 $0$ 到 $100000$。
- 误差不超过 $10^{-5}$ 即可。

**示例**：

```python
输入：[5,6,1]
输出：6.0
解释：
- 以 5 为根的子树：平均值 (5+6+1)/3 = 4
- 以 6 为根的子树：平均值 6/1 = 6
- 以 1 为根的子树：平均值 1/1 = 1
所以最大平均值是 6。
```

## 解题思路

### 思路 1：深度优先搜索

要计算每棵子树的平均值，需要知道每个子树的总节点数和值的总和。这可以通过**后序遍历**（先处理左右子树，再处理当前节点）来实现。

可以想象成从叶子往上「汇报」：左子树和右子树分别把自己那部分的「总人数」和「总分数」报给父节点，父节点汇总后再往上报。一路上凡是算出来的平均值都记下来，最后取最大的。

**步骤拆解：**

1. 定义递归函数 $dfs(node)$，返回 $(总和, 节点数)$。
2. 如果节点为空，返回 $(0, 0)$。
3. 递归处理左右子树，得到左右的总和和节点数。
4. 当前子树的总和 = 节点值 + 左总和 + 右总和；总节点数 = 1 + 左节点数 + 右节点数。
5. 计算当前子树的平均值，更新全局最大平均值。
6. 返回 $(总和, 节点数)$ 给父节点。
7. 最终返回全局最大平均值。

### 思路 1：代码

```python
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = 0.0  # 记录所有子树中的最大平均值
        
        def dfs(node):
            """返回 (当前子树的总和, 当前子树的节点数)"""
            if not node:
                return (0, 0)
            
            # 先递归处理左右子树
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # 汇总当前子树
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            # 计算当前子树的平均值，更新最大值
            avg = total_sum / total_count
            self.max_avg = max(self.max_avg, avg)
            
            return (total_sum, total_count)
        
        dfs(root)
        return self.max_avg
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。每个节点访问一次。
- **空间复杂度**：$O(h)$，$h$ 是树的高度，递归栈的深度。
