# [0367. 有效的完全平方数](https://leetcode.cn/problems/valid-perfect-square/)

- 标签：数学、二分查找
- 难度：简单

## 题目链接

- [0367. 有效的完全平方数 - 力扣](https://leetcode.cn/problems/valid-perfect-square/)

## 题目大意

**描述**：给定一个正整数 $num$。

**要求**：判断 num 是不是完全平方数。

**说明**：

- 要求不能使用内置的库函数，如 `sqrt`。
- $1 \le num \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：num = 16
输出：True
解释：返回 true，因为 4 * 4 = 16 且 4 是一个整数。
```

- 示例 2：

```python
输入：num = 14
输出：False
解释：返回 false，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。
```

## 解题思路

### 思路 1：二分查找

如果 $num$ 是完全平方数，则 $num = x \times x$，$x$ 为整数。问题就变为了对于正整数 $num$，是否能找到一个整数 $x$，使得 $x \times x = num$。

而对于 $x$，我们可以通过二分查找算法快速找到。

### 思路 1：代码

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                left = mid
                break
        return left * left == num
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$，其中 $n$ 为正整数 $num$ 的最大值。
- **空间复杂度**：$O(1)$。

