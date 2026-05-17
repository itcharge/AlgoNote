# [1237. 找出给定方程的正整数解](https://leetcode.cn/problems/find-positive-integer-solution-for-a-given-equation/)

- 标签：数学、双指针、二分查找、交互
- 难度：中等

## 题目链接

- [1237. 找出给定方程的正整数解 - 力扣](https://leetcode.cn/problems/find-positive-integer-solution-for-a-given-equation/)

## 题目大意

**描述**：给你一个函数 $f(x, y)$ 和一个目标结果 $z$，函数公式未知。已知函数是单调递增的：$f(x, y) < f(x+1, y)$ 且 $f(x, y) < f(x, y+1)$。$x$ 和 $y$ 都是正整数（$1$ 到 $1000$）。

**要求**：计算方程 $f(x, y) == z$ 所有可能的正整数数对，并按任意顺序返回。

**说明**：

- $1 \le z \le 10^3$。
- $1 \le x, y \le 10^3$。

**示例**：

- 示例 1：

```python
输入：function_id = 1, z = 5
输出：[[1,4],[2,3],[3,2],[4,1]]
解释：function_id = 1 暗含的函数式子为 f(x, y) = x + y
```

- 示例 2：

```python
输入：function_id = 2, z = 5
输出：[[1,5],[5,1]]
解释：function_id = 2 暗含的函数式子为 f(x, y) = x * y
```

## 解题思路

### 思路 1：双指针

###### 1. 核心思想

因为 $f(x, y)$ 关于 $x$ 和 $y$ 都是单调递增的，我们可以利用这个性质，用双指针法从两个方向逼近目标值。

具体做法是：固定 $x$ 从最小的 $1$ 开始，$y$ 从最大的 $1000$ 开始。这样在搜索过程中：
- 如果 $f(x, y) < z$，说明值太小了。由于 $y$ 已经不能再增大（它从最大值开始），需要增大 $x$ 来让值变大。
- 如果 $f(x, y) > z$，说明值太大了。由于 $x$ 已经不能再减小（它从最小值开始），需要减小 $y$ 来让值变小。
- 如果相等，记录结果，然后同时移动两个指针（$x$ 增大，$y$ 减小）继续搜索。

这个过程就像在一个二维单调矩阵中搜索目标值，$x$ 和 $y$ 分别沿着一个方向走，不会走回头路，所以 $x$ 和 $y$ 最多各移动 $1000$ 步。

###### 2. 具体步骤

**第 1 步**：初始化 $x = 1$，$y = 1000$，结果列表 $ans = []$。

**第 2 步**：当 $x \le 1000$ 且 $y \ge 1$ 时循环：
- 调用 $customfunction.f(x, y)$ 获取当前值 $val$。
- 如果 $val < z$：$x += 1$（值偏小，增大 $x$）。
- 如果 $val > z$：$y -= 1$（值偏大，减小 $y$）。
- 如果 $val == z$：将 $[x, y]$ 加入 $ans$，然后 $x += 1$，$y -= 1$（继续搜索其他解）。

**第 3 步**：返回 $ans$。

**结合示例 1 走一遍：**

$f(x, y) = x + y, z = 5$

双指针搜索过程：
- $(x=1, y=1000)$：$f=1001 > 5$ → $y=999$
- ...不断减小 $y$ 直到...
- $(x=1, y=4)$：$f=5$ → 记录 $[1,4]$，$x=2,y=3$
- $(x=2, y=3)$：$f=5$ → 记录 $[2,3]$，$x=3,y=2$
- $(x=3, y=2)$：$f=5$ → 记录 $[3,2]$，$x=4,y=1$
- $(x=4, y=1)$：$f=5$ → 记录 $[4,1]$，$x=5,y=0$

$y=0 < 1$，结束。结果：$[[1,4],[2,3],[3,2],[4,1]]$。

### 思路 1：代码

```python
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x, y = 1, 1000
        # 双指针从两个方向逼近目标值
        while x <= 1000 and y >= 1:
            val = customfunction.f(x, y)
            if val < z:
                x += 1  # 值偏小，增大 x
            elif val > z:
                y -= 1  # 值偏大，减小 y
            else:
                ans.append([x, y])
                x += 1
                y -= 1  # 找到一个解后继续搜索
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1000 + 1000) = O(1)$。$x$ 最多从 $1$ 增加到 $1000$，$y$ 最多从 $1000$ 减小到 $1$，总共移动步数不超过 $2000$，是常数时间。
- **空间复杂度**：$O(1)$，不考虑存储答案所需的空间。
