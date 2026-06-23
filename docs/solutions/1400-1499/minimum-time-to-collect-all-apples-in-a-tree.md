# [1443. 收集树上所有苹果的最少时间](https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree/)

- 标签：树、深度优先搜索、图、哈希表
- 难度：中等

## 题目链接

- [1443. 收集树上所有苹果的最少时间 - 力扣](https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree/)

## 题目大意

**描述**：给定一棵树，节点编号 $0 \sim n-1$，$parent[i]$ 表示节点 $i$ 的父节点（$parent[0] = -1$）。给定 $hasApple$ 数组，$hasApple[i] = True$ 表示节点 $i$ 有苹果。

从根节点 $0$ 出发，每次移动一条边需要 $1$ 秒。收集完所有苹果后返回根节点。

**要求**：返回收集所有苹果所需的最少时间。

**说明**：
- $1 \le n \le 10^5$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_1.png)

```python
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
输出：8 
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_2.png)

```python
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
输出：6
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
```

## 解题思路

### 思路 1：DFS

#### 1. 核心思想

从根节点开始 DFS。对于每个节点，递归处理其子树。如果子树中有苹果（或子树需要经过），则从当前节点走向子节点需要 $2$ 秒（来回）。

后序遍历，每个节点返回「从该节点出发，收集完其子树的所有苹果并回到该节点所需的时间」。

#### 2. 具体步骤

**第 1 步**：建图（邻接表）。

**第 2 步**：定义 DFS 函数 $dfs(u, parent)$：
- 初始化 $total\_time = 0$。
- 遍历 $u$ 的子节点 $v$：
  - $child\_time = dfs(v, u)$。
  - 如果 $child\_time > 0$ 或 $hasApple[v]$（子树有苹果），$total\_time += child\_time + 2$（去和回的 $2$ 秒）。
- 返回 $total\_time$。

**第 3 步**：返回 $dfs(0, -1)$。

#### 3. 举例说明

以 $n=7$，$parent=[-1,0,0,1,1,2,2]$，$hasApple=[False,False,True,False,True,True,False]$ 为例：

```
    0
   / \
  1   2
 / \ / \
3  4 5 6
    T T T
```

DFS：
- 节点 3：无子节点，无苹果 → 0
- 节点 4：无子节点，有苹果 → 0（但 $hasApple[4]=True$，在父节点 1 处会 $+2$）
- 节点 1：子节点 3 无，子节点 4 有苹果 → $0 + 2 = 2$
- 节点 5：无子，有苹果 → 0（在父节点 2 处 +2）
- 节点 6：无子，无苹果 → 0
- 节点 2：子节点 5 有苹果 → $0+2=2$
- 节点 0：子节点 1 需要走（$2$），子节点 2 需要走（$2$）→ $2+2=4$

总时间 = $4$ 秒。

### 思路 1：代码

```python
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, parent):
            total = 0
            for v in graph[u]:
                if v == parent:
                    continue
                child_time = dfs(v, u)
                if child_time > 0 or hasApple[v]:
                    total += child_time + 2
            return total

        return dfs(0, -1)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个节点遍历一次。
- **空间复杂度**：$O(n)$，邻接表和递归栈。
