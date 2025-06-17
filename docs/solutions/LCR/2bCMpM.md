# [LCR 107. 01 矩阵](https://leetcode.cn/problems/2bCMpM/)

- 标签：广度优先搜索、数组、动态规划、矩阵
- 难度：中等

## 题目链接

- [LCR 107. 01 矩阵 - 力扣](https://leetcode.cn/problems/2bCMpM/)

## 题目大意

给定一个由 `0` 和 `1` 组成的矩阵，两个相邻元素间的距离为 `1` 。

要求：找出每个元素到最近的 `0` 的距离，并输出为矩阵。

## 解题思路

题目要求的是每个 `1` 到 `0`的最短曼哈顿距离。换句话也可以求每个 `0` 到 `1` 的最短曼哈顿距离。这样做的好处是，可以从所有值为 `0` 的元素开始进行搜索，可以不断累积距离，直到遇到值为 `1` 的元素时，可以直接将累积距离直接赋值。

具体操作如下：将所有值为 `0` 的元素坐标加入访问集合中，对所有值为`0` 的元素上下左右进行搜索。每进行一次上下左右搜索，更新新位置的距离值，并把新的位置坐标加入队列和访问集合中，直到遇见值为 `1` 的元素停止搜索。

## 代码

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_count = len(mat)
        col_count = len(mat[0])
        dist_map = [[0 for _ in range(col_count)] for _ in range(row_count)]
        zeroes_pos = []
        for i in range(row_count):
            for j in range(col_count):
                if mat[i][j] == 0:
                    zeroes_pos.append((i, j))

        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        queue = collections.deque(zeroes_pos)
        visited = set(zeroes_pos)

        while queue:
            i, j = queue.popleft()
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < row_count and 0 <= new_j < col_count and (new_i, new_j) not in visited:
                    dist_map[new_i][new_j] = dist_map[i][j] + 1
                    queue.append((new_i, new_j))
                    visited.add((new_i, new_j))
        return dist_map
```

