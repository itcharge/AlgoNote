# [LCR 072. x 的平方根](https://leetcode.cn/problems/jJ0w9p/)

- 标签：数学、二分查找
- 难度：简单

## 题目链接

- [LCR 072. x 的平方根 - 力扣](https://leetcode.cn/problems/jJ0w9p/)

## 题目大意

要求：实现 `int sqrt(int x)` 函数。计算并返回 `x` 的平方根（只保留整数部分），其中 `x` 是非负整数。

## 解题思路

因为求解的是 x 开方的整数部分。所以我们可以从 0~x 的范围进行遍历，找到 k^2 <= x 的最大结果。

为了减少时间复杂度，使用二分查找的方式来搜索答案。

## 代码

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

