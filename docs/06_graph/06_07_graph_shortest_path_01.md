## 1. 单源最短路径简介

> **单源最短路径（Single Source Shortest Path）**：在一个带权图 $G = (V, E)$ 中，给定一个起点（源点）$v$，找到从这个源点出发，到图中其他所有顶点的最短路径长度。这里的「最短路径」指的是路径上所有边的权重之和最小。

简单来说，单源最短路径问题就是：从一个点出发，如何走到其他所有点，并且让每条路径的总权重最小。

这个问题在实际生活中非常常见，比如：  
- 地图导航（如何从一个城市到其他城市距离最短）  
- 网络路由（数据包如何选择最快的路径传输）  
- 通信网络优化等

常用的单源最短路径算法有：

1. **Dijkstra 算法**：一种贪心算法，适用于所有边权都为非负数的图。每次选择当前距离源点最近的未处理节点，并用它来更新其它节点的最短距离。
2. **Bellman-Ford 算法**：可以处理有负权边的图。它通过多次遍历所有边，不断尝试用更短的路径更新节点距离，逐步逼近最短路径。
3. **SPFA 算法**：是 Bellman-Ford 的队列优化版本。每次只处理那些距离被更新过的节点，通常效率更高。

不同算法适用于不同类型的图。根据实际问题的特点，选择合适的算法，才能高效地求解单源最短路径问题。

## 2. Dijkstra 算法

### 2.1 Dijkstra 算法的核心思想

> **Dijkstra 算法核心思想**：每次选出距离起点最近、最短路尚未确定的节点，用它去尝试更新其它节点的最短距离，逐步扩展，直到所有节点的最短路径都确定。

Dijkstra 算法是解决单源最短路径的经典方法，适用于所有边权为非负数的图。它的流程很简单：每次从未确定最短路的节点中，选出距离起点最近的那个，把它的最短距离「锁定」，并用它去更新其它节点的距离。重复这个过程，直到所有节点的最短路径都被确定。

本质上，Dijkstra 算法是一种贪心策略：每一步都相信当前能确定的最短距离，认为已经确定的节点最短路不会再被更优路径更新。这样一步步扩展，最终得到从起点到所有节点的最短路径。

需要注意的是，Dijkstra 算法 **不能处理有负权边的图**。如果图中存在负权边，最短路径可能会被后续的负权边更新，导致算法失效。这种情况下应使用 Bellman-Ford 或 SPFA 算法。

### 2.2 Dijkstra 算法的实现步骤

1. 初始化距离数组 $dist$：将起点 $source$ 的距离设为 $0$，其余所有节点的距离设为无穷大。
2. 准备一个访问集合 $visited$，用于记录哪些节点的最短路径已经确定。
3. 每次从未访问的节点中，选出距离起点最近的节点，将其加入 $visited$。
4. 用这个节点尝试更新所有相邻节点的最短距离。
5. 重复步骤 3 和 4，直到所有节点都被访问。
6. 最终，距离数组中即为起点到所有节点的最短路径长度。如果某些节点无法到达，距离仍为无穷大。

### 2.3 Dijkstra 算法的实现代码

```python
class Solution:
    def dijkstra(self, graph, n, source):
        """
        Dijkstra 算法求解单源最短路径
        :param graph: 邻接表表示的有向图，graph[u] = {v: w, ...}
        :param n: 节点总数（节点编号从 1 到 n）
        :param source: 源点编号
        :return: dist 数组，dist[i] 表示源点到 i 的最短距离
        """
        # 距离数组，初始化为无穷大
        dist = [float('inf')] * (n + 1)
        dist[source] = 0  # 源点到自身距离为 0

        visited = set()  # 已确定最短路的节点集合

        while len(visited) < n:
            # 在所有未访问的节点中，选择距离源点最近的节点
            current_node = -1
            min_distance = float('inf')
            for i in range(1, n + 1):
                if i not in visited and dist[i] < min_distance:
                    min_distance = dist[i]
                    current_node = i

            # 如果没有可处理的节点（说明剩下的节点不可达），提前结束
            if current_node == -1:
                break

            visited.add(current_node)  # 标记当前节点为已访问

            # 遍历当前节点的所有邻居，尝试更新最短距离
            for neighbor, weight in graph.get(current_node, {}).items():
                if neighbor not in visited:
                    if dist[current_node] + weight < dist[neighbor]:
                        dist[neighbor] = dist[current_node] + weight

        return dist

# 使用示例
# 构建一个有向图，邻接表表示
graph = {
    1: {2: 2, 3: 4},
    2: {3: 1, 4: 7},
    3: {4: 3},
    4: {}
}
n = 4  # 节点数量
source = 1  # 源点

dist = Solution().dijkstra(graph, n, source)
print("从节点", source, "到其他节点的最短距离：")
for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(f"到节点 {i} 的距离：不可达")
    else:
        print(f"到节点 {i} 的距离：{dist[i]}")
```

