# [0931. 下降路径最小和](https://leetcode.cn/problems/minimum-falling-path-sum/)

- 标签：数组、动态规划、矩阵
- 难度：中等

## 题目链接

- [0931. 下降路径最小和 - 力扣](https://leetcode.cn/problems/minimum-falling-path-sum/)

## 题目大意

**描述**：

给定一个 $n \times n$ 的方形整数数组 $matrix$。

**要求**：

请你找出并返回通过 $matrix$ 的下降路径的「最小和」。

**说明**：

- 「下降路径」可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 $(row, col)$ 的下一个元素应当是 $(row + 1, col - 1)$、$(row + 1, col)$ 或者 $(row + 1, col + 1)$。
- $n == matrix.length == matrix[i].length$。
- $1 \le n \le 10^{3}$。
- $-10^{3} \le matrix[i][j] \le 10^{3}$。

**示例**：

- 示例 1：

![](https://pic.leetcode.cn/1729566253-aneDag-image.png)

```python
输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：如图所示，为和最小的两条下降路径
```

- 示例 2：

![](https://pic.leetcode.cn/1729566282-dtXwRd-image.png)

```python
输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：如图所示，为和最小的下降路径
```

## 解题思路

### 思路 1：动态规划

这是一个经典的动态规划问题，类似于"最小路径和"。

1. **状态定义**：$dp[i][j]$ 表示到达位置 $(i, j)$ 的最小路径和。
2. **状态转移**：对于位置 $(i, j)$，可以从三个位置转移而来：
   - 正上方：$(i-1, j)$
   - 左上方：$(i-1, j-1)$
   - 右上方：$(i-1, j+1)$
   
   转移方程：$dp[i][j] = matrix[i][j] + \min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])$

3. **初始化**：第一行的值就是 $matrix[0][j]$。
4. **边界处理**：注意处理列的边界情况。
5. **返回结果**：最后一行的最小值。

**空间优化**：可以直接在原数组上修改，或使用滚动数组优化空间。

### 思路 1：代码

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # 从第二行开始，逐行计算最小路径和
        for i in range(1, n):
            for j in range(n):
                # 计算从上一行三个位置转移的最小值
                min_prev = matrix[i - 1][j]  # 正上方
                
                if j > 0:  # 左上方
                    min_prev = min(min_prev, matrix[i - 1][j - 1])
                
                if j < n - 1:  # 右上方
                    min_prev = min(min_prev, matrix[i - 1][j + 1])
                
                # 更新当前位置的最小路径和
                matrix[i][j] += min_prev
        
        # 返回最后一行的最小值
        return min(matrix[n - 1])
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是矩阵的边长，需要遍历整个矩阵。
- **空间复杂度**：$O(1)$，直接在原数组上修改。如果不能修改原数组，需要 $O(n^2)$ 的额外空间。
