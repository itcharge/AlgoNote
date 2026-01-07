# [0815. 公交路线](https://leetcode.cn/problems/bus-routes/)

- 标签：广度优先搜索、数组、哈希表
- 难度：困难

## 题目链接

- [0815. 公交路线 - 力扣](https://leetcode.cn/problems/bus-routes/)

## 题目大意

**描述**：

给定一个数组 $routes$ ，表示一系列公交线路，其中每个 $routes[i]$ 表示一条公交线路，第 $i$ 辆公交车将会在上面循环行驶。

- 例如，路线 $routes[0] = [1, 5, 7]$ 表示第 0 辆公交车会一直按序列 $1 \rightarrow 5 \rightarrow 7 \rightarrow 1 \rightarrow 5 \rightarrow 7 \rightarrow 1 \rightarrow ...$ 这样的车站路线行驶。

现在从 $source$ 车站出发（初始时不在公交车上），要前往 $target$ 车站。 期间仅可乘坐公交车。

**要求**：

求出「最少乘坐的公交车数量」。如果不可能到达终点车站，返回 $-1$。

**说明**：

- $1 \le routes.length \le 500.$。
- $1 \le routes[i].length \le 10^{5}$。
- $routes[i]$ 中的所有值互不相同。
- $sum(routes[i].length) \le 10^{5}$。
- $0 \le routes[i][j] \lt 10^{6}$。
- $0 \le source, target \lt 10^{6}$。

**示例**：

- 示例 1：

```python
输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
输出：2
解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
```

- 示例 2：

```python
输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
输出：-1
```

## 解题思路

### 思路 1：BFS（广度优先搜索）

这道题要求找到从起点到终点的最少乘坐公交车数量。可以将问题转化为图的最短路径问题：

- 每个公交站是一个节点。
- 如果两个站在同一条公交线路上，它们之间有边相连。

但直接建图会导致边数过多。更好的方法是：

- 将公交线路作为节点。
- 从起点站开始，找到所有经过该站的公交线路。
- 对于每条线路，找到该线路上的所有站点，再找到这些站点对应的其他线路。
- 使用 BFS 搜索最短路径。

算法步骤：

1. 如果起点等于终点，返回 0。
2. 建立站点到公交线路的映射。
3. 使用 BFS，从起点站开始：
   - 找到所有经过该站的公交线路。
   - 对于每条线路，遍历该线路上的所有站点。
   - 如果到达终点站，返回当前乘坐的公交车数量。
   - 否则，将新站点加入队列。
4. 使用 $\text{visited}$ 集合记录已访问的线路和站点，避免重复访问。

### 思路 1：代码

```python
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        from collections import defaultdict, deque
        
        # 如果起点等于终点，直接返回 0
        if source == target:
            return 0
        
        # 建立站点到公交线路的映射
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        # BFS
        queue = deque([source])
        visited_stops = {source}
        visited_routes = set()
        buses = 0
        
        while queue:
            buses += 1
            
            # 遍历当前层的所有站点
            for _ in range(len(queue)):
                stop = queue.popleft()
                
                # 找到所有经过该站的公交线路
                for route_idx in stop_to_routes[stop]:
                    # 如果该线路已访问，跳过
                    if route_idx in visited_routes:
                        continue
                    visited_routes.add(route_idx)
                    
                    # 遍历该线路上的所有站点
                    for next_stop in routes[route_idx]:
                        # 如果到达终点，返回结果
                        if next_stop == target:
                            return buses
                        
                        # 如果该站点未访问，加入队列
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)
        
        # 无法到达终点
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(N \times S)$，其中 $N$ 是公交线路的数量，$S$ 是每条线路的平均站点数。每条线路最多被访问一次，每次访问需要遍历该线路上的所有站点。
- **空间复杂度**：$O(N \times S)$，需要存储站点到线路的映射和 BFS 队列。
