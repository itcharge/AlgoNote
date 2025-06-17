## 1. 多源最短路径简介

> **多源最短路径（All-Pairs Shortest Paths）**：对于一个带权图 $G = (V, E)$，计算图中任意两个顶点之间的最短路径长度。

多源最短路径问题的核心是找到图中任意两个顶点之间的最短路径。这个问题在许多实际应用中都非常重要，比如：

1. 网络路由中的路由表计算
2. 地图导航系统中的距离矩阵计算
3. 社交网络中的最短关系链分析
4. 交通网络中的最优路径规划

常见的解决多源最短路径问题的算法包括：

1. **Floyd-Warshall 算法**：一种动态规划算法，可以处理负权边，但不能处理负权环。
2. **Johnson 算法**：结合了 Bellman-Ford 算法和 Dijkstra 算法，可以处理负权边，但不能处理负权环。
3. **重复 Dijkstra 算法**：对每个顶点运行一次 Dijkstra 算法，适用于无负权边的图。

## 2. Floyd-Warshall 算法

### 2.1 Floyd-Warshall 算法的算法思想

> **Floyd-Warshall 算法**：一种动态规划算法，通过逐步考虑中间顶点来更新任意两点之间的最短路径。

Floyd-Warshall 算法的核心思想是：

1. 对于图中的任意两个顶点 $i$ 和 $j$，考虑是否存在一个顶点 $k$，使得从 $i$ 到 $k$ 再到 $j$ 的路径比已知的从 $i$ 到 $j$ 的路径更短
2. 如果存在这样的顶点 $k$，则更新从 $i$ 到 $j$ 的最短路径
3. 通过考虑所有可能的中间顶点 $k$，最终得到任意两点之间的最短路径

### 2.2 Floyd-Warshall 算法的实现步骤

1. 初始化距离矩阵 $dist$，其中 $dist[i][j]$ 表示从顶点 $i$ 到顶点 $j$ 的最短路径长度
2. 对于每对顶点 $(i, j)$，如果存在边 $(i, j)$，则 $dist[i][j]$ 设为边的权重，否则设为无穷大
3. 对于每个顶点 $k$，作为中间顶点：
   - 对于每对顶点 $(i, j)$，如果 $dist[i][k] + dist[k][j] < dist[i][j]$，则更新 $dist[i][j]$
4. 重复步骤 3，直到考虑完所有可能的中间顶点
5. 返回最终的距离矩阵

### 2.3 Floyd-Warshall 算法的实现代码

```python
def floyd_warshall(graph, n):
    # 初始化距离矩阵
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    # 设置直接相连的顶点之间的距离
    for i in range(n):
        dist[i][i] = 0
        for j, weight in graph[i].items():
            dist[i][j] = weight
    
    # 考虑每个顶点作为中间顶点
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

代码解释：

1. `graph` 是一个字典，表示图的邻接表。例如，`graph[0] = {1: 3, 2: 4}` 表示从节点 0 到节点 1 的边权重为 3，到节点 2 的边权重为 4。
2. `n` 是图中顶点的数量。
3. `dist` 是一个二维数组，存储任意两点之间的最短路径长度。
4. 首先初始化距离矩阵，将对角线元素设为 0，表示顶点到自身的距离为 0。
5. 然后设置直接相连的顶点之间的距离。
6. 主循环中，对于每个顶点 $k$，考虑它作为中间顶点时，是否能缩短其他顶点之间的距离。
7. 最终返回的距离矩阵中，$dist[i][j]$ 表示从顶点 $i$ 到顶点 $j$ 的最短路径长度。

### 2.4 Floyd-Warshall 算法复杂度分析

- **时间复杂度**：$O(V^3)$
  - 需要三层嵌套循环，分别遍历所有顶点
  - 因此总时间复杂度为 $O(V^3)$

- **空间复杂度**：$O(V^2)$
  - 需要存储距离矩阵，大小为 $O(V^2)$
  - 不需要额外的空间来存储图的结构，因为使用邻接表表示

Floyd-Warshall 算法的主要优势在于：

1. 实现简单，容易理解
2. 可以处理负权边
3. 可以检测负权环（如果某个顶点到自身的距离变为负数，说明存在负权环）
4. 适用于稠密图

主要缺点：

1. 时间复杂度较高，不适用于大规模图
2. 空间复杂度较高，需要存储完整的距离矩阵
3. 不能处理负权环

## 3. Johnson 算法

### 3.1 Johnson 算法的算法思想

> **Johnson 算法**：一种结合了 Bellman-Ford 算法和 Dijkstra 算法的多源最短路径算法，可以处理负权边，但不能处理负权环。

Johnson 算法的核心思想是：

1. 通过重新赋权，将图中的负权边转换为非负权边
2. 对每个顶点运行一次 Dijkstra 算法，计算最短路径
3. 将结果转换回原始权重

### 3.2 Johnson 算法的实现步骤

1. 添加一个新的顶点 $s$，并添加从 $s$ 到所有其他顶点的边，权重为 0
2. 使用 Bellman-Ford 算法计算从 $s$ 到所有顶点的最短路径 $h(v)$
3. 重新赋权：对于每条边 $(u, v)$，新的权重为 $w(u, v) + h(u) - h(v)$
4. 对每个顶点 $v$，使用 Dijkstra 算法计算从 $v$ 到所有其他顶点的最短路径
5. 将结果转换回原始权重：对于从 $u$ 到 $v$ 的最短路径，原始权重为 $d(u, v) - h(u) + h(v)$

### 3.3 Johnson 算法的实现代码

```python
from collections import defaultdict
import heapq

