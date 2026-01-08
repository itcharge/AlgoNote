# [0878. 第 N 个神奇数字](https://leetcode.cn/problems/nth-magical-number/)

- 标签：数学、二分查找
- 难度：困难

## 题目链接

- [0878. 第 N 个神奇数字 - 力扣](https://leetcode.cn/problems/nth-magical-number/)

## 题目大意

**描述**：

- 一个正整数如果能被 $a$ 或 $b$ 整除，那么它是神奇的。
给定三个整数 $n$ , $a$, $b$。

**要求**：

返回第 $n$ 个神奇的数字。因为答案可能很大，所以返回答案对 $10^9 + 7$ 取模后的值。

**说明**：

- $1 \le n \le 10^{9}$。
- $2 \le a, b \le 4 \times 10^{4}$。

**示例**：

- 示例 1：

```python
输入：n = 1, a = 2, b = 3
输出：2
```

- 示例 2：

```python
输入：n = 4, a = 2, b = 3
输出：6
```

## 解题思路

### 思路 1:二分查找 + 容斥原理

要找第 $n$ 个神奇数字,我们可以使用二分查找。关键是如何计算不超过 $x$ 的神奇数字个数。

根据容斥原理,不超过 $x$ 的神奇数字个数为:
$$count(x) = \lfloor \frac{x}{a} \rfloor + \lfloor \frac{x}{b} \rfloor - \lfloor \frac{x}{lcm(a,b)} \rfloor$$

其中 $lcm(a,b)$ 是 $a$ 和 $b$ 的最小公倍数,可以通过 $lcm(a,b) = \frac{a \times b}{gcd(a,b)}$ 计算。

二分查找的范围:

- 左边界:$1$
- 右边界:$n \times \min(a, b)$

### 思路 1:代码

```python
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math
        
        MOD = 10**9 + 7
        
        # 计算最小公倍数
        lcm = a * b // math.gcd(a, b)
        
        # 计算不超过 x 的神奇数字个数
        def count(x):
            return x // a + x // b - x // lcm
        
        # 二分查找
        left, right = 1, n * min(a, b)
        
        while left < right:
            mid = (left + right) // 2
            if count(mid) < n:
                left = mid + 1
            else:
                right = mid
        
        return left % MOD
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(\log(n \times \min(a, b)))$,二分查找的时间复杂度。
- **空间复杂度**:$O(1)$,只使用常数额外空间。
