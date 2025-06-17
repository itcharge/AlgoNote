# [0073. 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/)

- 标签：数组、哈希表、矩阵
- 难度：中等

## 题目链接

- [0073. 矩阵置零 - 力扣](https://leetcode.cn/problems/set-matrix-zeroes/)

## 题目大意

**描述**：给定一个 $m \times n$ 大小的矩阵 $matrix$。

**要求**：如果一个元素为 $0$，则将其所在行和列所有元素都置为 $0$。

**说明**：

- 请使用「原地」算法。
- $m == matrix.length$。
- $n == matrix[0].length$。
- $1 \le m, n \le 200$。
- $-2^{31} \le matrix[i][j] \le 2^{31} - 1$。
- **进阶**：
  - 一个直观的解决方案是使用  $O(m \times n)$ 的额外空间，但这并不是一个好的解决方案。
  - 一个简单的改进方案是使用 $O(m + n)$ 的额外空间，但这仍然不是最好的解决方案。
  - 你能想出一个仅使用常量空间的解决方案吗？


**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```python
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```

## 解题思路

### 思路 1：使用标记变量

直观上可以使用两个数组来标记行和列出现 $0$ 的情况，但这样空间复杂度就是 $O(m+n)$ 了，不符合题意。

考虑使用数组原本的元素进行记录出现 $0$ 的情况。

1. 设定两个变量 $flag\underline{\hspace{0.5em}}row0$、$flag\underline{\hspace{0.5em}}col0$ 来标记第一行、第一列是否出现了 $0$。
2. 接下来我们使用数组第一行、第一列来标记 $0$ 的情况。
3. 对数组除第一行、第一列之外的每个元素进行遍历，如果某个元素出现 $0$ 了，则使用数组的第一行、第一列对应位置来存储 $0$ 的标记。
4. 再对数组除第一行、第一列之外的每个元素进行遍历，通过对第一行、第一列的标记 $0$ 情况，进行置为 $0$ 的操作。
5. 最后再根据 $flag\underline{\hspace{0.5em}}row0$、$flag\underline{\hspace{0.5em}}col0$ 的标记情况，对第一行、第一列进行置为 $0$ 的操作。

### 思路 1：代码

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        flag_col0 = False
        flag_row0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                flag_row0 = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$。
- **空间复杂度**：$O(1)$。

