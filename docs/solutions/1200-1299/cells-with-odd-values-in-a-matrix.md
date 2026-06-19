# [1252. 奇数值单元格的数目](https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/)

- 标签：数组、数学、模拟
- 难度：简单

## 题目链接

- [1252. 奇数值单元格的数目 - 力扣](https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/)

## 题目大意

**描述**：给定一个 $m \times n$ 的矩阵，初始所有元素为 $0$。再给一个二维数组 $indices$，其中 $indices[i] = [r_i, c_i]$ 表示对矩阵执行一次操作：将第 $r_i$ 行全部加 $1$，同时将第 $c_i$ 列全部加 $1$。

**要求**：执行完所有操作后，返回矩阵中奇数值单元格的数目。

**说明**：

- $1 \le m, n \le 50$。
- $1 \le indices.length \le 10^{3}$。
- $0 \le r_i < m$，$0 \le c_i < n$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/06/e1.png)

```python
输入：m = 2, n = 3, indices = [[0,1],[1,1]]
输出：6
解释：最开始的矩阵是 [[0,0,0],[0,0,0]]。
第一次增量操作后得到 [[1,2,1],[0,1,0]]。
最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。
```

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/06/e2.png)

```python
输入：m = 2, n = 2, indices = [[1,1],[0,0]]
输出：0
解释：最后的矩阵是 [[2,2],[2,2]]，里面没有奇数。
```

## 解题思路

### 思路 1：模拟 + 计数优化

###### 1. 核心思想

如果直接模拟：创建一个 $m \times n$ 的矩阵，遍历所有操作逐一加 $1$，最后再统计奇数个数，时间复杂度是 $O(len(indices) \times (m + n) + m \times n)$，虽然数据范围不大也能跑，但不够优雅。

实际上我们根本不需要真的维护整个矩阵。仔细观察会发现：

**每个单元格 $(i, j)$ 的最终值 = 第 $i$ 行被加的次数 + 第 $j$ 列被加的次数。**

而一个数是奇数，当且仅当它模 $2$ 等于 $1$。所以问题转化为：**一个行加次数的奇偶性和一个列加次数的奇偶性组合起来，有多少种组合结果是奇数？**

根据加法奇偶性规则：
- 奇数 + 奇数 = 偶数
- 奇数 + 偶数 = 奇数
- 偶数 + 奇数 = 奇数
- 偶数 + 偶数 = 偶数

所以行和列一奇一偶时，结果才是奇数。

###### 2. 具体步骤

**第 1 步：统计每行和每列被加的次数**

创建两个数组 $rows$ 和 $cols$，分别记录每行和每列被 $indices$ 操作的次数。

遍历 $indices$：
- $rows[r_i] += 1$
- $cols[c_i] += 1$

**第 2 步：统计奇偶分布**

遍历 $rows$，统计有多少行被加了奇数次，记为 $odd\_rows$。
遍历 $cols$，统计有多少列被加了奇数次，记为 $odd\_cols$。

那么：
- $odd\_rows$ 行是奇数行
- $m - odd\_rows$ 行是偶数行
- $odd\_cols$ 列是奇数列
- $n - odd\_cols$ 列是偶数列

**第 3 步：计算奇数值单元格数量**

奇数单元格需要行和列一奇一偶，所以：

$$\text{奇数值数量} = odd\_rows \times (n - odd\_cols) + (m - odd\_rows) \times odd\_cols$$

- $odd\_rows \times (n - odd\_cols)$：奇数行配偶数列
- $(m - odd\_rows) \times odd\_cols$：偶数行配奇数列

**结合示例 1 走一遍：**

$m = 2, n = 3, indices = [[0,1],[1,1]]$

统计次数：
- $rows = [1, 1]$（行 0 被加 1 次，行 1 被加 1 次）
- $cols = [0, 2, 0]$（列 1 被加 2 次，列 0 和列 2 被加 0 次）

奇偶分布：
- $odd\_rows = 2$（两行都是奇数次）
- $odd\_cols = 0$（三列都是偶数次）

计算结果：
$$2 \times (3 - 0) + (2 - 2) \times 0 = 6$$

和题目示例一致。

### 思路 1：代码

```python
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # 第 1 步：统计每行和每列被加的次数
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        # 第 2 步：统计奇数行和奇数列的数量
        odd_rows = sum(1 for v in rows if v % 2 == 1)
        odd_cols = sum(1 for v in cols if v % 2 == 1)

        # 第 3 步：奇数行配偶数列 + 偶数行配奇数列
        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(len(indices) + m + n)$。只需要遍历一次 $indices$（$O(len(indices))$）来累加次数，然后各遍历一次 $rows$ 和 $cols$（$O(m + n)$）来统计奇偶情况，不需要真的创建和遍历整个 $m \times n$ 矩阵。
- **空间复杂度**：$O(m + n)$。需要两个数组分别存储 $m$ 行的计数和 $n$ 列的计数，相比直接模拟的 $O(m \times n)$ 空间有了显著优化。
