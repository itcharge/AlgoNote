## 1. 深度优先搜索简介

> **深度优先搜索算法（Depth First Search）**：英文缩写为 DFS，是一种用于搜索树或图结构的算法。深度优先搜索算法采用了回溯思想，从起始节点开始，沿着一条路径尽可能深入地访问节点，直到无法继续前进时为止，然后回溯到上一个未访问的节点，继续深入搜索，直到完成整个搜索过程。

深度优先搜索算法中所谓的深度优先，就是说优先沿着一条路径走到底，直到无法继续深入时再回头。

在深度优先遍历的过程中，我们需要将当前遍历节点 $u$ 的相邻节点暂时存储起来，以便于在回退的时候可以继续访问它们。遍历到的节点顺序符合「后进先出」的特点，这正是「递归」和「堆栈」所遵循的规律，所以深度优先搜索可以通过「递归」或者「堆栈」来实现。

## 2. 深度优先搜索算法步骤

接下来我们以一个无向图为例，介绍一下深度优先搜索的算法步骤。

1. 选择起始节点 $u$，并将其标记为已访问。
2. 检查当前节点是否为目标节点（看具体题目要求）。
3. 如果当前节点 $u$ 是目标节点，则直接返回结果。
4. 如果当前节点 $u$ 不是目标节点，则遍历当前节点 $u$ 的所有未访问邻接节点。
5. 对每个未访问的邻接节点 $v$，从节点 $v$ 出发继续进行深度优先搜索（递归）。
6. 如果节点 $u$ 没有未访问的相邻节点，回溯到上一个节点，继续搜索其他路径。
7. 重复 $2 \sim 6$ 步骤，直到遍历完整个图或找到目标节点为止。

::: tabs#DFS

@tab <1>

