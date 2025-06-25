## 1. 二分图最大匹配简介

> **二分图最大匹配（Maximum Bipartite Matching）**：图论中的一个重要问题。在二分图中，我们需要找到最大的匹配数，即最多可以有多少对顶点之间形成匹配。

- **二分图**：图中的顶点可以被分成两个独立的集合，使得每条边的两个端点分别属于这两个集合。
- **匹配**：一组边的集合，其中任意两条边都没有共同的顶点。
- **最大匹配**：包含边数最多的匹配。

### 1.1 应用场景

二分图最大匹配在实际应用中有广泛的应用：

1. **任务分配**：将任务分配给工人，每个工人只能完成一个任务
2. **婚姻匹配**：将男生和女生进行配对
3. **网络流问题**：可以转化为最大流问题求解
4. **资源分配**：将资源分配给需求方
5. **学生选课**：将学生与课程进行匹配
6. **网络路由**：将数据包与可用路径进行匹配

### 1.2 优化方法

1. **使用邻接表**：对于稀疏图，使用邻接表可以显著减少空间复杂度
2. **双向搜索**：同时从左右两侧进行搜索，可以减少搜索次数
3. **预处理**：对图进行预处理，去除不可能形成匹配的边
4. **贪心匹配**：先进行贪心匹配，减少后续搜索的复杂度
5. **并行处理**：对于大规模图，可以使用并行算法提高效率

## 2. 匈牙利算法

### 2.1 匈牙利算法基本思想

匈牙利算法（Hungarian Algorithm）是求解二分图最大匹配的经典算法。其基本思想是：

1. 从左侧集合中任选一个未匹配的点开始
2. 尝试寻找增广路径
3. 如果找到增广路径，则更新匹配
4. 重复以上步骤直到无法找到增广路径

### 2.2 匈牙利算法实现代码

```python
def max_bipartite_matching(graph, left_size, right_size):
    # 初始化匹配数组
    match_right = [-1] * right_size
    result = 0
    
    # 对左侧每个顶点尝试匹配
    for left in range(left_size):
        # 记录右侧顶点是否被访问过
        visited = [False] * right_size
        
        # 如果找到增广路径，则匹配数加1
        if find_augmenting_path(graph, left, visited, match_right):
            result += 1
            
    return result

def find_augmenting_path(graph, left, visited, match_right):
    # 遍历右侧所有顶点
    for right in range(len(graph[left])):
        # 如果存在边且右侧顶点未被访问
        if graph[left][right] and not visited[right]:
            visited[right] = True
            
            # 如果右侧顶点未匹配，或者可以找到新的匹配
            if match_right[right] == -1 or find_augmenting_path(graph, match_right[right], visited, match_right):
                match_right[right] = left
                return True
                
    return False
```

### 2.3 匈牙利算法时间复杂度

- 匈牙利算法的时间复杂度为 O(VE)，其中 V 是顶点数，E 是边数
- 使用邻接矩阵存储图时，空间复杂度为 O(V²)
- 使用邻接表存储图时，空间复杂度为 O(V + E)


## 3. Hopcroft-Karp 算法

### 3.1 Hopcroft-Karp 算法基本思想

Hopcroft-Karp 算法是求解二分图最大匹配的一个更高效的算法，时间复杂度为 O(√VE)。其基本思想是：

1. 同时寻找多条不相交的增广路径
2. 使用 BFS 分层，然后使用 DFS 寻找增广路径
3. 每次迭代可以找到多条增广路径


### 3.2 Hopcroft-Karp 算法实现代码

```python
from collections import deque

def hopcroft_karp(graph, left_size, right_size):
    # 初始化匹配数组
    match_left = [-1] * left_size
    match_right = [-1] * right_size
    result = 0
    
    while True:
        # 使用 BFS 寻找增广路径
        dist = [-1] * left_size
        queue = deque()
        
        # 将未匹配的左侧顶点加入队列
        for i in range(left_size):
            if match_left[i] == -1:
                dist[i] = 0
                queue.append(i)
        
        # BFS 分层
        while queue:
            left = queue.popleft()
            for right in graph[left]:
                if match_right[right] == -1:
                    # 找到增广路径
                    break
                if dist[match_right[right]] == -1:
                    dist[match_right[right]] = dist[left] + 1
                    queue.append(match_right[right])
        
        # 使用 DFS 寻找增广路径
        def dfs(left):
            for right in graph[left]:
                if match_right[right] == -1 or \
                   (dist[match_right[right]] == dist[left] + 1 and \
                    dfs(match_right[right])):
                    match_left[left] = right
                    match_right[right] = left
                    return True
            return False
        
        # 尝试为每个未匹配的左侧顶点寻找增广路径
        found = False
        for i in range(left_size):
            if match_left[i] == -1 and dfs(i):
                found = True
                result += 1
        
        if not found:
            break
    
    return result
```

