## 1. 二分图最大匹配简介

> **二分图最大匹配（Maximum Bipartite Matching）**：图论中的一个基础且重要的问题。其目标是在一个二分图中，找到一组两两不相交的边，使得被匹配的点对数量最大。

- **匹配**：在二分图中，选择若干条边，使得这些边之间没有公共端点（即每个点最多只参与一条匹配边）。
- **最大匹配**：在所有可能的匹配中，选出包含边数最多的那一组，即让尽可能多的点被配对。

二分图最大匹配问题有多种经典算法，常用的有以下三类：

**1. 匈牙利算法（Hungarian Algorithm，DFS 增广路）**：

通过不断为未匹配的左侧点寻找「增广路」来扩展匹配的经典方法。它通常采用深度优先搜索（DFS）递归实现，代码简洁，易于理解，适合小中规模的数据场景。其时间复杂度为 $O(VE)$，实现简单，适合竞赛和工程快速上手，但在大规模稠密图下效率有限。

**2. Hopcroft-Karp 算法**：

通过分层 BFS 批量寻找多条增广路，每轮可以一次性扩展多组匹配，从而大幅提升效率。该算法先用 BFS 对图进行分层，再用 DFS 在分层图中寻找增广路，适合处理大规模稠密二分图。其时间复杂度为 $O(\sqrt{V}E)$，效率高，但实现相对匈牙利算法更为复杂。

**3. 网络流算法（最大流建模）**：

将二分图最大匹配问题转化为最大流问题：左侧点连接源点，右侧点连接汇点，边容量为 1，最大流即为最大匹配。常用的最大流算法有 Ford-Fulkerson、Edmonds-Karp、Dinic、ISAP 等。其时间复杂度依赖具体算法，Dinic 算法常见为 $O(\min(V^{2/3}, E^{1/2}) \cdot E)$。该方法可扩展到带权匹配、带容量等复杂约束，适合工程和综合性问题，但实现和调试相对繁琐。

## 2. 匈牙利算法

### 2.1 增广路介绍

在介绍匈牙利算法之前，先理解「增广路」的概念：

> **增广路（Augmenting Path）**：在当前的匹配状态下，从某个尚未匹配的左侧点出发，沿着图中的边依次前进，最终到达一个同样未被匹配的右侧点。要求这条路径上的边类型要交替出现：先走一条未被匹配的边，再走一条已被匹配的边，如此反复，直到终点。只要存在这样的路径，我们就可以把路径上边的匹配状态「翻转」——原本未匹配的边变为匹配，原本已匹配的边变为未匹配，从而让整体匹配数增加 $1$。

增广路的本质是「为未匹配的点找到一条可以扩展匹配的通路」。匈牙利算法正是不断寻找增广路，并沿着增广路调整匹配关系，从而逐步扩大整体匹配规模。

下面详细介绍匈牙利算法的基本思想。

### 2.2 匈牙利算法的基本思想

> **匈牙利算法的基本思想**：
> 
> 不断为左侧集合中尚未匹配的点寻找一条「增广路」，即从该点出发，通过深度优先搜索（DFS）探索一条起点和终点均为未匹配点、且匹配边与非匹配边交替出现的路径。如果找到这样的路径，就沿路径翻转匹配关系，使整体匹配数增加 1。重复这一过程，直到所有未匹配点都无法再找到增广路为止，最终得到最大匹配。

### 2.3 匈牙利算法的具体步骤

匈牙利算法的核心流程可以分为以下几个步骤：

1. **初始化匹配关系**：一开始，右侧所有点都没有被匹配（比如用 `match_right = [-1] * right_size` 表示，-1 代表未匹配）。
2. **依次为每个左侧点找对象**：遍历左侧集合的每个点 $u$，尝试为它找到一条「增广路」来配对。
3. **用 DFS 寻找增广路**：
   - 对当前左侧点 $u$，依次考察它能连到的每个右侧点 $v$：
     - 如果 $v$ 这轮还没被访问过，先标记已访问，避免重复。
     - 如果 $v$ 还没有配对，或者 $v$ 已配对的左侧点 $u'$ 能继续递归找到新的增广路，那么就让 $u$ 和 $v$ 配对（即 `match_right[v] = u`），并返回成功。
   - 如果所有邻接的右侧点都无法配对，则返回失败。
4. **重复上述过程**：
   - 每当成功为一个左侧点找到增广路并配对，整体匹配数加 1。
   - 继续尝试下一个左侧点，直到所有左侧点都无法再增广为止。
5. **输出最大匹配数**：最后统计一共配对了多少组，这个数就是二分图的最大匹配数。

