## 1. 单源最短路径简介

> **单源最短路径（Single Source Shortest Path）**：对于一个带权图 $G = (V, E)$，其中每条边的权重是一个实数。另外，给定 $v$  中的一个顶点，称之为源点。则源点到其他所有各个顶点之间的最短路径长度，称为单源最短路径。

这里的路径长度，指的是路径上各边权之和。

单源最短路径问题的核心是找到从源点到其他各个顶点的路径，使得路径上边的权重之和最小。这个问题在许多实际应用中都非常重要，比如网络路由、地图导航、通信网络优化等。

常见的解决单源最短路径问题的算法包括：

1. **Dijkstra 算法**：一种贪心算法，用于解决无负权边的情况。它逐步扩展当前已知最短路径的范围，选择当前距离起始节点最近的节点，并更新与该节点相邻的节点的距离。
2. **Bellman-Ford 算法**：适用于有负权边的情况。它通过多次迭代来逐步逼近最短路径，每次迭代都尝试通过更新边的权重来缩短路径。
3. **SPFA 算法**：优化的 Bellman-Ford 算法，它在每次迭代中不遍历所有的边，而是选择性地更新与当前节点相关的边，从而提高了算法的效率。

这些算法根据图的特点和问题的需求有所不同，选择适合的算法可以在不同情况下有效地解决单源最短路径问题。

## 2. Dijkstra 算法

### 2.1 Dijkstra 算法的算法思想

> **Dijkstra 算法的算法思想**：通过逐步选择距离起始节点最近的节点，并根据这些节点的路径更新其他节点的距离，从而逐步找到最短路径。

Dijkstra 算法是一种用来解决单源最短路径问题的算法。这个算法适用于没有负权边的图。算法的核心思想是从源点出发，逐步找到到其他所有点的最短路径。它通过不断选择当前距离源点最近的节点，并更新与该节点相邻的节点的距离，最终得到所有节点的最短路径。

Dijkstra 算法使用贪心的策略。它每次选择当前未处理的节点中距离源点最近的节点，认为这个节点的最短路径已经确定。然后，它用这个节点的最短路径去更新其他相邻节点的距离。这个过程重复进行，直到所有节点的最短路径都被确定。

Dijkstra 算法的一个重要特点是它不能处理有负权边的图。因为负权边可能导致已经确定的最短路径被破坏。如果图中存在负权边，应该使用 Bellman-Ford 算法或 SPFA 算法。

### 2.2 Dijkstra 算法的实现步骤

1. 初始化距离数组，将源节点 $source$ 的距离设为 $0$，其他节点的距离设为无穷大。
2. 维护一个访问数组 $visited$，记录节点是否已经被访问。
3. 每次从未访问的节点中找到距离最小的节点，标记为已访问。
4. 更新该节点的所有相邻节点的距离。
5. 重复步骤 $3 \sim 4$，直到所有节点都被访问。
6. 最后返回所有节点中最大的距离值，如果存在无法到达的节点则返回 $-1$。



### 2.3 Dijkstra 算法的实现代码

```python
class Solution:
    def dijkstra(self, graph, n, source):
        # 初始化距离数组
        dist = [float('inf') for _ in range(n + 1)]
        dist[source] = 0
        # 记录已处理的节点
        visited = set()

        while len(visited) < n:
            # 选择当前未处理的、距离源点最近的节点
            current_node = None
            min_distance = float('inf')
            for i in range(1, n + 1):
                if i not in visited and dist[i] < min_distance:
                    min_distance = dist[i]
                    current_node = i
            
            # 如果没有可处理的节点（非连通图），提前结束
            if current_node is None:
                break
            
            # 标记当前节点为已处理
            visited.add(current_node)
            
            # 更新相邻节点的距离
            for neighbor, weight in graph[current_node].items():
                new_distance = dist[current_node] + weight
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
        
        return dist

# 使用示例
# 创建一个有向图，使用邻接表表示
graph = {
    1: {2: 2, 3: 4},
    2: {3: 1, 4: 7},
    3: {4: 3},
    4: {}
}
n = 4  # 图中节点数量
source = 1  # 源节点

dist = Solution().dijkstra(graph, n, source)
print("从节点", source, "到其他节点的最短距离：")
for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(f"到节点 {i} 的距离：不可达")
    else:
        print(f"到节点 {i} 的距离：{dist[i]}")
```

### 2.4 Dijkstra 算法复杂度分析

