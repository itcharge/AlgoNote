# [0372. 超级次方](https://leetcode.cn/problems/super-pow/)

- 标签：数学、分治
- 难度：中等

## 题目链接

- [0372. 超级次方 - 力扣](https://leetcode.cn/problems/super-pow/)

## 题目大意

**描述**：

给定两个正整数 $a$ 和 $b$。其中 $b$ 是一个非常大的正整数且会以数组形式给出。

**要求**：

计算 $a^b$ 对 $1337$ 取模。

**说明**：

- $1 \le a \le 2^{31} - 1$。
- $1 \le b.length \le 2000$。
- $0 \le b[i] \le 9$。
- $b$ 不含前导 $0$。

**示例**：

- 示例 1：

```python
输入：a = 2, b = [3]
输出：8
```

- 示例 2：

```python
输入：a = 2, b = [1,0]
输出：1024
```

## 解题思路

### 思路 1：快速幂 + 模运算

**核心思想**：由于 $b$ 是一个非常大的数（以数组形式给出），直接计算 $a^b$ 会导致溢出。我们可以使用快速幂算法结合模运算的性质来高效计算 $a^b \bmod 1337$。

**数学原理**：

- 模运算性质：$(a \times b) \bmod m = ((a \bmod m) \times (b \bmod m)) \bmod m$
- 幂运算性质：$a^{b_1b_2...b_n} = a^{b_1 \times 10^{n-1}} \times a^{b_2 \times 10^{n-2}} \times ... \times a^{b_n}$
- 快速幂：$a^n = \begin{cases} 
  (a^{n/2})^2 & \text{if } n \text{ is even} \\
  a \times a^{n-1} & \text{if } n \text{ is odd}
  \end{cases}$

**算法步骤**：

1. **处理数组形式的指数**：将数组 $b$ 转换为实际的指数值，但由于 $b$ 可能非常大，我们需要逐位处理。

2. **快速幂计算**：对于每一位数字 $b[i]$，计算 $a^{b[i] \times 10^{n-i-1}} \bmod 1337$。

3. **模运算优化**：在每次乘法运算后都进行模运算，避免数值溢出。

4. **逐位累乘**：将每一位的结果相乘并对 $1337$ 取模。

### 思路 1：代码

```python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # 模数
        MOD = 1337
        
        # 快速幂函数：计算 base^exp % MOD
        def quick_pow(base: int, exp: int) -> int:
            result = 1
            base %= MOD  # 先对底数取模
            while exp > 0:
                if exp & 1:  # 如果指数是奇数
                    result = (result * base) % MOD
                base = (base * base) % MOD  # 底数平方
                exp >>= 1  # 指数右移一位（相当于除以2）
            return result
        
        # 处理数组形式的指数
        result = 1
        for digit in b:
            # 对于每一位数字，先计算 result^10，再乘以 a^digit
            result = quick_pow(result, 10)  # result^10 % MOD
            result = (result * quick_pow(a, digit)) % MOD  # 乘以 a^digit % MOD
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log k)$，其中 $n$ 是数组 $b$ 的长度，$k$ 是最大的指数值（最大为 $9$）。对于数组中的每一位数字，我们需要调用快速幂函数，快速幂的时间复杂度为 $O(\log k)$，总共有 $n$ 位数字。
- **空间复杂度**：$O(1)$，只使用了常数额外空间，没有使用额外的数据结构。
