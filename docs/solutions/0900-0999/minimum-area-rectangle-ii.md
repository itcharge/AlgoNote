# [0963. 最小面积矩形 II](https://leetcode.cn/problems/minimum-area-rectangle-ii/)

- 标签：几何、数组、哈希表、数学
- 难度：中等

## 题目链接

- [0963. 最小面积矩形 II - 力扣](https://leetcode.cn/problems/minimum-area-rectangle-ii/)

## 题目大意

**描述**：

给定一个 X-Y 平面上的点数组 $points$，其中 $points[i] = [x_i, y_i]$。

**要求**：

返回由这些点形成的任意矩形的最小面积，矩形的边「不一定」平行于 X 轴和 Y 轴。如果不存在这样的矩形，则返回 0。

答案只需在$10^{-5}$ 的误差范围内即可被视作正确答案。

**说明**：

- $1 \le points.length \le 50$。
- $points[i].length == 2$。
- $0 \le x_i, y_i \le 4 \times 10^{4}$。
- 所有给定的点都是「唯一」的。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2018/12/21/1a.png)

```python
输入： points = [[1,2],[2,1],[1,0],[0,1]]
输出： 2.00000
解释： 最小面积矩形由 [1,2]、[2,1]、[1,0]、[0,1] 组成，其面积为 2。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2018/12/22/2.png)

```python
输入： points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
输出： 1.00000
解释： 最小面积矩形由 [1,0]、[1,1]、[2,1]、[2,0] 组成，其面积为 1。
```

## 解题思路

### 思路 1：哈希表 + 几何

对于任意矩形，可以由对角线的两个点和中心点唯一确定。我们可以枚举所有点对作为对角线，然后检查是否存在另外两个点构成矩形。

1. **枚举对角线**：枚举所有点对 $(p_1, p_2)$ 作为对角线。
2. **计算中心和边长**：
   - 中心点：$(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2})$
   - 对角线长度：$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
3. **哈希存储**：使用哈希表存储 (中心点, 对角线长度) 到点对的映射。
4. **验证矩形**：对于相同中心和对角线长度的两对点，验证它们是否构成矩形（对角线互相垂直）。
5. **计算面积**：使用向量叉积计算矩形面积。

### 思路 1：代码

```python
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        from collections import defaultdict
        
        n = len(points)
        if n < 4:
            return 0.0
        
        # 哈希表：(中心点, 对角线长度平方) -> [(点1, 点2), ...]
        diagonals = defaultdict(list)
        
        # 枚举所有点对作为对角线
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # 计算中心点（使用 2 倍坐标避免浮点数）
                cx, cy = x1 + x2, y1 + y2
                
                # 计算对角线长度的平方
                dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
                
                # 存储到哈希表
                diagonals[(cx, cy, dist_sq)].append((i, j))
        
        min_area = float('inf')
        
        # 检查相同中心和对角线长度的点对
        for key, pairs in diagonals.items():
            if len(pairs) < 2:
                continue
            
            # 枚举所有点对组合
            for k in range(len(pairs)):
                for l in range(k + 1, len(pairs)):
                    i1, j1 = pairs[k]
                    i2, j2 = pairs[l]
                    
                    # 获取四个点
                    p1, p2 = points[i1], points[j1]
                    p3, p4 = points[i2], points[j2]
                    
                    # 计算两条边的向量
                    v1 = (p3[0] - p1[0], p3[1] - p1[1])
                    v2 = (p4[0] - p1[0], p4[1] - p1[1])
                    
                    # 检查是否垂直（点积为 0）
                    if v1[0] * v2[0] + v1[1] * v2[1] == 0:
                        # 计算面积
                        len1 = (v1[0] ** 2 + v1[1] ** 2) ** 0.5
                        len2 = (v2[0] ** 2 + v2[1] ** 2) ** 0.5
                        area = len1 * len2
                        min_area = min(min_area, area)
        
        return min_area if min_area != float('inf') else 0.0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 + m^2)$，其中 $n$ 是点的数量，$m$ 是相同中心和对角线长度的点对数量。枚举点对需要 $O(n^2)$，验证矩形需要 $O(m^2)$。
- **空间复杂度**：$O(n^2)$，哈希表最多存储 $O(n^2)$ 个点对。
