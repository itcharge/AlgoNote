# [1466. 重新规划路线](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

- 标签：深度优先搜索、广度优先搜索、图
- 难度：中等

## 题目链接

- [1466. 重新规划路线 - 力扣](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

## 题目大意

**描述**：给定 $n$ 座城市（编号 $0 \sim n-1$），和 $n-1$ 条有向边 $connections[i] = [a, b]$，表示从 $a$ 到 $b$ 的一条单向道路。

**要求**：返回最少需要改变方向的边数，使得所有道路都指向城市 $0$（所有城市都能到达 $0$）。

**说明**：
- $2 \le n \le 5 \times 10^4$。
- $connections$ 构成一棵树。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/30/sample_1_1819.png)

```python
输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/30/sample_2_1819.png)

```python
输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
```

## 解题思路

### 思路 1：DFS 或 BFS

#### 1. 核心思想

由于图是一棵树，从 $0$ 出发 BFS/DFS。对于每条边，如果是正向（从 $0$ 向外），则需要反转。如果是反向（指向 $0$），则不需要。

具体做法：将图视为无向图，从 $0$ 开始遍历，如果遇到的是原始图中的方向（$a \to b$），且需要从 $0$ 走向方向箭头的尾部→头部，则说明这条边的方向不对，需要反转计数。

更简洁：建双向图并标记原始方向。从 $0$ 开始 BFS，如果从一个节点沿着原始方向的出边走到邻居，则该边需要反转。

#### 2. 具体步骤

**第 1 步**：建图。对每条边 $[a, b]$，加入两条边：
- $a \to b$ 标记为正向（$1$）。
- $b \to a$ 标记为反向（$0$）。

**第 2 步**：从 $0$ 开始 BFS/DFS：
- 遍历邻居时，如果边标记为 $1$（原始方向是远离 $0$ 的方向），$count++$。
- 标记已访问。

**第 3 步**：返回 $count$。

#### 3. 举例说明

以 $n=6, connections=[[0,1],[1,3],[2,3],[4,0],[4,5]]$ 为例：

```
0 → 1 → 3 ← 2
↑
4 → 5
```

从 $0$ BFS：
- $0$ 的邻居：$1$（正向出→计数+1），$4$（反向入←不计数）
- $1$ 的邻居：$3$（正向出→计数+1）
- $4$ 的邻居：$0$（已访问），$5$（正向出→计数+1）

总计数 = $3$。

### 思路 1：代码

```python
from collections import deque, defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, 1))   # 正向：需要反转才指向 0
            graph[b].append((a, 0))   # 反向：指向 0 的方向

        q = deque([0])
        visited = {0}
        count = 0

        while q:
            u = q.popleft()
            for v, direction in graph[u]:
                if v not in visited:
                    visited.add(v)
                    if direction == 1:  # 正向边 = 需要反转
                        count += 1
                    q.append(v)

        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个节点访问一次。
- **空间复杂度**：$O(n)$，邻接表和队列。
