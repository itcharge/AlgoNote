# [0356. 直线镜像](https://leetcode.cn/problems/line-reflection/)

- 标签：数组、哈希表、数学
- 难度：中等

## 题目链接

- [0356. 直线镜像 - 力扣](https://leetcode.cn/problems/line-reflection/)

## 题目大意

**描述**：

在一个二维平面空间中，给定 $n$ 个点的坐标。

**要求**：

问，是否能找出一条平行于 $y$ 轴的直线，让这些点关于这条直线成镜像排布？

如果能，则返回 $true$，否则返回 $false$。

**说明**：

- 注意：题目数据中可能有重复的点。
- $n == points.length$。
- $1 \le n \le 10^4$。
- $-10^8 \le points[i][j] \le 10^8$。

- 进阶：你能找到比 O(n2) 更优的解法吗?

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/04/23/356_example_1.PNG)

```python
输入：points = [[1,1],[-1,1]]
输出：true
解释：可以找出 x = 0 这条线。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/04/23/356_example_2.PNG)

```python
输入：points = [[1,1],[-1,-1]]
输出：false
解释：无法找出这样一条线。
```

## 解题思路

### 思路 1：哈希表 + 数学

这道题的核心思想是：**利用数学性质，通过哈希表快速判断点集是否关于某条垂直线对称**。

解题步骤：

1. **去重处理**：由于题目数据中可能有重复的点，首先将点集转换为集合去重。

2. **计算对称轴**：如果点集关于垂直线 $x = k$ 对称，那么对于任意点 $(x, y)$，其对称点应该是 $(2k - x, y)$。所有点的 $x$ 坐标的平均值就是对称轴的位置，即 $k = \frac{\min(x) + \max(x)}{2}$。

3. **验证对称性**：遍历所有点，检查每个点 $(x, y)$ 的对称点 $(2k - x, y)$ 是否存在于点集中。

**关键点**：

- 对称轴位置：$k = \frac{\min(x) + \max(x)}{2}$。
- 对称点坐标：$(x, y)$ 关于 $x = k$ 的对称点是 $(2k - x, y)$。
- 使用集合存储点坐标，便于 $O(1)$ 时间查找。
- 时间复杂度为 $O(n)$，空间复杂度为 $O(n)$。

### 思路 1：代码

```python
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True
        
        # 去重并转换为集合，便于快速查找
        point_set = set()
        x_coords = []
        
        for point in points:
            x, y = point[0], point[1]
            point_set.add((x, y))
            x_coords.append(x)
        
        # 计算对称轴位置：k = (min_x + max_x) / 2
        min_x = min(x_coords)
        max_x = max(x_coords)
        k = (min_x + max_x) / 2
        
        # 检查每个点是否都有对应的对称点
        for x, y in point_set:
            # 计算对称点的 x 坐标
            symmetric_x = 2 * k - x
            # 检查对称点是否存在于点集中
            if (symmetric_x, y) not in point_set:
                return False
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是点的数量。需要遍历所有点两次：一次去重和收集坐标，一次验证对称性。
- **空间复杂度**：$O(n)$，需要 $O(n)$ 的空间存储去重后的点集和坐标列表。