### 2.4 匈牙利算法的代码实现

```python
def max_bipartite_matching(graph, left_size, right_size):
    """
    二分图最大匹配（匈牙利算法，DFS 增广路实现）
    :param graph: 邻接表，graph[u] 存储左侧点 u 能连接到的所有右侧点编号（如 [[], [0,2], ...]）
    :param left_size: 左侧点个数
    :param right_size: 右侧点个数
    :return: 最大匹配数
    """
    match_right = [-1] * right_size  # 记录每个右侧点当前匹配到的左侧点编号，-1 表示未匹配
    result = 0  # 匹配数

    for left in range(left_size):
        visited = [False] * right_size  # 每次为一个左侧点增广时，重置右侧点访问标记
        if find_augmenting_path(graph, left, visited, match_right):
            result += 1  # 成功增广，匹配数加一

    return result

def find_augmenting_path(graph, left, visited, match_right):
    """
    尝试为左侧点 left 寻找一条增广路
    :param graph: 邻接表
    :param left: 当前尝试增广的左侧点编号
    :param visited: 右侧点访问标记，防止重复访问
    :param match_right: 右侧点的匹配关系
    :return: 是否找到增广路
    """
    for right in graph[left]:  # 遍历 left 能连接到的所有右侧点
        if not visited[right]:  # 只尝试未访问过的右侧点
            visited[right] = True  # 标记已访问
            # 如果右侧点未匹配，或其当前匹配的左侧点还能找到新的增广路
            if match_right[right] == -1 or find_augmenting_path(graph, match_right[right], visited, match_right):
                match_right[right] = left  # 配对成功，更新匹配关系
                return True
    return False  # 没有找到增广路
```

### 2.5 匈牙利算法的算法分析

- **时间复杂度**：O(VE)，其中 V 表示顶点数，E 表示边数。每次尝试增广时，最坏情况下需要遍历所有边，整体复杂度为 O(VE)。
- **空间复杂度**：
  - 如果使用邻接矩阵存储图，空间复杂度为 O(V²)。
  - 如果使用邻接表存储图，空间复杂度为 O(V + E)。

## 3. Hopcroft-Karp 算法

### 3.1 Hopcroft-Karp 算法的基本思想

> **Hopcroft-Karp 算法的基本思想**：
> 
> 每轮通过 BFS 对图进行分层，快速找到所有最短的不相交增广路，然后用 DFS 同时增广多条路径，从而大幅提升匹配效率。与传统的匈牙利算法每次只增广一条路径不同，Hopcroft-Karp 算法每轮能批量增广多条路径，极大减少了总的增广次数，因此在大规模二分图上表现尤为优越。

### 3.2 Hopcroft-Karp 算法的具体步骤

#### Hopcroft-Karp 算法的具体步骤

Hopcroft-Karp 算法高效求解二分图最大匹配，其核心思想是 **分层批量增广**，每轮同时增广多条最短增广路，极大提升效率。具体流程如下：

1. **初始化匹配关系**：所有点一开始都没有匹配对象。
2. **分层（BFS）**：  
   - 首先，对所有未匹配的左侧点进行广度优先搜索（BFS），给每个左侧点分配一个「层号」。
   - 在搜索过程中，只能沿着「未匹配的边 → 已匹配的边」交替前进，这样就能构建出分层图。
   - 如果在 BFS 过程中遇到未匹配的右侧点，说明找到了增广路，并记录下最短的增广路长度。
3. **批量增广（DFS）**： 
   - 接下来，对所有未匹配的左侧点，按照分层图，用深度优先搜索（DFS）去找增广路。
   - 只在层号递增的方向递归查找，找到一条增广路就立即进行匹配。
   - 这样每一轮可以同时增广多条互不重叠的最短增广路，大大提高效率。
4. **重复迭代**：
   - 如果本轮找到了增广路，就更新匹配关系，然后回到第 $2$ 步，继续分层和增广。
   - 如果本轮没有找到任何增广路，算法结束，此时的匹配就是最大匹配。

### 3.3 Hopcroft-Karp 算法的代码实现

