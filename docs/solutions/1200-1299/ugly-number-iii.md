# [1201. 丑数 III](https://leetcode.cn/problems/ugly-number-iii/)

- 标签：数学、二分查找、数论
- 难度：中等

## 题目链接

- [1201. 丑数 III - 力扣](https://leetcode.cn/problems/ugly-number-iii/)

## 题目大意

**描述**：给定四个整数 $n$、$a$、$b$、$c$。

**要求**：返回第 $n$ 个能被 $a$、$b$ 或 $c$ 整除的正整数。

**说明**：

- $1 \le n, a, b, c \le 10^{9}$。
- $1 \le a, b, c \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10...，第 3 个是 4。
```

- 示例 2：

```python
输入：n = 4, a = 2, b = 3, c = 5
输出：6
```

- 示例 3：

```python
输入：n = 5, a = 2, b = 3, c = 5
输出：6
```

## 解题思路

### 思路 1：二分查找 + 容斥原理

#### 1. 核心思想

直接找到第 $n$ 个丑数比较困难，但我们可以反过来：**给定一个数 $x$，计算 $[1, x]$ 中有多少个丑数（能被 $a$、$b$ 或 $c$ 整除的数）**。这个计算可以用**容斥原理**在 $O(1)$ 时间内完成。

然后**二分查找**最小的 $x$，使得 $[1, x]$ 中丑数的数量 $\ge n$。

#### 2. 容斥原理

$[1, x]$ 中能被 $a$ 或 $b$ 或 $c$ 整除的数的数量：

$$count = \lfloor x/a \rfloor + \lfloor x/b \rfloor + \lfloor x/c \rfloor$$
$$- \lfloor x/lcm(a,b) \rfloor - \lfloor x/lcm(b,c) \rfloor - \lfloor x/lcm(a,c) \rfloor$$
$$+ \lfloor x/lcm(a,b,c) \rfloor$$

其中 $lcm$ 是**最小公倍数**。

#### 3. 具体步骤

**第 1 步**：计算 $a$、$b$、$c$ 两两的最小公倍数 $lcm_{ab}$、$lcm_{bc}$、$lcm_{ac}$，以及三者的最小公倍数 $lcm_{abc}$。

**第 2 步**：在区间 $[1, 2 \times 10^{9}]$ 内二分查找：
- 计算 $mid$ 处的丑数数量 $count$。
- 如果 $count \ge n$，缩小右边界（因为要找的是第一个满足条件的 $x$）。
- 否则扩大左边界。

**第 3 步**：返回左边界。

#### 4. 结合示例走一遍

$a=2, b=3, c=5$

二分查找第 $3$ 个丑数：

```
x=10: count(10) = 10/2 + 10/3 + 10/5 - 10/6 - 10/15 - 10/10 + 10/30
               = 5 + 3 + 2 - 1 - 0 - 1 + 0 = 8 ≥ 3, 缩右
x=5:  count(5) = 5/2 + 5/3 + 5/5 - 5/6 - 5/15 - 5/10 + 5/30
               = 2 + 1 + 1 - 0 - 0 - 0 + 0 = 4 ≥ 3, 缩右
x=3:  count(3) = 3/2 + 3/3 + 3/5 - 3/6 - 3/15 - 3/10 + 3/30
               = 1 + 1 + 0 - 0 - 0 - 0 + 0 = 2 < 3, 扩左
x=4:  count(4) = 4/2 + 4/3 + 4/5 - 4/6 - 4/15 - 4/10 + 4/30
               = 2 + 1 + 0 - 0 - 0 - 0 + 0 = 3 ≥ 3, 缩右
```

结果为 $4$。

### 思路 1：代码

```python
import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # 计算最小公倍数
        lcm_ab = a // math.gcd(a, b) * b
        lcm_bc = b // math.gcd(b, c) * c
        lcm_ac = a // math.gcd(a, c) * c
        lcm_abc = lcm_ab // math.gcd(lcm_ab, c) * c

        def count_ugly(x: int) -> int:
            """计算 [1, x] 中能被 a、b 或 c 整除的数的个数"""
            return (x // a + x // b + x // c
                    - x // lcm_ab - x // lcm_bc - x // lcm_ac
                    + x // lcm_abc)

        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if count_ugly(mid) >= n:
                right = mid
            else:
                left = mid + 1
        return left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log(2 \times 10^{9})) \approx O(31)$，二分查找约 $31$ 次，每次 $O(1)$ 计算容斥。
- **空间复杂度**：$O(1)$。
