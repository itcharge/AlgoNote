# [1202. 交换字符串中的元素](https://leetcode.cn/problems/smallest-string-with-swaps/)

- 标签：深度优先搜索、广度优先搜索、并查集、哈希表、字符串
- 难度：中等

## 题目链接

- [1202. 交换字符串中的元素 - 力扣](https://leetcode.cn/problems/smallest-string-with-swaps/)

## 题目大意

**描述**：给定一个字符串 `s`，再给定一个数组 `pairs`，其中 `pairs[i] = [a, b]` 表示字符串的第 `a` 个字符可以跟第 `b` 个字符交换。只要满足 `pairs` 中的交换关系，可以任意多次交换字符串中的字符。

**要求**：返回 `s` 经过若干次交换之后，可以变成的字典序最小的字符串。

**说明**：

- $1 \le s.length \le 10^5$。
- $0 \le pairs.length \le 10^5$。
- $0 \le pairs[i][0], pairs[i][1] < s.length$。
- `s` 中只含有小写英文字母。

**示例**：

- 示例 1：

```python
输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释： 
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
```

- 示例 2：

```python
输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
```

## 解题思路

### 思路 1：并查集

如果第 `a` 个字符可以跟第 `b` 个字符交换，第 `b` 个字符可以跟第 `c` 个字符交换，那么第 `a` 个字符、第 `b` 个字符、第 `c` 个字符之间就可以相互交换。我们可以把可以相互交换的「位置」都放入一个集合中。然后对每个集合中的字符进行排序。然后将其放置回在字符串中原有位置即可。

### 思路 1：代码

```python
import collections

class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = len(s)
        union_find = UnionFind(size)
        for pair in pairs:
            union_find.union(pair[0], pair[1])
        mp = collections.defaultdict(list)

        for i, ch in enumerate(s):
            mp[union_find.find(i)].append(ch)

        for vec in mp.values():
            vec.sort(reverse=True)

        ans = []
        for i in range(size):
            x = union_find.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()

        return "".join(ans)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log_2 n + m * \alpha(n))$。其中 $n$ 是字符串的长度，$m$ 为 $pairs$ 的索引对数量，$\alpha$ 是反 `Ackerman` 函数。
- **空间复杂度**：$O(n)$。