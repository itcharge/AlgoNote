# [1274. 矩形内船只的数目](https://leetcode.cn/problems/number-of-ships-in-a-rectangle/)

- 标签：数组、分治、交互
- 难度：困难

## 题目链接

- [1274. 矩形内船只的数目 - 力扣](https://leetcode.cn/problems/number-of-ships-in-a-rectangle/)

## 题目大意

**描述**：给定一个二维平面，平面上有一些船只。你可以调用 API $Sea.hasShips(topRight, bottomLeft)$ 来查询一个矩形区域内是否有至少一艘船，其中 $topRight$ 是右上角坐标，$bottomLeft$ 是左下角坐标。

**要求**：计算矩形 $[0,0]$ 到 $[1000,1000]$ 范围内的船只总数。每次查询 $hasShips$ 的耗时很高，需要尽量减少查询次数。

**说明**：

- 矩形范围 $[0,0]$ 到 $[1000,1000]$。
- $Sea.hasShips$ 返回 $True$ 表示矩形内至少有一艘船，否则表示没有船。

**示例**：

- 示例 1：

```python
输入：
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
输出：3
解释：在 [0,0] 到 [4,4] 范围内有 3 艘船。
```

## 解题思路

### 思路 1：分治（四分法）

#### 1. 核心思想

直接对每个点查询是不现实的（$1001 \times 1001 \approx 10^6$ 个点）。利用 $hasShips$ 可以判断矩形区域内是否有船，我们可以用**分治法**：

- 如果当前矩形区域没有船（$hasShips$ 返回 $False$），直接返回 $0$。
- 如果当前矩形区域只有一个点，且 $hasShips$ 返回 $True$，返回 $1$。
- 否则，将矩形四等分，递归处理每个子矩形。

这样，每次递归最多进行 $4$ 次查询，递归深度为 $\log_2(1000) \approx 10$。总查询次数远小于逐点查询。

#### 2. 分治思想、具体步骤、正确性

**分治思想**：将大矩形切成四个小矩形，分别统计每个小矩形内的船只数，然后相加。

**具体步骤**：

**第 1 步**：定义递归函数 $count(rect\_topRight, rect\_bottomLeft)$：
- 输入：矩形的右上角 $(x1, y1)$ 和左下角 $(x2, y2)$，满足 $x1 \ge x2$，$y1 \ge y2$。
- 如果矩形内没有船（$hasShips$ 返回 $False$），返回 $0$。
- 如果矩形缩成一个点（$x1 == x2$ 且 $y1 == y2$），返回 $1$（因为有船）。
- 否则，计算中点 $(mid\_x, mid\_y)$，将矩形四等分并递归求和。

**第 2 步**：在递归前先通过 $hasShips$ 判断，如果矩形内没有船，直接剪枝。

**第 3 步**：返回四个子矩形的船只数之和。

**正确性**：分治策略的正确性基于 $hasShips$ 的单调性——如果大矩形内没有船，它的所有子矩形内也一定没有船（剪枝的合理性）。将大矩形不断分割成小矩形递归处理，每个点最终会被恰好统计一次。

#### 3. 结合示例走一遍

假设船舶位置 $[[1,1],[2,2],[3,3],[5,5]]$，初始矩形 $[0,0]$ 到 $[4,4]$。

```
rectangle [4,4] - [0,0]: hasShips? True → 四等分
  矩形 1 [4,4] - [2,2]: hasShips? True → [5,5] 不在这个范围，只有 [2,2],[3,3]
    进一步分割 → ... → 最终找到 [2,2] 和 [3,3] → 2 艘
  矩形 2 [2,4] - [0,2]: hasShips? True → [1,1]
    进一步分割 → ... → 最终找到 [1,1] → 1 艘
  矩形 3 [4,2] - [2,0]: hasShips? False → 0 艘
  矩形 4 [2,2] - [0,0]: hasShips? True → [1,1] 已在上个矩形找到？不对，需要没有重叠
```

需要注意四分法的矩形划分不能重叠。如果用中点坐标分割为四个子矩形：
- 左上：$(x1, y1)$ 到 $(mid\_x+1, mid\_y+1)$
- 右上：$(x1, mid\_y)$ 到 $(mid\_x+1, y2)$
- 左下：$(mid\_x, y1)$ 到 $(x2, mid\_y+1)$
- 右下：$(mid\_x, mid\_y)$ 到 $(x2, y2)$

这种划分的细节比较多，另一个更简洁的方法是：当 $hasShips$ 返回 $True$ 但矩形面积 $> 1$ 时，沿着较长的边二分切割，而不是四等分。

### 思路 1：代码

```python
class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = topRight.x, topRight.y
        x2, y2 = bottomLeft.x, bottomLeft.y

        # 如果矩形内没有船，直接返回 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # 如果缩成一个点，说明有一艘船
        if x1 == x2 and y1 == y2:
            return 1

        # 沿较长边二分
        if x1 - x2 >= y1 - y2:
            # 按 x 方向二分
            mid_x = (x1 + x2) // 2
            # 左子矩形
            left = self.countShips(sea, Point(mid_x, y1), bottomLeft)
            # 右子矩形
            right = self.countShips(sea, topRight, Point(mid_x + 1, y2))
            return left + right
        else:
            # 按 y 方向二分
            mid_y = (y1 + y2) // 2
            # 下子矩形
            down = self.countShips(sea, Point(x1, mid_y), bottomLeft)
            # 上子矩形
            up = self.countShips(sea, topRight, Point(x2, mid_y + 1))
            return down + up
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是船只数量。每次 $hasShips$ 确认有船时才会继续分割，每次分割减半矩形面积，总递归次数与船只数量相关。
- **空间复杂度**：$O(\log(\max(w, h)))$，递归栈深度为矩形的二分深度，最多约 $\log_2(1000) \approx 10$。
