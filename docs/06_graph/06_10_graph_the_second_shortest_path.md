## 1.1 次短路径简介

> **次短路径**：给定一个带权有向图，求从起点到终点的次短路径。次短路径是指长度严格大于最短路径的所有路径中长度最小的那条路径。

### 1.1.1 问题特点

- 次短路径必须严格大于最短路径
- 可能存在多条最短路径，但次短路径是唯一的
- 如果不存在次短路径（如最短路径是唯一的），则返回 $-1$。

### 1.1.2 常见变体

1. 允许重复边的次短路径
2. 不允许重复边的次短路径
3. 带约束条件的次短路径（如必须经过某些节点）

## 1.2 次短路径基本思路

求解次短路径的常用方法是使用 Dijkstra 算法的变体。基本思路如下：

1. 使用 Dijkstra 算法找到最短路径。
2. 在寻找最短路径的过程中，同时维护次短路径。
3. 对于每个节点，我们需要维护两个距离值：
   - $dist1[u]$：从起点到节点 u 的最短距离。
   - $dist2[u]$：从起点到节点 u 的次短距离。

### 1.2.1 具体实现步骤

1. 初始化 $dist1$ 和 $dist2$ 数组，所有值设为无穷大。
2. 将起点加入优先队列，距离为 $0$。
3. 每次从队列中取出距离最小的节点 $u$。
4. 遍历 $u$ 的所有邻接节点 $v$：
   - 如果找到更短的路径，更新 $dist1[v]$。
   - 如果找到次短的路径，更新 $dist2[v]$。
5. 最终 $dist2[target]$ 即为所求的次短路径长度。

### 1.2.2 算法正确性证明

1. 对于任意节点 $u$，$dist1[u]$ 一定是最短路径长度。
2. 对于任意节点 $u$，$dist2[u]$ 一定是次短路径长度。
3. 算法会考虑所有可能的路径，因此不会遗漏次短路径。

## 1.3 次短路径代码实现

```python
import heapq

def second_shortest_path(n: int, edges: List[List[int]], start: int, end: int) -> int:
    """
    计算从起点到终点的次短路径长度
    
    参数:
        n: 节点数量
        edges: 边列表，每个元素为 [起点, 终点, 权重]
        start: 起始节点
        end: 目标节点
    
    返回:
        次短路径的长度，如果不存在则返回 -1
    """
    # 构建邻接表
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    # 初始化距离数组
    dist1 = [float('inf')] * n  # 最短距离
    dist2 = [float('inf')] * n  # 次短距离
    dist1[start] = 0
    
    # 优先队列，存储 (距离, 节点) 的元组
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # 如果当前距离大于次短距离，跳过
        if d > dist2[u]:
            continue
            
        # 遍历所有邻接节点
        for v, w in graph[u]:
            # 计算新的距离
            new_dist = d + w
            
            # 如果找到更短的路径
            if new_dist < dist1[v]:
                dist2[v] = dist1[v]  # 原来的最短路径变成次短路径
                dist1[v] = new_dist  # 更新最短路径
                heapq.heappush(pq, (new_dist, v))
            # 如果找到次短的路径
            elif new_dist > dist1[v] and new_dist < dist2[v]:
                dist2[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return dist2[end] if dist2[end] != float('inf') else -1

# 使用示例
n = 4
edges = [
    [0, 1, 1],
    [1, 2, 2],
    [2, 3, 1],
    [0, 2, 4],
    [1, 3, 5]
]
start = 0
end = 3

result = second_shortest_path(n, edges, start, end)
print(f"次短路径长度: {result}")
```

## 1.4 算法复杂度分析

- 时间复杂度：$O((V + E)\log V)$，其中 $V$ 是节点数，$E$ 是边数。
- 空间复杂度：$O(V)$，用于存储距离数组和优先队列。

## 1.5 应用场景

1. 网络路由：寻找备用路径。
2. 交通规划：寻找替代路线。
3. 通信网络：寻找备用通信路径。
4. 物流配送：规划备用配送路线。

## 1.6 注意事项

1. 次短路径必须严格大于最短路径。
2. 如果不存在次短路径，返回 $-1$。
3. 图中可能存在负权边，此时需要使用 Bellman-Ford 算法的变体。
4. 对于无向图，需要将每条边都加入两次。

## 练习题目

- [次短路径题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E6%AC%A1%E7%9F%AD%E8%B7%AF%E5%BE%84%E9%A2%98%E7%9B%AE)