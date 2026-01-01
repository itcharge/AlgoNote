# [0507. 完美数](https://leetcode.cn/problems/perfect-number/)

- 标签：数学
- 难度：简单

## 题目链接

- [0507. 完美数 - 力扣](https://leetcode.cn/problems/perfect-number/)

## 题目大意

**描述**：

对于一个「正整数」，如果它和除了它自身以外的所有「正因子」之和相等，我们称它为「完美数」。

给定一个整数 $n$。

**要求**：

如果是完美数，返回 true；否则返回 false。

**说明**：

- $1 \le num \le 10^{8}$。

**示例**：

- 示例 1：

```python
输入：num = 28
输出：true
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。
```

- 示例 2：

```python
输入：num = 7
输出：false
```

## 解题思路

### 思路 1：枚举因子

完美数的定义：一个正整数等于它所有正因子（不包括自身）之和。

我们可以枚举从 $1$ 到 $\sqrt{num}$ 的所有因子。对于每个因子 $i$：

- 如果 $num \% i == 0$，那么 $i$ 和 $num / i$ 都是因子（注意 $i \neq num / i$ 时，两个都要加上）。
- 累加所有因子，最后检查是否等于 $num$。

注意：$1$ 不是完美数（因为 $1$ 没有除了自身以外的正因子）。

### 思路 1：代码

```python
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        
        factor_sum = 1  # 1 是因子
        # 枚举从 2 到 sqrt(num) 的因子
        i = 2
        while i * i <= num:
            if num % i == 0:
                factor_sum += i
                # 如果 i != num / i，也要加上 num / i
                if i != num // i:
                    factor_sum += num // i
            i += 1
        
        return factor_sum == num
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\sqrt{num})$，需要枚举到 $\sqrt{num}$ 的所有因子。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
