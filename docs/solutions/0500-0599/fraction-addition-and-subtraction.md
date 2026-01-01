# [0592. 分数加减运算](https://leetcode.cn/problems/fraction-addition-and-subtraction/)

- 标签：数学、字符串、模拟
- 难度：中等

## 题目链接

- [0592. 分数加减运算 - 力扣](https://leetcode.cn/problems/fraction-addition-and-subtraction/)

## 题目大意

**描述**：

给定一个表示分数加减运算的字符串 $expression$。

**要求**：

返回一个字符串形式的计算结果。

这个结果应该是不可约分的分数，即「最简分数」。

如果最终结果是一个整数，例如 $2$，你需要将它转换成分数形式，其分母为 $1$。所以在上述例子中, $2$ 应该被转换为 $2/1$。

**说明**：

- 输入和输出字符串只包含 `0` 到 `9` 的数字，以及 `/`, `+` 和 `-`。
- 输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 `+` 会被省略掉。
- 输入只包含合法的 最简分数，每个分数的分子与分母的范围是 $[1,10]$。 如果分母是 $1$，意味着这个分数实际上是一个整数。
- 输入的分数个数范围是 $[1,10]$。
- 最终结果的分子与分母保证是 32 位整数范围内的有效整数。

**示例**：

- 示例 1：

```python
输入: expression = "-1/2+1/2"
输出: "0/1"
```

- 示例 2：

```python
输入: expression = "-1/2+1/2+1/3"
输出: "1/3"
```

## 解题思路

### 思路 1：解析字符串并计算

我们需要解析字符串，提取所有分数，然后进行加减运算。

步骤：

1. 解析字符串，提取所有分数。每个分数格式为 $\pm numerator/denominator$，第一个分数可能没有符号（默认为正）。
2. 将所有分数通分后相加。通分需要找到所有分母的最小公倍数 $lcm$，然后将每个分数的分子乘以 $lcm / denominator$。
3. 计算所有分子的和 $sum\_numerator$。
4. 将结果约分到最简形式。需要计算 $gcd(sum\_numerator, lcm)$，然后分子分母同时除以最大公约数。

### 思路 1：代码

```python
import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # 解析所有分数：提取分子和分母
        fractions = re.findall(r'([+-]?\d+)/(\d+)', expression)
        
        # 转换为整数列表
        numerators = []
        denominators = []
        for num_str, den_str in fractions:
            numerators.append(int(num_str))
            denominators.append(int(den_str))
        
        # 计算所有分母的最小公倍数
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        common_denominator = 1
        for den in denominators:
            common_denominator = lcm(common_denominator, den)
        
        # 将所有分数通分并求和
        total_numerator = 0
        for i in range(len(numerators)):
            total_numerator += numerators[i] * (common_denominator // denominators[i])
        
        # 约分到最简形式
        g = gcd(abs(total_numerator), common_denominator)
        total_numerator //= g
        common_denominator //= g
        
        return f"{total_numerator}/{common_denominator}"
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log M)$，其中 $n$ 是分数个数，$M$ 是分母的最大值。需要计算最小公倍数和最大公约数。
- **空间复杂度**：$O(n)$，存储所有分数的分子和分母。
