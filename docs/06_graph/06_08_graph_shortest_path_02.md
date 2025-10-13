## 1. Bellman-Ford 算法

### 1.1 Bellman-Ford 算法的核心思想

> **Bellman-Ford 算法**：一种可以处理带有负权边的单源最短路径算法，还能检测图中是否存在负权环。

Bellman-Ford 算法的本质思路如下：

1. 对图中所有的边，重复进行 $V - 1$ 轮「松弛」操作（$V$ 为顶点数）。
2. 每一轮松弛，就是尝试用每条边去更新目标节点的最短距离，看能否变得更短。
3. 如果在 $V - 1$ 轮松弛后，仍然有边可以继续更新距离，说明图中存在负权环。
4. 该算法可以正确处理负权边，但如果有负权环，则无法得到最短路径。

### 1.2 Bellman-Ford 算法的实现步骤

1. 初始化距离数组：源点距离设为 $0$，其余所有节点距离设为无穷大。
2. 重复 $V - 1$ 轮，每轮：
   - 遍历所有边
   - 对每条边尝试松弛：如果通过这条边能让目标节点距离更短，则更新
3. 第 $V$ 轮再遍历所有边，检查是否还能松弛：
   - 如果还能松弛，说明有负权环
   - 如果不能松弛，说明最短路径已确定
4. 返回最短路径的距离数组

### 1.3 Bellman-Ford 算法的代码实现

```python
class Solution:
    def bellmanFord(self, graph, n, source):
        """
        Bellman-Ford 算法求解单源最短路径，可处理负权边，并检测负权环。
        :param graph: 邻接表，graph[u] = {v: w, ...}
        :param n: 节点总数（节点编号从 1 到 n）
        :param source: 源点编号
        :return: dist 数组，dist[i] 表示源点到 i 的最短距离；如果存在负权环返回 None
        """
        # 初始化距离数组，所有点距离为正无穷，源点距离为 0
        dist = [float('inf')] * (n + 1)
        dist[source] = 0

        # 进行 n - 1 轮松弛操作
        for i in range(n - 1):
            updated = False  # 优化：记录本轮是否有更新
            # 遍历所有边，尝试松弛
            for u in graph:
                for v, w in graph[u].items():
                    # 如果 u 可达，且通过 u 到 v 更短，则更新
                    if dist[u] != float('inf') and dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        updated = True
            # 如果本轮没有任何更新，说明已提前收敛，可终止
            if not updated:
                break

        # 再遍历一遍所有边，检查是否还能松弛，如果能则存在负权环
        for u in graph:
            for v, w in graph[u].items():
                if dist[u] != float('inf') and dist[v] > dist[u] + w:
                    return None  # 存在负权环

        return dist
```

### 1.4 Bellman-Ford 算法复杂度分析

- **时间复杂度**：$O(VE)$。
   - Bellman-Ford 算法的核心在于「松弛」操作。对于 $V$ 个顶点，最短路径最多只需要经过 $V - 1$ 条边，因此算法需要进行 $V - 1$ 轮松弛，每一轮都要遍历所有的边。  
   - 每一轮松弛操作的时间复杂度为 $O(E)$，共进行 $V - 1$ 轮，总体时间复杂度为 $O((V - 1) \times E)$，通常简写为 $O(VE)$。  
   - 这种复杂度意味着 Bellman-Ford 算法在稠密图（边很多）时效率较低，但在稀疏图或边数较少时仍然可用。  
   - 另外，算法还会额外进行一次遍历所有边，用于检测负权环，但这不会改变主导复杂度。
- **空间复杂度**：$O(V)$。
   - 主要空间消耗在距离数组 $dist$，用于记录源点到每个节点的最短距离，大小为 $O(V)$。  
   - 图的存储采用邻接表（dict of dict），如果输入本身就是邻接表，则无需额外空间。  
   - 不需要像 Dijkstra 算法那样维护优先队列，也不需要额外的辅助数组，因此空间开销较小。  

## 2. SPFA 算法

### 2.1 SPFA 算法的核心思想

> **SPFA（Shortest Path Faster Algorithm）算法**：是 Bellman-Ford 算法的队列优化版本。它通过只处理那些「距离被更新过」的节点，显著减少了无效的松弛操作，从而提升了效率。

SPFA 的本质可以简单理解为：

