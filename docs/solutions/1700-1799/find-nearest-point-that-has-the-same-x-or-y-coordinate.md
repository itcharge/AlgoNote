# [1779. 找到最近的有相同 X 或 Y 坐标的点](https://leetcode.cn/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/)

- 标签：数组
- 难度：简单

## 题目链接

- [1779. 找到最近的有相同 X 或 Y 坐标的点 - 力扣](https://leetcode.cn/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/)

## 题目大意

**描述**：给定两个整数 `x` 和 `y`，表示笛卡尔坐标系下的 `(x, y)` 点。再给定一个数组 `points`，其中 `points[i] = [ai, bi]`，表示在 `(ai, bi)` 处有一个点。当一个点与 `(x, y)` 拥有相同的 `x` 坐标或者拥有相同的 `y` 坐标时，我们称这个点是有效的。

**要求**：返回数组中距离 `(x, y)` 点出曼哈顿距离最近的有效点在 `points` 中的下标位置。如果有多个最近的有效点，则返回下标最小的一个。如果没有有效点，则返回 `-1`。

**说明**：

- **曼哈顿距离**：`(x1, y1)` 和 `(x2, y2)` 之间的曼哈顿距离为 `abs(x1 - x2) + abs(y1 - y2)` 。
- $1 \le points.length \le 10^4$。
- $points[i].length == 2$。
- $1 \le x, y, ai, bi \le 10^4$。

**示例**：

- 示例 1：

```python
输入：x = 3, y = 4, points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
输出：2
解释：在所有点中 [3, 1]、[2, 4]、[4, 4] 为有效点。其中 [2, 4]、[4, 4] 距离 [3, 4] 曼哈顿距离最近，都为 1。[2, 4] 下标最小，所以返回 2。
```

## 解题思路

### 思路 1：

- 使用 `min_dist` 记录下有效点中最近的曼哈顿距离，初始化为 `float('inf')`。使用 `min_index` 记录下符合要求的最小下标。
- 遍历 `points` 数组，遇到有效点之后计算一下当前有效点与 `(x, y)` 的曼哈顿距离，并判断更新一下有效点中最近的曼哈顿距离 `min_dist` 和符合要求的最小下标 `min_index`。
- 遍历完之后，判断一下 `min_dist` 是否等于 `float('inf')`。如果等于，说明没有找到有效点，则返回 `-1`。如果不等于，则返回符合要求的最小下标 `min_index`。

## 代码

### 思路 1 代码：

```python
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        min_index = 0
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(points[i][0] - x) + abs(points[i][1] - y)
                if dist < min_dist:
                    min_dist = dist
                    min_index = i

        if min_dist == float('inf'):
            return -1
        return min_index
```

