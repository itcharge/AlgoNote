# [0834. 树中距离之和](https://leetcode.cn/problems/sum-of-distances-in-tree/)

- 标签：树、深度优先搜索、图、动态规划
- 难度：困难

## 题目链接

- [0834. 树中距离之和 - 力扣](https://leetcode.cn/problems/sum-of-distances-in-tree/)

## 题目大意

**描述**：给定一个无向、连通的树。树中有 $n$ 个标记为 $0 \sim n - 1$ 的节点以及 $n - 1$ 条边 。

给定整数 $n$ 和数组 $edges$，其中 $edges[i] = [ai, bi]$ 表示树中的节点 $ai$ 和 $bi$ 之间有一条边。

**要求**：返回长度为 $n$ 的数组 $answer$，其中 $answer[i]$ 是树中第 $i$ 个节点与所有其他节点之间的距离之和。

**说明**：

- $1 \le n \le 3 \times 10^4$。
- $edges.length == n - 1$。
- $edges[i].length == 2$。
- $0 \le ai, bi < n$。
- $ai \ne bi$。
- 给定的输入保证为有效的树。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)

```python
输入: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释: 树如图所示。
我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg)

```python
输入: n = 2, edges = [[1,0]]
输出: [1,1]
```

## 解题思路

### 思路 1：树形 DP + 二次遍历换根法

最容易想到的做法是：枚举 $n$ 个节点，以每个节点为根节点进行树形 DP。

对于节点 $u$，定义 $dp[u]$ 为：以节点 $u$ 为根节点的树，它的所有子节点到它的距离之和。

然后进行一轮深度优先搜索，在搜索的过程中得到以节点 $v$ 为根节点的树，节点 $v$ 与所有其他子节点之间的距离之和 $dp[v]$。还能得到子树的节点个数 $sizes[v]$。

对于节点 $v$ 来说，其对 $dp[u]$ 的贡献为：节点 $v$ 与所有其他子节点之间的距离之和，再加上需要经过 $u \rightarrow v$ 这条边的节点个数，即 $dp[v] + sizes[v]$。

可得到状态转移方程为：$dp[u] = \sum_{v \in graph[u]}(dp[v] + sizes[v])$。

这样，对于 $n$ 个节点来说，需要进行 $n$ 次树形 DP，这种做法的时间复杂度为 $O(n^2)$，而 $n$ 的范围为 $[1, 3 \times 10^4]$，这样做会导致超时，因此需要进行优化。

我们可以使用「二次遍历换根法」进行优化，从而在 $O(n)$ 的时间复杂度内解决这道题。

以编号为 $0$ 的节点为根节点，进行两次深度优先搜索。

1. 第一次遍历：从编号为 $0$ 的根节点开始，自底向上地计算出节点 $0$ 到其他的距离之和，记录在 $ans[0]$ 中。并且统计出以子节点为根节点的子树节点个数 $sizes[v]$。
2. 第二次遍历：从编号为 $0$ 的根节点开始，自顶向下地枚举每个点，计算出将每个点作为新的根节点时，其他节点到根节点的距离之和。如果当前节点为 $v$，其父节点为 $u$，则自顶向下计算出 $ans[u]$ 之后，我们将根节点从 $u$ 换为节点 $v$，子树上的点到新根节点的距离比原来都小了 $1$，非子树上剩下所有点到新根节点的距离比原来都大了 $1$。则可以据此计算出节点 $v$ 与其他节点的距离和为：$ans[v] = ans[u] + n - 2 \times sizes[u]$。

### 思路 1：代码

```python
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        ans = [0 for _ in range(n)]

        sizes = [1 for _ in range(n)]
        def dfs(u, fa, depth):
            ans[0] += depth
            for v in graph[u]:
                if v == fa:
                    continue
                dfs(v, u, depth + 1)
                sizes[u] += sizes[v]

        def reroot(u, fa):
            for v in graph[u]:
                if v == fa:
                    continue
                ans[v] = ans[u] + n - 2 * size[v]
                reroot(v, u)

        dfs(0, -1, 0)
        reroot(0, -1)
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为树的节点个数。
- **空间复杂度**：$O(n)$。

