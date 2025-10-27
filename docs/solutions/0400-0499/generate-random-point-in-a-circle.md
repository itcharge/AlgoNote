# [0478. 在圆内随机生成点](https://leetcode.cn/problems/generate-random-point-in-a-circle/)

- 标签：几何、数学、拒绝采样、随机化
- 难度：中等

## 题目链接

- [0478. 在圆内随机生成点 - 力扣](https://leetcode.cn/problems/generate-random-point-in-a-circle/)

## 题目大意

**描述**：

给定圆的半径和圆心的位置。

**要求**：

实现函数 `randPoint`，在圆中产生均匀随机点。

实现 `Solution` 类:

- `Solution(double radius, double x_center, double y_center)` 用圆的半径 $radius$ 和圆心的位置 $(x_center, y_center)$ 初始化对象
- `randPoint()` 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 $[x, y]$。

**说明**：

- $0 \lt radius \le 10^{8}$。
- $-10^{7} \le x\_center, y\_center \le 10^{7}$。
- `randPoint` 最多被调用 $3 \times 10^{4}$ 次。

**示例**：

- 示例 1：

```python
输入: 
["Solution","randPoint","randPoint","randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
解释:
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint ();//返回[-0.02493，-0.38077]
solution.randPoint ();//返回[0.82314,0.38945]
solution.randPoint ();//返回[0.36572,0.17248]
```

## 解题思路

### 思路 1：拒绝采样

这道题要求在圆内生成均匀随机点。最直观的方法是 **拒绝采样（Rejection Sampling）**。

**算法思路**：

1. 在圆的外接正方形区域内随机生成点 $[x, y]$，其中 $x \in [x\_center - radius, x\_center + radius]$，$y \in [y\_center - radius, y\_center + radius]$。
2. 判断点是否在圆内：计算点与圆心的距离 $dist = \sqrt{(x - x\_center)^2 + (y - y\_center)^2}$。
3. 如果 $dist \le radius$，则接受该点；否则拒绝，重新生成。
4. 重复生成直到得到一个在圆内的点。

### 思路 1：代码

```python
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius  # 圆的半径
        self.x_center = x_center  # 圆心 x 坐标
        self.y_center = y_center  # 圆心 y 坐标

    def randPoint(self) -> List[float]:
        # 在外接正方形内生成随机点
        while True:
            # 生成 [x_center - radius, x_center + radius] 范围内的随机 x 坐标
            x = random.uniform(self.x_center - self.radius, self.x_center + self.radius)
            # 生成 [y_center - radius, y_center + radius] 范围内的随机 y 坐标
            y = random.uniform(self.y_center - self.radius, self.y_center + self.radius)
            
            # 计算点到圆心的距离
            dist = ((x - self.x_center) ** 2 + (y - self.y_center) ** 2) ** 0.5
            
            # 如果点在圆内（包括圆周上），则接受该点
            if dist <= self.radius:
                return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$ 期望时间复杂度。由于每次生成点的成功率为 $\frac{\pi r^2}{(2r)^2} = \frac{\pi}{4} \approx 0.785$，期望生成次数为常数级。
- **空间复杂度**：$O(1)$。只使用了常数个变量。
