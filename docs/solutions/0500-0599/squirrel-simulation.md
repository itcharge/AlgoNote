# [0573. 松鼠模拟](https://leetcode.cn/problems/squirrel-simulation/)

- 标签：数组、数学
- 难度：中等

## 题目链接

- [0573. 松鼠模拟 - 力扣](https://leetcode.cn/problems/squirrel-simulation/)

## 题目大意

**描述**：

在一个平面上，有一棵树、一只松鼠和若干坚果。给定：

- $height$ 和 $width$：平面的高度和宽度。
- $tree$：树的位置 $[tree\_x, tree\_y]$。
- $squirrel$：松鼠的初始位置 $[squirrel\_x, squirrel\_y]$。
- $nuts$：坚果的位置列表 $[[nut1\_x, nut1\_y], [nut2\_x, nut2\_y], ...]$。

松鼠需要将所有坚果收集到树的位置。每次只能携带一个坚果，并且能够向上、下、左、右四个方向移动到相邻的单元格。

**要求**：

返回松鼠收集所有坚果饼主义放在树下的最小移动距离。

**说明**：

- **距离** 是指移动的次数。
- $1 \le height, width \le 100$。
- $tree.length == 2$。
- $squirrel.length == 2$。
- $1 \le nuts.length \le 5000$。
- $nuts[i].length == 2$。
- $0 \le tree_r, squirrel_r, nuti_r \le height$。
- $0 \le tree_c, squirrel_c, nuti_c \le width$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/04/24/squirrel1-grid.jpg)

```python
输入：height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]
输出：12
解释：为实现最小的距离，松鼠应该先摘 [2, 5] 位置的坚果。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/04/24/squirrel2-grid.jpg)

```python
输入：height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]
输出：3
```

## 解题思路

### 思路 1：贪心算法

关键观察：

- 除了第一个坚果，其他所有坚果都需要从树出发，拿到坚果再回到树，距离为 $2 \times dist(tree, nut)$
- 第一个坚果是从松鼠位置出发，距离为 $dist(squirrel, nut) + dist(nut, tree)$

总距离 = $\sum_{i=0}^{n-1} 2 \times dist(tree, nuts[i]) - dist(tree, first\_nut) + dist(squirrel, first\_nut)$

为了最小化总距离，应该选择使 $dist(squirrel, nut) - dist(tree, nut)$ 最小的坚果作为第一个收集的坚果。

### 思路 1：代码

```python
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # 计算曼哈顿距离
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # 计算所有坚果到树的距离之和的两倍（假设都从树出发）
        total_distance = 0
        for nut in nuts:
            total_distance += 2 * manhattan_distance(tree, nut)
        
        # 找到最优的第一个坚果
        # 第一个坚果的额外距离是：dist(squirrel, nut) - dist(tree, nut)
        min_diff = float('inf')
        for nut in nuts:
            diff = manhattan_distance(squirrel, nut) - manhattan_distance(tree, nut)
            min_diff = min(min_diff, diff)
        
        return total_distance + min_diff
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是坚果的数量。需要遍历所有坚果两次。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
