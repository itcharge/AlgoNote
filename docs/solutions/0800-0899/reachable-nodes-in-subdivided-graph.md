# [0882. 细分图中的可到达节点](https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/)

- 标签：图、最短路、堆（优先队列）
- 难度：困难

## 题目链接

- [0882. 细分图中的可到达节点 - 力扣](https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/)

## 题目大意

**描述**：

给定一个无向图（原始图），图中有 $n$ 个节点，编号从 0 到 $n - 1$ 。你决定将图中的每条边「细分」为一条节点链，每条边之间的新节点数各不相同。

图用由边组成的二维数组 $edges$ 表示，其中 $edges[i] = [u_i, v_i, cnt_i]$ 表示原始图中节点 $u_i$ 和 $v_i$ 之间存在一条边，$cnt_i$ 是将边「细分」后的新节点总数。注意，$cnt_i == 0$ 表示边不可细分。
要「」边 $[u_i, v_i]$ ，需要将其替换为 $(cnt_i + 1)$ 条新边，和 $cnt_i$ 个新节点。新节点为 $x1, x2, ..., xcnt_i$，新边为 $[ui, x1], [x1, x2], [x2, x3], ..., [xcnt_i-1, xcnt_i], [xcnt_i, v_i]$。

现在得到一个「新的细分图」，请你计算从节点 0 出发，可以到达多少个节点？如果节点间距离是 $maxMoves$ 或更少，则视为 可以到达。

给定原始图和 $maxMoves$。

**要求**：

返回「新的细分图中从节点 0 出发 可到达的节点数」。

**说明**：

- $0 \le edges.length \le min(n \times (n - 1) / 2, 10^{4})$。
- $edges[i].length == 3$。
- $0 \le u_i \lt v_i \lt n$。
- 图中「不存在平行边」。
- $0 \le cnt_i \le 10^{4}$。
- $0 \le maxMoves \le 10^{9}$。
- $1 \le n \le 3000$。

**示例**：

- 示例 1：

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/01/origfinal.png)

```python
输入：edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
输出：13
解释：边的细分情况如上图所示。
可以到达的节点已经用黄色标注出来。
```

- 示例 2：

```python
输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
输出：23
```

## 解题思路

### 思路 1:Dijkstra 最短路

这道题的关键是：从节点 0 出发,在 $maxMoves$ 步内能到达多少个节点(包括原始节点和细分后的新节点)。

使用 Dijkstra 算法计算从节点 0 到其他所有节点的最短距离。对于每条边:
- 如果能从两端都到达这条边,需要避免重复计数中间的新节点
- 从节点 $u$ 出发,能到达边上的新节点数为 $\min(cnt, maxMoves - dist[u])$
- 从节点 $v$ 出发,能到达边上的新节点数为 $\min(cnt, maxMoves - dist[v])$
- 这条边上能到达的新节点总数为 $\min(cnt, \text{从u到达的数量} + \text{从v到达的数量})$

### 思路 1:代码

```python
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        import heapq
        from collections import defaultdict
        
        # 构建图
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt
        
        # Dijkstra 算法
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]  # (距离, 节点)
        visited = set()
        
        while heap:
            d, u = heapq.heappop(heap)
            
            if u in visited:
                continue
            visited.add(u)
            
            # 更新相邻节点的距离
            for v, cnt in graph[u].items():
                # 到达节点 v 需要的步数:到达 u 的步数 + 边上的新节点数 + 1
                new_dist = d + cnt + 1
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
        
        # 统计可到达的节点数
        result = 0
        
        # 统计原始节点
        for i in range(n):
            if dist[i] <= maxMoves:
                result += 1
        
        # 统计边上的新节点
        for u, v, cnt in edges:
            # 从 u 出发能到达的新节点数
            from_u = max(0, maxMoves - dist[u]) if dist[u] <= maxMoves else 0
            # 从 v 出发能到达的新节点数
            from_v = max(0, maxMoves - dist[v]) if dist[v] <= maxMoves else 0
            # 这条边上能到达的新节点总数(避免重复计数)
            result += min(cnt, from_u + from_v)
        
        return result
```

### 思路 1:复杂度分析

- **时间复杂度**:$O((n + m) \log n)$,其中 $n$ 是节点数,$m$ 是边数。Dijkstra 算法的时间复杂度。
- **空间复杂度**:$O(n + m)$,需要存储图和距离数组。
