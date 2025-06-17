# [0323. 无向图中连通分量的数目](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/)

- 标签：深度优先搜索、广度优先搜索、并查集、图
- 难度：中等

## 题目链接

- [0323. 无向图中连通分量的数目 - 力扣](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/)

## 题目大意

**描述**：给定 `n` 个节点（编号从 `0` 到 `n - 1`）的图的无向边列表 `edges`，其中 `edges[i] = [u, v]` 表示节点 `u` 和节点 `v` 之间有一条无向边。

**要求**：计算该无向图中连通分量的数量。

**说明**：

- $1 \le n \le 2000$。
- $1 \le edges.length \le 5000$。
- $edges[i].length == 2$。
- $0 \le ai \le bi < n$。
- $ai != bi$。
- `edges` 中不会出现重复的边。

**示例**：

- 示例 1：

```python
输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]
 0          3
 |          |
 1 --- 2    4 
输出: 2
```

- 示例 2：

```python
输入: n = 5 和 edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
 0           4
 |           |
 1 --- 2 --- 3
输出:  1
```

## 解题思路

先来看一下图论中相关的名次解释。

- **连通图**：在无向图中，如果可以从顶点 $v_i$ 到达 $v_j$，则称 $v_i$ 和 $v_j$ 连通。如果图中任意两个顶点之间都连通，则称该图为连通图。
- **无向图的连通分量**：如果该图为连通图，则连通分量为本身；否则将无向图中的极大连通子图称为连通分量，每个连通分量都是一个连通图。
- **无向图的连通分量个数**：无向图的极大连通子图的个数。

接下来我们来解决这道题。

### 思路 1：深度优先搜索

1. 使用 `visited` 数组标记遍历过的节点，使用 `count` 记录连通分量数量。
2. 从未遍历过的节点 `u` 出发，连通分量数量加 1。然后遍历与 `u` 节点构成无向边，且为遍历过的的节点 `v`。
3. 再从 `v` 出发继续深度遍历。
4. 直到遍历完与`u`  直接相关、间接相关的节点之后，再遍历另一个未遍历过的节点，继续上述操作。
5. 最后输出连通分量数目。

### 思路 1：代码

```python
class Solution:
    def dfs(self, visited, i, graph):
        visited[i] = True
        for j in graph[i]:
            if not visited[j]:
                self.dfs(visited, j, graph)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = [False for _ in range(n)]
        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(visited, i, graph)
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中$n$ 是顶点个数。
- **空间复杂度**：$O(n)$。

### 思路 2：广度优先搜索

1. 使用变量 `count` 记录连通分量个数。使用集合变量 `visited` 记录访问过的节点，使用邻接表 `graph` 记录图结构。
2. 从 `0` 开始，依次遍历 `n` 个节点。
3. 如果第 `i` 个节点未访问过：
   1. 将其添加到 `visited` 中。
   2. 并且连通分量个数累加，即 `count += 1`。
   3. 定义一个队列 `queue`，将第 `i` 个节点加入到队列中。
   4. 从队列中取出第一个节点，遍历与其链接的节点，并将未遍历过的节点加入到队列 `queue` 和 `visited` 中。
   5. 直到队列为空，则继续向后遍历。
4. 最后输出连通分量数目 `count`。

### 思路 2：代码

```python
import collections

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                count += 1
                queue = collections.deque([i])
                while queue:
                    node_u = queue.popleft()
                    for node_v in graph[node_u]:
                        if node_v not in visited:
                            visited.add(node_v)
                            queue.append(node_v)
        return count
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。其中$n$ 是顶点个数。
- **空间复杂度**：$O(n)$。
