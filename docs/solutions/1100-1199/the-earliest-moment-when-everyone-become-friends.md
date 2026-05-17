# [1101. 彼此熟识的最早时间](https://leetcode.cn/problems/the-earliest-moment-when-everyone-become-friends/)

- 标签：并查集、数组、排序
- 难度：中等

## 题目链接

- [1101. 彼此熟识的最早时间 - 力扣](https://leetcode.cn/problems/the-earliest-moment-when-everyone-become-friends/)

## 题目大意

**描述**：在一个社交圈子里，有 $n$ 个人（编号 $0$ 到 $n-1$）。给定一份日志列表 $logs$，$logs[i] = [timestamp_i, x_i, y_i]$ 表示在 $timestamp_i$ 时刻，$x_i$ 和 $y_i$ 成为朋友。友谊是相互的，并且可以传递（朋友的朋友也是朋友）。

**要求**：返回所有人之间都互相认识的最早时间。如果不可能，返回 $-1$。

**说明**：

- $2 \le n \le 10^3$。
- $1 \le logs.length \le 10^4$。
- 所有时间戳均不相同。

**示例**：

- 示例 1：

```python
输入：logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
输出：20190301
```

- 示例 2：

```python
输入：logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
输出：3
```

## 解题思路

### 思路 1：并查集

**拆解步骤**：

1. **按时间排序**：把 $logs$ 按时间戳从小到大排序，模拟时间流逝。

2. **初始化并查集**：一开始每个人自己是一个连通分量，共 $n$ 个分量。

3. **按时间顺序处理每条日志**：
   - 合并 $x_i$ 和 $y_i$ 所在的分量
   - 如果合并成功（两个分量原来不连通），连通分量数减 $1$
   - 检查当前连通分量数是否为 $1$
   - 如果是，返回当前时间戳

4. **处理完所有日志后仍未全部连通**，返回 $-1$。

### 思路 1：代码

```python
class UnionFind:
    """并查集，用来快速判断和合并社交圈子"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n  # 当前连通分量的个数

    def find(self, x):
        # 找组长的组长……直到找到根节点（路径压缩加速后续查找）
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 合并两个人的圈子，如果本来就在一起，返回 False
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[px] = py
        self.count -= 1  # 合并后连通分量减少一个
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # 按时间戳从小到大排序
        logs.sort(key=lambda x: x[0])

        uf = UnionFind(n)

        for timestamp, x, y in logs:
            uf.union(x, y)
            # 如果只剩下一个连通分量，说明所有人都认识了
            if uf.count == 1:
                return timestamp

        # 所有日志处理完还没全部连通
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \log m + m \alpha(n))$。用人话说就是：排序需要花 $m \log m$ 时间（$m$ 是日志数量），然后处理每条日志时并查集的操作几乎是常数时间。
- **空间复杂度**：$O(n)$。并查集需要存储 $n$ 个人的父节点信息。
