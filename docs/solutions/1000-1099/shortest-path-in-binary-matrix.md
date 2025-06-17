# [1091. 二进制矩阵中的最短路径](https://leetcode.cn/problems/shortest-path-in-binary-matrix/)

- 标签：广度优先搜索、数组、矩阵
- 难度：中等

## 题目链接

- [1091. 二进制矩阵中的最短路径 - 力扣](https://leetcode.cn/problems/shortest-path-in-binary-matrix/)

## 题目大意

给定一个 `n * n` 的二进制矩阵 `grid`。 `grid` 中只含有 `0` 或者 `1`。`grid` 中的畅通路径是一条从左上角 `(0, 0)` 位置上到右下角 `(n - 1, n - 1)`位置上的路径。该路径同时满足以下要求：

- 路径途径的所有单元格的值都是 `0`。
- 路径中所有相邻的单元格应该在 `8` 个方向之一上连通（即相邻两单元格之间彼此不同且共享一条边或者一个角）。
- 畅通路径的长度是该路径途径的单元格总数。

要求：计算出矩阵中最短畅通路径的长度。如果不存在这样的路径，返回 `-1`。

## 解题思路

使用广度优先搜索查找最短路径。具体做法如下：

1. 使用队列 `queue` 存放当前节点位置，使用 set 集合 `visited` 存放遍历过的节点位置。使用 `count` 记录最短路径。将起始位置 `(0, 0)` 加入到 `queue` 中，并标记为访问过。
2. 如果队列不为空，则令 `count += 1`，并将队列中的节点位置依次取出。对于每一个节点位置：
   - 先判断是否为右下角节点，即 `(n - 1, n - 1)`。如果是则返回当前最短路径长度 `count`。
   - 如果不是，则继续遍历 `8` 个方向上、没有访问过、并且值为 `0` 的相邻单元格。
   - 将其加入到队列 `queue` 中，并标记为访问过。
3. 重复进行第 2 步骤，直到队列为空时，返回 `-1`。

## 代码

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        size = len(grid)
        directions = {(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)}
        visited = set((0, 0))
        queue = [(0, 0)]
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                row, col = queue.pop(0)

                if row == size - 1 and col == size - 1:
                    return count
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if 0 <= new_row < size and 0 <= new_col < size and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
        return -1
```

