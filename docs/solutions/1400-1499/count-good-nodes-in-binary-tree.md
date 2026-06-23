# [1448. 统计二叉树中好节点的数目](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目链接

- [1448. 统计二叉树中好节点的数目 - 力扣](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/)

## 题目大意

**描述**：给定一棵二叉树 $root$。定义「好节点」为从根节点到该节点路径上的最大值等于该节点值的节点。

**要求**：返回二叉树中好节点的数量。

**说明**：
- 节点数范围 $[1, 10^5]$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/16/test_sample_1.png)

```python
输入：root = [3,1,4,3,null,1,5]
输出：4
解释：图中蓝色节点为好节点。
根节点 (3) 永远是个好节点。
节点 4 -> (3,4) 是路径中的最大值。
节点 5 -> (3,4,5) 是路径中的最大值。
节点 3 -> (3,1,3) 是路径中的最大值。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/16/test_sample_2.png)

```python
输入：root = [3,3,null,4,2]
输出：3
解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。
```

## 解题思路

### 思路 1：DFS 传递路径最大值

#### 1. 核心思想

DFS 遍历二叉树，在递归过程中传递从根到当前节点的最大值 $max\_val$。如果当前节点值 $\ge max\_val$，则它是一个好节点。

#### 2. 具体步骤

**第 1 步**：定义递归函数 $dfs(node, max\_val)$：
- 如果 $node$ 为空，返回 $0$。
- $count = 0$。
- 如果 $node.val \ge max\_val$，$count = 1$，更新 $max\_val = node.val$。
- 递归左右子树，累加计数。

**第 2 步**：从根节点开始 $dfs(root, root.val)$。

#### 3. 举例说明

以二叉树 `[3,1,4,3,null,1,5]` 为例：

```
    3 (好)
   / \
  1   4 (好)
 /   / \
3(好)1  5(好)
```

- 根 3：路径最大值=3，$3 \ge 3$ → 好
- 节点 1：路径最大值=3，$1 < 3$ → 不好
- 节点 3（左子）：路径最大值=3，$3 \ge 3$ → 好
- 节点 4：路径最大值=3，$4 \ge 3$ → 好
- 节点 1（左孙）：路径最大值=4，$1 < 4$ → 不好
- 节点 5：路径最大值=4，$5 \ge 4$ → 好

好节点总数 = $4$。

### 思路 1：代码

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            count = 0
            if node.val >= max_val:
                count = 1
                max_val = node.val
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count

        return dfs(root, float('-inf'))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个节点访问一次。
- **空间复杂度**：$O(h)$，递归栈深度。

---

### 思路 2：迭代栈

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        stack = [(root, float('-inf'))]
        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                count += 1
                max_val = node.val
            if node.right:
                stack.append((node.right, max_val))
            if node.left:
                stack.append((node.left, max_val))
        return count
```
