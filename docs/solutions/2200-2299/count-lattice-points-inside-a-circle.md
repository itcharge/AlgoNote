# [2249. 统计圆内格点数目](https://leetcode.cn/problems/count-lattice-points-inside-a-circle/)

- 标签：几何、数组、哈希表、数学、枚举
- 难度：中等

## 题目链接

- [2249. 统计圆内格点数目 - 力扣](https://leetcode.cn/problems/count-lattice-points-inside-a-circle/)

## 题目大意

**描述**：给定一个二维整数数组 `circles`。其中 `circles[i] = [xi, yi, ri]` 表示网格上圆心为 `(xi, yi)` 且半径为 `ri` 的第 $i$ 个圆。

**要求**：返回出现在至少一个圆内的格点数目。

**说明**：

- **格点**：指的是整数坐标对应的点。
- 圆周上的点也被视为出现在圆内的点。
- $1 \le circles.length \le 200$。
- $circles[i].length == 3$。
- $1 \le xi, yi \le 100$。
- $1 \le ri \le min(xi, yi)$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2022/03/02/exa-11.png)

```python
输入：circles = [[2,2,1]]
输出：5
解释：
给定的圆如上图所示。
出现在圆内的格点为 (1, 2)、(2, 1)、(2, 2)、(2, 3) 和 (3, 2)，在图中用绿色标识。
像 (1, 1) 和 (1, 3) 这样用红色标识的点，并未出现在圆内。
因此，出现在至少一个圆内的格点数目是 5。
```

- 示例 2：

```python
输入：circles = [[2,2,2],[3,4,1]]
输出：16
解释：
给定的圆如上图所示。
共有 16 个格点出现在至少一个圆内。
其中部分点的坐标是 (0, 2)、(2, 0)、(2, 4)、(3, 2) 和 (4, 4)。
```

## 解题思路

### 思路 1：枚举算法

题目要求中 $1 \le xi, yi \le 100$，$1 \le ri \le min(xi, yi)$。则圆中点的范围为 $1 \le x, y \le 200$。

我们可以枚举所有坐标和所有圆，检测该坐标是否在圆中。

为了优化枚举范围，我们可以先遍历一遍所有圆，计算最小、最大的 $x$、$y$ 范围，再枚举所有坐标和所有圆，并进行检测。

### 思路 1：代码

```python
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        min_x, min_y = 200, 200
        max_x, max_y = 0, 0
        for circle in circles:
            if circle[0] + circle[2] > max_x:
                max_x = circle[0] + circle[2]
            if circle[0] - circle[2] < min_x:
                min_x = circle[0] - circle[2]
            if circle[1] + circle[2] > max_y:
                max_y = circle[1] + circle[2]
            if circle[1] - circle[2] < min_y:
                min_y = circle[1] - circle[2]
        
        ans = 0
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for xi, yi, ri in circles:
                    if (xi - x) * (xi - x) + (yi - y) * (yi - y) <= ri * ri:
                        ans += 1
                        break
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(x \times y)$，其中 $x$、$y$ 分别为横纵坐标的个数。
- **空间复杂度**：$O(1)$。
