# [1253. 重构 2 行二进制矩阵](https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/)

- 标签：贪心、数组、矩阵
- 难度：中等

## 题目链接

- [1253. 重构 2 行二进制矩阵 - 力扣](https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/)

## 题目大意

**描述**：给定一个 $2$ 行 $n$ 列的二进制数组：

- 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 $0$ 就是 $1$。
- 第 $0$ 行的元素之和为 $upper$。
- 第 $1$ 行的元素之和为 $lowe$r。
- 第 $i$ 列（从 $0$ 开始编号）的元素之和为 $colsum[i]$，$colsum$ 是一个长度为 $n$ 的整数数组。

**要求**：你需要利用 $upper$，$lower$ 和 $colsum$ 来重构这个矩阵，并以二维整数数组的形式返回它。

**说明**：

- 如果有多个不同的答案，那么任意一个都可以通过本题。
- 如果不存在符合要求的答案，就请返回一个空的二维数组。
- $1 \le colsum.length \le 10^5$。
- $0 \le upper, lower \le colsum.length$。
- $0 \le colsum[i] \le 2$。

**示例**：

- 示例 1：

```python
输入：upper = 2, lower = 1, colsum = [1,1,1]
输出：[[1,1,0],[0,0,1]]
解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
```

- 示例 2：

```python
输入：upper = 2, lower = 3, colsum = [2,2,1,1]
输出：[]
```

## 解题思路

### 思路 1：贪心算法

1. 先构建一个 $2 \times n$ 的答案数组 $ans$，其中 $ans[0]$ 表示矩阵的第 $0$ 行，$ans[1]$ 表示矩阵的第 $1$​ 行。
2. 遍历数组 $colsum$，对于当前列的和 $colsum[i]$ 来说：
   1. 如果 $colsum[i] == 2$，则需要将 $ans[0][i]$ 和 $ans[1][i]$ 都置为 $1$，此时 $upper$ 和 $lower$ 各自减去 $1$。
   2. 如果 $colsum[i] == 1$，则需要将 $ans[0][i]$ 置为 $1$ 或将 $ans[1][i]$ 置为 $1$。我们优先使用元素和多的那一项。
      1. 如果 $upper > lower$，则优先使用 $upper$，将 $ans[0][i]$ 置为 $1$，并且令 $upper$ 减去 $1$。
      2. 如果 $upper \le lower$，则优先使用 $lower$，将 $ans[1][i]$ 置为 $1$，并且令 $lower$ 减去 $1$。
   3. 如果 $colsum[i] == 0$，则需要将 $ans[0][i]$ 和 $ans[1][i]$ 都置为 $0$。
3. 在遍历过程中，如果出现 $upper < 0$ 或者 $lower < 0$，则说明无法构造出满足要求的矩阵，则直接返回空数组。
4. 遍历结束后，如果 $upper$ 和 $lower$ 都为 $0$，则返回答案数组 $ans$；否则返回空数组。

### 思路 1：代码

```Python
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        size = len(colsum)
        ans = [[0 for _ in range(size)] for _ in range(2)]

        for i in range(size):
            if colsum[i] == 2:
                ans[0][i] = ans[1][i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1
                    lower -= 1
            if upper < 0 or lower < 0:
                return []
        if lower != 0 or upper != 0:
            return []
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

