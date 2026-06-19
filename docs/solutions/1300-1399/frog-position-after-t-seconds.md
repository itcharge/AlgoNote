# [1377. T 秒后青蛙的位置](https://leetcode.cn/problems/frog-position-after-t-seconds/)

- 标签：树、深度优先搜索、广度优先搜索、图
- 难度：困难

## 题目链接

- [1377. T 秒后青蛙的位置 - 力扣](https://leetcode.cn/problems/frog-position-after-t-seconds/)

## 题目大意

**描述**：给定一棵树（编号 $1$ 到 $n$），青蛙从 $1$ 号节点开始，每秒等概率跳到一个相邻的未访问过的节点，或者停在原地。给定目标节点 $target$ 和时间 $t$。

**要求**：返回 $t$ 秒后青蛙在 $target$ 的概率。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/12/21/frog1.jpg)

```python
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
输出：0.16666666666666666 
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有 1/2 的概率跳到顶点 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/12/21/frog2.jpg)

```python
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
输出：0.3333333333333333
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳到顶点 7 。
```


## 解题思路

### 思路 1：DFS 概率传播

#### 1. 核心思想

从根节点 DFS，记录到达每个节点的概率和时间。如果到达 $target$，根据剩余时间计算最终概率：
- 如果正好在 $t$ 秒到达，返回概率。
- 如果 $t$ 秒内到达且还有剩余时间，如果该节点有子节点，概率为 $0$（青蛙必须继续跳）；否则可以停在原地，概率不变。

#### 2. 具体步骤

**第 1 步**：建图（双向）。

**第 2 步**：DFS 从 $1$ 开始，带父节点防止回溯。

**第 3 步**：计算概率并处理时间条件。

### 思路 1：代码

```python
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, parent, time, prob):
            if time > t:
                return 0.0
            if node == target and time == t:
                return prob
            if node == target:
                # 如果 target 有子节点（非叶节点），概率为 0
                children = [c for c in g[node] if c != parent]
                if children:
                    return 0.0
                return prob

            children = [c for c in g[node] if c != parent]
            if not children:
                return 0.0

            res = 0.0
            for child in children:
                res += dfs(child, node, time + 1, prob / len(children))
            return res

        return dfs(1, -1, 0, 1.0)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
