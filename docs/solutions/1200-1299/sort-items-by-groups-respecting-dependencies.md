# [1203. 项目管理](https://leetcode.cn/problems/sort-items-by-groups-respecting-dependencies/)

- 标签：深度优先搜索、广度优先搜索、图、拓扑排序
- 难度：困难

## 题目链接

- [1203. 项目管理 - 力扣](https://leetcode.cn/problems/sort-items-by-groups-respecting-dependencies/)

## 题目大意

**描述**：有 $n$ 个项目（编号 $0$ 到 $n-1$）和 $m$ 个小组（编号 $0$ 到 $m-1$）。每个项目可能属于某个小组，也可能不属于任何小组（记为 $-1$）。项目之间存在依赖关系：$beforeItems[i]$ 是一个列表，表示完成项目 $i$ 之前需要先完成的项目。

**要求**：给出一个排序结果，使得：
1. 同一个小组的项目在结果中相邻排列。
2. 项目之间的依赖关系得到满足（如果 $a$ 在 $beforeItems[b]$ 中，则 $a$ 必须排在 $b$ 之前）。

如果无法满足，返回空列表。

**说明**：

- $1 \le m \le n \le 3 \times 10^{4}$。

**示例**：

- 示例 1：

```python
输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
输出：[6,3,4,1,5,2,0,7]
解释：一种可能的排序为 [6,3,4,1,5,2,0,7]。
```

## 解题思路

### 思路 1：拓扑排序（双重排序）

#### 1. 核心思想

这道题有两个维度的排序要求：
1. **组间排序**：不同小组的项目之间，如果存在跨组依赖，需要确定组的先后顺序。
2. **组内排序**：同一小组的项目内部，需要按依赖关系排序。

这需要用到**拓扑排序**，而且是**两层拓扑排序**：

第一层：对"组"做拓扑排序。
第二层：对每个组内部的"项目"做拓扑排序。

#### 2. 建图、遍历、标记、收集

**建图**：

1. 给没有小组的项目分配虚拟组（从 $m$ 开始递增）。
2. 构建**组间依赖图**：如果项目 $a$（属于组 $g_a$）依赖项目 $b$（属于组 $g_b$）且 $g_a \ne g_b$，则 $g_b \to g_a$ 有一条边。
3. 构建**组内依赖图**：如果项目 $a$ 和项目 $b$ 属于同一个组，且 $a$ 依赖 $b$，则在组内图中加边 $b \to a$。

**遍历与标记**：

1. 对组间图做拓扑排序，得到组的顺序。
2. 对每个组内部的图做拓扑排序，得到组内项目的顺序。

**收集**：按组的顺序将各组的内部排序结果拼接起来。

**合法性**：如果任何一次拓扑排序发现环（排序结果长度不等于节点数），则无法满足需求，返回空列表。

#### 3. 具体步骤

**第 1 步**：给没有小组的项目分配虚拟组 ID。将 $group[i] = -1$ 的项目赋值为 $m, m+1, \dots$，并更新 $m$。

**第 2 步**：构建组间图 $group\_graph$ 和组内图 $inner\_graph$（每个组一个图）。

**第 3 步**：对组间图做拓扑排序。

**第 4 步**：对每个组做拓扑排序。

**第 5 步**：按组间顺序拼接组内排序结果。

#### 4. 拓扑排序模板

```python
def topological_sort(graph, nodes):
    in_deg = {node: 0 for node in nodes}
    for u in graph:
        for v in graph[u]:
            in_deg[v] = in_deg.get(v, 0) + 1
    queue = [node for node in nodes if in_deg[node] == 0]
    result = []
    while queue:
        u = queue.pop(0)
        result.append(u)
        for v in graph[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
    return result if len(result) == len(nodes) else []
```

### 思路 1：代码

```python
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 1. 给没有小组的项目分配虚拟组
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # 2. 建图
        group_graph = defaultdict(list)      # 组间依赖图
        inner_graph = [defaultdict(list) for _ in range(m)]  # 每个组的内部图
        group_in_deg = [0] * m
        inner_in_deg = [defaultdict(int) for _ in range(m)]

        # 组内节点集合
        group_nodes = [set() for _ in range(m)]
        for i in range(n):
            group_nodes[group[i]].add(i)

        for i in range(n):
            gi = group[i]
            for pre in beforeItems[i]:
                gp = group[pre]
                if gi == gp:
                    # 同组依赖：加入组内图
                    inner_graph[gi][pre].append(i)
                    inner_in_deg[gi][i] = inner_in_deg[gi].get(i, 0) + 1
                else:
                    # 跨组依赖：加入组间图
                    group_graph[gp].append(gi)
                    group_in_deg[gi] += 1

        # 3. 组间拓扑排序
        group_queue = deque([g for g in range(m) if group_in_deg[g] == 0])
        group_order = []
        while group_queue:
            g = group_queue.popleft()
            group_order.append(g)
            for ng in group_graph[g]:
                group_in_deg[ng] -= 1
                if group_in_deg[ng] == 0:
                    group_queue.append(ng)
        if len(group_order) != m:
            return []  # 组间有环

        # 4. 组内拓扑排序
        ans = []
        for g in group_order:
            # 对组 g 做拓扑排序
            q = deque([node for node in group_nodes[g] if inner_in_deg[g].get(node, 0) == 0])
            inner_order = []
            while q:
                node = q.popleft()
                inner_order.append(node)
                for nxt in inner_graph[g][node]:
                    inner_in_deg[g][nxt] -= 1
                    if inner_in_deg[g][nxt] == 0:
                        q.append(nxt)
            if len(inner_order) != len(group_nodes[g]):
                return []  # 组内有环
            ans.extend(inner_order)

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m + E)$，其中 $E$ 是总的依赖边数。建图和两次拓扑排序都需要线性时间。
- **空间复杂度**：$O(n + m + E)$，存储各种图结构。
