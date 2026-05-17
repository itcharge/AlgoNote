# [1260. 二维网格迁移](https://leetcode.cn/problems/shift-2d-grid/)

- 标签：数组、矩阵、模拟
- 难度：简单

## 题目链接

- [1260. 二维网格迁移 - 力扣](https://leetcode.cn/problems/shift-2d-grid/)

## 题目大意

**描述**：给定一个 $m \times n$ 的二维网格 $grid$ 和一个整数 $k$。需要将网格中的元素进行 $k$ 次迁移操作。

每次迁移操作定义如下：
- 位于最后一行的元素会移动到第一行（即行号变为 $0$，列号加 $1$）。
- 位于最后一列的元素会移动到下一行的第一列。
- 其他元素向右移动一列。

实际上，就是将网格展开成一维数组，元素整体向右循环移动 $k$ 步，然后再折叠回二维网格。

**要求**：返回 $k$ 次迁移操作后的二维网格。

**说明**：

- $m == grid.length$，$n == grid[i].length$。
- $1 \le m \le 50$，$1 \le n \le 50$。
- $1 \le k \le 100$。

**示例**：

- 示例 1：

```python
输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[9,1,2],[3,4,5],[6,7,8]]
```

- 示例 2：

```python
输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
```

## 解题思路

### 思路 1：一维展开 + 循环右移

#### 1. 核心思想

迁移操作的规律等价于：将二维网格按行展开为一维数组，循环向右移动 $k$ 步，再按行折叠回二维网格。

#### 2. 具体步骤

**第 1 步**：将二维网格 $grid$ 按行展开为一维数组 $arr$。

**第 2 步**：计算 $k$ 对总元素个数 $m \times n$ 取模（因为迁移 $m \times n$ 次等于没动）。

**第 3 步**：计算 $arr$ 中每个元素在原一维数组中的新位置。循环右移 $k$ 步意味着：原来在位置 $i$ 的元素会移动到位置 $(i + k) \% total$。

**第 4 步**：将新的一维数组按行折叠回二维网格。

**第 5 步**：返回结果。

#### 3. 结合示例走一遍

$grid = [[1,2,3],[4,5,6],[7,8,9]], k=1$

展开：$arr = [1,2,3,4,5,6,7,8,9]$

循环右移 $1$ 步：$arr' = [9,1,2,3,4,5,6,7,8]$

折叠：$[[9,1,2],[3,4,5],[6,7,8]]$

### 思路 1：代码

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n

        # 展平
        arr = [0] * total
        for i in range(m):
            for j in range(n):
                arr[i * n + j] = grid[i][j]

        # 循环右移 k 步
        k %= total
        new_arr = [0] * total
        for i in range(total):
            new_pos = (i + k) % total
            new_arr[new_pos] = arr[i]

        # 折叠回二维
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = new_arr[i * n + j]
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(mn)$，$m$ 和 $n$ 是网格维度。需要遍历两次网格（展开和折叠）。
- **空间复杂度**：$O(mn)$，需要存储一维展开数组。

### 优化

如果不想显式展开，可以直接用坐标映射：

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_pos = (i * n + j + k) % total
                ni, nj = new_pos // n, new_pos % n
                ans[ni][nj] = grid[i][j]
        return ans
```

这样省去了显式的一维数组，代码更简洁。
