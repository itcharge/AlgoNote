# [1476. 子矩形查询](https://leetcode.cn/problems/subrectangle-queries/)

- 标签：设计、数组、矩阵
- 难度：中等

## 题目链接

- [1476. 子矩形查询 - 力扣](https://leetcode.cn/problems/subrectangle-queries/)

## 题目大意

**要求**：实现一个类 SubrectangleQueries，它的构造函数的参数是一个 $rows \times cols $的矩形（这里用整数矩阵表示），并支持以下两种操作：

1. `updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)`：用 $newValue$ 更新以 $(row1,col1)$ 为左上角且以 $(row2,col2)$ 为右下角的子矩形。

2. `getValue(int row, int col)`：返回矩形中坐标 (row,col) 的当前值。

**说明**：

- 最多有 $500$ 次 `updateSubrectangle` 和 `getValue` 操作。
- $1 <= rows, cols <= 100$。
- $rows == rectangle.length$。
- $cols == rectangle[i].length$。
- $0 <= row1 <= row2 < rows$。
- $0 <= col1 <= col2 < cols$。
- $1 <= newValue, rectangle[i][j] <= 10^9$。
- $0 <= row < rows$。
- $0 <= col < cols$。

**示例**：

- 示例 1：

```python
输入：
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
输出：
[null,1,null,5,5,null,10,5]
解释：
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);  
// 初始的 (4x3) 矩形如下：
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // 返回 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// 此次更新后矩形变为：
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5 
subrectangleQueries.getValue(0, 2); // 返回 5
subrectangleQueries.getValue(3, 1); // 返回 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// 此次更新后矩形变为：
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10 
subrectangleQueries.getValue(3, 1); // 返回 10
subrectangleQueries.getValue(0, 2); // 返回 5
```

- 示例 2：

```python
输入：
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
输出：
[null,1,null,100,100,null,20]
解释：
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // 返回 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // 返回 100
subrectangleQueries.getValue(2, 2); // 返回 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // 返回 20

```

## 解题思路

### 思路 1：暴力

矩形最大为 $row \times col == 100 \times 100$，则每次更新最多需要更新 $10000$ 个值，更新次数最多为 $500$ 次。

用暴力更新的方法最多需要更新 $5000000$ 次，我们可以尝试一下用暴力更新的方法解决本题（提交后发现可以通过）。

### 思路 1：代码

```Python
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue


    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(row \times col \times 500)$。
- **空间复杂度**：$O(row \times col)$。
