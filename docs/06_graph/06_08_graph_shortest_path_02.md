## 1. Bellman-Ford 算法

### 1.1 Bellman-Ford 算法的算法思想

> **Bellman-Ford 算法**：一种用于计算单源最短路径的算法，可以处理图中存在负权边的情况，并且能够检测负权环。

Bellman-Ford 算法的核心思想是：
1. 对图中的所有边进行 $V-1$ 次松弛操作，其中 $V$ 是图中顶点的数量
2. 每次松弛操作都会尝试通过当前边来缩短源点到目标顶点的距离
3. 如果在 $V-1$ 次松弛后还能继续松弛，说明图中存在负权环
4. 算法可以处理负权边，但不能处理负权环

### 1.2 Bellman-Ford 算法的实现步骤

1. 初始化距离数组，将源节点的距离设为 $0$，其他节点的距离设为无穷大
2. 进行 $V-1$ 次迭代，每次迭代：
   - 遍历图中的所有边
   - 对每条边进行松弛操作：如果通过当前边可以缩短源点到目标顶点的距离，则更新距离
3. 进行第 $V$ 次迭代，检查是否还能继续松弛：
   - 如果还能松弛，说明图中存在负权环
   - 如果不能松弛，说明已经找到最短路径
4. 返回最短路径距离数组

### 1.3 Bellman-Ford 算法的实现代码

```python
class Solution:
    def bellmanFord(self, graph, n, source):
        # 初始化距离数组
        dist = [float('inf') for _ in range(n + 1)]
        dist[source] = 0

        # 进行 V-1 次迭代
        for i in range(n - 1):
            # 遍历所有边
            for vi in graph:
                for vj in graph[vi]:
                    # 松弛操作
                    if dist[vj] > graph[vi][vj] + dist[vi]:
                        dist[vj] = graph[vi][vj] + dist[vi]

        # 检查是否存在负权环
        for vi in graph:
            for vj in graph[vi]:
                if dist[vj] > dist[vi] + graph[vi][vj]:
                    return None  # 存在负权环

        return dist
```

代码解释：

1. `graph` 是一个字典，表示图的邻接表。例如，`graph[1] = {2: 3, 3: 4}` 表示从节点 1 到节点 2 的边权重为 3，到节点 3 的边权重为 4。
2. `n` 是图中顶点的数量。
3. `source` 是源节点的编号。
4. `dist` 数组存储源点到各个节点的最短距离。
5. 外层循环进行 $V-1$ 次迭代，确保所有可能的最短路径都被找到。
6. 内层循环遍历所有边，进行松弛操作。
7. 最后检查是否存在负权环，如果存在则返回 None。

### 1.4 Bellman-Ford 算法复杂度分析

- **时间复杂度**：$O(VE)$
  - 需要进行 $V-1$ 次迭代
  - 每次迭代需要遍历所有边 $E$
  - 因此总时间复杂度为 $O(VE)$

- **空间复杂度**：$O(V)$
  - 需要存储距离数组，大小为 $O(V)$
  - 不需要额外的空间来存储图的结构，因为使用邻接表表示


## 2. SPFA 算法

### 2.1 SPFA 算法的算法思想

> **SPFA 算法（Shortest Path Faster Algorithm）**：是 Bellman-Ford 算法的一种队列优化版本，通过使用队列来维护待更新的节点，从而减少不必要的松弛操作。

SPFA 算法的核心思想是：
1. 使用队列来维护待更新的节点，而不是像 Bellman-Ford 算法那样遍历所有边
2. 只有当某个节点的距离被更新时，才将其加入队列
3. 通过这种方式，避免了大量不必要的松弛操作，提高了算法的效率
4. 算法可以处理负权边，并且能够检测负权环

### 2.2 SPFA 算法的实现步骤

1. 初始化距离数组，将源节点的距离设为 $0$，其他节点的距离设为无穷大
2. 创建一个队列，将源节点加入队列
3. 当队列不为空时：
   - 取出队首节点
   - 遍历该节点的所有相邻节点
   - 如果通过当前节点可以缩短到相邻节点的距离，则更新距离
   - 如果相邻节点不在队列中，则将其加入队列
4. 重复步骤 3，直到队列为空
5. 返回最短路径距离数组

### 2.3 SPFA 算法的实现代码

```python
from collections import deque

def spfa(graph, n, source):
    # 初始化距离数组
    dist = [float('inf') for _ in range(n + 1)]
    dist[source] = 0
    
    # 初始化队列和访问数组
    queue = deque([source])
    in_queue = [False] * (n + 1)
    in_queue[source] = True
    
    # 记录每个节点入队次数，用于检测负环
    count = [0] * (n + 1)
    
    while queue:
        # 取出队首节点
        current = queue.popleft()
        in_queue[current] = False
        
        # 遍历当前节点的所有相邻节点
        for neighbor, weight in graph[current].items():
            # 如果通过当前节点可以缩短距离
            if dist[neighbor] > dist[current] + weight:
                dist[neighbor] = dist[current] + weight
                count[neighbor] += 1
                
                # 如果节点入队次数超过 n-1 次，说明存在负环
                if count[neighbor] >= n:
                    return None
                
                # 如果相邻节点不在队列中，将其加入队列
                if not in_queue[neighbor]:
                    queue.append(neighbor)
                    in_queue[neighbor] = True
    
    return dist
```

代码解释：

1. `graph` 是一个字典，表示图的邻接表。例如，`graph[1] = {2: 3, 3: 4}` 表示从节点 1 到节点 2 的边权重为 3，到节点 3 的边权重为 4。
2. `n` 是图中顶点的数量。
3. `source` 是源节点的编号。
4. `dist` 数组存储源点到各个节点的最短距离。
5. `queue` 是一个双端队列，用于维护待更新的节点。
6. `in_queue` 数组用于记录节点是否在队列中，避免重复入队。
7. `count` 数组用于记录每个节点的入队次数，用于检测负环。
8. 主循环中，每次从队列中取出一个节点，遍历其所有相邻节点，如果发现更短的路径则更新距离并将相邻节点加入队列。
9. 如果某个节点的入队次数超过 $n-1$ 次，说明图中存在负环，返回 None。

### 2.4 SPFA 算法复杂度分析

- **时间复杂度**：
  - 平均情况下：$O(kE)$，其中 $k$ 是每个节点的平均入队次数
  - 最坏情况下：$O(VE)$，与 Bellman-Ford 算法相同
  - 实际运行中，SPFA 算法通常比 Bellman-Ford 算法快很多

- **空间复杂度**：$O(V)$
  - 需要存储距离数组，大小为 $O(V)$
  - 需要存储队列和访问数组，大小为 $O(V)$
  - 因此总空间复杂度为 $O(V)$

## 练习题目

- [单源最短路径题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E5%8D%95%E6%BA%90%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84%E9%A2%98%E7%9B%AE)