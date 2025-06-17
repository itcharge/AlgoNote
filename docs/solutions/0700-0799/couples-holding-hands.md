# [0765. 情侣牵手](https://leetcode.cn/problems/couples-holding-hands/)

- 标签：贪心、深度优先搜索、广度优先搜索、并查集、图
- 难度：困难

## 题目链接

- [0765. 情侣牵手 - 力扣](https://leetcode.cn/problems/couples-holding-hands/)

## 题目大意

**描述**：$n$ 对情侣坐在连续排列的 $2 \times n$ 个座位上，想要牵对方的手。人和座位用 $0 \sim 2 \times n - 1$ 的整数表示。情侣按顺序编号，第一对是 $(0, 1)$，第二对是 $(2, 3)$，以此类推，最后一对是 $(2 \times n - 2, 2 \times n - 1)$。

给定代表情侣初始座位的数组 `row`，`row[i]` 表示第 `i` 个座位上的人的编号。

**要求**：计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。每一次交换可以选择任意两人，让他们互换座位。

**说明**：

- $2 \times n == row.length$。
- $2 \le n \le 30$。
- $n$ 是偶数。
- $0 \le row[i] < 2 \times n$。
- $row$ 中所有元素均无重复。

**示例**：

- 示例 1：

```python
输入: row = [0,2,1,3]
输出: 1
解释: 只需要交换row[1]和row[2]的位置即可。
```

- 示例 2：

```python
输入: row = [3,2,0,1]
输出: 0
解释: 无需交换座位，所有的情侣都已经可以手牵手了。
```

## 解题思路

### 思路 1：并查集

先观察一下可以直接牵手的情侣特点：

- 编号一定相邻。
- 编号为一个奇数一个偶数。
- 偶数 + 1 = 奇数。

将每对情侣的编号 `(0, 1) (2, 3) (4, 5) ...` 除以 `2` 可以得到 `(0, 0) (1, 1) (2, 2) ...`，这样相同编号就代表是一对情侣。

1. 按照 `2` 个一组的顺序，遍历一下所有编号。
   1. 如果相邻的两人编号除以 `2` 相同，则两人是情侣，将其合并到一个集合中。
   2. 如果相邻的两人编号不同，则将其合并到同一个集合中，而这两个人分别都有各自的对象，所以在后续遍历中两个人各自的对象和他们同组上的另一个人一定都会并到统一集合中，最终形成一个闭环。比如 `(0, 1) (1, 3) (2, 0) (3, 2)`。假设闭环对数为 `k`，最少需要交换 `k  - 1` 次才能让情侣牵手。
2. 假设 `n` 对情侣中有 `m` 个闭环，则 `至少交换次数 = (n1 - 1) + (n2 - 1) + ... + (nn - 1) = n - m`。

### 思路 1：代码

```python
class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.parent[root_x] = root_y
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        size = len(row)
        n = size // 2
        count = n
        union_find = UnionFind(n)
        for i in range(0, size, 2):
            if union_find.union(row[i] // 2, row[i + 1] // 2):
                count -= 1
        return n - count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \alpha(n))$。其中 $n$ 是数组  $row$ 长度，$\alpha$ 是反 `Ackerman` 函数。
- **空间复杂度**：$O(n)$。