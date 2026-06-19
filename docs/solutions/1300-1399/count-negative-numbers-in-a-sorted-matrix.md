# [1351. 统计有序矩阵中的负数](https://leetcode.cn/problems/count-negative-numbers-in-a-sorted-matrix/)

- 标签：数组、二分查找、矩阵
- 难度：简单

## 题目链接

- [1351. 统计有序矩阵中的负数 - 力扣](https://leetcode.cn/problems/count-negative-numbers-in-a-sorted-matrix/)

## 题目大意

**描述**：给定一个 $m \times n$ 的矩阵 $grid$，每行按非递增顺序排列（从左到右递减），每列也按非递增顺序排列（从上到下递减）。

**要求**：返回矩阵中负数的个数。

**说明**：
- $1 \le m, n \le 100$。
- $-100 \le grid[i][j] \le 100$。

**示例**：

- 示例 1：

```python
输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。
```

- 示例 2：

```python
输入：grid = [[3,2],[1,0]]
输出：0
```


## 解题思路

### 思路 1：逐行二分

#### 1. 核心思想

每行是非递增的，所以负数一定出现在每行的末尾。对每行二分查找第一个负数出现的位置。

#### 2. 具体步骤

**第 1 步**：初始化 $ans = 0$。

**第 2 步**：对每行，用二分查找找到第一个小于 $0$ 的位置 $pos$。该行的负数为 $n - pos$。

**第 3 步**：累加各行的负数个数。

### 思路 1：代码

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for row in grid:
            # 二分找第一个小于 0 的元素
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid
                else:
                    left = mid + 1
            ans += n - left
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(m \log n)$。
- **空间复杂度**：$O(1)$。
