## 1. 广度优先搜索简介

> **广度优先搜索算法（Breadth First Search，简称 BFS）**：是一种用于遍历或搜索树、图等结构的经典算法。BFS 从起始节点出发，按照层级逐步向外扩展，优先访问距离起点较近的节点，再访问距离较远的节点，直到遍历完整个结构或找到目标节点。

由于 BFS 的遍历顺序具有「先进先出」的特性，因此通常借助「队列」来实现。

## 2. 广度优先搜索算法步骤

下面以无向图为例，简要梳理广度优先搜索的基本流程：

1. 将起始节点 $u$ 加入队列，并标记为已访问。
2. 当队列不为空时，重复以下操作：
   1. 从队列头部取出一个节点 $x$，访问该节点。
   2. 遍历 $x$ 的所有未被访问的邻接节点 $v$，将它们加入队列并标记为已访问，避免重复访问。
3. 如果在遍历过程中找到目标节点，可提前结束；否则直到队列为空为止。

::: tabs#BFS

@tab <1>

![广度优先搜索 1](https://qcdn.itcharge.cn/images/20230905152316.png)

@tab <2>

![广度优先搜索 2](https://qcdn.itcharge.cn/images/20230905152327.png)

@tab <3>

![广度优先搜索 3](http://qcdn.itcharge.cn/images/20231009141628.png)

@tab <4>

![广度优先搜索 4](https://qcdn.itcharge.cn/images/20230905152401.png)

@tab <5>

![广度优先搜索 5](https://qcdn.itcharge.cn/images/20230905152420.png)

@tab <6>

![广度优先搜索 6](https://qcdn.itcharge.cn/images/20230905152433.png)

@tab <7>

![广度优先搜索 7](https://qcdn.itcharge.cn/images/20230905152445.png)

:::

## 3. 基于队列实现的广度优先搜索

### 3.1 基于队列实现的广度优先搜索算法步骤

1. 定义 $graph$ 为无向图的邻接表，$visited$ 为已访问节点的集合，$queue$ 为队列，$u$ 为起始节点。实现函数 `def bfs(graph, u):`。
2. 将起始节点 $u$ 加入 $visited$ 集合，并入队到 $queue$。
3. 当 $queue$ 非空时，循环执行以下操作：
   1. 弹出队首节点 $u$，访问该节点，并进行相应处理（如打印、判定等，视题目要求）。
   2. 遍历 $u$ 的所有邻接节点 $v$，如果 $v$ 未被访问，则将 $v$ 加入 $visited$ 集合，并入队到 $queue$。
4. 重复上述过程，直到队列为空，遍历结束。

### 3.2 基于队列实现的广度优先搜索实现代码

```python
import collections

class Solution:
    def bfs(self, graph, u):
        visited = set()                     # 使用 visited 标记访问过的节点
        queue = collections.deque([])       # 使用 queue 存放临时节点
        
        visited.add(u)                      # 将起始节点 u 标记为已访问
        queue.append(u)                     # 将起始节点 u 加入队列中
        
        while queue:                        # 队列不为空
            u = queue.popleft()             # 取出队头节点 u
            print(u)                        # 访问节点 u
            for v in graph[u]:              # 遍历节点 u 的所有未访问邻接节点 v
                if v not in visited:        # 节点 v 未被访问
                    visited.add(v)          # 将节点 v 标记为已访问
                    queue.append(v)         # 将节点 v 加入队列中
                

graph = {
    "1": ["2", "3"],
    "2": ["1", "3", "4"],
    "3": ["1", "2", "4", "5"],
    "4": ["2", "3", "5", "6"],
    "5": ["3", "4"],
    "6": ["4", "7"],
    "7": []
}

# 基于队列实现的广度优先搜索
Solution().bfs(graph, "1")
```

## 4. 广度优先搜索应用

### 4.1 克隆图

#### 4.1.1 题目链接

- [133. 克隆图 - 力扣（LeetCode）](https://leetcode.cn/problems/clone-graph/)

#### 4.1.2 题目大意

**描述**：以每个节点的邻接列表形式（二维列表）给定一个无向连通图，其中 $adjList[i]$ 表示值为 $i + 1$ 的节点的邻接列表，$adjList[i][j]$ 表示值为 $i + 1$ 的节点与值为 $adjList[i][j]$ 的节点有一条边。

**要求**：返回该图的深拷贝。

**说明**：

- 节点数不超过 $100$。
- 每个节点值 $Node.val$ 都是唯一的，$1 \le Node.val \le 100$。
- 无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
- 由于图是无向的，如果节点 $p$ 是节点 $q$ 的邻居，那么节点 $q$ 也必须是节点 $p$ 的邻居。
- 图是连通图，你可以从给定节点访问到所有节点。

**示例**：

- 示例 1：

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

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/01/graph-1.png)

```python
输入：adjList = [[2],[1]]
输出：[[2],[1]]
```

#### 4.1.3 解题思路

##### 思路 1：广度优先搜索

1. 使用哈希表 $visited$ 记录原图节点与其克隆节点的映射关系，键为原图节点，值为对应的克隆节点。使用队列 $queue$ 辅助实现广度优先遍历。
2. 首先根据起始节点 $node$ 创建其克隆节点，并加入哈希表：`visited[node] = Node(node.val, [])`，同时将 $node$ 入队：`queue.append(node)`。
3. 当队列不为空时，循环执行以下操作：
   1. 弹出队首节点 $node_u$，遍历其所有邻居 $node_v$。
   2. 如果 $node_v$ 尚未被访问（即不在 $visited$ 中），则为其创建克隆节点，加入哈希表，并入队：`visited[node_v] = Node(node_v.val, [])`，`queue.append(node_v)`。
   3. 将 $node_v$ 的克隆节点加入 $node_u$ 的克隆节点的邻居列表：`visited[node_u].neighbors.append(visited[node_v])`。
4. 队列为空时，广度优先遍历结束，返回起始节点的克隆节点 `visited[node]` 即可。

##### 思路 1：代码

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = dict()
        queue = collections.deque()

        visited[node] = Node(node.val, [])
        queue.append(node)

        while queue:
            node_u = queue.popleft()
            for node_v in node_u.neighbors:
                if node_v not in visited:
                    visited[node_v] = Node(node_v.val, [])
                    queue.append(node_v)
                visited[node_u].neighbors.append(visited[node_v])
        
        return visited[node]
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 为图中节点数量。
- **空间复杂度**：$O(n)$。

### 4.2 岛屿的最大面积

#### 4.2.1 题目链接

- [695. 岛屿的最大面积 - 力扣（LeetCode）](https://leetcode.cn/problems/max-area-of-island/)

#### 4.2.2 题目大意

**描述**：给定一个只包含 $0$、$1$ 元素的二维数组，$1$ 代表岛屿，$0$ 代表水。一座岛的面积就是上下左右相邻的 $1$ 所组成的连通块的数目。

**要求**：计算出最大的岛屿面积。

**说明**：

- $m == grid.length$。
- $n == grid[i].length$。
- $1 \le m, n \le 50$。
- $grid[i][j]$ 为 $0$ 或 $1$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

```python
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
```

- 示例 2：

```python
输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0
```

#### 4.2.3 解题思路

##### 思路 1：广度优先搜索

1. 定义变量 $ans$ 用于记录当前找到的最大岛屿面积。
2. 遍历整个二维数组，对于每个值为 $1$ 的格子：
   1. 将该格子置为 $0$，并将其坐标加入队列 $queue$，同时用 $temp\_ans$ 记录当前岛屿的面积（初始为 1）。
   2. 当队列 $queue$ 非空时，取出队首元素 $(i, j)$，遍历其上下左右四个方向的相邻格子。如果相邻格子为 $1$，则将其置为 $0$（避免重复访问），并加入队列，同时 $temp\_ans$ 加一。
   3. 重复上述过程，直到队列为空，表示当前岛屿已全部遍历完毕。
   4. 用 $ans = \max(ans, temp\_ans)$ 更新最大岛屿面积。
3. 遍历结束后，返回 $ans$ 作为最大岛屿面积。

##### 思路 1：代码

```python
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    temp_ans = 1
                    queue = collections.deque([(i, j)])
                    while queue:
                        i, j = queue.popleft()
                        for direct in directs:
                            new_i = i + direct[0]
                            new_j = j + direct[1]
                            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols or grid[new_i][new_j] == 0:
                                continue
                            grid[new_i][new_j] = 0
                            queue.append((new_i, new_j))
                            temp_ans += 1

                    ans = max(ans, temp_ans)
        return ans
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $m$ 和 $n$ 分别为行数和列数。
- **空间复杂度**：$O(n \times m)$。

## 练习题目

- [0463. 岛屿的周长](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0400-0499/island-perimeter.md)
- [0752. 打开转盘锁](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/open-the-lock.md)
- [0279. 完全平方数](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/perfect-squares.md)
- [0542. 01 矩阵](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0500-0599/01-matrix.md)
- [0322. 零钱兑换](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/coin-change.md)
- [LCR 130. 衣橱整理](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/LCR/ji-qi-ren-de-yun-dong-fan-wei-lcof.md)

- [广度优先搜索题目列表](https://github.com/itcharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2%E9%A2%98%E7%9B%AE)

## 参考资料

- 【文章】[广度优先搜索 - LeetBook - 力扣（LeetCode）](https://leetcode.cn/leetbook/read/bfs/e69rh1/)

