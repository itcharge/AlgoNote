## 1. 多源最短路径简介

> **多源最短路径（All-Pairs Shortest Paths）**：指的是在一个带权图 $G = (V, E)$ 中，计算任意两个顶点之间的最短路径长度。

多源最短路径问题的本质，就是要找出图中每一对顶点之间的最短路径。这类问题在实际生活和工程中非常常见，例如：

1. 网络通信中，生成路由表以确定任意两点之间的最优传输路径；
2. 地图导航系统中，计算所有地点之间的距离矩阵；
3. 社交网络分析中，寻找两个人之间的最短关系链；
4. 交通网络中，规划任意两地之间的最优行车路线。

常用的多源最短路径算法有：

1. **Floyd-Warshall 算法**：一种基于动态规划的方法，能处理负权边，但无法处理负权环。
2. **Johnson 算法**：结合了 Bellman-Ford 和 Dijkstra 算法，既能处理负权边，也能高效应对稀疏图，但同样不能处理负权环。
3. **多次 Dijkstra 算法**：对每个顶点分别运行一次 Dijkstra 算法，适用于没有负权边的图。

## 2. Floyd-Warshall 算法

### 2.1 Floyd-Warshall 算法的核心思想

> **Floyd-Warshall 算法**：这是一种经典的动态规划算法，通过不断尝试引入不同的中间节点，来优化任意两点之间的最短路径。

通俗来说，Floyd-Warshall 算法的核心思想如下：

1. 假设要找从顶点 $i$ 到顶点 $j$ 的最短路径，试着经过某个中间顶点 $k$，看看能不能让路径更短。
2. 如果发现「先从 $i$ 到 $k$，再从 $k$ 到 $j$」的路径比原来「直接从 $i$ 到 $j$」的路径更短，就用这个更短的路径来更新答案。
3. 依次尝试所有顶点作为中间点 $k$，每次都用上述方法去优化所有点对之间的最短路径，最终就能得到全局最优解。

### 2.2 Floyd-Warshall 算法的实现步骤

1. 先初始化一个距离矩阵 $dist$，$dist[i][j]$ 表示从顶点 $i$ 到顶点 $j$ 的当前最短路径长度。
2. 如果 $i$ 和 $j$ 之间有直接的边，就把 $dist[i][j]$ 设为这条边的权重；如果没有，设为无穷大（表示不可达）。
3. 然后，依次枚举每个顶点 $k$ 作为「中转站」：
   - 对于所有顶点对 $(i, j)$，如果「从 $i$ 经过 $k$ 到 $j$」的路径更短（即 $dist[i][k] + dist[k][j] < dist[i][j]$），就用更短的路径更新 $dist[i][j]$。
4. 重复第 3 步，直到所有顶点都被作为中间点尝试过。
5. 最终，$dist$ 矩阵中每个 $dist[i][j]$ 就是从 $i$ 到 $j$ 的最短路径长度。

### 2.3 Floyd-Warshall 算法的实现代码

```python
def floyd_warshall(graph, n):
    """
    Floyd-Warshall 算法，计算所有点对之间的最短路径。
    :param graph: 邻接表，graph[i] = {j: weight, ...}，节点编号为 0~n-1
    :param n: 节点总数
    :return: dist 矩阵，dist[i][j] 表示 i 到 j 的最短路径长度
    """
    # 初始化距离矩阵，所有点对距离设为无穷大
    dist = [[float('inf')] * n for _ in range(n)]
    
    # 距离矩阵对角线设为 0，表示自己到自己的距离为 0
    for i in range(n):
        dist[i][i] = 0
        # 设置直接相连的顶点之间的距离
        for j, weight in graph.get(i, {}).items():
            dist[i][j] = weight

    # 三重循环，枚举每个中间点 k
    for k in range(n):
        for i in range(n):
            # 跳过不可达的起点
            if dist[i][k] == float('inf'):
                continue
            for j in range(n):
                # 跳过不可达的终点
                if dist[k][j] == float('inf'):
                    continue
                # 如果经过 k 能让 i 到 j 更短，则更新
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
```

### 2.4 Floyd-Warshall 算法分析

- **时间复杂度**：$O(V^3)$  
  - 算法包含三重嵌套循环，分别枚举所有中间点、起点和终点，因此总时间复杂度为 $O(V^3)$。

- **空间复杂度**：$O(V^2)$  
  - 主要空间消耗在距离矩阵 $dist$，需要 $O(V^2)$ 的空间。  
  - 由于采用邻接表存储原图结构，无需额外空间存储图的边。

**Floyd-Warshall 算法优点**：

1. 实现简洁，易于理解和编码。
2. 能处理负权边（但不能有负权环）。
3. 可用于检测负权环（如果某个顶点 $i$ 满足 $dist[i][i] < 0$，则存在负权环）。
4. 特别适合稠密图（边数接近 $V^2$）。

**Floyd-Warshall 算法缺点**：

