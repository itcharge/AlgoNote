# [1292. 元素和小于等于阈值的正方形的最大边长](https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

- 标签：数组、二分查找、矩阵、前缀和
- 难度：中等

## 题目链接

- [1292. 元素和小于等于阈值的正方形的最大边长 - 力扣](https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

## 题目大意

**描述**：给定一个 $m \times n$ 的矩阵 $mat$ 和一个整数阈值 $threshold$。

**要求**：返回矩阵中元素和不超过 $threshold$ 的正方形的最大边长。如果没有这样的正方形，返回 $0$。

**说明**：

- $1 \le m, n \le 300$。
- $0 \le mat[i][j] \le 10^{5}$。
- $0 \le threshold \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：边长为 2 的正方形有 4 个，元素和分别为 4、4、4、9，最大边长为 2。
```

- 示例 2：

```python
输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
输出：0
```

## 解题思路

### 思路 1：二维前缀和 + 枚举边长

#### 1. 核心思想

要快速计算任意正方形的元素和，需要用到**二维前缀和**。二维前缀和 $prefix[i][j]$ 表示矩阵从左上角 $(0,0)$ 到 $(i-1,j-1)$ 这个矩形区域内所有元素的和。通过容斥原理，可以在 $O(1)$ 时间内计算出任意矩形区域的和。

有了二维前缀和后，可以直接枚举所有可能的正方形（左上角位置和边长），检查其元素和是否 $\le threshold$，取最大边长。

总时间复杂度 $O(m \times n \times \min(m, n))$。$m, n \le 300$，最坏 $300 \times 300 \times 300 = 2700$ 万，勉强可行。但可以用二分查找优化到 $O(mn \times \log(\min(m,n)))$。

#### 2. 二维前缀和公式

$prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + mat[i][j]$

$(r_1, c_1)$ 到 $(r_2, c_2)$ 的矩形和（左上角为 $(r_1, c_1)$，右下角为 $(r_2, c_2)$）：

$sum = prefix[r_2+1][c_2+1] - prefix[r_1][c_2+1] - prefix[r_2+1][c_1] + prefix[r_1][c_1]$

#### 3. 具体步骤

**第 1 步**：构建二维前缀和数组 $prefix$，大小为 $(m+1) \times (n+1)$。

**第 2 步**：枚举边长 $k$（从 $\min(m, n)$ 到 $1$），检查是否存在一个 $k \times k$ 的正方形满足条件：
- 遍历所有左上角位置 $(i, j)$，其中 $0 \le i \le m-k$，$0 \le j \le n-k$。
- 用前缀和计算正方形元素和，如果 $\le threshold$，返回 $k$。

**第 3 步**：如果没有找到，返回 $0$。

### 思路 1：代码

```python
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 构建二维前缀和
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + mat[i][j]

        # 从大到小枚举边长
        max_side = min(m, n)
        for k in range(max_side, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    # 计算以 (i,j) 为左上角，边长为 k 的正方形的元素和
                    r1, c1 = i, j
                    r2, c2 = i + k - 1, j + k - 1
                    total = (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1]
                             - prefix[r2 + 1][c1] + prefix[r1][c1])
                    if total <= threshold:
                        return k
        return 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(mn \times \min(m, n))$，二维前缀和构建 $O(mn)$，枚举正方形最坏 $O(mn \times \min(m,n))$。
- **空间复杂度**：$O(mn)$，存储二维前缀和数组。

### 思路 2：二维前缀和 + 二分答案

#### 1. 核心思想

边长的合法性具有单调性：如果边长为 $k$ 存在满足条件的正方形，那么边长 $< k$ 也一定存在（因为更小的正方形和更小）。反之，如果边长为 $k$ 不存在，那么边长 $> k$ 也不存在。

因此可以对边长进行二分查找，将时间复杂度降到 $O(mn \times \log(\min(m,n)))$。

#### 2. 具体步骤

**第 1 步**：构建二维前缀和数组。

**第 2 步**：在 $[0, \min(m, n)]$ 范围内二分查找最大边长：
- $check(k)$：检查是否存在一个 $k \times k$ 的正方形，其元素和 $\le threshold$。
- 如果 $check(mid)$ 为真，说明边长还可以更大，$left = mid$。
- 否则 $right = mid - 1$。

**第 3 步**：返回 $left$。

#### 3. 代码

```python
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 构建二维前缀和
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + mat[i][j]

        # 检查是否存在边长为 k 的满足条件的正方形
        def can(k: int) -> bool:
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (prefix[i + k][j + k] - prefix[i][j + k]
                             - prefix[i + k][j] + prefix[i][j])
                    if total <= threshold:
                        return True
            return False

        # 二分查找最大边长
        left, right = 0, min(m, n)
        while left < right:
            mid = (left + right + 1) // 2
            if can(mid):
                left = mid
            else:
                right = mid - 1
        return left
```

#### 4. 复杂度分析

- **时间复杂度**：$O(mn \times \log(\min(m, n)))$，二分需要 $O(\log(\min(m,n)))$ 次，每次 $check$ 需要 $O(mn)$ 时间。
- **空间复杂度**：$O(mn)$。

对于 $m, n \le 300$，思路 1 已经足够快。但如果矩阵更大（如 $1000 \times 1000$），思路 2 的优势就会明显体现出来。
