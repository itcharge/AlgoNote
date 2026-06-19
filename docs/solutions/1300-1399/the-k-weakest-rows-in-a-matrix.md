# [1337. 矩阵中战斗力最弱的 K 行](https://leetcode.cn/problems/the-k-weakest-rows-in-a-matrix/)

- 标签：数组、二分查找、矩阵、排序、堆（优先队列）
- 难度：简单

## 题目链接

- [1337. 矩阵中战斗力最弱的 K 行 - 力扣](https://leetcode.cn/problems/the-k-weakest-rows-in-a-matrix/)

## 题目大意

**描述**：给定一个 $m \times n$ 的矩阵 $mat$，矩阵中的元素都是 $0$ 或 $1$。其中 $1$ 代表军人，$0$ 代表平民。每行中的 $1$ 都在 $0$ 之前出现（即每行军人在前，平民在后）。

定义一行战斗力为该行中 $1$ 的个数。

**要求**：返回所有行中战斗力最弱的 $k$ 行的索引（按战斗力升序排列，如果战斗力相同，则索引小的在前）。

**说明**：
- $2 \le n, m \le 100$。
- $1 \le k \le m$。

**示例**：

- 示例 1：

```python
输入：mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
输出：[2,0,3]
解释：
每行中的军人数目：
行 0 -> 2 
行 1 -> 4 
行 2 -> 1 
行 3 -> 2 
行 4 -> 5 
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
```

- 示例 2：

```python
输入：mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
输出：[0,2]
解释： 
每行中的军人数目：
行 0 -> 1 
行 1 -> 4 
行 2 -> 1 
行 3 -> 1 
从最弱到最强对这些行排序后得到 [0,2,3,1]
```


## 解题思路

### 思路 1：二分查找 + 排序

#### 1. 核心思想

每行是排序的（$1$ 在前 $0$ 在后），可以用二分查找（二分找最后一个 $1$ 的位置）快速确定每行的战斗力。然后排序取前 $k$ 个。

#### 2. 具体步骤

**第 1 步**：对每行 $mat[i]$，用二分查找找到第一个 $0$ 的位置，即为该行 $1$ 的个数（战斗力 $power[i]$）。如果全为 $1$，则战斗力为 $n$。

**第 2 步**：构造列表 $rows = [(power[i], i) \; for \; i \; in \; range(m)]$。

**第 3 步**：按 $(power, index)$ 排序，取前 $k$ 个的索引。

#### 3. 举例说明

以 $mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,0,0]]$ 为例：

| 行   | 战斗力 | 索引 |
| --- | ----- | --- |
| 第 0 行 | 2     | 0   |
| 第 1 行 | 4     | 1   |
| 第 2 行 | 1     | 2   |
| 第 3 行 | 2     | 3   |
| 第 4 行 | 3     | 4   |

排序（战斗力，索引）：$(1,2), (2,0), (2,3), (3,4), (4,1)$。

前 $k=3$ 个：$[2, 0, 3]$。

### 思路 1：代码

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])

        def binary_search(row):
            """找第一个 0 的位置（即 1 的个数）"""
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left

        # 计算每行战斗力
        rows = []
        for i in range(m):
            power = binary_search(mat[i])
            rows.append((power, i))

        # 排序取前 k 个
        rows.sort()
        return [idx for _, idx in rows[:k]]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \log n + m \log m)$，二分每行 $O(\log n)$，排序 $O(m \log m)$。
- **空间复杂度**：$O(m)$，存储 $(power, index)$ 对。

---

### 思路 2：直接计数（$m, n$ 较小）

由于 $m, n \le 100$，可以直接用 `sum()` 计算每行战斗力：

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = [(sum(mat[i]), i) for i in range(len(mat))]
        rows.sort()
        return [idx for _, idx in rows[:k]]
```

复杂度 $O(m \times n + m \log m)$，对于 $100 \times 100$ 规模完全可行。

---

### 思路 3：最大堆

需要前 $k$ 小时，也可以用最大堆维护最小的 $k$ 个（堆顶是堆中最大的，新元素小于堆顶时才入堆）。但排序法更简洁。
