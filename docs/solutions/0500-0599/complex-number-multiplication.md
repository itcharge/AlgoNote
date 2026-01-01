# [0537. 复数乘法](https://leetcode.cn/problems/complex-number-multiplication/)

- 标签：数学、字符串、模拟
- 难度：中等

## 题目链接

- [0537. 复数乘法 - 力扣](https://leetcode.cn/problems/complex-number-multiplication/)

## 题目大意

**描述**：

复数可以用字符串表示，遵循 "实部 + 虚部 i" 的形式，并满足下述条件：

- 实部 是一个整数，取值范围是 $[-100, 100]$。
- 虚部 也是一个整数，取值范围是 $[-100, 100]$。
- $i^2 == -1$。

给定两个字符串表示的复数 $num1$ 和 $num2$。

**要求**：

遵循复数表示形式，返回表示它们乘积的字符串。

**说明**：

- $num1$ 和 $num2$ 都是有效的复数表示。

**示例**：

- 示例 1：

```python
输入：num1 = "1+1i", num2 = "1+1i"
输出："0+2i"
解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
```

- 示例 2：

```python
输入：num1 = "1+-1i", num2 = "1+-1i"
输出："0+-2i"
解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。
```

## 解题思路

### 思路 1：解析并计算

复数乘法的公式：$(a + bi) \times (c + di) = (ac - bd) + (ad + bc)i$

步骤：

1. 解析两个复数字符串，提取实部 $a, c$ 和虚部 $b, d$
2. 计算结果的实部：$ac - bd$
3. 计算结果的虚部：$ad + bc$
4. 格式化输出结果

### 思路 1：代码

```python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # 解析 num1: 格式为 "a+bi" 或 "a+-bi"
        def parse_complex(num_str: str) -> tuple:
            # 找到 '+' 的位置（可能是最后一个 '+'）
            plus_idx = num_str.rfind('+')
            real = int(num_str[:plus_idx])
            # 虚部去掉 'i'
            imag = int(num_str[plus_idx + 1:-1])
            return real, imag
        
        # 解析两个复数
        a, b = parse_complex(num1)
        c, d = parse_complex(num2)
        
        # 计算复数乘法：(a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = a * c - b * d
        imag_part = a * d + b * c
        
        # 格式化输出
        return f"{real_part}+{imag_part}i"
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$，字符串解析和计算都是常数时间。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
