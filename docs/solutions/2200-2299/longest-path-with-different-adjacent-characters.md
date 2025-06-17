# [2246. 相邻字符不同的最长路径](https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/)

- 标签：树、深度优先搜索、图、拓扑排序、数组、字符串
- 难度：困难

## 题目链接

- [2246. 相邻字符不同的最长路径 - 力扣](https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/)

## 题目大意

**描述**：给定一个长度为 $n$ 的数组 $parent$ 来表示一棵树（即一个连通、无向、无环图）。该树的节点编号为 $0 \sim n - 1$，共 $n$ 个节点，其中根节点的编号为 $0$。其中 $parent[i]$ 表示节点 $i$ 的父节点，由于节点 $0$ 是根节点，所以 $parent[0] == -1$。再给定一个长度为 $n$ 的字符串，其中 $s[i]$ 表示分配给节点 $i$ 的字符。

**要求**：找出路径上任意一对相邻节点都没有分配到相同字符的最长路径，并返回该路径的长度。

**说明**：

- $n == parent.length == s.length$。
- $1 \le n \le 10^5$。
- 对所有 $i \ge 1$ ，$0 \le parent[i] \le n - 1$ 均成立。
- $parent[0] == -1$。
- $parent$ 表示一棵有效的树。
- $s$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2022/03/25/testingdrawio.png)

```python
输入：parent = [-1,0,0,1,1,2], s = "abacbe"
输出：3
解释：任意一对相邻节点字符都不同的最长路径是：0 -> 1 -> 3 。该路径的长度是 3 ，所以返回 3。
可以证明不存在满足上述条件且比 3 更长的路径。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2022/03/25/graph2drawio.png)

```python
输入：parent = [-1,0,0,0], s = "aabc"
输出：3
解释：任意一对相邻节点字符都不同的最长路径是：2 -> 0 -> 3 。该路径的长度为 3 ，所以返回 3。
```

## 解题思路

### 思路 1：树形 DP + 深度优先搜索

因为题目给定的是表示父子节点的 $parent$  数组，为了方便递归遍历相邻节点，我们可以根据 $partent$ 数组，建立一个由父节点指向子节点的有向图 $graph$。

如果不考虑相邻节点是否为相同字符这一条件，那么这道题就是在求树的直径（树的最长路径长度）中的节点个数。

对于根节点为 $u$ 的树来说：

1. 如果其最长路径经过根节点 $u$，则 **最长路径长度 = 某子树中的最长路径长度 + 另一子树中的最长路径长度 + 1**。
2. 如果其最长路径不经过根节点 $u$，则 **最长路径长度 = 某个子树中的最长路径长度**。

即：**最长路径长度 = max(某子树中的最长路径长度 + 另一子树中的最长路径长度 + 1，某个子树中的最长路径长度)**。

对此，我们可以使用深度优先搜索递归遍历 $u$ 的所有相邻节点 $v$，并在递归遍历的同时，维护一个全局最大路径和变量 $ans$，以及当前节点 $u$ 的最大路径长度变量 $u\underline{\hspace{0.5em}}len$。

1. 先计算出从相邻节点 $v$ 出发的最长路径长度 $v\underline{\hspace{0.5em}}len$。
2. 更新维护全局最长路径长度为 $self.ans = max(self.ans, \quad u\underline{\hspace{0.5em}}len + v\underline{\hspace{0.5em}}len + 1)$。
3. 更新维护当前节点 $u$ 的最长路径长度为 $u\underline{\hspace{0.5em}}len = max(u\underline{\hspace{0.5em}}len, \quad v\underline{\hspace{0.5em}}len + 1)$。

因为题目限定了「相邻节点字符不同」，所以在更新全局最长路径长度和当前节点 $u$ 的最长路径长度时，我们需要判断一下节点 $u$ 与相邻节点 $v$ 的字符是否相同，只有在字符不同的条件下，才能够更新维护。

最后，因为题目要求的是树的直径（树的最长路径长度）中的节点个数，而：**路径的节点 = 路径长度 + 1**，所以最后我们返回 $self.ans + 1$ 作为答案。

### 思路 1：代码

```python
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        size = len(parent)

        # 根据 parent 数组，建立有向图
        graph = [[] for _ in range(size)]
        for i in range(1, size):
            graph[parent[i]].append(i)

        ans = 0
        def dfs(u):
            nonlocal ans
            u_len = 0                                   # u 节点的最大路径长度
            for v in graph[u]:                          # 遍历 u 节点的相邻节点
                v_len = dfs(v)                          # 相邻节点的最大路径长度
                if s[u] != s[v]:                        # 相邻节点字符不同
                    ans = max(ans, u_len + v_len + 1)   # 维护最大路径长度
                    u_len = max(u_len, v_len + 1)       # 更新 u 节点的最大路径长度
            return u_len                                # 返回 u 节点的最大路径长度

        dfs(0)
        return ans + 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是树的节点数目。
- **空间复杂度**：$O(n)$。
