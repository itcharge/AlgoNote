# [1329. 将矩阵按对角线排序](https://leetcode.cn/problems/sort-the-matrix-diagonally/)

- 标签：数组、矩阵、排序
- 难度：中等

## 题目链接

- [1329. 将矩阵按对角线排序 - 力扣](https://leetcode.cn/problems/sort-the-matrix-diagonally/)

## 题目大意

**描述**：给定一个 $m \times n$ 的整数矩阵 $mat$。

**要求**：将矩阵的每一条「左上到右下」的对角线按升序排序，返回排序后的矩阵。

**说明**：
- 对角线：从左上到右下，每条对角线上元素的 $(i - j)$ 值相同。
- $m, n \le 100$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/25/1482_example_1_2.png)

```python
输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
```

- 示例 2：

```python
输入：mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
输出：[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
```


## 解题思路

### 思路 1：分组排序

#### 1. 核心思想

按 $(i - j)$ 将元素分组，每个组对应一条对角线。同一对角线上的元素具有相同的 $i - j$ 值（范围从 $-(n-1)$ 到 $m-1$）。

对每条对角线，收集元素 → 排序 → 放回原位置。

#### 2. 具体步骤

**第 1 步**：建立字典 $diagonals$，以 $(i - j)$ 为键，值为该对角线上的元素列表。

**第 2 步**：遍历矩阵，将每个元素加入对应的字典键中。

**第 3 步**：对每个键对应的列表升序排序。

**第 4 步**：将排序后的元素按 $(i - j)$ 重新填入矩阵。

#### 3. 对角线编号说明

矩阵中每个元素 $(i, j)$ 的 $i - j$ 值范围：
- 最小值：$-(n-1)$（右上角）
- 最大值：$m-1$（左下角）

每个相同 $i - j$ 值的格子在一条对角线上。

#### 4. 举例说明

以 $mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]$ 为例：

```
3 3 1 1
2 2 1 2
1 1 1 2
```

对角线分组（$i-j$ 值）：
- $i-j=2$：$[3]$
- $i-j=1$：$[2,1]$
- $i-j=0$：$[1,2,1]$ → 排序 $[1,1,2]$
- $i-j=-1$：$[3,1,1]$ → 排序 $[1,1,3]$
- $i-j=-2$：$[1,2]$ → 排序 $[1,2]$
- $i-j=-3$：$[2]$

放回后得到：

```
1 1 1 1
1 2 2 2
1 2 3 3
```

### 思路 1：代码

```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diag = {}  # key: i-j, value: list of elements

        # 第 1 步：按对角线分组
        for i in range(m):
            for j in range(n):
                key = i - j
                if key not in diag:
                    diag[key] = []
                diag[key].append(mat[i][j])

        # 第 2 步：每条对角线排序
        for key in diag:
            diag[key].sort(reverse=True)  # 逆序，方便 pop 从末尾取（保持顺序）

        # 第 3 步：放回矩阵
        for i in range(m):
            for j in range(n):
                key = i - j
                mat[i][j] = diag[key].pop()  # 从末尾取，保持正序

        return mat
```

优化版：不需要逆序，直接用队列或指针：

```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diag = {}

        for i in range(m):
            for j in range(n):
                diag.setdefault(i - j, []).append(mat[i][j])

        for key in diag:
            diag[key].sort()

        # 用指针遍历放回
        ptr = {key: 0 for key in diag}
        for i in range(m):
            for j in range(n):
                key = i - j
                mat[i][j] = diag[key][ptr[key]]
                ptr[key] += 1

        return mat
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n \times \log(\min(m,n)))$，每条对角线排序，最长对角线长度 $\min(m,n)$。
- **空间复杂度**：$O(m \times n)$，存储所有对角线元素。

---

### 思路 2：原地排序（冒泡思路）

由于矩阵规模较小（$m,n \le 100$），可以模拟在每条对角线上做冒泡排序。但分组排序法更简洁高效。
