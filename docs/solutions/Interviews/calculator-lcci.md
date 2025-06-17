# [面试题 16.26. 计算器](https://leetcode.cn/problems/calculator-lcci/)

- 标签：栈、数学、字符串
- 难度：中等

## 题目链接

- [面试题 16.26. 计算器 - 力扣](https://leetcode.cn/problems/calculator-lcci/)

## 题目大意

给定一个包含正整数、加（`+`）、减（`-`）、乘（`*`）、除（`/`）的算出表达式（括号除外）。表达式仅包含非负整数，`+`、`-`、`*`、`/` 四种运算符和空格 ` `。整数除法仅保留整数部分。

要求：计算其结果。

## 解题思路

计算表达式中，乘除运算优先于加减运算。我们可以先进行乘除运算，再将进行乘除运算后的整数值放入原表达式中相应位置，再依次计算加减。

可以考虑使用一个栈来保存进行乘除运算后的整数值。正整数直接压入栈中，负整数，则将对应整数取负号，再压入栈中。这样最终计算结果就是栈中所有元素的和。

具体做法：

- 遍历字符串 s，使用变量 op 来标记数字之前的运算符，默认为 `+`。
- 如果遇到数字，继续向后遍历，将数字进行累积，得到完整的整数 num。判断当前 op 的符号。
  - 如果 op 为 `+`，则将 num 压入栈中。
  - 如果 op 为 `-`，则将 -num 压入栈中。
  - 如果 op 为 `*`，则将栈顶元素 top 取出，计算 top * num，并将计算结果压入栈中。
  - 如果 op 为 `/`，则将栈顶元素 top 取出，计算 int(top / num)，并将计算结果压入栈中。
- 如果遇到 `+`、`-`、`*`、`/` 操作符，则更新 op。
- 最后将栈中整数进行累加，并返回结果。

## 代码

```python
class Solution:
    def calculate(self, s: str) -> int:
        size = len(s)
        stack = []
        op = '+'
        index = 0
        while index < size:
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                num = ord(s[index]) - ord('0')
                while index + 1 < size and s[index + 1].isdigit():
                    index += 1
                    num = 10 * num + ord(s[index]) - ord('0')
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                elif op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))
            elif s[index] in "+-*/":
                op = s[index]
            index += 1
        return sum(stack)
```

