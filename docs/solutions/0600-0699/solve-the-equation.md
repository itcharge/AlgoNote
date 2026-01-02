# [0640. 求解方程](https://leetcode.cn/problems/solve-the-equation/)

- 标签：数学、字符串、模拟
- 难度：中等

## 题目链接

- [0640. 求解方程 - 力扣](https://leetcode.cn/problems/solve-the-equation/)

## 题目大意

**描述**：

给定一个方程 $equation$。

**要求**：

求解一个给定的方程，将 $x$ 以字符串 `"x=#value"` 的形式返回。该方程仅包含 `'+'`，`'-'` 操作，变量 $x$ 和其对应系数。

如果方程没有解或存在的解不为整数，请返回 `"No $solution$"` 。如果方程有无限解，则返回 `"Infinite solutions"`。

题目保证，如果方程中只有一个解，则 `'x'` 的值是一个整数。

**说明**：

- $3 \le equation.length \le 10^{3}$。
- $equation$ 只有一个 `'='`。
- 方程由绝对值在 $[0, 10^{3}]$ 范围内且无任何前导零的整数和变量 `'x'` 组成。

**示例**：

- 示例 1：

```python
输入: equation = "x+5-3+x=6+x-2"
输出: "x=2"
```

- 示例 2：

```python
输入: equation = "x=x"
输出: "Infinite solutions"
```

## 解题思路

### 思路 1：字符串解析 + 模拟

这道题目要求求解一元一次方程。需要解析方程字符串，分别统计等号左右两边的 $x$ 的系数和常数项。

1. 将方程按 '=' 分割成左右两部分。
2. 对于每一部分，解析出 $x$ 的系数和常数项：
   - 遍历字符串，识别数字、符号和变量 $x$。
   - 如果是 $x$ 的系数，累加到 $x\_coef$。
   - 如果是常数，累加到 $const$。
3. 将右边的系数和常数移到左边（符号取反）。
4. 根据最终的系数和常数判断：
   - 如果系数为 0 且常数为 0，返回 "Infinite solutions"。
   - 如果系数为 0 且常数不为 0，返回 "No solution"。
   - 否则，返回 "x=#value"，其中 value = -常数 / 系数。

### 思路 1：代码

```python
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(s):
            """解析表达式，返回 x 的系数和常数项"""
            x_coef = 0
            const = 0
            i = 0
            n = len(s)
            
            while i < n:
                # 读取符号
                sign = 1
                if s[i] == '+':
                    i += 1
                elif s[i] == '-':
                    sign = -1
                    i += 1
                
                # 读取数字
                num = 0
                has_num = False
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    has_num = True
                    i += 1
                
                # 判断是 x 还是常数
                if i < n and s[i] == 'x':
                    # 如果没有数字，系数为 1
                    x_coef += sign * (num if has_num else 1)
                    i += 1
                else:
                    # 常数项
                    const += sign * num
            
            return x_coef, const
        
        # 分割等号左右两边
        left, right = equation.split('=')
        
        # 解析左右两边
        left_x, left_const = parse(left)
        right_x, right_const = parse(right)
        
        # 移项：左边 - 右边 = 0
        x_coef = left_x - right_x
        const = left_const - right_const
        
        # 判断解的情况
        if x_coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            # x = -const / x_coef
            return f"x={-const // x_coef}"
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是方程字符串的长度。需要遍历字符串解析表达式。
- **空间复杂度**：$O(1)$，只使用了常数级别的额外空间。
