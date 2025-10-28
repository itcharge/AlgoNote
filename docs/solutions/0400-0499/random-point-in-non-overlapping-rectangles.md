# [0497. 非重叠矩形中的随机点](https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/)

- 标签：水塘抽样、数组、数学、二分查找、有序集合、前缀和、随机化
- 难度：中等

## 题目链接

- [0497. 非重叠矩形中的随机点 - 力扣](https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/)

## 题目大意

**描述**：

给定一个由非重叠的轴对齐矩形的数组 $rects$ ，其中 $rects[i] = [ai, bi, xi, yi]$ 表示 $(ai, bi)$ 是第 $i$ 个矩形的左下角点，$(xi, yi)$ 是第 $i$ 个矩形的右上角点。

**要求**：

设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。

在给定的矩形覆盖的空间内的任何整数点都有可能被返回。

实现 `Solution` 类:

- `Solution(int[][] rects)` 用给定的矩形数组 $rects$ 初始化对象。
- `int[] pick()` 返回一个随机的整数点 $[u, v]$ 在给定的矩形所覆盖的空间内。

**说明**：

- 整数点是具有整数坐标的点。
- $1 \le rects.length \le 10^{3}$。
- $rects[i].length == 4$。
- $-10^{9} \le ai \lt xi \le 10^{9}$。
- $-10^{9} \le bi \lt yi \le 10^{9}$。
- $xi - ai \le 2000$。
- $yi - bi \le 2000$。
- 所有的矩形不重叠。
- $pick$ 最多被调用 $10^{4}$ 次。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/07/24/lc-pickrandomrec.jpg)

```python
输入: 
["Solution", "pick", "pick", "pick", "pick", "pick"]
[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
输出: 
[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]

解释：
Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // 返回 [1, -2]
solution.pick(); // 返回 [1, -1]
solution.pick(); // 返回 [-1, -2]
solution.pick(); // 返回 [-2, -2]
solution.pick(); // 返回 [0, 0]
```

## 解题思路

### 思路 1：前缀和 + 二分查找

这道题的关键是要让所有满足要求的点等概率被返回。

我们可以将问题分成两步：

1. **随机选择一个矩形**：由于不同矩形包含的点数不同，我们需要根据点数加权随机选择一个矩形。
2. **在选中的矩形内随机选一个点**：在矩形内均匀随机选择整数点坐标。

具体实现：

对于每个矩形 $rects[i] = [a_i, b_i, x_i, y_i]$，它包含的点数为：
$count_i = (x_i - a_i + 1) \times (y_i - b_i + 1)$

我们在初始化时：

- 计算每个矩形的点数 $count_i$。
- 建立前缀和数组 $prefix$，其中 $prefix[i] = \sum_{j=0}^{i} count_j$。
- 记录所有矩形信息。

在调用 `pick()` 时：

- 生成一个随机整数 $target$，范围为 $[1, prefix[n-1]]$。
- 使用二分查找找到第一个 $prefix[i] \ge target$ 的矩形索引 $i$。
- 在矩形 $i$ 内随机选择一个点：横坐标在 $[a_i, x_i]$ 范围内随机，纵坐标在 $[b_i, y_i]$ 范围内随机。
- 返回该点的坐标 $[rand_x, rand_y]$。

这样就能保证每个点被选中的概率相等。

### 思路 1：代码

```python
import random
import bisect

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # prefix[i] 表示前 i 个矩形（包括第 i 个）包含的总点数
        self.prefix = []
        
        # 计算每个矩形的点数并建立前缀和数组
        for a, b, x, y in rects:
            # 计算矩形包含的点数：(x - a + 1) * (y - b + 1)
            count = (x - a + 1) * (y - b + 1)
            # 前缀和为前一个值加上当前矩形的点数
            if self.prefix:
                self.prefix.append(self.prefix[-1] + count)
            else:
                self.prefix.append(count)

    def pick(self) -> List[int]:
        # 在 [1, prefix[-1]] 范围内随机选择一个目标值
        target = random.randint(1, self.prefix[-1])
        
        # 使用二分查找找到目标值所在的矩形索引
        # bisect_left 返回第一个 >= target 的位置
        rect_idx = bisect.bisect_left(self.prefix, target)
        
        # 获取对应矩形
        a, b, x, y = self.rects[rect_idx]
        
        # 在矩形内随机选择点的横坐标和纵坐标
        rand_x = random.randint(a, x)
        rand_y = random.randint(b, y)
        
        return [rand_x, rand_y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 初始化：$O(n)$，其中 $n$ 是矩形数量。需要遍历所有矩形计算前缀和。
  - `pick()` 方法：$O(\log n)$。二分查找时间为 $O(\log n)$。
- **空间复杂度**：$O(n)$。需要存储前缀和数组。