1. 时间复杂度较高，不适合节点数很大的图。
2. 空间复杂度较高，需要维护完整的 $V \times V$ 距离矩阵。
3. 无法处理存在负权环的情况（如果有负权环，最短路无意义）。

## 3. Johnson 算法

### 3.1 Johnson 算法的核心思想

> **Johnson 算法**：是一种结合 Bellman-Ford 和 Dijkstra 算法的多源最短路径算法，能够处理负权边，但无法处理负权环。

Johnson 算法的核心思想如下：

1. 通过对图进行重新赋权，将所有边权变为非负，从而使 Dijkstra 算法适用；
2. 对每个顶点分别运行一次 Dijkstra 算法，计算其到其他所有顶点的最短路径；
3. 最后将结果还原为原图的最短路径权值。

### 3.2 Johnson 算法的实现步骤

1. 向原图添加一个新顶点 $s$，并从 $s$ 向所有其他顶点连一条权重为 0 的边；
2. 使用 Bellman-Ford 算法以 $s$ 为源点，计算 $s$ 到每个顶点 $v$ 的最短距离 $h(v)$；
3. 对于原图中的每条边 $(u, v)$，将其权重调整为 $w'(u, v) = w(u, v) + h(u) - h(v)$，使所有边权非负；
4. 对每个顶点 $u$，以 $u$ 为源点在重新赋权后的图上运行 Dijkstra 算法，得到 $u$ 到所有顶点的最短距离 $d'(u, v)$；
5. 最终结果还原为原图权重：$d(u, v) = d'(u, v) - h(u) + h(v)$，即为原图中 $u$ 到 $v$ 的最短路径长度。

### 3.3 Johnson 算法的实现代码

```python
from collections import defaultdict
import heapq

def johnson(graph, n):
    """
    Johnson 算法：多源最短路径，支持负权边但不支持负权环。
    :param graph: 邻接表，graph[u] = {v: w, ...}，节点编号 0~n-1
    :param n: 节点总数
    :return: dist 矩阵，dist[i][j] 表示 i 到 j 的最短路径长度；如果有负权环返回 None
    """
    # 1. 构建新图，添加超级源点 s（编号为 n），从 s 向所有顶点连权重为 0 的边
    new_graph = defaultdict(dict)
    for u in graph:
        for v, w in graph[u].items():
            new_graph[u][v] = w
    for u in range(n):
        new_graph[n][u] = 0  # s -> u，权重为 0

    # 2. Bellman-Ford 算法，计算超级源点 s 到每个顶点的最短距离 h(v)
    h = [float('inf')] * (n + 1)
    h[n] = 0  # s 到自身距离为 0
    # 最多 n 轮松弛
    for _ in range(n):
        updated = False
        for u in new_graph:
            for v, w in new_graph[u].items():
                if h[u] != float('inf') and h[v] > h[u] + w:
                    h[v] = h[u] + w
                    updated = True
        if not updated:
            break

    # 检查负权环：如果还能松弛，说明有负环
    for u in new_graph:
        for v, w in new_graph[u].items():
            if h[u] != float('inf') and h[v] > h[u] + w:
                return None  # 存在负权环

    # 3. 重新赋权：w'(u,v) = w(u,v) + h[u] - h[v]，保证所有边权非负
    reweighted_graph = defaultdict(dict)
    for u in graph:
        for v, w in graph[u].items():
            reweighted_graph[u][v] = w + h[u] - h[v]

    # 4. 对每个顶点运行 Dijkstra 算法，计算最短路径
    dist = [[float('inf')] * n for _ in range(n)]
    for source in range(n):
        d = [float('inf')] * n
        d[source] = 0
        heap = [(0, source)]
        visited = [False] * n
        while heap:
            cur_dist, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in reweighted_graph[u].items():
                if d[v] > cur_dist + w:
                    d[v] = cur_dist + w
                    heapq.heappush(heap, (d[v], v))
        # 5. 还原原图权重
        for v in range(n):
            if d[v] != float('inf'):
                dist[source][v] = d[v] - h[source] + h[v]
    return dist
```

### 3.4 Johnson 算法复杂度分析

- **时间复杂度**：$O(VE \log V)$
  - 需要运行一次 Bellman-Ford 算法，时间复杂度为 $O(VE)$
  - 需要运行 $V$ 次 Dijkstra 算法，每次时间复杂度为 $O(E \log V)$
  - 因此总时间复杂度为 $O(VE \log V)$

- **空间复杂度**：$O(V^2)$
  - 主要空间消耗在距离矩阵（$O(V^2)$）以及重新赋权后的图（$O(E)$）。
  - 因此总体空间复杂度为 $O(V^2)$。

## 练习题目

- [0815. 公交路线](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0800-0899/bus-routes.md)
- [1162. 地图分析](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1100-1199/as-far-from-land-as-possible.md)

- [多源最短路径题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%A4%9A%E6%BA%90%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84%E9%A2%98%E7%9B%AE)