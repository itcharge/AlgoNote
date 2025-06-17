## 1.1 差分约束系统简介

> **差分约束系统（System of Difference Constraints）**：一种特殊的线性规划问题，其中每个约束条件都是形如 $x_i - x_j \leq c$ 的不等式。这类问题可以通过图论中的最短路径算法来求解。

## 1.2 问题形式

给定一组形如 $x_i - x_j \leq c$ 的约束条件，其中：

- $x_i, x_j$ 是变量。
- $c$ 是常数。

我们的目标是找到一组满足所有约束条件的变量值。

## 1.3 图论建模

差分约束系统可以转化为有向图问题：

1. 将每个变量 $x_i$ 看作图中的一个顶点。
2. 对于约束 $x_i - x_j \leq c$，添加一条从 $j$ 到 $i$ 的边，权重为 $c$。
3. 添加一个虚拟源点 $s$，向所有顶点连一条权重为 $0$ 的边。

## 1.4 求解方法

1. **Bellman-Ford 算法**：
   - 如果图中存在负环，则无解。
   - 否则，从源点到各点的最短路径长度即为对应变量的解。

2. **SPFA 算法**：
   - 队列优化的 Bellman-Ford 算法。
   - 适用于稀疏图。

## 1.5 应用场景

1. 任务调度问题
2. 区间约束问题
3. 资源分配问题
4. 时间序列分析

## 1.6 代码实现

```python
def solve_difference_constraints(n, constraints):
    # 构建图
    graph = [[] for _ in range(n + 1)]
    for i, j, c in constraints:
        graph[j].append((i, c))
    
    # 添加虚拟源点
    for i in range(n):
        graph[n].append((i, 0))
    
    # Bellman-Ford 算法
    dist = [float('inf')] * (n + 1)
    dist[n] = 0
    
    # 松弛操作
    for _ in range(n):
        for u in range(n + 1):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    # 检查负环
    for u in range(n + 1):
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                return None  # 存在负环，无解
    
    return dist[:n]  # 返回前 n 个变量的解
```

## 1.7 算法复杂度

- 时间复杂度：

  - **Bellman-Ford 算法**：

    - 最坏情况：$O(VE)$。

    - 其中 $V$ 为顶点数，$E$ 为边数。

    - 需要进行 $V-1$ 次松弛操作，每次操作遍历所有边。

  - **SPFA 算法**：
    - 平均情况：$O(kE)$，其中 $k$ 为每个点的平均入队次数。
    - 最坏情况：$O(VE)$。
    - 实际运行时间通常优于 Bellman-Ford 算法。
  
- 空间复杂度：

  - **Bellman-Ford 算法**：

    - $O(V + E)$

    - 需要存储图结构：$O(V + E)$。

    - 需要存储距离数组：$O(V)$。

  - **SPFA 算法**：

    - $O(V + E)$。

    - 需要存储图结构：$O(V + E)$。

    - 需要存储距离数组：$O(V)$。

    - 需要存储队列：$O(V)$。

### 1.8 优化建议

1. 对于稀疏图，优先使用 SPFA 算法。
2. 对于稠密图，可以考虑使用 Bellman-Ford 算法。
3. 如果问题规模较大，可以考虑使用其他优化算法或启发式方法。

### 1.9 注意事项

1. 差分约束系统可能有多个解
2. 如果存在负环，则无解
3. 实际应用中需要注意数值精度问题
4. 对于大规模问题，可以考虑使用其他优化算法

## 练习题目

- [差分约束系统题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%B7%AE%E5%88%86%E7%BA%A6%E6%9D%9F%E7%B3%BB%E7%BB%9F)