# [1523. 在区间范围内统计奇数数目](https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/)

- 标签：数学
- 难度：简单

## 题目链接

- [1523. 在区间范围内统计奇数数目 - 力扣](https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/)

## 题目大意

**描述**：给定两个非负整数 `low` 和 `high`。

**要求**：返回 `low` 与 `high` 之间（包括二者）的奇数数目。

**说明**：

- $0 \le low \le high \le 10^9$。

**示例**：

- 示例 1：

```python
输入：low = 3, high = 7
输出：3
解释：3 到 7 之间奇数数字为 [3,5,7]
```

## 解题思路

### 思路 1：

暴力枚举 `[low, high]` 之间的奇数可能会超时。我们可以通过公式直接计算出 `[0, low - 1]` 之间的奇数个数和 `[0, high]` 之间的奇数个数，然后将两者相减即为答案。

计算奇数个数的公式为：$pre(x) = \lfloor \frac{x + 1}{2} \rfloor$。

## 代码

### 思路 1 代码：

```python
class Solution:
    def pre(self, val):
        return (val + 1) >> 1

    def countOdds(self, low: int, high: int) -> int:
        return self.pre(high) - self.pre(low - 1)
```

