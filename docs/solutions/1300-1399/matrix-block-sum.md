# [1314. 矩阵区域和](https://leetcode.cn/problems/matrix-block-sum/)

- 标签：数组、矩阵、前缀和
- 难度：中等

## 题目链接

- [1314. 矩阵区域和 - 力扣](https://leetcode.cn/problems/matrix-block-sum/)

## 题目大意

**描述**：给定一个 $m \times n$ 的矩阵 $mat$ 和一个整数 $k$。

**要求**：返回一个矩阵 $ans$，其中 $ans[i][j]$ 是 $mat[i-k..i+k][j-k..j+k]$ 范围内所有元素的和。

**示例**：

- 示例 1：

```python
输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
```

- 示例 2：

```python
输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]
```


## 解题思路

### 思路 1：二维前缀和

#### 1. 核心思想

构建二维前缀和，用容斥原理 $O(1)$ 计算每个 $k \times k$ 区域的和。

#### 2. 具体步骤

**第 1 步**：构建前缀和 $prefix$，$prefix[i+1][j+1]$ 表示 $mat[0..i][0..j]$ 的和。

**第 2 句活活**：对每个 $(i,j)$，计算左上角 $(r1,c1)$ 和右下角 $(r2,c2)$ 坐标（边界裁剪），用前缀和公式求和。

### 思路 1：代码

```python
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + mat[i][j]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m - 1, i + k), min(n - 1, j + k)
                ans[i][j] = (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1]
                             - prefix[r2 + 1][c1] + prefix[r1][c1])
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(mn)$。
- **空间复杂度**：$O(mn)$。
