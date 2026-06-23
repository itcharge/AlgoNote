# [1465. 切割后面积最大的蛋糕](https://leetcode.cn/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

- 标签：数组、贪心、排序
- 难度：中等

## 题目链接

- [1465. 切割后面积最大的蛋糕 - 力扣](https://leetcode.cn/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

## 题目大意

**描述**：给定一个矩形蛋糕，高 $h$，宽 $w$。给定两个数组 $horizontalCuts$ 和 $verticalCuts$，分别表示水平和垂直切割的位置。

**要求**：返回切割后面积最大的那一块蛋糕的面积。结果对 $10^9 + 7$ 取模。

**说明**：
- $2 \le h, w \le 10^9$。
- $1 \le cuts.length \le 10^5$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_2.png)

```python
输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
输出：4 
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_3.png)

```python
输入：h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
输出：6
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色和黄色的两份蛋糕面积最大。
```

## 解题思路

### 思路 1：排序 + 最大间隔

#### 1. 核心思想

切割后蛋糕块的面积由相邻水平切割线之间的最大距离和相邻垂直切割线之间的最大距离决定。

最宽的蛋糕块面积 = 最大水平间隔 × 最大垂直间隔。

#### 2. 具体步骤

**第 1 步**：将 $horizontalCuts$ 排序，加入 $0$ 和 $h$ 作为边界。

**第 2 步**：计算所有相邻水平切割线之间的间隔，取最大值 $max\_h$。

**第 3 步**：同理计算 $max\_w$。

**第 4 步**：返回 $max\_h \times max\_w \% MOD$。

#### 3. 举例说明

以 $h=5, w=4, horizontalCuts=[1,3], verticalCuts=[1]$ 为例：

水平间隔：$[0,1,3,5]$ → $max\_h = \max(1-0, 3-1, 5-3) = \max(1,2,2) = 2$

垂直间隔：$[0,1,4]$ → $max\_w = \max(1-0, 4-1) = \max(1,3) = 3$

最大面积 = $2 \times 3 = 6$。

### 思路 1：代码

```python
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7

        # 水平方向最大间隔
        horizontalCuts.sort()
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1])

        # 垂直方向最大间隔
        verticalCuts.sort()
        max_w = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i - 1])

        return (max_h * max_w) % MOD
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n + m \log m)$，排序。
- **空间复杂度**：$O(1)$。
