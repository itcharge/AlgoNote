# [1617. 统计子树中城市之间最大距离](https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/)

- 标签：位运算、树、动态规划、状态压缩、枚举
- 难度：困难

## 题目链接

- [1617. 统计子树中城市之间最大距离 - 力扣](https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/)

## 题目大意

**描述**：给定一个整数 $n$，代表 $n$ 个城市，城市编号为 $1 \sim n$。同时给定一个大小为 $n - 1$ 的数组 $edges$，其中 $edges[i] = [u_i, v_i]$ 表示城市 $u_i$ 和 $v_i$ 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵树。

**要求**：返回一个大小为 $n - 1$ 的数组，其中第 $i$ 个元素（下标从 $1$ 开始）是城市间距离恰好等于 $i$ 的子树数目。

**说明**：

- **两个城市间距离**：定义为它们之间需要经过的边的数目。
- **一棵子树**：城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。
- $2 \le n \le 15$。
- $edges.length == n - 1$。
- $edges[i].length == 2$。
- $1 \le u_i, v_i \le n$。
- 题目保证 $(ui, vi)$ 所表示的边互不相同。

**示例**：

- 示例 1：

```python
输入：n = 4, edges = [[1,2],[2,3],[2,4]]
输出：[3,4,0]
解释：
子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
不存在城市间最大距离为 3 的子树。
```

- 示例 2：

```python
输入：n = 2, edges = [[1,2]]
输出：[1]
```

## 解题思路

### 思路 1：树形 DP + 深度优先搜索

因为题目中给定 $n$ 的范围为 $2 \le n \le 15$，范围比较小，我们可以通过类似「[0078. 子集](https://leetcode.cn/problems/subsets/)」中二进制枚举的方式，得到所有子树的子集。

而对于一个确定的子树来说，求子树中两个城市间距离就是在求子树的直径，这就跟 [「1245. 树的直径」](https://leetcode.cn/problems/tree-diameter/) 和 [「2246. 相邻字符不同的最长路径」](https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/) 一样了。

那么这道题的思路就变成了：

1. 通过二进制枚举的方式，得到所有子树。
2. 对于当前子树，通过树形 DP + 深度优先搜索的方式，计算出当前子树的直径。
3. 统计所有子树直径中经过的不同边数个数，将其放入答案数组中。

### 思路 1：代码

```python
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]                              # 建图
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        def dfs(mask, u):
            nonlocal visited, diameter
            visited |= 1 << u                                       # 标记 u 访问过
            u_len = 0                                               # u 节点的最大路径长度
            for v in graph[u]:                                      # 遍历 u 节点的相邻节点
                if (visited >> v) & 1 == 0 and mask >> v & 1:       # v 没有访问过，且在子集中
                    v_len = dfs(mask, v)                            # 相邻节点的最大路径长度
                    diameter = max(diameter, u_len + v_len + 1)     # 维护最大路径长度
                    u_len = max(u_len, v_len + 1)                   # 更新 u 节点的最大路径长度
            return u_len
        
        ans = [0 for _ in range(n - 1)]

        for mask in range(3, 1 << n):                               # 二进制枚举子集
            if mask & (mask - 1) == 0:                              # 子集至少需要两个点
                continue
            visited = 0
            diameter = 0
            u = mask.bit_length() - 1        
            dfs(mask, u)                                            # 在子集 mask 中递归求树的直径
            if visited == mask:
                ans[diameter - 1] += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times 2^n)$，其中 $n$ 为给定的城市数目。
- **空间复杂度**：$O(n)$。
