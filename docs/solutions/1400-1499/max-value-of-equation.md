# [1499. 满足不等式的最大值](https://leetcode.cn/problems/max-value-of-equation/)

- 标签：队列、数组、滑动窗口、单调队列、堆（优先队列）
- 难度：困难

## 题目链接

- [1499. 满足不等式的最大值 - 力扣](https://leetcode.cn/problems/max-value-of-equation/)

## 题目大意

**描述**：给定一个数组 $points$，其中 $points[i] = [x_i, y_i]$ 且 $x_1 < x_2 < \dots < x_n$。还有一个整数 $k$。

**要求**：返回满足 $|x_i - x_j| \le k$ 的最大 $y_i + y_j + |x_i - x_j|$ 值。

**说明**：
- $2 \le points.length \le 10^5$。
- $1 \le k \le 2 \times 10^9$。

**示例**：

- 示例 1：

```python
输入：points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
输出：4
解释：前两个点满足 |xi - xj| <= 1 ，代入方程计算，则得到值 3 + 0 + |1 - 2| = 4 。第三个和第四个点也满足条件，得到值 10 + -10 + |5 - 6| = 1 。
没有其他满足条件的点，所以返回 4 和 1 中最大的那个。
```

- 示例 2：

```python
输入：points = [[0,0],[3,0],[9,2]], k = 3
输出：3
解释：只有前两个点满足 |xi - xj| <= 3 ，代入方程后得到值 0 + 0 + |0 - 3| = 3 。
```

## 解题思路

### 思路 1：单调队列

#### 1. 核心思想

因为 $x_i < x_j$，$|x_i - x_j| = x_j - x_i$。公式变为：

$$y_i + y_j + (x_j - x_i) = (y_i - x_i) + (y_j + x_j)$$

对于固定的 $j$，要最大化 $(y_i - x_i) + (y_j + x_j)$，只需在满足 $x_j - x_i \le k$ 的 $i$ 中最大化 $(y_i - x_i)$。

这是一个滑动窗口最大值问题，用单调队列维护 $(y_i - x_i)$ 的最大值，且 $i$ 在 $[j - k, j-1]$ 范围内。

#### 2. 具体步骤

**第 1 步**：用双端队列 $dq$ 存储索引，按 $(y_i - x_i)$ 从大到小排列。

**第 2 步**：遍历 $j = 0 \to n-1$：
- 从队头移除不满足 $x_j - x_{dq[0]} \le k$ 的索引。
- 如果 $dq$ 非空，用队头计算候选值 $(y_{dq[0]} - x_{dq[0]}) + (y_j + x_j)$ 更新答案。
- 将 $j$ 加入队列（维护单调递减）。
  - 当队尾的 $(y_{tail} - x_{tail}) \le (y_j - x_j)$ 时，弹出队尾。

**第 3 步**：返回答案。

#### 3. 举例说明

以 $points = [[1,3],[2,0],[5,10],[6,-10]], k = 1$ 为例：

- $j=0$：队列空，入队 $[0]$，$val=3-1=2$
- $j=1$：$x_1-x_0=1 \le 1$，$x_1-x_0=1$ 在范围内。队头 $0$，候选 $2+(0+2)=4$，更新 $ans=4$。入队 $1$（$0-2=-2$）。
- $j=2$：$x_2-x_0=4>1$，弹出 $0$。$x_2-x_1=3>1$，弹出 $1$。队列空，$j=2$ 无配对。入队 $2$（$10-5=5$）。
- $j=3$：$x_3-x_2=1 \le 1$，候选 $5+(-10+6)=1$，$ans$ 不变。入队 $3$（$-10-6=-16$）。

结果：$4$。

### 思路 1：代码

```python
from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        dq = deque()
        ans = float('-inf')

        for j in range(n):
            xj, yj = points[j]
            # 移除窗口外的点
            while dq and xj - points[dq[0]][0] > k:
                dq.popleft()

            # 用队头计算答案
            if dq:
                i = dq[0]
                ans = max(ans, (points[i][1] - points[i][0]) + (yj + xj))

            # 维护单调递减（按 yi - xi）
            while dq and (points[dq[-1]][1] - points[dq[-1]][0]) <= (yj - xj):
                dq.pop()
            dq.append(j)

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个元素入队出队各一次。
- **空间复杂度**：$O(n)$。
