# [0069. x 的平方根](https://leetcode.cn/problems/sqrtx/)

- 标签：数学、二分查找
- 难度：简单

## 题目链接

- [0069. x 的平方根 - 力扣](https://leetcode.cn/problems/sqrtx/)

## 题目大意

**要求**：实现 `int sqrt(int x)` 函数。计算并返回 $x$ 的平方根（只保留整数部分），其中 $x$ 是非负整数。

**说明**：

- $0 \le x \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：x = 4
输出：2
```

- 示例 2：

```python
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
```

## 解题思路

### 思路 1：二分查找

因为求解的是 $x$ 开方的整数部分。所以我们可以从 $0 \sim x$ 的范围进行遍历，找到 $k^2 \le x$ 的最大结果。

为了减少算法的时间复杂度，我们使用二分查找的方法来搜索答案。

### 思路 1：代码

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。二分查找算法的时间复杂度为 $O(\log n)$。
- **空间复杂度**：$O(1)$。只用到了常数空间存放若干变量。

