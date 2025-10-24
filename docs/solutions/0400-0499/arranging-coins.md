# [0441. 排列硬币](https://leetcode.cn/problems/arranging-coins/)

- 标签：数学、二分查找
- 难度：简单

## 题目链接

- [0441. 排列硬币 - 力扣](https://leetcode.cn/problems/arranging-coins/)

## 题目大意

**描述**：

你总共有 $n$ 枚硬币，并计划将它们按阶梯状排列。对于一个由 $k$ 行组成的阶梯，其第 $i$ 行必须正好有 $i$ 枚硬币。阶梯的最后一行 可能 是不完整的。

给定一个数字 $n$。

**要求**：

计算并返回可形成「完整阶梯行」的总行数。

**说明**：

- $1 \le n \le 2^{31} - 1$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg)

```python
输入：n = 5
输出：2
解释：因为第三行不完整，所以返回 2 。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg)

```python
输入：n = 8
输出：3
解释：因为第四行不完整，所以返回 3 。
```

## 解题思路

### 思路 1：数学公式

1. 我们需要找到最大的完整行数 $k$，使得前 $k$ 行使用的硬币总数不超过 $n$。
2. 前 $k$ 行使用的硬币总数为：$1 + 2 + 3 + \cdots + k = \frac{k(k+1)}{2}$。
3. 我们需要找到最大的 $k$，使得 $\frac{k(k+1)}{2} \leq n$。
4. 解这个不等式：$k^2 + k - 2n \leq 0$。
5. 使用求根公式：$k = \frac{-1 + \sqrt{1 + 8n}}{2}$。
6. 由于 $k$ 必须是正整数，我们取 $\lfloor \frac{-1 + \sqrt{1 + 8n}}{2} \rfloor$。

### 思路 1：代码

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 使用数学公式直接计算
        # k = floor((-1 + sqrt(1 + 8n)) / 2)
        return int((-1 + math.sqrt(1 + 8 * n)) // 2)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$，只需要一次数学计算。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
