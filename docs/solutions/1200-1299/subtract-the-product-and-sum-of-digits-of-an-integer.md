# [1281. 整数的各位积和之差](https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

- 标签：数学
- 难度：简单

## 题目链接

- [1281. 整数的各位积和之差 - 力扣](https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

## 题目大意

**描述**：给定一个整数 `n`。

**要求**：计算并返回该整数「各位数字之积」与「各位数字之和」的差。

**说明**：

- $1 <= n <= 10^5$。

**示例**：

- 示例 1：

```python
输入：n = 234
输出：15

解释：
各位数之积 2 * 3 * 4 = 24 
各位数之和 2 + 3 + 4 = 9 
结果 24 - 9 = 15
```

## 解题思路

### 思路 1：数学

- 通过取模运算得到 `n` 的最后一位，即 `n %= 10`。
- 然后去除  `n`  的最后一位，及`n //= 10`。
- 一次求出各位数字之积与各位数字之和，并返回其差值。

### 思路 1：数学代码

```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10
        return product - total
```

