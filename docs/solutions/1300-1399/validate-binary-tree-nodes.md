# [1361. 验证二叉树](https://leetcode.cn/problems/validate-binary-tree-nodes/)

- 标签：树、深度优先搜索、广度优先搜索、并查集、图、二叉树
- 难度：中等

## 题目链接

- [1361. 验证二叉树 - 力扣](https://leetcode.cn/problems/validate-binary-tree-nodes/)

## 题目大意

**描述**：给定 $n$ 个节点（编号 $0 \sim n-1$）和两个数组 $leftChild$ 和 $rightChild$。其中 $leftChild[i]$ 表示节点 $i$ 的左子节点编号（如果为 $-1$ 表示无左子），$rightChild[i]$ 表示节点 $i$ 的右子节点编号。

**要求**：判断这些节点能否构成一棵**有效的二叉树**。

**说明**：
- 二叉树定义：每个节点最多有两个子节点，且只有一个根节点，所有节点连通。
- $1 \le n \le 10^4$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/23/1503_ex1.png)

```python
输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
输出：true
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/23/1503_ex2.png)

```python
输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
输出：false
```


## 解题思路

### 思路 1：入度统计 + BFS 连通性检查

#### 1. 核心思想

一棵有效的二叉树需要满足以下条件：
1. **只有一个根节点**：入度为 $0$ 的节点有且仅有一个。
2. **所有非根节点入度恰为 $1$**：每个节点（除了根）只能有一个父节点。
3. **没有环**：从根节点遍历应当能访问到所有节点。
4. **每个节点最多有两个子节点**：左子节点和右子节点分别至多一个（题目定义本身就满足）。

因此算法分为三步：
1. 统计入度，找到根节点（入度为 $0$ 的唯一节点）。
2. 检查是否有节点入度 $\ge 2$（入度 $\ge 2$ 意味着有多个父节点）。
3. 从根节点 BFS，检查是否能访问所有节点。

#### 2. 具体步骤

**第 1 步**：统计入度数组 $indegree$，遍历 $i$：
- 如果 $leftChild[i] \ne -1$，$indegree[leftChild[i]]++$
- 如果 $rightChild[i] \ne -1$，$indegree[rightChild[i]]++$

同时还需检查：一个子节点是否被多次引用（入度 $\ge 2$），或某个节点被同时设为左子和右子。

**第 2 步**：找到根节点（入度为 $0$ 且出现在 $leftChild$/$rightChild$ 中或被作为根判断）。实际上根节点就是唯一入度为 $0$ 的节点。

如果没有入度为 $0$ 的节点（有环），或入度为 $0$ 的节点不止一个（多棵树），返回 $False$。

**第 3 步**：从根节点 BFS，统计访问到的节点数。如果能够访问所有 $n$ 个节点，返回 $True$。

#### 3. 举例说明

**例 1**：$n=4$，$leftChild=[1,-1,3,-1]$，$rightChild=[2,-1,-1,-1]$

```
      0
     / \
    1   2
       /
      3
```

入度：$indegree=[0,1,1,1]$，根为 $0$。BFS 能访问全部 $4$ 个节点 → $True$。

**例 2**：$n=4$，$leftChild=[1,-1,3,-1]$，$rightChild=[2,3,-1,-1]$

节点 $3$ 被节点 $1$（右子）和节点 $2$（左子）同时引用，入度 $=2$ → $False$。

#### 4. 易错点

- 根节点可能不止一个：形成森林，不是一棵树。
- 存在环：如 $0$ 的左子是 $1$，$1$ 的左子是 $0$。
- 存在节点不可达：从根出发不能访问所有节点。

### 思路 1：代码

```python
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
                                 rightChild: List[int]) -> bool:
        # 第 1 步：统计入度
        indegree = [0] * n
        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    indegree[child] += 1
                    # 入度 > 1 说明有多个父节点
                    if indegree[child] > 1:
                        return False

        # 第 2 步：找到根节点（入度为 0 的唯一节点）
        root = None
        for i in range(n):
            if indegree[i] == 0:
                if root is None:
                    root = i
                else:
                    return False  # 多于一个根

        if root is None:
            return False  # 没有根（有环）

        # 第 3 步：BFS 检查连通性
        visited = set()
        queue = [root]
        visited.add(root)

        for node in queue:
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    if child in visited:
                        return False  # 有环或多个父节点指向同一节点
                    visited.add(child)
                    queue.append(child)

        return len(visited) == n
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个节点遍历一次。
- **空间复杂度**：$O(n)$，$visited$ 集合和队列。

---

### 思路 2：并查集

也可以用并查集判断：
1. 每个子节点只能有一个父节点（合并前子节点尚未被合并过）。
2. 合并时不能形成环（两个节点已经在同一集合中）。
3. 最终仅有一个连通分量。

```python
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
                                 rightChild: List[int]) -> bool:
        parent = list(range(n))
        indegree = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False  # 形成环
            parent[ry] = rx
            return True

        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child == -1:
                    continue
                # 子节点已有父节点
                if indegree[child] == 1:
                    return False
                # 合并（检查环）
                if not union(i, child):
                    return False
                indegree[child] += 1

        # 检查连通分量是否为 1
        root_set = set(find(i) for i in range(n))
        return len(root_set) == 1
```