```python
from collections import deque

def hopcroft_karp(graph, left_size, right_size):
    """
    Hopcroft-Karp 算法求二分图最大匹配
    :param graph: List[List[int]]，graph[i] 存储左侧点 i 能连到的所有右侧点编号
    :param left_size: 左侧点数量
    :param right_size: 右侧点数量
    :return: 最大匹配数
    """
    # match_left[i] = j 表示左侧点 i 匹配到右侧点 j，未匹配为 -1
    match_left = [-1] * left_size
    # match_right[j] = i 表示右侧点 j 匹配到左侧点 i，未匹配为 -1
    match_right = [-1] * right_size
    result = 0  # 匹配数

    while True:
        # 1. BFS 分层，dist[i] 表示左侧点 i 到未匹配状态的最短距离
        dist = [-1] * left_size
        queue = deque()
        for i in range(left_size):
            if match_left[i] == -1:
                dist[i] = 0
                queue.append(i)
        # 标记本轮是否存在增广路
        found_augmenting = False

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if match_right[v] == -1:
                    # 右侧点 v 未匹配，说明存在增广路
                    found_augmenting = True
                elif dist[match_right[v]] == -1:
                    # 沿着匹配边走，分层
                    dist[match_right[v]] = dist[u] + 1
                    queue.append(match_right[v])

        if not found_augmenting:
            # 没有增广路，算法结束
            break

        # 2. DFS 尝试批量增广
        def dfs(u):
            for v in graph[u]:
                # 如果右侧点未匹配，或者可以沿着分层图递归找到增广路
                if match_right[v] == -1 or (dist[match_right[v]] == dist[u] + 1 and dfs(match_right[v])):
                    match_left[u] = v
                    match_right[v] = u
                    return True
            # 没有找到增广路
            return False

        # 3. 对所有未匹配的左侧点尝试增广
        for i in range(left_size):
            if match_left[i] == -1:
                if dfs(i):
                    result += 1

    return result
```

### 3.4 Hopcroft-Karp 算法的算法分析

- **时间复杂度**：$O(\sqrt{V}E)$，其中 $V$ 为顶点数，$E$ 为边数。相比传统匈牙利算法，Hopcroft-Karp 算法通过分层批量增广，大幅减少了增广路的查找次数，提升了整体效率。
- **空间复杂度**：$O(V + E)$，主要用于存储邻接表、匹配关系和辅助队列等数据结构。

### 3.5 Hopcroft-Karp 算法优化

1. **双向 BFS**：从左右两侧同时进行 BFS，进一步缩小搜索范围，加快分层过程。
2. **动态分层策略**：根据当前的匹配情况灵活调整分层方式，提高增广路查找效率。
3. **贪心预处理**：在正式执行算法前，先用贪心策略进行初步匹配，为后续批量增广打下基础。
4. **并行与分布式优化**：利用多线程或分布式计算资源，实现 BFS/DFS 的并行处理，提升整体运行速度。

## 4. 网络流算法

### 4.1 网络流算法的基本思想

二分图最大匹配问题可以巧妙地转化为网络流中的最大流问题来求解。其核心思想如下：

- **建模方式**：将二分图的左侧点、右侧点分别作为网络中的两类节点，额外引入一个「源点」和一个「汇点」。
    - 源点 $S$ 向所有左侧点连一条容量为 $1$ 的有向边。
    - 所有右侧点向汇点 $T$ 连一条容量为 $1$ 的有向边。
    - 原二分图中每条左侧点 $u$ 到右侧点 $v$ 的边，建一条 $u \to v$ 的有向边，容量为 $1$。
- **流量含义**：每条边的容量为 $1$，表示每个点最多只能参与一次匹配。网络中从 $S$ 到 $T$ 的最大流量，恰好等于二分图的最大匹配数。
- **求解过程**：使用最大流算法（如 Ford-Fulkerson、Edmonds-Karp、Dinic 等）在该网络上求 $S$ 到 $T$ 的最大流，流量的大小即为最大匹配数。


> **网络流算法的直观理解**：
>
> 每当在网络中找到一条从 $S$ 到 $T$ 的增广路径，就等价于在原二分图中新增一对匹配。由于每个点与源点或汇点之间的边容量均为 $1$，确保每个点最多只参与一次匹配，严格满足二分图匹配的要求。


### 4.2 网络流算法的具体步骤

### 4.2 网络流算法的具体步骤

将二分图最大匹配问题转化为最大流问题，通常分为以下几个步骤：

1. **引入源点与汇点**：新增源点 $S$ 和汇点 $T$。
2. **源点连向左侧所有点**：从 $S$ 向每个左侧点各连一条容量为 $1$ 的有向边，表示每个左侧点最多参与一次匹配。
3. **右侧所有点连向汇点**：从每个右侧点向 $T$ 各连一条容量为 $1$ 的有向边，表示每个右侧点最多参与一次匹配。
4. **原二分图边建模**：对于原图中每条左侧点 $u$ 到右侧点 $v$ 的边，添加 $u \to v$ 的有向边，容量为 $1$。
5. **执行最大流算法**：在该网络上运行最大流算法（如 Edmonds-Karp、Dinic 等），计算 $S$ 到 $T$ 的最大流量。
6. **得到最大匹配数**：最大流的数值即为原二分图的最大匹配数。

