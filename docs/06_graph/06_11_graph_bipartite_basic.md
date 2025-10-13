## 1. 二分图简介

> **二分图（Bipartite Graph）**：又称「二部图」，是一类特殊的无向图。其顶点集可以被划分为两个互不重叠的子集，且所有边仅连接这两个子集之间的顶点，同一子集内的顶点之间没有边相连。

直观地说，就是「左边只连右边，左边不互连；右边只连左边，右边不互连」。

## 2. 二分图判定

> **二分图判定**：判断一个无向图是否可以将所有顶点划分为两个互不重叠的集合，使得每条边的两个端点都分别属于不同的集合。换句话说，图中不存在奇数长度的环，则该图为二分图。

### 2.1 二分图判定的具体步骤

判断一个无向图是否为二分图，常用的方法是「染色法」：通过给图的每个顶点染上两种不同的颜色，检查是否能做到每条边的两个端点颜色不同。具体步骤如下：

1. **初始化染色数组**：为每个顶点分配颜色标记，初始均为未染色（如 0 表示未染色，1 和 -1 分别代表两种颜色）。
2. **遍历所有顶点**：对每个未染色的顶点，执行一次 BFS 或 DFS 染色（因图可能不连通，需分别处理每个连通分量）。
3. **染色与冲突检测**：
    - 从当前顶点开始，赋予一种颜色（如 1）。
    - 遍历其所有邻接点：
        - 如果邻接点未染色，则染为相反颜色（-1），并递归 / 迭代继续处理；
        - 如果邻接点已染色且与当前顶点颜色相同，则发生冲突，说明不是二分图，立即返回 `False`。
4. **全部顶点染色无冲突**：如果所有顶点均成功染色且未出现冲突，则该图为二分图。


### 2.2 二分图判定的代码实现

```python
def is_bipartite(graph):
    """
    判断无向图是否为二分图（染色法）
    :param graph: List[List[int]]，邻接表表示的无向图
    :return: bool，是否为二分图
    """
    n = len(graph)
    colors = [0] * n  # 0 表示未染色，1 和 -1 表示两种颜色

    def dfs(node, color):
        """
        对节点 node 进行染色，并递归染色其所有邻居
        :param node: 当前节点编号
        :param color: 当前节点应染的颜色（1 或 -1）
        :return: bool，如果染色无冲突返回 True，否则 False
        """
        colors[node] = color  # 给当前节点染色
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                # 邻居和当前节点颜色相同，冲突，非二分图
                return False
            if colors[neighbor] == 0:
                # 邻居未染色，递归染成相反颜色
                if not dfs(neighbor, -color):
                    return False
        return True

    for i in range(n):
        if colors[i] == 0:
            # 只对未染色的节点（新连通分量）进行 DFS 染色
            if not dfs(i, 1):
                return False  # 染色过程中发现冲突，非二分图
    return True  # 所有节点染色无冲突，是二分图
```

### 2.3 二分图判定的算法分析

- **时间复杂度**：$O(V + E)$，其中 $V$ 为顶点数，$E$ 为边数。每个顶点和每条边最多被访问一次。
- **空间复杂度**：$O(V)$，主要用于存储颜色数组和递归/队列。


## 练习题目

- [0785. 判断二分图](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/is-graph-bipartite.md)

- [二分图基础题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E4%BA%8C%E5%88%86%E5%9B%BE%E5%9F%BA%E7%A1%80%E9%A2%98%E7%9B%AE)