### 2.4 Dijkstra 算法复杂度分析

- **时间复杂度**：$O(V^2)$。
  - 外层循环每次选择一个未访问且距离最小的节点，共进行 $O(V)$ 次。  
  - 每次选择最小距离节点时，需要遍历所有未访问节点，复杂度为 $O(V)$。  
  - 因此整体时间复杂度为 $O(V^2)$。

- **空间复杂度**：$O(V)$。 
  - 主要空间消耗在距离数组 $dist$ 和访问集合 $visited$，各占 $O(V)$。  
  - 总空间复杂度为 $O(V)$。


## 3. 堆优化 Dijkstra 算法

### 3.1 堆优化 Dijkstra 算法思想

> **堆优化 Dijkstra 算法**：利用优先队列（小根堆）高效选取当前距离最小的节点，将原本 $O(V^2)$ 的查找过程优化为 $O(\log V)$，显著提升算法效率。

传统 Dijkstra 算法每次都要遍历所有未访问节点以找到距离最小者，时间复杂度为 $O(V)$。堆优化后，借助优先队列动态维护所有待处理节点的最短距离，每次取出最小值仅需 $O(\log V)$。

堆优化 Dijkstra 算法的核心思想如下：
1. 用优先队列实时维护所有待处理节点的最短距离；
2. 每次弹出距离最小的节点进行松弛操作；
3. 如果发现更短路径，则更新距离并将新距离入队；
4. 依靠堆的性质，始终保证每次处理的都是当前距离最小的节点。

### 3.2 堆优化 Dijkstra 算法实现步骤

1. 初始化距离数组，源点距离设为 $0$，其余节点设为无穷大。
2. 创建优先队列，将源节点及其距离 $(0, source)$ 入队。
3. 当优先队列非空时，重复以下操作：
   - 弹出队首（距离最小）节点；
   - 如果该节点的距离已大于当前最短距离，跳过；
   - 否则，遍历其所有邻居，尝试松弛：
     - 如果通过当前节点到邻居的距离更短，则更新距离并将新距离入队。
4. 队列为空时结束，返回所有节点的最短距离数组。

### 3.3 堆优化 Dijkstra 算法实现代码

```python
import heapq

class Solution:
    def dijkstra(self, graph, n, source):
        """
        堆优化 Dijkstra 算法，计算单源最短路径
        :param graph: 邻接表，graph[u] = {v: w, ...}
        :param n: 节点总数（节点编号从 1 到 n）
        :param source: 源点编号
        :return: dist[i] 表示源点到 i 的最短距离
        """
        # 距离数组，初始化为无穷大
        dist = [float('inf')] * (n + 1)
        dist[source] = 0  # 源点到自身距离为 0

        # 小根堆，存储 (距离, 节点) 元组
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            # 如果弹出的节点距离不是最短的，说明已被更新，跳过
            if current_distance > dist[current_node]:
                continue

            # 遍历当前节点的所有邻居
            for neighbor, weight in graph.get(current_node, {}).items():
                new_distance = current_distance + weight
                # 如果找到更短路径，则更新并入堆
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return dist

# 使用示例
# 构建一个有向图，邻接表表示
graph = {
    1: {2: 2, 3: 4},
    2: {3: 1, 4: 7},
    3: {4: 3},
    4: {}
}
n = 4  # 节点数量
source = 1  # 源点编号

dist = Solution().dijkstra(graph, n, source)
print("从节点", source, "到其他节点的最短距离：")
for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(f"到节点 {i} 的距离：不可达")
    else:
        print(f"到节点 {i} 的距离：{dist[i]}")
```

### 3.4 堆优化 Dijkstra 算法复杂度分析

- **时间复杂度**：$O((V + E) \log V)$。
  - 堆优化 Dijkstra 算法中，每个节点最多会被弹出优先队列一次，每次弹出操作的复杂度为 $O(\log V)$。  
  - 每条边在松弛操作时最多会导致一次入堆，入堆操作的复杂度同样为 $O(\log V)$。  
  - 因此，总体时间复杂度为 $O((V + E) \log V)$，其中 $V$ 为节点数，$E$ 为边数。

- **空间复杂度**：$O(V)$。  
  - 主要空间消耗在距离数组和优先队列，二者最坏情况下均为 $O(V)$ 级别。

## 练习题目

- [0743. 网络延迟时间](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/network-delay-time.md)
- [0787. K 站中转内最便宜的航班](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/cheapest-flights-within-k-stops.md)
- [1631. 最小体力消耗路径](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1600-1699/path-with-minimum-effort.md)

- [单源最短路径题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8D%95%E6%BA%90%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84%E9%A2%98%E7%9B%AE)