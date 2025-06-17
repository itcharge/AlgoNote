# [面试题 08.10. 颜色填充](https://leetcode.cn/problems/color-fill-lcci/)

- 标签：深度优先搜索、广度优先搜索、数组、矩阵
- 难度：简单

## 题目链接

- [面试题 08.10. 颜色填充 - 力扣](https://leetcode.cn/problems/color-fill-lcci/)

## 题目大意

给定一个二维整数矩阵 `image`，其中 `image[i][j]` 表示矩阵第 `i` 行、第 `j` 列上网格块的颜色值。再给定一个起始位置 `(sr, sc)`，以及一个目标颜色 `newColor`。

要求：对起始位置 `(sr, sc)` 所在位置周围区域填充颜色为 `newColor`。并返回填充后的图像 `image`。

- 周围区域：颜色相同且在上、下、左、右四个方向上存在相连情况的若干元素。

## 解题思路

深度优先搜索。使用二维数组 `visited` 标记访问过的节点。遍历上、下、左、右四个方向上的点。如果下一个点位置越界，或者当前位置与下一个点位置颜色不一样，则对该节点进行染色。

在遍历的过程中注意使用 `visited` 标记访问过的节点，以免重复遍历。

## 代码

```python
class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(self, image, i, j, origin_color, color, visited):
        rows, cols = len(image), len(image[0])

        for direct in self.directs:
            new_i = i + direct[0]
            new_j = j + direct[1]

            # 下一个位置越界，则当前点在边界，对其进行着色
            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                image[i][j] = color
                continue

            # 如果访问过，则跳过
            if visited[new_i][new_j]:
                continue

            # 如果下一个位置颜色与当前颜色相同，则继续搜索
            if image[new_i][new_j] == origin_color:
                visited[new_i][new_j] = True
                self.dfs(image, new_i, new_j, origin_color, color, visited)
            # 下一个位置颜色与当前颜色不同，则当前位置为连通区域边界，对其进行着色
            else:
                image[i][j] = color

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image

        rows, cols = len(image), len(image[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        visited[sr][sc] = True

        self.dfs(image, sr, sc, image[sr][sc], newColor, visited)

        return image
```

