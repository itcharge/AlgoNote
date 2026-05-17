# [1168. 水资源分配优化](https://leetcode.cn/problems/optimize-water-distribution-in-a-village/)

- 标签：并查集、图、最小生成树、堆（优先队列）
- 难度：困难

## 题目链接

- [1168. 水资源分配优化 - 力扣](https://leetcode.cn/problems/optimize-water-distribution-in-a-village/)

## 题目大意

**描述**：村里面一共有 $n$ 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。对于每个房子 $i$，有两种供水方案：
- **建井**：直接在房子内建造水井，成本为 $wells[i-1]$。
- **接管**：从另一口井铺设管道引水，数组 $pipes$ 给出了铺设管道的成本，其中 $pipes[j] = [house1_j, house2_j, cost_j]$ 表示连接房子 $house1_j$ 和 $house2_j$ 的成本。连接是双向的。

**要求**：返回为所有房子都供水的最低总成本。

**说明**：

- $2 \le n \le 10^{4}$。
- $wells.length == n$。
- $0 \le wells[i] \le 10^{5}$。
- $1 \le pipes.length \le 10^{4}$。
- $pipes[j].length == 3$。
- $1 \le house1_j, house2_j \le n$。
- $0 \le cost_j \le 10^{5}$。

**示例**：

- 示例 1：

```python
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/08/23/1359_ex1.png)

输入：n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
输出：3
解释：最好的策略是在第一个房子里建造水井（成本为 1），然后将其他房子铺设管道连起来（成本为 2），所以总成本为 3。
```

- 示例 2：

```python
输入：n = 2, wells = [1,1], pipes = [[1,2,1]]
输出：2
```

## 解题思路

### 思路 1：最小生成树（添加虚拟节点）

**为什么这个方法是对的？** 每个房子要么自己建井（连到虚拟水源），要么通过管道从其他房子引水（连到其他房子）。最终所有房子都必须有水源，所以整个图（房子 $+$ 虚拟水源）必须连通。最小生成树恰好能找到连通所有节点的最小成本方案。

**拆解步骤（Kruskal 算法）**：

1. **构建所有边**：
   - 对于每个房子 $i$，添加一条虚拟边 $(0, i, wells[i-1])$，表示建井的成本。
   - 直接将已有的管道加入边列表。

2. **对所有边按成本从小到大排序**。

3. **用并查集逐个连边**：从成本最小的边开始，如果这条边连接的两个节点还没有连通，就选择这条边并合并它们。

4. **选了 $n$ 条边后停止**（$n+1$ 个节点需要 $n$ 条边连通）。

### 思路 1：代码

```python
class UnionFind:
    """并查集，用来快速判断两个节点是否已经连通"""
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        # 路径压缩，让后续查找更快
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 合并两个节点所在的集合，返回是否成功合并
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[px] = py
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # 收集所有边：管道边的成本
        edges = []
        for house1, house2, cost in pipes:
            edges.append((cost, house1, house2))

        # 虚拟水源是节点 0，连接水源到每个房子的成本就是建井成本
        for i, well_cost in enumerate(wells):
            edges.append((well_cost, 0, i + 1))

        # 按成本从小到大排序（Kruskal 算法的核心）
        edges.sort()

        # 用并查集维护连通性，一共 n+1 个节点（0 到 n）
        uf = UnionFind(n + 1)
        total_cost = 0
        edges_used = 0

        for cost, u, v in edges:
            # 如果这条边连接的两个节点还没连通，就选它
            if uf.union(u, v):
                total_cost += cost
                edges_used += 1
                # 连通 n+1 个节点需要 n 条边
                if edges_used == n:
                    break

        return total_cost
```

### 思路 1：复杂度分析

- **时间复杂度**：$O((n + m) \log (n + m))$，其中 $m$ 是管道数量。用人话说就是：总共有 $n + m$ 条边，排序需要 $O((n+m) \log (n+m))$ 时间，并查集操作接近常数，所以排序是最花时间的步骤。
- **空间复杂度**：$O(n + m)$，需要存储所有边的信息。
