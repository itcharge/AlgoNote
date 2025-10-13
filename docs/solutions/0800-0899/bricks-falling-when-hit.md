# [0803. 打砖块](https://leetcode.cn/problems/bricks-falling-when-hit/)

- 标签：并查集、数组、矩阵
- 难度：困难

## 题目链接

- [0803. 打砖块 - 力扣](https://leetcode.cn/problems/bricks-falling-when-hit/)

## 题目大意

**描述**：给定一个 $m \times n$ 大小的二元网格，其中 $1$ 表示砖块，$0$ 表示空白。砖块稳定（不会掉落）的前提是：

- 一块砖直接连接到网格的顶部。
- 或者至少有一块相邻（4 个方向之一）砖块稳定不会掉落时。

再给定一个数组 $hits$，这是需要依次消除砖块的位置。每当消除 $hits[i] = (row_i, col_i)$ 位置上的砖块时，对应位置的砖块（如果存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

**要求**：返回一个数组 $result$，其中 $result[i]$ 表示第 $i$ 次消除操作对应掉落的砖块数目。

**说明**：

- 消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。
- $m == grid.length$。
- $n == grid[i].length$。
- $1 \le m, n \le 200$。
- $grid[i][j]$ 为 $0$ 或 $1$。
- $1 \le hits.length \le 4 \times 10^4$。
- $hits[i].length == 2$。
- $0 \le xi \le m - 1$。
- $0 \le yi \le n - 1$。
- 所有 $(xi, yi)$ 互不相同。

**示例**：

- 示例 1：

```python
输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
输出：[2]
解释：网格开始为：
[[1,0,0,0]，
 [1,1,1,0]]
消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0]
 [0,1,1,0]]
两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
[[1,0,0,0],
 [0,0,0,0]]
因此，结果为 [2]。
```

- 示例 2：

```python
输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
输出：[0,0]
解释：网格开始为：
[[1,0,0,0],
 [1,1,0,0]]
消除 (1,1) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [1,0,0,0]]
剩下的砖都很稳定，所以不会掉落。网格保持不变：
[[1,0,0,0], 
 [1,0,0,0]]
接下来消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [0,0,0,0]]
剩下的砖块仍然是稳定的，所以不会有砖块掉落。
因此，结果为 [0,0]。
```

## 解题思路

### 思路 1：并查集

一个很直观的想法：

- 将所有砖块放入一个集合中。
- 根据 $hits$ 数组的顺序，每敲掉一块砖。则将这块砖与相邻（4 个方向）的砖块断开集合。
- 然后判断哪些砖块会掉落，从集合中删除会掉落的砖块，并统计掉落砖块的数量。
  - **掉落砖块的数目 = 击碎砖块之前与屋顶相连的砖块数目 - 击碎砖块之后与屋顶相连的砖块数目 - 1**。

涉及集合问题，很容易想到用并查集来做。但是并查集主要用于合并查找集合，不适合断开集合。我们可以反向思考问题：

- 先将 $hits$ 中的所有位置上的砖块敲掉。
- 将剩下的砖块建立并查集。
- 逆序填回被敲掉的砖块，并与相邻（4 个方向）的砖块合并。这样问题就变为了 **补上砖块会新增多少个砖块粘到屋顶**。

整个算法步骤具体如下：

1. 先将二维数组 $grid$ 复制一份到二维数组 $copy\_gird$ 上。这是因为遍历 $hits$ 元素时需要判断原网格是空白还是被打碎的砖块。
2. 在 $copy\_grid$ 中将 $hits$ 中打碎的砖块赋值为 $0$。
3. 建立并查集，将房顶上的砖块合并到一个集合中。
4. 逆序遍历 $hits$，将 $hits$ 中的砖块补到 $copy\_grid$ 中，并计算每一步中有多少个砖块粘到屋顶上（与屋顶砖块在一个集合中），并存入答案数组对应位置。
5. 最后输出答案数组。

### 思路 1：代码

```python
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

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
        self.size[root_y] += self.size[root_x]
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        root_x = self.find(x)
        return self.size[root_x]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        rows, cols = len(grid), len(grid[0])

        def is_area(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def get_index(x, y):
            return x * cols + y

        copy_grid = [[grid[i][j] for j in range(cols)] for i in range(rows)]

        for hit in hits:
            copy_grid[hit[0]][hit[1]] = 0

        union_find = UnionFind(rows * cols + 1)

        for j in range(cols):
            if copy_grid[0][j] == 1:
                union_find.union(j, rows * cols)

        for i in range(1, rows):
            for j in range(cols):
                if copy_grid[i][j] == 1:
                    if copy_grid[i - 1][j] == 1:
                        union_find.union(get_index(i - 1, j), get_index(i, j))
                    if j > 0 and copy_grid[i][j - 1] == 1:
                        union_find.union(get_index(i, j - 1), get_index(i, j))

        size_hits = len(hits)
        res = [0 for _ in range(size_hits)]
        for i in range(size_hits - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]
            if grid[x][y] == 0:
                continue
            origin = union_find.get_size(rows * cols)
            if x == 0:
                union_find.union(y, rows * cols)
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if is_area(new_x, new_y) and copy_grid[new_x][new_y] == 1:
                    union_find.union(get_index(x, y), get_index(new_x, new_y))
            curr = union_find.get_size(rows * cols)
            res[i] = max(0, curr - origin - 1)
            copy_grid[x][y] = 1
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n \times \alpha(m \times n))$，其中 $\alpha$ 是反 Ackerman 函数。
- **空间复杂度**：$O(m \times n)$。