### 3.3 Hopcroft-Karp 算法复杂度

- **时间复杂度**：O(√VE)，其中 V 是顶点数，E 是边数
- **空间复杂度**：O(V + E)
- **优点**：
  1. 比匈牙利算法更高效
  2. 适合处理大规模图
  3. 可以并行化实现
- **缺点**：
  1. 实现相对复杂
  2. 常数因子较大
  3. 对于小规模图可能不如匈牙利算法

### 3.4 Hopcroft-Karp 算法优化

1. **双向 BFS**：同时从左右两侧进行 BFS，减少搜索空间
2. **动态分层**：根据当前匹配状态动态调整分层策略
3. **预处理**：使用贪心算法进行初始匹配
4. **并行化**：利用多线程或分布式计算提高效率

## 4. 网络流算法

### 4.1 网络流算法实现步骤

二分图最大匹配问题可以转化为最大流问题来求解。具体步骤如下：

1. 添加源点和汇点
2. 将二分图转化为网络流图
3. 使用最大流算法求解

### 4.2 网络流算法实现代码

```python
from collections import defaultdict

def max_flow_bipartite_matching(graph, left_size, right_size):
    # 构建网络流图
    flow_graph = defaultdict(dict)
    source = left_size + right_size
    sink = source + 1
    
    # 添加源点到左侧顶点的边
    for i in range(left_size):
        flow_graph[source][i] = 1
        flow_graph[i][source] = 0
    
    # 添加右侧顶点到汇点的边
    for i in range(right_size):
        flow_graph[left_size + i][sink] = 1
        flow_graph[sink][left_size + i] = 0
    
    # 添加二分图中的边
    for i in range(left_size):
        for j in graph[i]:
            flow_graph[i][left_size + j] = 1
            flow_graph[left_size + j][i] = 0
    
    # 使用 Ford-Fulkerson 算法求解最大流
    def bfs():
        parent = [-1] * (sink + 1)
        queue = deque([source])
        parent[source] = -2
        
        while queue:
            u = queue.popleft()
            for v, capacity in flow_graph[u].items():
                if parent[v] == -1 and capacity > 0:
                    parent[v] = u
                    if v == sink:
                        return parent
                    queue.append(v)
        return None
    
    def ford_fulkerson():
        max_flow = 0
        while True:
            parent = bfs()
            if not parent:
                break
            
            # 找到增广路径上的最小容量
            v = sink
            min_capacity = float('inf')
            while v != source:
                u = parent[v]
                min_capacity = min(min_capacity, flow_graph[u][v])
                v = u
            
            # 更新流量
            v = sink
            while v != source:
                u = parent[v]
                flow_graph[u][v] -= min_capacity
                flow_graph[v][u] += min_capacity
                v = u
            
            max_flow += min_capacity
        
        return max_flow
    
    return ford_fulkerson()
```

### 4.3 网络流算法复杂度

- **时间复杂度**：
  1. Ford-Fulkerson 算法：O(VE²)
  2. Dinic 算法：O(V²E)
  3. ISAP 算法：O(V²E)
- **空间复杂度**：O(V + E)

## 5. 算法复杂度分析

1. **匈牙利算法**
   - 时间复杂度：O(VE)
   - 优点：实现简单，容易理解
   - 缺点：对于大规模图效率较低
   - 适用场景：小规模图，需要快速实现

2. **Hopcroft-Karp 算法**
   - 时间复杂度：O(√VE)
   - 优点：效率更高，适合大规模图
   - 缺点：实现相对复杂
   - 适用场景：大规模图，需要高效算法

3. **网络流算法**
   - 时间复杂度：O(VE²) 或 O(V²E)
   - 优点：可以处理更复杂的问题，如带权匹配
   - 缺点：实现复杂，常数较大
   - 适用场景：带权匹配，复杂约束条件

## 练习题目

- [LCP 04. 覆盖](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/LCP/broken-board-dominoes.md)	
- [1947. 最大兼容性评分和](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1900-1999/maximum-compatibility-score-sum.md)	
- [1595. 连通两组点的最小成本](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1500-1599/minimum-cost-to-connect-two-groups-of-points.md)	

- [二分图最大匹配题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E4%BA%8C%E5%88%86%E5%9B%BE%E6%9C%80%E5%A4%A7%E5%8C%B9%E9%85%8D%E9%A2%98%E7%9B%AE)