- **时间复杂度**：$O(V^2)$
  - 外层循环需要遍历所有节点，时间复杂度为 $O(V)$
  - 内层循环需要遍历所有未访问的节点来找到距离最小的节点，时间复杂度为 $O(V)$
  - 因此总时间复杂度为 $O(V^2)$

- **空间复杂度**：$O(V)$
  - 需要存储距离数组 `dist`，大小为 $O(V)$
  - 需要存储访问集合 `visited`，大小为 $O(V)$
  - 因此总空间复杂度为 $O(V)$


## 3. 堆优化的 Dijkstra 算法

### 3.1 堆优化的 Dijkstra 算法思想

> **堆优化的 Dijkstra 算法**：通过使用优先队列（堆）来优化选择最小距离节点的过程，从而降低算法的时间复杂度。

在原始的 Dijkstra 算法中，每次都需要遍历所有未访问的节点来找到距离最小的节点，这个过程的时间复杂度是 $O(V)$。通过使用优先队列（堆）来维护当前已知的最短距离，我们可以将这个过程的时间复杂度优化到 $O(\log V)$。

堆优化的主要思想是：
1. 使用优先队列存储当前已知的最短距离
2. 每次从队列中取出距离最小的节点进行处理
3. 当发现更短的路径时，将新的距离加入队列
4. 通过优先队列的特性，保证每次取出的都是当前最小的距离

### 3.2 堆优化的 Dijkstra 算法实现步骤

1. 初始化距离数组，将源节点的距离设为 $0$，其他节点的距离设为无穷大。
2. 创建一个优先队列，将源节点及其距离 $(0, source)$ 加入队列。
3. 当队列不为空时：
   - 取出队列中距离最小的节点
   - 如果该节点的距离大于已知的最短距离，则跳过
   - 否则，遍历该节点的所有相邻节点
   - 如果通过当前节点到达相邻节点的距离更短，则更新距离并将新的距离加入队列
4. 重复步骤 3，直到队列为空
5. 返回所有节点的最短距离

### 3.3 堆优化的 Dijkstra 算法实现代码

```python
import heapq

class Solution:
    def dijkstra(self, graph, n, source):
        # 初始化距离数组
        dist = [float('inf') for _ in range(n + 1)]
        dist[source] = 0
        
        # 创建优先队列，存储 (距离, 节点) 的元组
        priority_queue = [(0, source)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # 如果当前距离大于已知的最短距离，跳过
            if current_distance > dist[current_node]:
                continue
                
            # 遍历当前节点的所有相邻节点
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return dist

# 使用示例
# 创建一个有向图，使用邻接表表示
graph = {
    1: {2: 2, 3: 4},
    2: {3: 1, 4: 7},
    3: {4: 3},
    4: {}
}
n = 4  # 图中节点数量
source = 1  # 源节点

dist = Solution().dijkstra(graph, n, source)
print("从节点", source, "到其他节点的最短距离：")
for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(f"到节点 {i} 的距离：不可达")
    else:
        print(f"到节点 {i} 的距离：{dist[i]}")
```

代码解释：

1. `graph` 是一个字典，表示图的邻接表。例如，`graph[1] = {2: 3, 3: 4}` 表示从节点 1 到节点 2 的边权重为 3，到节点 3 的边权重为 4。
2. `n` 是图中顶点的数量。
3. `source` 是源节点的编号。
4. `dist` 数组存储源点到各个节点的最短距离。
5. `priority_queue` 是一个优先队列，用来选择当前距离源点最近的节点。队列中的元素是 (距离, 节点) 的元组。
6. 主循环中，每次从队列中取出距离最小的节点。如果该节点的距离已经被更新过，跳过。
7. 对于当前节点的每一个邻居，计算通过当前节点到达邻居的距离。如果这个距离比已知的更短，更新距离并将邻居加入队列。
8. 最终，`dist` 数组中存储的就是源点到所有节点的最短距离。

### 3.4 堆优化的 Dijkstra 算法复杂度分析

- **时间复杂度**：$O((V + E) \log V)$
  - 每个节点最多被加入优先队列一次，每次操作的时间复杂度为 $O(\log V)$
  - 每条边最多被处理一次，每次处理的时间复杂度为 $O(\log V)$
  - 因此总时间复杂度为 $O((V + E) \log V)$

- **空间复杂度**：$O(V)$
  - 需要存储距离数组，大小为 $O(V)$。
  - 优先队列在最坏情况下可能存储所有节点，大小为 $O(V)$。
