# [2427. 公因子的数目](https://leetcode.cn/problems/number-of-common-factors/)

- 标签：数学、枚举、数论
- 难度：简单

## 题目链接

- [2427. 公因子的数目 - 力扣](https://leetcode.cn/problems/number-of-common-factors/)

## 题目大意

**描述**：给定两个正整数 $a$ 和 $b$。

**要求**：返回 $a$ 和 $b$ 的公因子数目。

**说明**：

- **公因子**：如果 $x$ 可以同时整除 $a$ 和 $b$，则认为 $x$ 是 $a$ 和 $b$ 的一个公因子。
- $1 \le a, b \le 1000$。

**示例**：

- 示例 1：

```python
输入：a = 12, b = 6
输出：4
解释：12 和 6 的公因子是 1、2、3、6。
```

- 示例 2：

```python
输入：a = 25, b = 30
输出：2
解释：25 和 30 的公因子是 1、5。
```

## 解题思路

### 思路 1：枚举算法

最直接的思路就是枚举所有 $[1, min(a, b)]$ 之间的数，并检查是否能同时整除 $a$ 和 $b$。

当然，因为 $a$ 与 $b$ 的公因子肯定不会超过 $a$ 与 $b$ 的最大公因数，则我们可以直接枚举 $[1, gcd(a, b)]$ 之间的数即可，其中 $gcd(a, b)$ 是 $a$ 与 $b$ 的最大公约数。

### 思路 1：代码

```python
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, math.gcd(a, b) + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\sqrt{min(a, b)})$。
- **空间复杂度**：$O(1)$。
