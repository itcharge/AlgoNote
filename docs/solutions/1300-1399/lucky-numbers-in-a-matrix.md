# [1380. 矩阵中的幸运数](https://leetcode.cn/problems/lucky-numbers-in-a-matrix/)

- 标签：数组、矩阵
- 难度：简单

## 题目链接

- [1380. 矩阵中的幸运数 - 力扣](https://leetcode.cn/problems/lucky-numbers-in-a-matrix/)

## 题目大意

**描述**：给定一个 $m \times n$ 的矩阵，矩阵中的数字互不相同。幸运数是同时满足以下条件的数：同行最小、同列最大。

**要求**：返回矩阵中所有的幸运数。

**示例**：

- 示例 1：

```python
输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
```

- 示例 2：

```python
输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
```


## 解题思路

### 思路 1：模拟

#### 1. 核心思想

先找出每行的最小值，再找出每列的最大值。如果一个数同时是行最小和列最大，就是幸运数。

#### 2. 代码

```python
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_min = [min(row) for row in matrix]
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    ans.append(matrix[i][j])
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(mn)$。
- **空间复杂度**：$O(m + n)$。
