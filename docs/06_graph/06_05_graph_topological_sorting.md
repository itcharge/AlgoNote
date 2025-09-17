## 1. 拓扑排序简介

> **拓扑排序（Topological Sorting）**：是一种针对有向无环图（DAG）的排序方法。它将图中的所有顶点排成一个线性序列，使得对于任意一条有向边 $<u, v>$，顶点 $u$ 都排在顶点 $v$ 的前面。这个线性序列就叫做拓扑序列。

需要注意的是，只有有向无环图（DAG）才可以进行拓扑排序。无向图或者有向有环图都无法进行拓扑排序。

![有向无环图](https://qcdn.itcharge.cn/images/202405092308713.png)

以上图为例，这是一个有向无环图（DAG）。$v_1 \rightarrow v_2 \rightarrow v_3 \rightarrow v_4 \rightarrow v_5 \rightarrow v_6$ 是其中一个拓扑序列。$v_1 \rightarrow v_2 \rightarrow v_3 \rightarrow v_4 \rightarrow v_6 \rightarrow v_5$ 也是一个拓扑序列。也就是说，同一个有向无环图可能有多个不同的拓扑序列。

## 2. 拓扑排序的实现方法

拓扑排序常用两种实现方式，分别是「Kahn 算法」和「DFS 深度优先搜索算法」。下面我们分别用通俗易懂的方式介绍它们的核心思路。

### 2.1 Kahn 算法

> **Kahn 算法的核心思想**：
>
> 1. 不断寻找入度为 $0$ 的节点（即没有依赖的节点），将其加入结果序列。
> 2. 删除该节点及其所有出边（即把它对其他节点的影响去除）。
> 3. 重复上述过程，直到所有节点都被处理，或者没有入度为 $0$ 的节点可选（此时说明图中有环，无法拓扑排序）。

#### 2.1.1 Kahn 算法的详细步骤

1. 用一个数组 $indegrees$ 记录每个节点的入度（有多少条边指向它）。
2. 用一个集合 $S$（可以用队列、栈等）存放所有当前入度为 $0$ 的节点。
3. 每次从 $S$ 中取出一个节点 $u$，将其加入拓扑序列 $order$。
4. 遍历 $u$ 的所有邻接节点 $v$，将 $v$ 的入度减 $1$。如果 $v$ 的入度变为 $0$，就把 $v$ 加入 $S$。
5. 重复上述步骤，直到 $S$ 为空。如果此时还有节点未被加入 $order$，说明图中有环，无法拓扑排序。
6. 如果所有节点都被加入 $order$，那么 $order$ 就是该图的一个拓扑序列。

#### 2.1.2 Kahn 算法的实现代码

```python
import collections

class Solution:
    # 拓扑排序，graph 中包含所有顶点的有向边关系（包括无边顶点）
    def topologicalSortingKahn(self, graph: dict):
        # 初始化所有顶点的入度为 0
        indegrees = {u: 0 for u in graph}
        # 统计每个顶点的入度
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1

        # 将所有入度为 0 的顶点加入队列 S
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        order = []  # 用于存储拓扑序列

        while S:
            u = S.pop()  # 取出一个入度为 0 的顶点
            order.append(u)  # 加入拓扑序列
            for v in graph[u]:  # 遍历 u 的所有邻接点
                indegrees[v] -= 1  # 删除 u 指向 v 的边，v 入度减 1
                if indegrees[v] == 0:
                    S.append(v)  # 如果 v 入度为 0，加入队列

        # 如果 order 长度小于顶点数，说明有环，无法拓扑排序
        if len(order) != len(indegrees):
            return []
        return order  # 返回拓扑序列

    def findOrder(self, n: int, edges):
        """
        n: 顶点个数，编号为 0 ~ n - 1
        edges: 边列表，每条边为 (u, v)，表示 u 指向 v
        返回一个拓扑序列（如果有环则返回空列表）
        """
        # 构建邻接表
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
        # 调用 Kahn 算法进行拓扑排序
        return self.topologicalSortingKahn(graph)
```

### 2.2 基于 DFS 的拓扑排序算法

> **DFS 拓扑排序的核心思想**：
>
> 1. 对于某个顶点 $u$，用深度优先搜索遍历所有从 $u$ 出发的有向边 $<u, v>$。只有当 $u$ 的所有相邻顶点 $v$ 都已经被搜索完毕后，才将 $u$ 加入拓扑序列。这样保证 $u$ 一定排在所有 $v$ 的前面。
> 2. 因此，我们可以在每次递归回溯到顶点 $u$ 时，把 $u$ 加入一个栈（或列表），最后将栈中的元素逆序输出，就是一种拓扑排序。

#### 2.2.1 DFS 拓扑排序的具体步骤

1. 用集合 $visited$ 记录哪些顶点已经被访问，避免重复遍历。
2. 用集合 $onStack$ 记录当前递归路径上的顶点。如果在一次深搜过程中遇到已经在 $onStack$ 中的顶点，说明图中有环，无法拓扑排序。
3. 用布尔变量 $hasCycle$ 标记图中是否存在环。
4. 对每个未被访问的顶点 $u$，执行以下操作：
   1. 如果 $u$ 已经在 $onStack$，说明遇到了环，直接返回。
   2. 如果 $u$ 已经被访问过，或者已经检测到有环，也直接返回。
5. 标记 $u$ 已访问，并加入 $onStack$，然后递归遍历 $u$ 的所有邻接点 $v$。
6. 当 $u$ 的所有邻接点都遍历完毕后，将 $u$ 加入拓扑序列 $order$。
7. 回溯时，将 $u$ 从 $onStack$ 中移除。
8. 对所有顶点重复上述过程，直到全部遍历完或检测到环。
9. 如果没有环，最后将 $order$ 逆序输出，就是拓扑排序结果。

#### 2.2.2 DFS 深度优先搜索算法实现代码

```python
import collections

class Solution:
    # 基于 DFS 的拓扑排序，graph 为邻接表，包含所有顶点（即使无出边也要有键）
    def topologicalSortingDFS(self, graph: dict):
        visited = set()      # 记录已访问过的顶点，防止重复遍历
        onStack = set()      # 记录当前递归路径上的顶点，用于检测环
        order = []           # 存储拓扑序列（后序遍历结果）
        hasCycle = False     # 标记图中是否存在环

        def dfs(u):
            nonlocal hasCycle
            if hasCycle:     # 已经检测到环，直接返回
                return
            if u in onStack:
                # 当前节点在递归栈中，说明存在环
                hasCycle = True
                return
            if u in visited:
                # 已访问过，无需重复遍历
                return

            visited.add(u)       # 标记 u 已访问
            onStack.add(u)       # 标记 u 在当前递归路径上

            for v in graph[u]:   # 遍历 u 的所有邻接点
                dfs(v)           # 递归访问 v

            order.append(u)      # 后序位置加入拓扑序列
            onStack.remove(u)    # 回溯时移除 u，恢复递归路径标记

        # 对所有顶点做 DFS，防止图不连通
        for u in graph:
            if u not in visited:
                dfs(u)

        if hasCycle:
            # 有环，无法拓扑排序
            return []
        order.reverse()  # 后序遍历逆序即为拓扑序
        return order

    def findOrder(self, n: int, edges):
        """
        n: 顶点个数，编号为 0 ~ n-1
        edges: 边列表，每条边为 (u, v)，表示 u 指向 v
        返回一个拓扑序列（有环则返回空列表）
        """
        # 构建邻接表，确保每个顶点都在 graph 中
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
        return self.topologicalSortingDFS(graph)
```

## 3. 拓扑排序的应用

拓扑排序可以用来解决一些依赖关系的问题，比如项目的执行顺序，课程的选修顺序等。

### 3.1 课程表 II

#### 3.1.1 题目链接

- [210. 课程表 II - 力扣](https://leetcode.cn/problems/course-schedule-ii/)

#### 3.1.2 题目大意

**描述**：给定一个整数 $numCourses$，代表这学期必须选修的课程数量，课程编号为 $0 \sim numCourses - 1$。再给定一个数组 $prerequisites$ 表示先修课程关系，其中 $prerequisites[i] = [ai, bi]$ 表示如果要学习课程 $ai$ 则必须要先完成课程 $bi$。

**要求**：返回学完所有课程所安排的学习顺序。如果有多个正确的顺序，只要返回其中一种即可。如果无法完成所有课程，则返回空数组。

**说明**：

- $1 \le numCourses \le 2000$。
- $0 \le prerequisites.length \le numCourses \times (numCourses - 1)$。
- $prerequisites[i].length == 2$。
- $0 \le ai, bi < numCourses$。
- $ai \ne bi$。
- 所有$[ai, bi]$ 互不相同。

**示例**：

- 示例 1：

```python
输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1]。
```

- 示例 2：

```python
输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出：[0,2,1,3]
解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3]。
```

#### 3.1.3 解题思路

##### 思路 1：拓扑排序

本题是「[0207. 课程表](https://leetcode.cn/problems/course-schedule/)」的进阶版，只需在上一题的基础上增加一个用于记录课程顺序的数组 $order$。

具体思路如下：

1. 用哈希表 $graph$ 构建课程之间的依赖关系图，同时统计每门课程的入度，存入 $indegrees$ 数组。
2. 使用队列 $S$，将所有入度为 $0$ 的课程编号加入队列。
3. 每次从队列中取出一个课程 $u$，将其加入结果数组 $order$。
4. 遍历课程 $u$ 指向的所有后继课程 $v$，将 $v$ 的入度减 $1$。若 $v$ 的入度变为 $0$，则将 $v$ 加入队列 $S$。
5. 重复步骤 $3$ 和 $4$，直到队列为空。
6. 最后判断 $order$ 的长度是否等于课程总数。如果相等，说明可以完成所有课程，返回 $order$；否则说明存在环，无法完成所有课程，返回空数组。

##### 思路 1：代码

```python
import collections

class Solution:
    # 拓扑排序，graph 中包含所有顶点的有向边关系（包括无边顶点）
    def topologicalSortingKahn(self, graph: dict):
        indegrees = {u: 0 for u in graph}   # indegrees 用于记录所有顶点入度
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1           # 统计所有顶点入度
        
        # 将入度为 0 的顶点存入集合 S 中
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        order = []                          # order 用于存储拓扑序列
        
        while S:
            u = S.pop()                     # 从集合中选择一个没有前驱的顶点 0
            order.append(u)                 # 将其输出到拓扑序列 order 中
            for v in graph[u]:              # 遍历顶点 u 的邻接顶点 v
                indegrees[v] -= 1           # 删除从顶点 u 出发的有向边
                if indegrees[v] == 0:       # 如果删除该边后顶点 v 的入度变为 0
                    S.append(v)             # 将其放入集合 S 中
        
        if len(indegrees) != len(order):    # 还有顶点未遍历（存在环），无法构成拓扑序列
            return []
        return order                        # 返回拓扑序列
    
    
    def findOrder(self, numCourses: int, prerequisites):
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
            
        for v, u in prerequisites:
            graph[u].append(v)
            
        return self.topologicalSortingKahn(graph)
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 为课程数，$m$ 为先修课程的要求数。
- **空间复杂度**：$O(n + m)$。

## 练习题目

- [0207. 课程表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/course-schedule.md)
- [0210. 课程表 II](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/course-schedule-ii.md)
- [0802. 找到最终的安全状态](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0800-0899/find-eventual-safe-states.md)

- [拓扑排序题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%9B%BE%E7%9A%84%E6%8B%93%E6%89%91%E6%8E%92%E5%BA%8F%E9%A2%98%E7%9B%AE)