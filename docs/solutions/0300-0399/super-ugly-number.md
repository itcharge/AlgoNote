# [0313. 超级丑数](https://leetcode.cn/problems/super-ugly-number/)

- 标签：数组、数学、动态规划
- 难度：中等

## 题目链接

- [0313. 超级丑数 - 力扣](https://leetcode.cn/problems/super-ugly-number/)

## 题目大意

**描述**：

「超级丑数」是一个正整数，并满足其所有质因数都出现在质数数组 $primes$ 中。

给定一个整数 $n$ 和一个整数数组 $primes$。

**要求**：

返回第 $n$ 个 超级丑数。

**说明**：

- 题目数据保证第 $n$ 个「超级丑数」在 $32-bit$ 带符号整数范围内。
- $1 \le n \le 10^{5}$。
- $1 \le primes.length \le 10^{3}$。
- $2 \le primes[i] \le 10^{3}$。
- 题目数据 保证 $primes[i]$ 是一个质数。
- $primes$ 中的所有值都「互不相同」，且按「递增顺序」排列。

**示例**：

- 示例 1：

```python
输入：n = 12, primes = [2,7,13,19]
输出：32 
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
```

- 示例 2：

```python
输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
```

## 解题思路

### 思路 1：动态规划 + 多指针

**核心思想**：超级丑数是只包含给定质数数组中质因数的正整数。我们可以使用动态规划的思想，维护一个数组 $dp$ 来存储前 $n$ 个超级丑数，并使用多个指针来跟踪每个质数应该与哪个超级丑数相乘。

**数学原理**：

- 超级丑数序列：$1, p_1, p_2, p_1^2, p_1 \times p_2, p_2^2, p_1^3, ...$
- 每个超级丑数都可以表示为：$dp[i] = \min(dp[pointer[j]] \times primes[j])$，其中 $j$ 遍历所有质数
- 当 $dp[i] = dp[pointer[j]] \times primes[j]$ 时，将 $pointer[j]$ 加 1

**算法步骤**：

1. **初始化**：创建数组 $dp$ 存储超级丑数，$dp[0] = 1$。创建指针数组 $pointers$，初始化为全 0。

2. **动态规划计算**：对于 $i$ 从 1 到 $n-1$：
   - 计算所有可能的候选值：$candidates[j] = dp[pointers[j]] \times primes[j]$
   - 找到最小值：$dp[i] = \min(candidates)$
   - 更新指针：对于所有 $j$，如果 $dp[i] = candidates[j]$，则 $pointers[j]++$

3. **返回结果**：返回 $dp[n-1]$。

### 思路 1：代码

```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # dp[i] 表示第 i+1 个超级丑数
        dp = [0] * n
        dp[0] = 1  # 第一个超级丑数是 1
        
        # pointers[j] 表示 primes[j] 应该与 dp[pointers[j]] 相乘
        pointers = [0] * len(primes)
        
        # 计算第 2 到第 n 个超级丑数
        for i in range(1, n):
            # 计算所有可能的候选值
            candidates = [dp[pointers[j]] * primes[j] for j in range(len(primes))]
            
            # 找到最小值作为下一个超级丑数
            dp[i] = min(candidates)
            
            # 更新指针：如果当前超级丑数等于某个候选值，则对应指针加 1
            for j in range(len(primes)):
                if dp[i] == dp[pointers[j]] * primes[j]:
                    pointers[j] += 1
        
        return dp[n - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times k)$，其中 $n$ 是要求的超级丑数个数，$k$ 是质数数组的长度。对于每个超级丑数，我们需要遍历所有质数来计算候选值并更新指针。
- **空间复杂度**：$O(n + k)$，其中 $O(n)$ 用于存储 $dp$ 数组，$O(k)$ 用于存储 $pointers$ 数组。
