# [0625. 最小因式分解](https://leetcode.cn/problems/minimum-factorization/)

- 标签：贪心、数学
- 难度：中等

## 题目链接

- [0625. 最小因式分解 - 力扣](https://leetcode.cn/problems/minimum-factorization/)

## 题目大意

**描述**：

给定一个正整数 $num$。

**要求**：

找出最小的正整数 $x$ 使得 $x$ 的所有数位相乘恰好等于 $num$。

如果不存在这样的结果或者结果不是 32 位有符号整数，返回 $0$。

**说明**：

- $1 \le num \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：num = 48
输出：68
```

- 示例 2：

```python
输入：num = 15
输出：35
```

## 解题思路

### 思路 1：贪心 + 因数分解

#### 思路 1：算法描述

要找到最小的正整数 $x$，使得 $x$ 的所有数位相乘等于 `num`。

**核心思路**：

- 为了让 $x$ 最小，应该让 $x$ 的位数尽可能少，每一位尽可能大。
- 从 $9$ 到 $2$ 依次尝试分解 `num`，将因子从小到大排列（贪心：让结果最小）。
- 特殊情况：如果 $num < 10$，直接返回 `num`。

**算法步骤**：

1. 如果 $num < 10$，直接返回 `num`。
2. 从 $9$ 到 $2$ 依次尝试分解 `num`：
   - 如果 `num` 能被 $i$ 整除，将 $i$ 加入结果列表。
   - 继续分解 $num / i$。
3. 如果最后 $num > 1$，说明无法分解（存在大于 $9$ 的质因子），返回 $0$。
4. 将结果列表从小到大排列并转换为整数，检查是否超过 32 位整数范围。

#### 思路 1：代码

```python
class Solution:
    def smallestFactorization(self, num: int) -> int:
        # 特殊情况
        if num < 10:
            return num
        
        # 从 9 到 2 依次分解
        digits = []
        for i in range(9, 1, -1):
            while num % i == 0:
                digits.append(i)
                num //= i
        
        # 如果 num > 1，说明存在大于 9 的质因子，无法分解
        if num > 1:
            return 0
        
        # 将数字从小到大排列（贪心：让结果最小）
        digits.sort()
        
        # 转换为整数
        result = 0
        for digit in digits:
            result = result * 10 + digit
        
        # 检查是否超过 32 位整数范围
        if result > 2**31 - 1:
            return 0
        
        return result
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(\log num)$，需要分解 `num` 的所有因子。
- **空间复杂度**：$O(\log num)$，需要存储分解后的数字。
