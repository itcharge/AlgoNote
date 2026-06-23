# [1439. 有序矩阵中的第 k 个最小数组和](https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)

- 标签：数组、二分查找、矩阵、堆（优先队列）
- 难度：困难

## 题目链接

- [1439. 有序矩阵中的第 k 个最小数组和 - 力扣](https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)

## 题目大意

**描述**：给定一个 $m \times n$ 的矩阵 $mat$，每行已升序排列。从每行各选一个数组成一个长度为 $m$ 的数组，数组和为 $m$ 个数的和。

**要求**：返回所有可能的数组和中第 $k$ 小的和。

**说明**：
- $1 \le m, n \le 40$。
- $1 \le k \le \min(200, n^m)$。

**示例**：

- 示例 1：

```python
输入：mat = [[1,3,11],[2,4,6]], k = 5
输出：7
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。
```

- 示例 2：

```python
输入：mat = [[1,3,11],[2,4,6]], k = 9
输出：17
```

## 解题思路

### 思路 1：最小堆 + 逐层合并

#### 1. 核心思想

逐行合并。假设已经知道前 $i-1$ 行的前 $k$ 小和（列表 $prev$），计算加入第 $i$ 行后的前 $k$ 小和。

对于 $prev$ 中的每个和 $s$，加上第 $i$ 行的每个元素 $mat[i][j]$，取前 $k$ 小。用最小堆或直接排序取前 $k$。

#### 2. 具体步骤

**第 1 步**：初始化 $prev = mat[0]$（第一行的前 $k$ 小，实际就是所有元素）。

**第 2 步**：遍历第 $i = 1 \to m-1$ 行：
- 用最小堆或生成所有 $prev + mat[i][j]$ 的组合，取前 $k$ 小。

优化：因为 $k \le 200$，$prev$ 最多保留 $k$ 个，每行 $n \le 40$，每次合并最多 $k \times n \le 8000$ 个候选。

**第 3 步**：返回 $prev[k-1]$。

#### 3. 举例说明

以 $mat = [[1,3,11],[2,4,6]], k = 5$ 为例：

第 0 行：$prev = [1,3,11]$
第 1 行：合并

$1+2=3, 1+4=5, 1+6=7$
$3+2=5, 3+4=7, 3+6=9$
$11+2=13, 11+4=15, 11+6=17$

前 5 小：$[3,5,5,7,7]$，返回 $prev[4]=7$。

### 思路 1：代码

```python
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        prev = mat[0][:k]  # 最多 k 个

        for i in range(1, m):
            # 合并第 i 行
            candidates = []
            for s in prev:
                for j in range(min(n, k)):
                    candidates.append(s + mat[i][j])
            # 取前 k 小
            prev = heapq.nsmallest(k, candidates)

        return prev[k - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times k \times n \times \log(kn))$，$k \le 200$，$n \le 40$，可行。
- **空间复杂度**：$O(k \times n)$。

---

### 思路 2：二分查找 + 计数

也可以二分答案 $mid$，检查有多少个数组和 $\le mid$ 的数组个数是否 $\ge k$。计数用 DFS 剪枝（当 $prefix + (remaining\_rows) \times min\_val > mid$ 时剪枝）。但思路 1 已足够。
