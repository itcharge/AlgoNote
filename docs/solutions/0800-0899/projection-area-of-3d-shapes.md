# [0883. 三维形体投影面积](https://leetcode.cn/problems/projection-area-of-3d-shapes/)

- 标签：几何、数组、数学、矩阵
- 难度：简单

## 题目链接

- [0883. 三维形体投影面积 - 力扣](https://leetcode.cn/problems/projection-area-of-3d-shapes/)

## 题目大意

**描述**：

在 $n \times n$ 的网格 $grid$ 中，我们放置了一些与 $x$，$y$，$z$ 三轴对齐的 $1 \times 1 \times 1$ 立方体。

每个值 $v = grid[i][j]$ 表示有一列 $v$ 个正方体叠放在格子 $(i, j)$ 上。

现在，我们查看这些立方体在 $xy$、$yz$ 和 $zx$ 平面上的投影。

「投影」就像影子，将「三维」形体映射到一个「二维」平面上。从顶部、前面和侧面看立方体时，我们会看到「影子」。

**要求**：

返回「所有三个投影的总面积」。

**说明**：

- $n == grid.length == grid[i].length$。
- $1 \le n \le 50$。
- $0 \le grid[i][j] \le 50$。

**示例**：

- 示例 1：

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png)

```python
输入：[[1,2],[3,4]]
输出：17
解释：这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。
```

- 示例 2：

```python
输入：grid = [[2]]
输出：5
```

## 解题思路

### 思路 1:数学 + 模拟

三维形体在三个平面上的投影面积分别为:

1. **xy 平面(俯视图)**:每个非零格子贡献 1 的面积,即统计非零格子的个数。
2. **yz 平面(正视图)**:每一行的最大值之和,因为从前面看,每一行的高度由该行最高的立方体决定。
3. **zx 平面(侧视图)**:每一列的最大值之和,因为从侧面看,每一列的高度由该列最高的立方体决定。

### 思路 1:代码

```python
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_area = 0  # xy 平面投影面积
        yz_area = 0  # yz 平面投影面积
        zx_area = 0  # zx 平面投影面积
        
        for i in range(n):
            row_max = 0  # 第 i 行的最大值
            col_max = 0  # 第 i 列的最大值
            
            for j in range(n):
                # 统计非零格子
                if grid[i][j] > 0:
                    xy_area += 1
                
                # 更新行最大值
                row_max = max(row_max, grid[i][j])
                # 更新列最大值
                col_max = max(col_max, grid[j][i])
            
            yz_area += row_max
            zx_area += col_max
        
        return xy_area + yz_area + zx_area
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n^2)$,其中 $n$ 是网格的边长。需要遍历整个网格。
- **空间复杂度**:$O(1)$,只使用常数额外空间。
