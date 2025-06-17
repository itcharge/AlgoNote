# [0733. 图像渲染](https://leetcode.cn/problems/flood-fill/)

- 标签：深度优先搜索、广度优先搜索、数组、矩阵
- 难度：简单

## 题目链接

- [0733. 图像渲染 - 力扣](https://leetcode.cn/problems/flood-fill/)

## 题目大意

给定一个二维数组 image 表示图画，数组的每个元素值表示该位置的像素值大小。再给定一个坐标 (sr, sc) 表示图像渲染开始的位置。然后再给定一个新的颜色值 newColor。现在要求：将坐标 (sr, sc) 以及 (sr, sc) 相连的上下左右区域上与 (sr, sc) 原始颜色相同的区域染色为 newColor。返回染色后的二维数组。



## 解题思路

从起点开始，对上下左右四个方向进行广度优先搜索。每次搜索到一个位置时，如果该位置上的像素值与初始位置像素值相同，则更新该位置像素值，并将该位置加入队列中。最后将二维数组返回。

- 注意：如果起点位置初始颜色和新颜色值 newColor 相同，则不需要染色，直接返回原数组即可。

## 代码

```python
import collections

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        queue = collections.deque([(sr, sc)])
        oriColor = image[sr][sc]
        while queue:
            point = queue.popleft()
            image[point[0]][point[1]] = newColor
            for direction in directions:
                new_i = point[0] + direction[0]
                new_j = point[1] + direction[1]
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == oriColor:
                    queue.append((new_i, new_j))
        return image
```

