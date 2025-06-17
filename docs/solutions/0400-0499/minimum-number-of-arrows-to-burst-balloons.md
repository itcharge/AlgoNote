# [0452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)

- 标签：贪心、数组、排序
- 难度：中等

## 题目链接

- [0452. 用最少数量的箭引爆气球 - 力扣](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)

## 题目大意

**描述**：在一个坐标系中有许多球形的气球。对于每个气球，给定气球在 x 轴上的开始坐标和结束坐标 $(x_{start}, x_{end})$。

同时，在 $x$ 轴的任意位置都能垂直发出弓箭，假设弓箭发出的坐标就是 x。那么如果有气球满足 $x_{start} \le x \le x_{end}$，则该气球就会被引爆，且弓箭可以无限前进，可以将满足上述要求的气球全部引爆。

现在给定一个数组 `points`，其中 $points[i] = [x_{start}, x_{end}]$ 代表每个气球的开始坐标和结束坐标。

**要求**：返回能引爆所有气球的最小弓箭数。

**说明**：

- $1 \le points.length \le 10^5$。
- $points[i].length == 2$。
- $-2^{31} \le x_{start} < x_{end} \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用 2 支箭来爆破:
- 在x = 6 处射出箭，击破气球 [2,8] 和 [1,6]。
- 在x = 11 处发射箭，击破气球 [10,16] 和 [7,12]。
```

- 示例 2：

```python
输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要 4 支箭。
```

## 解题思路

### 思路 1：贪心算法

弓箭的起始位置和结束位置可以看做是一段区间，直观上来看，为了使用最少的弓箭数，可以尽量射中区间重叠最多的地方。

所以问题变为了：**如何寻找区间重叠最多的地方，也就是区间交集最多的地方。**

我们将 `points` 按结束坐标升序排序（为什么按照结束坐标排序后边说）。

然后维护两个变量：一个是当前弓箭的坐标 `arrow_pos`、另一个是弓箭的数目 `count`。

为了尽可能的穿过更多的区间，所以每一支弓箭都应该尽可能的从区间的结束位置穿过，这样才能覆盖更多的区间。

初始情况下，第一支弓箭的坐标为第一个区间的结束位置，然后弓箭数为 $1$。然后依次遍历每段区间。

如果遇到弓箭坐标小于区间起始位置的情况，说明该弓箭不能引爆该区间对应的气球，需要用新的弓箭来射，所以弓箭数加 $1$，弓箭坐标也需要更新为新区间的结束位置。

最终返回弓箭数目。

再来看为什么将 `points` 按结束坐标升序排序而不是按照开始坐标升序排序？

其实也可以，但是按开始坐标排序不如按结束坐标排序简单。

按开始坐标升序排序需要考虑一种情况：有交集关系的区间中，有的区间结束位置比较早。比如 `[0, 6]、[1, 2] [4, 5]`，按照开始坐标升序排序的话，就像下图一样：

```
[0..................6]
   [1..2]    
             [4..5]
```

第一箭的位置需要进行迭代判断，取区间 `[0, 6]、[1, 2]` 中结束位置最小的位置，即 `arrow_pos = min(points[i][1], arrow_pos)`，然后再判断接下来的区间是否能够引爆。

而按照结束坐标排序的话，箭的位置一开始就确定了，不需要再改变和判断箭的位置，直接判断区间即可。

### 思路 1：代码

1. 按照结束位置升序排序

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrow_pos = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if arrow_pos < points[i][0]:
                count += 1
                arrow_pos = points[i][1]
        return count
```

2. 按照开始位置升序排序

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[0])
        arrow_pos = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if arrow_pos < points[i][0]:
                count += 1
                arrow_pos = points[i][1]
            else:
                arrow_pos = min(points[i][1], arrow_pos)
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$， 其中 $n$ 是数组 `points` 的长度。
- **空间复杂度**：$O(\log n)$。

