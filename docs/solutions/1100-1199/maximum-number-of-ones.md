# [1183. 矩阵中 1 的最大数量](https://leetcode.cn/problems/maximum-number-of-ones/)

- 标签：贪心、数学、排序、堆（优先队列）
- 难度：困难

## 题目链接

- [1183. 矩阵中 1 的最大数量 - 力扣](https://leetcode.cn/problems/maximum-number-of-ones/)

## 题目大意

**描述**：有一个 $width \times height$ 的矩阵，元素只能是 $0$ 或 $1$。限制条件是：矩阵中每个大小为 $sideLength \times sideLength$ 的正方形子阵里，$1$ 的数量不能超过 $maxOnes$。

**要求**：整个矩阵中最多能放多少个 $1$？

**说明**：

- $1 \le width, height \le 10^3$。
- $1 \le sideLength \le width, height$。
- $0 \le maxOnes \le sideLength \times sideLength$。

**示例**：

```python
输入：width=3, height=3, sideLength=2, maxOnes=1
输出：4
```

## 解题思路

### 思路 1：周期性 + 贪心

这道题的关键在于理解矩阵的**周期性结构**。因为约束条件是针对每一个 $sideLength \times sideLength$ 的子阵的，所以整个矩阵可以看作由多个这样的子阵平铺而成。

**核心观察：** 把整个矩阵按 $sideLength$ 分成若干块，每个块中相同「模板位置」的格子，在约束上受到相同的限制。

用人话讲：如果我们把矩阵划分成一个个 $sideLength \times sideLength$ 的块，那么每个块中位置 $[r][c]$（比如左上角）在所有块中都受到相同的限制——要么全是 1，要么全是 0。

**所以策略是：**

1. 对于模板（$sideLength \times sideLength$）中的每个位置 $(r, c)$，计算它在整个矩阵中出现了多少次（即它的「贡献」）。

2. 把所有位置的贡献从大到小排序。

3. 因为每个子阵中 1 最多 $maxOnes$ 个，我们最多选 $maxOnes$ 个模板位置设为 1。贪心地选贡献最大的那些位置，就能让总共的 1 的数量最大。

**步骤拆解：**

1. 遍历模板的每个位置 $(r, c)$：
   - 计算它在行方向上的出现次数：$(height - r + sideLength - 1) / sideLength$（向上取整）。
   - 计算它在列方向上的出现次数：$(width - c + sideLength - 1) / sideLength$（向上取整）。
   - 总贡献 = 行方向次数 × 列方向次数。

2. 把所有贡献按从大到小排序。

3. 取前 $maxOnes$ 个贡献值相加，即为最大 1 的数量。

### 思路 1：代码

```python
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        contributions = []
        
        # 遍历 $sideLength \times sideLength$ 模板中的每个位置
        for r in range(sideLength):
            for c in range(sideLength):
                # 该位置在行方向（纵向）上出现的次数
                row_count = (height - r + sideLength - 1) // sideLength
                # 该位置在列方向（横向）上出现的次数
                col_count = (width - c + sideLength - 1) // sideLength
                contribution = row_count * col_count
                contributions.append(contribution)
        
        # 从大到小排序，取前 maxOnes 个
        contributions.sort(reverse=True)
        
        return sum(contributions[:maxOnes])
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(sideLength^2 \log sideLength)$。主要是排序的时间。
- **空间复杂度**：$O(sideLength^2)$。存储模板中每个位置的贡献。
