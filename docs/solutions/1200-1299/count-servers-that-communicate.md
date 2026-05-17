# [1267. 统计参与通信的服务器](https://leetcode.cn/problems/count-servers-that-communicate/)

- 标签：深度优先搜索、广度优先搜索、并查集、数组、计数、矩阵
- 难度：中等

## 题目链接

- [1267. 统计参与通信的服务器 - 力扣](https://leetcode.cn/problems/count-servers-that-communicate/)

## 题目大意

**描述**：这里有一幅服务器分布图，服务器的位置标识在 $m \times n$ 的整数矩阵网格 $grid$ 中，$1$ 表示单元格上有服务器，$0$ 表示没有。如果两台服务器位于同一行或者同一列，就认为它们之间可以进行通信。

**要求**：统计并返回能够与至少一台其他服务器进行通信的服务器的数量。

**说明**：

- $m == grid.length$。
- $n == grid[i].length$。
- $1 \le m \le 250$。
- $1 \le n \le 250$。
- $grid[i][j] == 0$ or $1$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/untitled-diagram-6.jpg)

```python
输入：grid = [[1,0],[0,1]]
输出：0
解释：没有一台服务器能与其他服务器进行通信。
```

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/untitled-diagram-4-1.jpg)

```python
输入：grid = [[1,0],[1,1]]
输出：3
解释：所有这些服务器都至少可以与一台别的服务器进行通信。
```

## 解题思路

### 思路 1：行列计数

###### 1. 核心思想

一台服务器能通信的条件非常直观：**它所在的行或列上至少还有另一台服务器**。因为通信只要求同行或同列，不要求相邻。

所以不需要复杂的图遍历或并查集。我们只需要两趟扫描：
- 第一趟：统计每行和每列分别有多少台服务器。
- 第二趟：对每个服务器，检查它所在行或列的服务器数量是否大于 $1$。

###### 2. 具体步骤

**第 1 步：统计行列服务器数量**

获取矩阵的行数 $m$ 和列数 $n$。创建两个数组 $rows$ 和 $cols$，长度分别为 $m$ 和 $n$，初始全为 $0$。

遍历整个矩阵，当遇到 $grid[i][j] == 1$ 时：
- $rows[i] += 1$（第 $i$ 行多了一台服务器）
- $cols[j] += 1$（第 $j$ 列多了一台服务器）

**第 2 步：统计可通信服务器**

再次遍历整个矩阵，当遇到 $grid[i][j] == 1$ 时，检查 $rows[i] > 1$ 或 $cols[j] > 1$。只要满足任意一个，说明该服务器至少有一台同行或同列的服务器，计数加 $1$。

**第 3 步：返回计数**

**结合示例走一遍：**

示例 1：
$$grid = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$

统计行列：$rows = [1, 1], cols = [1, 1]$

检查：两个服务器各自的行和列都只有它自己（$rows[i] = 1$ 且 $cols[j] = 1$），都无法通信。返回 $0$。

示例 2：
$$grid = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$$

统计行列：
- $(0,0)$：$rows[0]=1, cols[0]=1$
- $(1,0)$：$rows[1]=1, cols[0]=2$
- $(1,1)$：$rows[1]=2, cols[1]=1$

检查：
- $(0,0)$：$rows[0]=1$ 且 $cols[0]=2 > 1$ → 可通信 ✓
- $(1,0)$：$rows[1]=2 > 1$ → 可通信 ✓
- $(1,1)$：$rows[1]=2 > 1$ → 可通信 ✓

返回 $3$。

### 思路 1：代码

```python
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 第 1 步：统计每行和每列的服务器数量
        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        # 第 2 步：检查每个服务器能否通信
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$，需要遍历整个矩阵两次（一次统计，一次检查），每次遍历都是 $O(m \times n)$。
- **空间复杂度**：$O(m + n)$，需要两个数组分别存储 $m$ 行的计数和 $n$ 列的计数。
