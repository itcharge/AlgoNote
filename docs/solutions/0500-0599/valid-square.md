# [0593. 有效的正方形](https://leetcode.cn/problems/valid-square/)

- 标签：几何、数学
- 难度：中等

## 题目链接

- [0593. 有效的正方形 - 力扣](https://leetcode.cn/problems/valid-square/)

## 题目大意

**描述**：

给定 2D 空间中四个点的坐标 $p1$, $p2$, $p3$ 和 $p4$。

**要求**：

如果这四个点构成一个正方形，则返回 true。

**说明**：

- 点的坐标 $pi$ 表示为 $[xi, yi]$。 输入没有任何顺序。
- 一个有效的正方形有四条等边和四个等角（90 度角）。
- $p1.length == p2.length == p3.length == p4.length == 2$。
- $-10^{4} \le xi, yi \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: true
```

- 示例 2：

```python
输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
输出：false
```

## 解题思路

### 思路 1：距离判断

一个有效的正方形需要满足：

1. 四条边长度相等。
2. 两条对角线长度相等。
3. 四个角都是 90 度（可以通过边长的平方和等于对角线平方的一半来判断，即 $a^2 + b^2 = c^2$）。

我们可以计算所有点对之间的距离，对于一个正方形，应该有：

- 4 条边长度相等（设为 $side$）。
- 2 条对角线长度相等（设为 $diagonal$）。
- 满足 $2 \times side^2 = diagonal^2$（勾股定理）。

计算所有 $6$ 个点对之间的距离，排序后应该得到：$4$ 个相等的边长度和 $2$ 个相等的对角线长度，且满足上述关系。同时需要排除所有点重合的情况。

### 思路 1：代码

```python
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1: List[int], p2: List[int]) -> int:
            # 计算两点间距离的平方（避免浮点数误差）
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        # 计算所有点对之间的距离平方
        points = [p1, p2, p3, p4]
        distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                dist = distance(points[i], points[j])
                distances.append(dist)
        
        # 排序距离
        distances.sort()
        
        # 检查：应该有 4 条相等的边和 2 条相等的对角线
        # 且满足 2 * side^2 = diagonal^2
        # 同时排除所有点重合的情况（最小距离不能为 0）
        if distances[0] == 0:
            return False
        
        # 前 4 个应该是边，后 2 个应该是对角线
        return distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5] and 2 * distances[0] == distances[4]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$，固定计算 $6$ 个点对的距离并排序。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
