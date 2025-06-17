# [LCR 112. 矩阵中的最长递增路径](https://leetcode.cn/problems/fpTFWP/)

- 标签：深度优先搜索、广度优先搜索、图、拓扑排序、记忆化搜索、数组、动态规划、矩阵
- 难度：困难

## 题目链接

- [LCR 112. 矩阵中的最长递增路径 - 力扣](https://leetcode.cn/problems/fpTFWP/)

## 题目大意

给定一个 `m * n` 大小的整数矩阵 `matrix`。要求：找出其中最长递增路径的长度。

对于每个单元格，可以往上、下、左、右四个方向移动，不能向对角线方向移动或移动到边界外。

## 解题思路

深度优先搜索。使用二维数组 `record` 存储遍历过的单元格最大路径长度，已经遍历过的单元格就不需要再次遍历了。

## 代码

```python
class Solution:
    max_len = 0
    directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        record = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(i, j):
            record[i][j] = 1
            for direction in self.directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if 0 <= new_i < rows and 0 <= new_j < cols and matrix[new_i][new_j] > matrix[i][j]:
                    if record[new_i][new_j] == 0:
                        dfs(new_i, new_j)
                    record[i][j] = max(record[i][j], record[new_i][new_j] + 1)
            self.max_len = max(self.max_len, record[i][j])

        for i in range(rows):
            for j in range(cols):
                if record[i][j] == 0:
                    dfs(i, j)
        return self.max_len
```

