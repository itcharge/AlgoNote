# [1175. 质数排列](https://leetcode.cn/problems/prime-arrangements/)

- 标签：数学
- 难度：简单

## 题目链接

- [1175. 质数排列 - 力扣](https://leetcode.cn/problems/prime-arrangements/)

## 题目大意

**描述**：给定一个整数 $n$。从 $1$ 到 $n$ 给你 $n$ 个数和 $n$ 个位置（索引从 $1$ 开始）。要求所有的「质数」都必须放在「质数索引」的位置上。

**要求**：返回可能的排列方案总数。由于答案可能很大，返回结果模 $10^9 + 7$。

**说明**：

- 质数是大于 $1$ 且只能被 $1$ 和自身整除的数。
- $1 \le n \le 10^3$。

**示例**：

- 示例 1：

```python
输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
```

- 示例 2：

```python
输入：n = 100
输出：682289015
```

## 解题思路

### 思路 1：数学 + 排列组合

**为什么用阶乘？** 假设有 $p$ 个质数和 $p$ 个质数位置。第一个质数有 $p$ 个位置可选，第二个有 $p-1$ 个，依此类推，所以排列方式 = $p \times (p-1) \times \cdots \times 1 = p!$。非质数同理。

**拆解步骤**：

1. **统计质数个数**：遍历 $1$ 到 $n$，判断每个数是不是质数。

2. **判断质数的方法**：
   - 小于 $2$ 的不是质数
   - $2$ 是质数
   - 偶数（除了 $2$）不是质数
   - 从 $3$ 到 $\sqrt{n}$，步长为 $2$，检查是否有因子

3. **计算阶乘**：分别计算质数个数的阶乘和（总个数 - 质数个数）的阶乘，每步都取模 $10^9 + 7$。

4. **两个阶乘相乘**，再取模，得到最终答案。

### 思路 1：代码

```python
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # 判断一个数是不是质数
        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            # 只需要检查到 sqrt(num) 就够了
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        # 统计 1 到 n 中有多少个质数
        prime_count = 0
        for i in range(1, n + 1):
            if is_prime(i):
                prime_count += 1

        # 计算阶乘（一边乘一边取模）
        def factorial(num):
            result = 1
            for i in range(1, num + 1):
                result = (result * i) % MOD
            return result

        # 质数排列数 × 非质数排列数
        return (factorial(prime_count) * factorial(n - prime_count)) % MOD
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \sqrt{n})$。用人话说就是：对每个数都要判断它是不是质数，每个判断需要 $\sqrt{n}$ 次除法，所以总时间约等于 $n \times \sqrt{n}$。
- **空间复杂度**：$O(1)$。只用了几个变量，没有额外存储。