def johnson(graph, n):
    # 添加新顶点 s
    new_graph = defaultdict(dict)
    for u in graph:
        for v, w in graph[u].items():
            new_graph[u][v] = w
        new_graph[n][u] = 0  # 从 s 到所有顶点的边权重为 0
    
    # 使用 Bellman-Ford 算法计算 h(v)
    h = [float('inf')] * (n + 1)
    h[n] = 0
    
    for _ in range(n):
        for u in new_graph:
            for v, w in new_graph[u].items():
                if h[v] > h[u] + w:
                    h[v] = h[u] + w
    
    # 检查是否存在负权环
    for u in new_graph:
        for v, w in new_graph[u].items():
            if h[v] > h[u] + w:
                return None  # 存在负权环
    
    # 重新赋权
    reweighted_graph = defaultdict(dict)
    for u in graph:
        for v, w in graph[u].items():
            reweighted_graph[u][v] = w + h[u] - h[v]
    
    # 对每个顶点运行 Dijkstra 算法
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for source in range(n):
        # 初始化距离数组
        d = [float('inf')] * n
        d[source] = 0
        
        # 使用优先队列
        pq = [(0, source)]
        visited = set()
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            
            for v, w in reweighted_graph[u].items():
                if d[v] > current_dist + w:
                    d[v] = current_dist + w
                    heapq.heappush(pq, (d[v], v))
        
        # 转换回原始权重
        for v in range(n):
            if d[v] != float('inf'):
                dist[source][v] = d[v] - h[source] + h[v]
    
    return dist
```

代码解释：

1. `graph` 是一个字典，表示图的邻接表。
2. `n` 是图中顶点的数量。
3. 首先添加一个新的顶点 $s$，并添加从 $s$ 到所有其他顶点的边，权重为 0。
4. 使用 Bellman-Ford 算法计算从 $s$ 到所有顶点的最短路径 $h(v)$。
5. 检查是否存在负权环，如果存在则返回 None。
6. 重新赋权，将图中的负权边转换为非负权边。
7. 对每个顶点运行一次 Dijkstra 算法，计算最短路径。
8. 将结果转换回原始权重，得到最终的距离矩阵。

### 3.4 Johnson 算法复杂度分析

- **时间复杂度**：$O(VE \log V)$
  - 需要运行一次 Bellman-Ford 算法，时间复杂度为 $O(VE)$
  - 需要运行 $V$ 次 Dijkstra 算法，每次时间复杂度为 $O(E \log V)$
  - 因此总时间复杂度为 $O(VE \log V)$

- **空间复杂度**：$O(V^2)$
  - 需要存储距离矩阵，大小为 $O(V^2)$
  - 需要存储重新赋权后的图，大小为 $O(E)$
  - 因此总空间复杂度为 $O(V^2)$
