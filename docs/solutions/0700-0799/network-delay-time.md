# [0743. 网络延迟时间](https://leetcode.cn/problems/network-delay-time/)

- 标签：深度优先搜索、广度优先搜索、图、最短路、堆（优先队列）
- 难度：中等

## 题目链接

- [0743. 网络延迟时间 - 力扣](https://leetcode.cn/problems/network-delay-time/)

## 题目大意

**描述**：

有 $n$ 个节点组成的网络，节点标记为 $1 \sim n$。

给定一个列表 $times[i] = (u_i, v_i, w_i)$，表示信号经过有向边的传递时间，其中 $u_i$ 是源节点，$v_i$ 是目标节点，$w_i$ 是一个信号从源节点传递到目标节点的时间。

给定一个整数 $n$，表示 $n$ 个节点。

给定一个节点 $k$，表示从节点 $k$ 发出一个信号。

**要求**：

需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 $-1$。

**说明**：

- $1 \le k \le n \le 100$。
- $1 \le times.length \le 6000$。
- $times[i].length == 3$。
- $1 \le u_i, v_i \le n$。
- $u_i \ne v_i$。
- $0 \le w_i \le 100$。
- 所有 $(u_i, v_i)$ 对都互不相同（即不含重复边）。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

```python
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
```

- 示例 2：

```python
输入：times = [[1,2,1]], n = 2, k = 1
输出：1
```

## 解题思路

### 思路 1：Bellman Ford 算法

Bellman Ford 算法核心思想：通过「松弛操作」来逐步更新从源节点 $k$ 到所有其他节点的最短距离。

**算法步骤**：

1. **初始化距离数组**：将源节点 $k$ 的距离 $dist[k]$ 设为 $0$，其他节点的距离设为无穷大。

2. **松弛操作**：进行 $n - 1$ 轮松弛，每轮遍历所有边 $(u_i, v_i, w_i)$，如果 $dist[v_i] > dist[u_i] + w_i$，则更新 $dist[v_i] = dist[u_i] + w_i$。

3. **检测负环**（本题不需要）：再次遍历所有边，如果仍然存在 $dist[v_i] > dist[u_i] + w_i$，说明存在负权环。

4. **返回结果**：找出距离数组中的最大值，如果存在无法到达的节点（距离仍为无穷大），则返回 $-1$。

**关键点**：

- 经过 $n - 1$ 轮松弛后，所有可达节点的最短距离已经确定。
- 由于本题没有负权边，不需要检测负环，但保留检测逻辑也无妨。

### 思路 1：代码

```python
from typing import List

class Solution:
    def bellmanFord(self, graph, n, source):
        """Bellman Ford 算法实现
        
        Args:
            graph: 图的邻接表表示，graph[u][v] 表示边 (u, v) 的权重
            n: 节点数量
            source: 源节点
            
        Returns:
            距离数组，dist[i] 表示从源节点到节点 i 的最短距离
        """
        # 初始化距离数组，所有节点距离设为无穷大
        dist = [float('inf') for _ in range(n + 1)]
        # 源节点距离设为 0
        dist[source] = 0

        # 进行 n - 1 轮松弛操作
        for i in range(n - 1):
            # 遍历所有边进行松弛
            for u in graph:
                for v in graph[u]:
                    # 如果可以通过 u 更新 v 的距离，则更新
                    if dist[v] > graph[u][v] + dist[u]:
                        dist[v] = graph[u][v] + dist[u]

        # 检测负权环（本题不需要，但保留检测逻辑）
        for u in graph:
            for v in graph[u]:
                if dist[v] > dist[u] + graph[u][v]:
                    return None

        return dist

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """计算网络延迟时间
        
        Args:
            times: 边列表，每个元素为 (u, v, w)，表示从 u 到 v 的边权重为 w
            n: 节点数量
            k: 源节点
            
        Returns:
            所有节点收到信号的最短时间，如果存在无法到达的节点则返回 -1
        """
        # 构建邻接表
        graph = dict()
        for u, v, w in times:
            if u not in graph:
                graph[u] = dict()
            if v not in graph[u]:
                graph[u][v] = w

        # 使用 Bellman Ford 算法计算最短距离
        dist = self.bellmanFord(graph, n, k)
        
        # 如果返回 None，说明存在负权环（本题不会出现）
        if dist is None:
            return -1

        # 找出最大距离
        ans = 0
        for i in range(1, len(dist)):
            # 如果存在无法到达的节点，返回 -1
            if dist[i] >= float('inf'):
                return -1
            ans = max(ans, dist[i])
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(V \times E)$，其中 $V$ 是节点的数量，$E$ 是边的数量。需要进行 $V - 1$ 轮松弛，每轮遍历所有 $E$ 条边。
- **空间复杂度**：$O(V + E)$，其中 $V$ 是节点的数量，$E$ 是边的数量。需要存储邻接表和距离数组。

### 思路 2：朴素 Dijkstra 算法

朴素 Dijkstra 算法：不使用优先队列，而是每次遍历所有未访问的节点来找到距离最小的节点。虽然时间复杂度较高，但实现更直观。

**算法步骤**：

1. **初始化距离数组**：将源节点 $k$ 的距离 $dist[k]$ 设为 $0$，其他节点的距离设为无穷大。

2. **维护访问数组**：使用 $visited$ 数组记录节点是否已经被访问。

3. **贪心选择**：每次从未访问的节点中找到距离 $dist[u]$ 最小的节点 $u$，标记为已访问。

4. **松弛操作**：更新节点 $u$ 的所有相邻节点 $v$ 的距离，如果 $dist[v] > dist[u] + w(u, v)$，则更新 $dist[v] = dist[u] + w(u, v)$。

5. **重复步骤**：重复步骤 $3 \sim 4$，直到所有节点都被访问。

6. **返回结果**：找出距离数组中的最大值，如果存在无法到达的节点（距离仍为无穷大），则返回 $-1$。

**关键点**：

- Dijkstra 算法适用于非负权图，每次选择距离最小的节点进行松弛。
- 由于题目约束 $0 \le w_i \le 100$，所有边权非负，可以使用 Dijkstra 算法。

### 思路 2：代码

```python
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """计算网络延迟时间（朴素 Dijkstra 算法）
        
        Args:
            times: 边列表，每个元素为 (u, v, w)，表示从 u 到 v 的边权重为 w
            n: 节点数量
            k: 源节点
            
        Returns:
            所有节点收到信号的最短时间，如果存在无法到达的节点则返回 -1
        """
        # 使用哈希表构建邻接表
        graph = dict()
        for u, v, w in times:
            if u not in graph:
                graph[u] = dict()
            graph[u][v] = w
        
        # 初始化距离数组和访问数组
        dist = [float('inf')] * (n + 1)
        dist[k] = 0  # 源节点距离设为 0
        visited = [False] * (n + 1)
        
        # 遍历所有节点，每次选择一个未访问的距离最小的节点
        for _ in range(n):
            # 找到未访问的距离最小的节点
            min_dist = float('inf')
            u = -1
            for i in range(1, n + 1):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i
            
            # 如果没有找到可达的节点，说明存在无法到达的节点
            if u == -1:
                return -1
                
            # 标记当前节点为已访问
            visited[u] = True
            
            # 更新相邻节点的距离
            if u in graph:
                for v, w in graph[u].items():
                    # 如果通过 u 到达 v 的距离更短，则更新
                    if not visited[v] and dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
        
        # 找出最大距离
        return max(dist[1:])
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(V^2 + E)$，其中 $V$ 是节点的数量，$E$ 是边的数量。每次需要遍历所有节点找到最小距离节点，总共需要 $V$ 次，每次遍历需要 $O(V)$ 的时间。更新边的操作需要 $O(E)$ 的时间。
- **空间复杂度**：$O(V + E)$，其中 $V$ 是节点的数量，$E$ 是边的数量。需要存储邻接表、距离数组和访问数组。

### 思路 3：Dijkstra 算法（堆优化）

Dijkstra 算法是解决单源最短路径问题的经典算法。在这个问题中，我们可以使用 Dijkstra 算法来找到从节点 $k$ 到所有其他节点的最短路径。

堆优化版本的 Dijkstra 算法：使用优先队列（最小堆）来维护待处理的节点，避免每次遍历所有节点查找最小距离节点，从而降低时间复杂度。

**算法步骤**：

1. **构建邻接表**：使用邻接表存储图结构，方便遍历相邻节点。

2. **初始化距离数组**：将源节点 $k$ 的距离 $dist[k]$ 设为 $0$，其他节点的距离设为无穷大。

3. **初始化优先队列**：将源节点 $k$ 及其距离 $0$ 加入优先队列。

4. **贪心选择**：每次从优先队列中取出距离 $dist[u]$ 最小的节点 $u$。

5. **跳过无效节点**：如果当前距离大于已知最短距离，说明该节点已被更优路径访问过，跳过。

6. **松弛操作**：更新节点 $u$ 的所有相邻节点 $v$ 的距离，如果 $dist[v] > dist[u] + w(u, v)$，则更新 $dist[v] = dist[u] + w(u, v)$ 并将 $(dist[v], v)$ 加入优先队列。

7. **重复步骤**：重复步骤 $4 \sim 6$，直到优先队列为空。

8. **返回结果**：找出距离数组中的最大值，如果存在无法到达的节点（距离仍为无穷大），则返回 $-1$。

**关键点**：

- 使用优先队列可以将查找最小距离节点的时间复杂度从 $O(V)$ 降低到 $O(\log V)$。
- 同一个节点可能被多次加入优先队列，但只有距离更小的才会被处理。


### 思路 3：代码

```python
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """计算网络延迟时间（Dijkstra 算法堆优化版本）
        
        Args:
            times: 边列表，每个元素为 (u, v, w)，表示从 u 到 v 的边权重为 w
            n: 节点数量
            k: 源节点
            
        Returns:
            所有节点收到信号的最短时间，如果存在无法到达的节点则返回 -1
        """
        # 构建邻接表
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 初始化距离数组，所有节点距离设为无穷大
        dist = [float('inf')] * (n + 1)
        dist[k] = 0  # 源节点距离设为 0
        
        # 使用优先队列（最小堆）存储待处理的节点，格式为 (距离, 节点编号)
        pq = [(0, k)]
        
        while pq:
            # 取出距离最小的节点
            d, u = heapq.heappop(pq)
            # 如果当前距离大于已知最短距离，说明该节点已被更优路径访问过，跳过
            if d > dist[u]:
                continue
                
            # 遍历相邻节点
            for v, w in graph[u]:
                # 如果通过 u 到达 v 的距离更短，则更新
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    # 将更新后的节点加入优先队列
                    heapq.heappush(pq, (dist[v], v))
        
        # 找出最大距离
        max_dist = max(dist[1:])
        # 如果存在无法到达的节点，返回 -1
        return max_dist if max_dist != float('inf') else -1
```

### 思路 3：复杂度分析

- **时间复杂度**：$O(E \log V)$，其中 $E$ 是边的数量，$V$ 是节点的数量。每次从优先队列中取出一个节点需要 $O(\log V)$ 的时间，总共需要处理 $E$ 条边。
- **空间复杂度**：$O(V + E)$，其中 $V$ 是节点的数量，$E$ 是边的数量。需要存储邻接表和优先队列。

### 思路 4：SPFA 算法

SPFA（Shortest Path Faster Algorithm）：Bellman-Ford 算法的一个优化版本。它使用队列来维护待更新的节点，只有当节点的距离被更新时，才将其加入队列，从而避免不必要的松弛操作。

**算法步骤**：

1. **初始化距离数组**：将源节点 $k$ 的距离 $dist[k]$ 设为 $0$，其他节点的距离设为无穷大。

2. **初始化队列**：将源节点 $k$ 加入队列，并使用 $in\_queue$ 数组标记节点是否在队列中。

3. **队列处理**：从队列中取出一个节点 $u$，标记其不在队列中。

4. **松弛操作**：遍历节点 $u$ 的所有相邻节点 $v$：
   - 如果 $dist[v] > dist[u] + w(u, v)$，则更新 $dist[v] = dist[u] + w(u, v)$。
   - 如果节点 $v$ 不在队列中，则将其加入队列并标记。

5. **重复步骤**：重复步骤 $3 \sim 4$，直到队列为空。

6. **返回结果**：找出距离数组中的最大值，如果存在无法到达的节点（距离仍为无穷大），则返回 $-1$。

**关键点**：

- SPFA 算法只对距离发生变化的节点进行松弛，避免了对所有边的重复检查。
- 在非负权图中，SPFA 算法的性能通常优于 Bellman-Ford 算法。
- 由于题目约束 $0 \le w_i \le 100$，所有边权非负，不会出现负权环，SPFA 算法可以正常使用。

### 思路 4：代码

```python
from typing import List
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """计算网络延迟时间（SPFA 算法）
        
        Args:
            times: 边列表，每个元素为 (u, v, w)，表示从 u 到 v 的边权重为 w
            n: 节点数量
            k: 源节点
            
        Returns:
            所有节点收到信号的最短时间，如果存在无法到达的节点则返回 -1
        """
        # 使用哈希表构建邻接表
        graph = dict()
        for u, v, w in times:
            if u not in graph:
                graph[u] = dict()
            graph[u][v] = w
        
        # 初始化距离数组，所有节点距离设为无穷大
        dist = [float('inf')] * (n + 1)
        dist[k] = 0  # 源节点距离设为 0
        
        # 使用队列存储待更新的节点
        queue = deque([k])
        # 记录节点是否在队列中，避免重复入队
        in_queue = [False] * (n + 1)
        in_queue[k] = True
        
        while queue:
            # 取出队头节点
            u = queue.popleft()
            in_queue[u] = False
            
            # 遍历相邻节点
            if u in graph:
                for v, w in graph[u].items():
                    # 如果通过 u 到达 v 的距离更短，则更新
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        # 如果节点不在队列中，则加入队列
                        if not in_queue[v]:
                            queue.append(v)
                            in_queue[v] = True
        
        # 找出最大距离
        max_dist = max(dist[1:])
        # 如果存在无法到达的节点，返回 -1
        return max_dist if max_dist != float('inf') else -1
```

### 思路 4：复杂度分析

- **时间复杂度**：平均情况下为 $O(kE)$，其中 $E$ 是边的数量，$k$ 是每个节点入队的平均次数。在最坏情况下可能退化为 $O(VE)$。
- **空间复杂度**：$O(V + E)$，其中 $V$ 是节点的数量，$E$ 是边的数量。需要存储邻接表、距离数组和队列。