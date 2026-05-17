# [1240. 铺瓷砖](https://leetcode.cn/problems/tiling-a-rectangle-with-the-fewest-squares/)

- 标签：动态规划、回溯
- 难度：困难

## 题目链接

- [1240. 铺瓷砖 - 力扣](https://leetcode.cn/problems/tiling-a-rectangle-with-the-fewest-squares/)

## 题目大意

**描述**：给定一个 $n \times m$ 的矩形，需要用最少数量的正方形瓷砖铺满。瓷砖大小可以任意（即边长可以是任意正整数），但不能重叠，不能超出矩形边界。

**要求**：返回最少需要的瓷砖数量。

**说明**：

- $1 \le n, m \le 13$。

**示例**：

- 示例 1：

```python
输入：n = 2, m = 3
输出：3
解释：可以用 3 块瓷砖铺满：1 块 2×2 + 2 块 1×1。
```

- 示例 2：

```python
输入：n = 5, m = 8
输出：5
```

## 解题思路

### 思路 1：回溯 + 剪枝

#### 1. 核心思想

$n, m \le 13$，搜索空间有限但也不小。需要用回溯法枚举所有可能的铺法，同时用剪枝来加速。

核心思路：逐行逐列地填充。用一个二维数组 $filled$ 标记每个格子是否已被覆盖。

每次找到第一个未被覆盖的格子 $(r, c)$，尝试从该位置开始放置不同大小的正方形（边长为 $1$ 到 $\min(n-r, m-c)$）。放置后标记这些格子已被覆盖，递归填充其余部分，然后回溯。

#### 2. 选择、限制与终止

- **选择**：在当前第一个空白格子 $(r,c)$ 处，尝试放置边长为 $s$ 的正方形（$s$ 从大到小或从小到大）。
- **限制**：正方形必须在矩形范围内，且覆盖的所有格子都未被填充。
- **终止**：所有格子都被覆盖 → 更新最小值。

#### 3. 剪枝

- 如果当前使用的瓷砖数已经 $\ge$ 当前最优解，剪枝。
- 从大到小尝试正方形边长可能更快找到较优解（贪心直觉，但需要正确性保证，所以不能直接贪心，只是帮助剪枝）。

#### 4. 结合示例走一遍

$n=2, m=3$

初始 $filled$ 全是 $0$。

```
找到第一个空白 (0,0):
- 尝试边长 2（最大 min(2,3)=2）：覆盖 (0,0)(0,1)(1,0)(1,1)
  剩余空白 (0,2) 和 (1,2):
  找到第一个空白 (0,2):
  - 只能放边长 1: 覆盖 (0,2)
    剩余空白 (1,2):
    - 边长 1: 覆盖 (1,2)
    瓷砖数=3，记录 ans=3
```

### 思路 1：代码

```python
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # filled[i][j] = 1 表示已被覆盖
        filled = [[0] * m for _ in range(n)]
        self.ans = n * m  # 最坏情况全用 1×1

        def can_place(r, c, s):
            """检查以 (r,c) 为左上角、边长为 s 的正方形是否可放"""
            for i in range(r, r + s):
                for j in range(c, c + s):
                    if filled[i][j]:
                        return False
            return True

        def fill(r, c, s, val):
            """将以 (r,c) 为左上角、边长为 s 的正方形填充/取消填充"""
            for i in range(r, r + s):
                for j in range(c, c + s):
                    filled[i][j] = val

        def backtrack(cnt):
            if cnt >= self.ans:
                return
            # 找到第一个未被覆盖的格子
            for r in range(n):
                for c in range(m):
                    if not filled[r][c]:
                        # 尝试从大到小放置正方形
                        max_s = min(n - r, m - c)
                        for s in range(max_s, 0, -1):
                            if can_place(r, c, s):
                                fill(r, c, s, 1)
                                backtrack(cnt + 1)
                                fill(r, c, s, 0)
                        return  # 这个格子必须被填充，尝试完所有可能后返回
            # 所有格子都被覆盖
            self.ans = min(self.ans, cnt)

        backtrack(0)
        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(4^{n \times m})$ 或更优。实际搜索树远小于理论上界，因为剪枝效果很好。$n,m \le 13$ 时可接受。
- **空间复杂度**：$O(n \times m)$，递归栈深度和 $filled$ 数组。

### 思路 2：动态规划（理论可行但状态复杂）

理论上，这个问题也可以用 DP + 记忆化搜索，将矩形切割成子矩形来求解。但由于矩形切割的方式很多（不是所有切法都是横平竖直的），状态转移很复杂，回溯法反而是这类"铺瓷砖"问题最常用的解法。
