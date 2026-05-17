# [1273. 删除树节点](https://leetcode.cn/problems/delete-tree-nodes/)

- 标签：树、深度优先搜索、广度优先搜索、数组
- 难度：中等

## 题目链接

- [1273. 删除树节点 - 力扣](https://leetcode.cn/problems/delete-tree-nodes/)

## 题目大意

**描述**：给你一棵以节点 $0$ 为根节点的树，定义如下：
- 节点的总数为 $nodes$ 个。
- 第 $i$ 个节点的值为 $value[i]$。
- 第 $i$ 个节点的父节点是 $parent[i]$（$parent[0] = -1$）。

你需要删除节点值之和为 $0$ 的每一棵子树。在完成所有删除之后，返回树中剩余节点的数目。

**要求**：返回剩余节点的数目。

**说明**：

- $1 \le nodes \le 10^4$。
- $parent.length == nodes$。
- $0 \le parent[i] \le nodes - 1$。
- $parent[0] == -1$ 表示节点 $0$ 是树的根。
- $value.length == nodes$。
- $-10^5 \le value[i] \le 10^5$。
- 题目输入数据保证是一棵有效的树。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/30/1421_sample_1.png)

```python
输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
输出：2
```

- 示例 2：

```python
输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
输出：6
```

## 解题思路

### 思路 1：后序遍历（DFS）

###### 1. 核心思想

删除和为 $0$ 的子树：如果一棵子树的所有节点值加起来等于 $0$，就把这棵子树整个砍掉。

关键问题是**处理顺序**：删除一个子树时，它的子节点可能已经被删除了吗？不能。我们必须先知道子树的完整和才能判断它是否该被删除。所以需要**从叶子节点向上**计算——这正好是树的后序遍历（先处理子节点，再处理父节点）。

后序遍历的顺序保证了：一个节点的所有子节点都被处理完之后，我们才处理该节点本身。这样就能正确地递归判断。

###### 2. 具体步骤

**第 1 步：建图**

根据 $parent$ 数组构建每个节点的子节点列表 $children$。根节点 $0$ 的父节点是 $-1$，其余节点 $i$ 的父节点是 $parent[i]$，所以将 $i$ 添加到 $children[parent[i]]$ 中。

**第 2 步：后序遍历**

定义递归函数 $dfs(u)$，返回两个值：
- $sum$：以 $u$ 为根的子树中所有节点的值之和（删除操作之前）。
- $cnt$：以 $u$ 为根的子树中经过删除后剩余节点的个数。

递归过程：
- 初始化 $total\_sum = value[u]$，$total\_cnt = 1$。
- 遍历 $u$ 的所有子节点 $v$，递归调用 $dfs(v)$，将返回的子树和与剩余节点数累加到 $total\_sum$ 和 $total\_cnt$ 中。
- 处理完所有子节点后，如果 $total\_sum == 0$，说明整棵子树和为 $0$，应该全部删除，返回 $(0, 0)$。
- 否则返回 $(total\_sum, total\_cnt)$。

**第 3 步：返回结果**

根节点的 $dfs(0)$ 返回的剩余节点数就是答案。

**结合示例 1 走一遍：**

$nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]$

建树：
- 节点 $0$ 的子节点：$1, 2$
- 节点 $1$ 的子节点：$3$
- 节点 $2$ 的子节点：$4, 5, 6$

后序遍历：
- $dfs(3)$：$value[3]=0$，$sum=0$ → 返回 $(0, 0)$（节点 $3$ 被删除）
- $dfs(1)$：$value[1]=-2$，加上子节点 $3$ 的 $(0,0)$，$sum=-2$，不删除 → 返回 $(-2, 1)$
- $dfs(4)$：$value[4]=-2$ → 返回 $(-2, 1)$
- $dfs(5)$：$value[5]=-1$ → 返回 $(-1, 1)$
- $dfs(6)$：$value[6]=-1$ → 返回 $(-1, 1)$
- $dfs(2)$：$value[2]=4$，加上子节点 $4,5,6$ 的 $(-2,-1,-1)$，$sum = 4 - 2 - 1 - 1 = 0$ → 返回 $(0, 0)$（以 $2$ 为根的整棵子树被删除）
- $dfs(0)$：$value[0]=1$，加上子节点 $1$ 的 $(-2,1)$ 和子节点 $2$ 的 $(0,0)$，$sum = 1 - 2 = -1$，$cnt = 1 + 1 = 2$ → 返回 $(-1, 2)$

最终剩余 $2$ 个节点。

### 思路 1：代码

```python
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        # 第 1 步：构建子节点列表
        children = [[] for _ in range(nodes)]
        for i in range(1, nodes):
            children[parent[i]].append(i)

        # 第 2 步：后序遍历，返回 (子树和, 剩余节点数)
        def dfs(u):
            total_sum = value[u]
            total_cnt = 1
            # 先递归处理所有子节点
            for v in children[u]:
                child_sum, child_cnt = dfs(v)
                total_sum += child_sum
                total_cnt += child_cnt
            # 如果整棵子树和为 0，全部删除
            if total_sum == 0:
                return (0, 0)
            return (total_sum, total_cnt)

        # 第 3 步：从根节点开始
        return dfs(0)[1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(nodes)$，每个节点恰好被访问一次，后序遍历的总时间与节点数成正比。
- **空间复杂度**：$O(nodes)$，递归栈的深度在最坏情况下（树退化为链）为 $nodes$。同时需要 $children$ 数组存储每个节点的子节点列表，总大小也是 $O(nodes)$。
