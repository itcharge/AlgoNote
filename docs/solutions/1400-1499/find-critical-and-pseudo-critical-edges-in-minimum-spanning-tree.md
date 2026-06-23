# [1489. 找到最小生成树里的关键边和伪关键边](https://leetcode.cn/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

- 标签：并查集、图、最小生成树、排序、强连通分量
- 难度：困难

## 题目链接

- [1489. 找到最小生成树里的关键边和伪关键边 - 力扣](https://leetcode.cn/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

## 题目大意

**描述**：给定 $n$ 个节点和 $m$ 条边（带权）。定义：
- **关键边**：如果删除该边，最小生成树的权值和会增加（即该边是所有 MST 的必需边）。
- **伪关键边**：虽然不是关键边，但出现在某些 MST 中（不是所有 MST 都必需，但至少有一个 MST 包含它）。

**要求**：返回关键边和伪关键边的索引列表。

**说明**：
- $2 \le n \le 100$。
- $1 \le m \le 200$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/21/ex1.png)

```python
输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
输出：[[0,1],[2,3,4,5]]
解释：上图描述了给定图。
下图是所有的最小生成树。
![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/21/msts.png)
注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。


示例 2 ：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/21/ex2.png)

输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
输出：[[],[0,1,2,3]]
解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。
```

- 示例 2：

```python
输入：
输出：
```

## 解题思路

### 思路 1：Kruskal + 枚举

#### 1. 核心思想

先用 Kruskal 求出 MST 的基准权值 $base\_weight$。

然后对每条边分别测试：
1. **强制选择该边**：将该边加入 MST（提前加入并查集），再对剩余边跑 Kruskal。如果得到的 MST 总权值等于 $base\_weight$，则该边出现在某个 MST 中，不是关键边。
2. **删除该边**：在 Kruskal 中跳过该边。如果得到的 MST 总权值大于 $base\_weight$（或无法连通），则该边是关键边。

#### 2. 具体步骤

**第 1 步**：给边添加索引，按权值排序。

**第 2 步**：Kruskal 计算 $base\_weight$（标准 MST 权值和）。

**第 3 步**：遍历每条边 $e$：
- 删除测试：跳过 $e$ 跑 Kruskal。如果权值 $> base\_weight$ 或不能连通，$e$ 是关键边。
- 否则，强制测试：先加入 $e$ 跑 Kruskal。如果权值 $== base\_weight$，$e$ 是伪关键边。

**第 4 步**：返回关键边和伪关键边列表。

#### 3. 复杂度优化

$n \le 100$，$m \le 200$。对每条边分别跑 Kruskal 是 $O(m^2 \log m + m^2 \alpha(n))$，即约 $200^2 = 40000$ 条边次，可行。

### 思路 1：代码

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        self.count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int,
                                            edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        # 给边加索引
        edge_list = [(u, v, w, idx) for idx, (u, v, w) in enumerate(edges)]
        edge_list.sort(key=lambda x: x[2])

        def kruskal(block_edge=-1, force_edge=-1):
            """返回MST总权和，-1表示不能连通"""
            uf = UnionFind(n)
            weight = 0
            if force_edge != -1:
                u, v, w, _ = edge_list[force_edge]
                uf.union(u, v)
                weight += w
            for i, (u, v, w, _) in enumerate(edge_list):
                if i == block_edge:
                    continue
                if uf.union(u, v):
                    weight += w
            # 检查是否所有节点连通
            root = uf.find(0)
            for i in range(1, n):
                if uf.find(i) != root:
                    return -1
            return weight

        # 基准 MST 权值
        base = kruskal()

        critical = []
        pseudo_critical = []

        for i in range(m):
            # 删除测试
            if kruskal(block_edge=i) != base:
                critical.append(edge_list[i][3])
            else:
                # 强制测试
                if kruskal(force_edge=i) == base:
                    pseudo_critical.append(edge_list[i][3])

        return [critical, pseudo_critical]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m^2 \log m)$，对每条边跑一次 Kruskal。
- **空间复杂度**：$O(n + m)$。