### 4.3 网络流算法的代码实现

```python
from collections import defaultdict, deque

def max_flow_bipartite_matching(graph, left_size, right_size):
    """
    使用网络流（Ford-Fulkerson 算法）求解二分图最大匹配
    :param graph: List[List[int]]，左侧每个点可连的右侧点编号列表
    :param left_size: 左侧点个数
    :param right_size: 右侧点个数
    :return: 最大匹配数
    """
    # 构建网络流图，节点编号：
    # 0 ~ left_size-1：左侧点
    # left_size ~ left_size+right_size-1：右侧点
    # source: left_size+right_size
    # sink: left_size+right_size+1
    flow_graph = defaultdict(dict)
    source = left_size + right_size
    sink = source + 1

    # 源点到左侧点，容量为 1
    for i in range(left_size):
        flow_graph[source][i] = 1
        flow_graph[i][source] = 0  # 反向边，初始为 0

    # 右侧点到汇点，容量为 1
    for i in range(right_size):
        right_node = left_size + i
        flow_graph[right_node][sink] = 1
        flow_graph[sink][right_node] = 0  # 反向边

    # 左侧点到右侧点，容量为 1
    for i in range(left_size):
        for j in graph[i]:
            right_node = left_size + j
            flow_graph[i][right_node] = 1
            flow_graph[right_node][i] = 0  # 反向边

    def bfs():
        """
        BFS 寻找一条增广路，返回每个节点的父节点
        """
        parent = [-1] * (sink + 1)
        queue = deque([source])
        parent[source] = -2  # 源点特殊标记

        while queue:
            u = queue.popleft()
            for v, capacity in flow_graph[u].items():
                # 只走有剩余容量且未访问过的点
                if parent[v] == -1 and capacity > 0:
                    parent[v] = u
                    if v == sink:
                        return parent  # 找到汇点，返回路径
                    queue.append(v)
        return None  # 未找到增广路

    def ford_fulkerson():
        """
        主流程：不断寻找增广路并更新残量网络
        """
        max_flow = 0
        while True:
            parent = bfs()
            if not parent:
                break  # 没有增广路，算法结束

            # 计算本次增广路的最小残量（本题均为 1，写全以便扩展）
            v = sink
            min_capacity = float('inf')
            while v != source:
                u = parent[v]
                min_capacity = min(min_capacity, flow_graph[u][v])
                v = u

            # 沿增广路更新正反向边的容量
            v = sink
            while v != source:
                u = parent[v]
                flow_graph[u][v] -= min_capacity
                flow_graph[v][u] += min_capacity
                v = u

            max_flow += min_capacity  # 累加总流量

        return max_flow

    return ford_fulkerson()
```

### 4.4 网络流算法的算法分析

- **时间复杂度分析**：
  1. **Ford-Fulkerson 算法**：$O(VE^2)$。该算法每次通过 DFS/BFS 寻找一条增广路，每次最多增加 1 单位流量，最坏情况下需要 $O(E)$ 次增广，每次增广遍历 $O(E)$ 条边，总共 $O(VE^2)$。适合边权为 1 或较小的稀疏图，实际中常用于教学和小规模数据。
  2. **Dinic 算法**：$O(V^2E)$。Dinic 算法通过分层网络和多路增广优化了增广过程，理论上在一般网络流问题中表现优秀，尤其适合稠密图。对于二分图最大匹配，Dinic 的实际复杂度可降为 $O(\sqrt{V}E)$，但一般网络流场景下为 $O(V^2E)$。
  3. **ISAP 算法**：$O(V^2E)$。ISAP（Improved Shortest Augmenting Path）算法通过维护距离标号和当前弧优化增广过程，适合大规模稠密图，实际表现优于 Dinic，但理论复杂度同为 $O(V^2E)$。

- **空间复杂度**：$O(V + E)$。主要用于存储残量网络（邻接表/矩阵）和辅助数组（如层次、前驱、队列等），与图的规模线性相关。



## 练习题目

- [LCP 04. 覆盖](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/LCP/broken-board-dominoes.md)	
- [1947. 最大兼容性评分和](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1900-1999/maximum-compatibility-score-sum.md)	
- [1595. 连通两组点的最小成本](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1500-1599/minimum-cost-to-connect-two-groups-of-points.md)	

- [二分图最大匹配题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E4%BA%8C%E5%88%86%E5%9B%BE%E6%9C%80%E5%A4%A7%E5%8C%B9%E9%85%8D%E9%A2%98%E7%9B%AE)