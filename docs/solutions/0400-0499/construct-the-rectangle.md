# [0492. 构造矩形](https://leetcode.cn/problems/construct-the-rectangle/)

- 标签：数学
- 难度：简单

## 题目链接

- [0492. 构造矩形 - 力扣](https://leetcode.cn/problems/construct-the-rectangle/)

## 题目大意

**描述**：

作为一位 web 开发者， 懂得怎样去规划一个页面的尺寸是很重要的。所以，现给定一个具体的矩形页面面积，你的任务是设计一个长度为 $L$ 和宽度为 $W$ 且满足以下要求的矩形的页面。

**要求**：

1. 你设计的矩形页面必须等于给定的目标面积。
2. 宽度 $W$ 不应大于长度 $L$，换言之，要求 $L \ge W$。
3. 长度 $L$ 和宽度 $W$ 之间的差距应当尽可能小。

返回一个 数组 $[L, W]$，其中 $L$ 和 $W$ 是你按照顺序设计的网页的长度和宽度。

**说明**：

- $1 \le area \le 10^{7}$。

**示例**：

- 示例 1：

```python
输入: 4
输出: [2, 2]
解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
```

- 示例 2：

```python
输入: area = 37
输出: [37,1]
```

## 解题思路

### 思路 1：数学方法

1. 我们需要找到两个整数 $L$ 和 $W$，使得 $L \times W = area$ 且 $L \geq W$，并且 $L - W$ 尽可能小。
2. 由于 $L \geq W$，我们可以从 $W = \lfloor \sqrt{area} \rfloor$ 开始向下遍历，找到第一个能整除 $area$ 的 $W$。
3. 这样找到的 $W$ 是最大的可能宽度，对应的 $L = \frac{area}{W}$ 是最小的可能长度，从而使得 $L - W$ 最小。
4. 如果 $area$ 是完全平方数，则 $L = W = \sqrt{area}$ 是最优解。

### 思路 1：代码

```python
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # 从 sqrt(area) 开始向下遍历，找到最大的能整除 area 的宽度
        width = int(area ** 0.5)
        
        # 向下遍历，找到第一个能整除 area 的宽度
        while width > 0:
            if area % width == 0:
                # 找到能整除的宽度，计算对应的长度
                length = area // width
                return [length, width]
            width -= 1
        
        # 理论上不会到达这里，因为 width=1 时一定能整除
        return [area, 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\sqrt{area})$，最坏情况下需要遍历从 $\sqrt{area}$ 到 $1$ 的所有整数。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