1. 用队列维护「待处理」的节点，而不是每轮都遍历所有边。
2. 只有当某个节点的最短距离被更新时，才把它加入队列，等待后续处理。
3. 这样可以跳过很多不需要松弛的节点，避免重复无效计算。
4. SPFA 能处理负权边，也能检测负权环。

### 2.2 SPFA 算法的实现步骤

1. 初始化距离数组：源点距离设为 $0$，其余节点距离设为无穷大。
2. 创建一个队列，把源点加入队列。
3. 当队列不为空时，重复以下操作：
   - 取出队首节点 $u$。
   - 遍历 $u$ 的所有邻居 $v$。
   - 如果通过 $u$ 到 $v$ 的距离更短，则更新 $v$ 的距离。
   - 如果 $v$ 不在队列中，则将 $v$ 加入队列，等待后续处理。
4. 重复上述过程，直到队列为空。
5. 最终返回源点到各节点的最短距离数组。

这样，SPFA 只会处理那些「有可能被更新」的节点，效率通常远高于朴素的 Bellman-Ford 算法，尤其在稀疏图中表现更优。

### 2.3 SPFA 算法的代码实现

```python
from collections import deque

def spfa(graph, n, source):
    """
    SPFA（Shortest Path Faster Algorithm）算法，求解单源最短路径，可处理负权边，并检测负权环。
    :param graph: 邻接表，graph[u] = {v: w, ...}
    :param n: 节点总数（节点编号从 1 到 n）
    :param source: 源点编号
    :return: dist 数组，dist[i] 表示源点到 i 的最短距离；如果存在负权环返回 None
    """
    # 距离数组，初始化为无穷大，dist[i] 表示源点到 i 的最短距离
    dist = [float('inf')] * (n + 1)
    dist[source] = 0  # 源点到自身距离为 0

    # 队列，存储待处理的节点
    queue = deque()
    queue.append(source)

    # 标记数组，in_queue[i] 表示节点 i 是否在队列中，避免重复入队
    in_queue = [False] * (n + 1)
    in_queue[source] = True

    # 记录每个节点的入队次数，用于检测负权环
    count = [0] * (n + 1)
    count[source] = 1  # 源点已入队一次

    while queue:
        u = queue.popleft()
        in_queue[u] = False  # 当前节点出队

        # 遍历 u 的所有邻居 v
        for v, w in graph.get(u, {}).items():
            # 如果通过 u 到 v 的距离更短，则更新
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                # 只有距离被更新，才需要考虑入队
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    count[v] += 1
                    # 如果某个节点入队次数超过 n-1，说明存在负权环
                    if count[v] >= n:
                        return None  # 存在负权环，返回 None

    return dist
```

### 2.4 SPFA 算法复杂度分析

- **时间复杂度**：
   - 平均情况下，SPFA 算法的时间复杂度为 $O(kE)$，其中 $E$ 表示边数，$k$ 是每个节点的平均入队次数。由于大多数实际图中 $k$ 较小，SPFA 的实际运行效率通常远高于 Bellman-Ford。
   - 最坏情况下，SPFA 的时间复杂度退化为 $O(VE)$，其中 $V$ 为节点数。这种情况一般出现在存在大量负权边或特殊构造的图中，此时每条边都可能被反复松弛，导致每个节点最多入队 $V$ 次，与 Bellman-Ford 算法相同。
   - 总结：虽然最坏情况下复杂度与 Bellman-Ford 一致，但在绝大多数实际应用中，SPFA 算法由于只处理被更新的节点，往往能大幅减少无效操作，运行速度更快。
- **空间复杂度**：$O(V)$。
   - 主要空间消耗包括：
      - 距离数组 $dist$，用于记录源点到每个节点的最短距离，空间为 $O(V)$；
      - 队列 $queue$，用于存储待处理节点，最坏情况下队列长度为 $O(V)$；
      - 标记数组 $in\_queue$ 和入队次数数组 $count$，均为 $O(V)$。
   - 因此，SPFA 算法的总空间复杂度为 $O(V)$，适合大多数实际场景。

## 练习题目

- [0743. 网络延迟时间](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/network-delay-time.md)
- [0787. K 站中转内最便宜的航班](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/cheapest-flights-within-k-stops.md)
- [1631. 最小体力消耗路径](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1600-1699/path-with-minimum-effort.md)

- [单源最短路径题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8D%95%E6%BA%90%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84%E9%A2%98%E7%9B%AE)