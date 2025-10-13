# [0867. 转置矩阵](https://leetcode.cn/problems/transpose-matrix/)

- 标签：数组、矩阵、模拟
- 难度：简单

## 题目链接

- [0867. 转置矩阵 - 力扣](https://leetcode.cn/problems/transpose-matrix/)

## 题目大意

给定一个二维数组 matrix。返回 matrix 的转置矩阵。

## 解题思路

直接模拟求解即可。先求出 matrix 的规模。如果 matrix 是 m * n 的矩阵。则创建一个 n * m 大小的矩阵 transposed。根据转置的规则对 transposed 的每个元素进行赋值。最终返回 transposed。

## 代码

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transposed = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed
```