![深度优先搜索 1](https://qcdn.itcharge.cn/images/202309042321406.png)

@tab <2>

![深度优先搜索 2](https://qcdn.itcharge.cn/images/202309042323911.png)

@tab <3>

![深度优先搜索 3](https://qcdn.itcharge.cn/images/202309042324370.png)

@tab <4>

![深度优先搜索 4](https://qcdn.itcharge.cn/images/202309042325587.png)

@tab <5>

![深度优先搜索 5](https://qcdn.itcharge.cn/images/202309042325689.png)

@tab <6>

![深度优先搜索 6](https://qcdn.itcharge.cn/images/202309042325770.png)

:::

## 3. 基于递归实现的深度优先搜索

### 3.1 基于递归实现的深度优先搜索算法步骤

深度优先搜索算法可以通过递归来实现，以下是基于递归实现的深度优先搜索算法步骤：

1. 定义 $graph$ 为存储无向图的嵌套数组变量，$visited$ 为标记访问节点的集合变量。$u$ 为当前遍历边的开始节点。定义 `def dfs_recursive(graph, u, visited):` 为递归实现的深度优先搜索方法。
2. 选择起始节点 $u$，并将其标记为已访问，即将节点 $u$ 放入 $visited$ 中（`visited.add(u)`）。
3. 检查当前节点 $u$ 是否为目标节点（看具体题目要求）。
4. 如果当前节点 $u$ 是目标节点，则直接返回结果。
5. 如果当前节点 $u$ 不是目标节点，则遍历当前节点 $u$ 的所有未访问邻接节点。
6. 对每个未访问的邻接节点 $v$，从节点 $v$ 出发继续进行深度优先搜索（递归），即调用 `dfs_recursive(graph, v, visited)`。
7. 如果节点 $u$ 没有未访问的相邻节点，则回溯到最近访问的节点，继续搜索其他路径。
8. 重复 $3 \sim 7$ 步骤，直到遍历完整个图或找到目标节点为止。

### 3.2 基于递归实现的深度优先搜索实现代码

```python
class Solution:
    def dfs_recursive(self, graph, u, visited):
        print(u)                        # 访问节点
        visited.add(u)                  # 节点 u 标记其已访问

        for v in graph[u]:
            if v not in visited:        # 节点 v 未访问过
                # 深度优先搜索遍历节点
                self.dfs_recursive(graph, v, visited)
        

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}

# 基于递归实现的深度优先搜索
visited = set()
Solution().dfs_recursive(graph, "A", visited)
```

## 4. 基于堆栈实现的深度优先搜索

### 4.1 基于堆栈实现的深度优先搜索算法步骤

深度优先搜索算法除了基于递归实现之外，还可以基于堆栈来实现。同时，为了防止多次遍历同一节点，在使用栈存放节点访问记录时，我们将「当前节点」以及「下一个将要访问的邻接节点下标」一同存入栈中，从而在出栈时，可以通过下标直接找到下一个邻接节点，而不用遍历所有邻接节点。

以下是基于堆栈实现的深度优先搜索的算法步骤：

1. 定义 $graph$ 为存储无向图的嵌套数组变量，$visited$ 为标记访问节点的集合变量。$start$ 为当前遍历边的开始节点。定义 $stack$ 用于存放节点访问记录的栈结构。
2. 选择起始节点 $u$，检查当前节点 $u$ 是否为目标节点（看具体题目要求）。
3. 如果当前节点 $u$ 是目标节点，则直接返回结果。
4. 如果当前节点 $u$ 不是目标节点，则将节点 $u$ 以及节点 $u$ 下一个将要访问的邻接节点下标 $0$ 放入栈中，并标记为已访问，即 `stack.append([u, 0])`，`visited.add(u)`。
5. 如果栈不为空，取出 $stack$ 栈顶元素节点 $u$，以及节点 $u$ 下一个将要访问的邻接节点下标 $i$。
6. 根据节点 $u$ 和下标 $i$，取出将要遍历的未访问过的邻接节点 $v$。
7. 将节点 $u$ 以及节点 u 的下一个邻接节点下标 $i + 1$ 放入栈中。
8. 访问节点 $v$，并对节点进行相关操作（看具体题目要求）。
9. 将节点 $v$ 以及节点 $v$ 下一个邻接节点下标 $0$ 放入栈中，并标记为已访问，即 `stack.append([v, 0])`，`visited.add(v)`。
10. 重复步骤 $5 \sim 9$，直到 $stack$ 栈为空或找到目标节点为止。

### 4.2 基于堆栈实现的深度优先搜索实现代码

```python
class Solution:
    def dfs_stack(self, graph, u):
        print(u)                            # 访问节点 u
        visited, stack = set(), []          # 使用 visited 标记访问过的节点, 使用栈 stack 存放临时节点
        
        stack.append([u, 0])                # 将节点 u，节点 u 的下一个邻接节点下标放入栈中，下次将遍历 graph[u][0]
        visited.add(u)                      # 将起始节点 u 标记为已访问
        
    
        while stack:
            u, i = stack.pop()              # 取出节点 u，以及节点 u 下一个将要访问的邻接节点下标 i
            
            if i < len(graph[u]):
                v = graph[u][i]             # 取出邻接节点 v
                stack.append([u, i + 1])    # 下一次将遍历 graph[u][i + 1]
                if v not in visited:        # 节点 v 未访问过
                    print(v)                # 访问节点 v
                    stack.append([v, 0])    # 下一次将遍历 graph[v][0]
                    visited.add(v)          # 将节点 v 标记为已访问                
        

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}

# 基于堆栈实现的深度优先搜索
Solution().dfs_stack(graph, "A")
```

## 5. 深度优先搜索应用

### 5.1 岛屿数量

#### 5.1.1 题目链接

- [200. 岛屿数量 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-islands/)

#### 5.1.2 题目大意

**描述**：给定一个由字符 `'1'`（陆地）和字符 `'0'`（水）组成的的二维网格 `grid`。

**要求**：计算网格中岛屿的数量。

**说明**：

- 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
- 此外，你可以假设该网格的四条边均被水包围。
- $m == grid.length$。
- $n == grid[i].length$。
- $1 \le m, n \le 300$。
- $grid[i][j]$ 的值为 `'0'` 或 `'1'`。

**示例**：

- 示例 1：

```python
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
```

- 示例 2：

```python
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
```

#### 5.1.3 解题思路

如果把上下左右相邻的字符 `'1'` 看做是 `1` 个连通块，这道题的目的就是求解一共有多少个连通块。

使用深度优先搜索或者广度优先搜索都可以。

##### 思路 1：深度优先搜索

1. 遍历 $grid$。
2. 对于每一个字符为 `'1'` 的元素，遍历其上下左右四个方向，并将该字符置为 `'0'`，保证下次不会被重复遍历。
3. 如果超出边界，则返回 $0$。
4. 对于 $(i, j)$ 位置的元素来说，递归遍历的位置就是 $(i - 1, j)$、$(i, j - 1)$、$(i + 1, j)$、$(i, j + 1)$ 四个方向。每次遍历到底，统计数记录一次。
5. 最终统计出深度优先搜索的次数就是我们要求的岛屿数量。

##### 思路 1：代码

```python
class Solution:
    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$。其中 $m$ 和 $n$ 分别为行数和列数。
- **空间复杂度**：$O(m \times n)$。

### 5.2 克隆图

#### 5.2.1 题目链接

- [133. 克隆图 - 力扣（LeetCode）](https://leetcode.cn/problems/clone-graph/)

#### 5.2.2 题目大意

**描述**：以每个节点的邻接列表形式（二维列表）给定一个无向连通图，其中 $adjList[i]$ 表示值为 $i + 1$ 的节点的邻接列表，$adjList[i][j]$ 表示值为 $i + 1$ 的节点与值为 $adjList[i][j]$ 的节点有一条边。

**要求**：返回该图的深拷贝。

**说明**：

- 节点数不超过 $100$。
- 每个节点值 $Node.val$ 都是唯一的，$1 \le Node.val \le 100$。
- 无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
- 由于图是无向的，如果节点 $p$ 是节点 $q$ 的邻居，那么节点 $q$ 也必须是节点 $p$ 的邻居。
- 图是连通图，你可以从给定节点访问到所有节点。

**示例**：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/01/133_clone_graph_question.png)

```python
输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
输出：[[2,4],[1,3],[2,4],[1,3]]
解释：
图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
```

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/01/graph-1.png)

```python
输入：adjList = [[2],[1]]
输出：[[2],[1]]
```

#### 5.2.3 解题思路

所谓深拷贝，就是构建一张与原图结构、值均一样的图，但是所用的节点不再是原图节点的引用，即每个节点都要新建。

可以用深度优先搜索或者广度优先搜索来做。

##### 思路 1：深度优先搜索

1. 使用哈希表 $visitedDict$ 来存储原图中被访问过的节点和克隆图中对应节点，键值对为「原图被访问过的节点：克隆图中对应节点」。
2. 从给定节点开始，以深度优先搜索的方式遍历原图。
   1. 如果当前节点被访问过，则返回隆图中对应节点。
   2. 如果当前节点没有被访问过，则创建一个新的节点，并保存在哈希表中。
   3. 遍历当前节点的邻接节点列表，递归调用当前节点的邻接节点，并将其放入克隆图中对应节点。
3. 递归结束，返回克隆节点。

##### 思路 1：代码

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visitedDict = dict()

        def dfs(node: 'Node') -> 'Node':
            if node in visitedDict:
                return visitedDict[node]

            clone_node = Node(node.val, [])
            visitedDict[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node

        return dfs(node)
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 为图中节点数量。
- **空间复杂度**：$O(n)$。

## 参考资料

- 【文章】[深度优先搜索 - LeetBook - 力扣（LeetCode）](https://leetcode.cn/leetbook/read/dfs/egx6xc/)
- 【文章】[算法数据结构：深度优先搜索（DFS） - 掘金](https://juejin.cn/post/6864348493721387021)
- 【文章】[Python 图的 BFS 与 DFS - 黄蜜桃的博客 - CSDN 博客](https://blog.csdn.net/qq_37738656/article/details/83027943)
- 【文章】[图的深度优先遍历（递归、非递归；邻接表，邻接矩阵）_zjq_smile 的博客 - CSDN博客](https://blog.csdn.net/zscfa/article/details/75947816)
- 【题解】[200. 岛屿数量（DFS / BFS） - 岛屿数量 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/)