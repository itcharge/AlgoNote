# [0447. 回旋镖的数量](https://leetcode.cn/problems/number-of-boomerangs/)

- 标签：数组、哈希表、数学
- 难度：中等

## 题目链接

- [0447. 回旋镖的数量 - 力扣](https://leetcode.cn/problems/number-of-boomerangs/)

## 题目大意

给定平面上点坐标的数组 points，其中 $points[i] = [x_i, y_i]$。判断 points 中是否存在三个点 i，j，k，满足 i 和 j 之间的距离等于 i 和 k 之间的距离，即 $dist[i, j] = dist[i, k]$。找出满足上述关系的答案数量。

## 解题思路

使用哈希表记录每两个点之间的距离。然后使用两重循环遍历坐标数组，对于每两个点 i、点 j，计算两个点之间的距离，并将距离存进哈希表中。再从哈希表中选取距离相同的关系中依次选出两个，作为三个点之间的距离关系 $dist[i, j] =dist[i, k]$，因为还需考虑顺序，所以共有 $value * (value-1)$ 种情况。累加到答案中。

## 代码

```python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for point_i in points:
            dis_dict = dict()
            for point_j in points:
                if point_i != point_j:
                    dx = point_i[0] - point_j[0]
                    dy = point_i[1] - point_j[1]
                    dis = dx * dx + dy * dy
                    if dis in dis_dict:
                        dis_dict[dis] += 1
                    else:
                        dis_dict[dis] = 1
            for value in dis_dict.values():
                ans += value*(value-1)
        return ans
```

