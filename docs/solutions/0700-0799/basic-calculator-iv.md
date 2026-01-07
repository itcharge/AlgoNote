# [0770. 基本计算器 IV](https://leetcode.cn/problems/basic-calculator-iv/)

- 标签：栈、递归、哈希表、数学、字符串
- 难度：困难

## 题目链接

- [0770. 基本计算器 IV - 力扣](https://leetcode.cn/problems/basic-calculator-iv/)

## 题目大意

**描述**：

给定一个表达式如 `expression = "e + 8 - a + 5"` 和一个求值映射，如 `{"e": 1}`（给定的形式为 `evalvars = ["e"]` 和 `evalints = [1]`。

**要求**：

返回表示简化表达式的标记列表，例如 `["-1*a","14"]`。

- 表达式交替使用块和符号，每个块和符号之间有一个空格。
- 块要么是括号中的表达式，要么是变量，要么是非负整数。
- 变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 `"2x"` 或 `"-x"` 这样的前导系数或一元运算符。

表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。

- 例如，`expression = "1 + 2 * 3"` 的答案是 ["7"]。

输出格式如下：

- 对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。
- 例如，我们永远不会写像 `"b*a*c"` 这样的项，只写 `"a*b*c"`。
- 项的次数等于被乘的自变量的数目，并计算重复项。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。
- 例如，`"a*a*b*c"` 的次数为 $4$。
- 项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 $1$ 仍然要打印出来。
- 格式良好的一个示例答案是 `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]`。
- 系数为 $0$ 的项（包括常数项）不包括在内。
- 例如，`"0"` 的表达式输出为 `[]`。

注意：你可以假设给定的表达式均有效。所有中间结果都在区间 $[-2^{31}, 2^{31} - 1]$ 内。

**说明**：

- $1 \le expression.length \le 250$。
- expression 由小写英文字母，数字 '+', '-', '*', '(', ')', ' ' 组成。
- expression 不包含任何前空格或后空格。
- expression 中的所有符号都用一个空格隔开。
- $0 \le evalvars.length \le 10^{3}$。
- $1 \le evalvars[i].length \le 20$。
- $evalvars[i]$ 由小写英文字母组成。
- $evalints.length == evalvars.length$。
- $-10^{3} \le evalints[i] \le 10^{3}$。

**示例**：

- 示例 1：

```python
输入：expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
输出：["-1*a","14"]
```

- 示例 2：

```python
输入：expression = "e - 8 + temperature - pressure",
evalvars = ["e", "temperature"], evalints = [1, 12]
输出：["-1*pressure","5"]
```

## 解题思路

### 思路 1：递归 + 哈希表 + 多项式运算

这道题要求实现一个支持变量的计算器，需要处理加减乘运算、括号和变量替换。

核心思路：

1. 定义多项式类，支持加减乘运算。
2. 多项式用字典表示，键是变量的元组（按字典序排序），值是系数。
3. 使用递归下降解析表达式。
4. 先将给定的变量替换为常数，再进行计算。

算法步骤：

1. 创建多项式类 `Poly`，支持：
   - 加法：合并同类项。
   - 减法：系数取反后加法。
   - 乘法：分配律展开。
2. 解析表达式：
   - 使用递归下降解析器处理括号、加减乘运算。
   - 遇到变量时，如果在求值映射中，替换为常数；否则保留为变量。
3. 格式化输出：
   - 按次数从高到低、字典序排序。
   - 格式化每一项。

### 思路 1：代码

```python
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        from collections import Counter
        
        # 创建变量求值映射
        eval_map = dict(zip(evalvars, evalints))
        
        # 多项式类
        class Poly:
            def __init__(self, terms=None):
                # terms: {变量元组: 系数}
                self.terms = Counter(terms) if terms else Counter()
            
            def __add__(self, other):
                result = Poly(self.terms)
                for key, val in other.terms.items():
                    result.terms[key] += val
                return result
            
            def __sub__(self, other):
                result = Poly(self.terms)
                for key, val in other.terms.items():
                    result.terms[key] -= val
                return result
            
            def __mul__(self, other):
                result = Poly()
                for k1, v1 in self.terms.items():
                    for k2, v2 in other.terms.items():
                        # 合并变量（按字典序排序）
                        key = tuple(sorted(k1 + k2))
                        result.terms[key] += v1 * v2
                return result
            
            def to_list(self):
                # 转换为输出格式
                # 删除系数为 0 的项
                items = [(k, v) for k, v in self.terms.items() if v != 0]
                # 排序：先按次数降序，再按字典序
                items.sort(key=lambda x: (-len(x[0]), x[0]))
                
                result = []
                for vars_tuple, coef in items:
                    if vars_tuple:
                        result.append(f"{coef}*{'*'.join(vars_tuple)}")
                    else:
                        result.append(str(coef))
                return result
        
        # 解析表达式
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
        
        def parse():
            """解析加减表达式"""
            nonlocal idx
            left = parse_term()
            
            while idx < len(tokens) and tokens[idx] in ['+', '-']:
                op = tokens[idx]
                idx += 1
                right = parse_term()
                if op == '+':
                    left = left + right
                else:
                    left = left - right
            
            return left
        
        def parse_term():
            """解析乘法表达式"""
            nonlocal idx
            left = parse_factor()
            
            while idx < len(tokens) and tokens[idx] == '*':
                idx += 1
                right = parse_factor()
                left = left * right
            
            return left
        
        def parse_factor():
            """解析因子（数字、变量或括号表达式）"""
            nonlocal idx
            token = tokens[idx]
            idx += 1
            
            if token == '(':
                result = parse()
                idx += 1  # 跳过 ')'
                return result
            elif token.lstrip('-').isdigit():
                # 数字
                return Poly({(): int(token)})
            else:
                # 变量
                if token in eval_map:
                    return Poly({(): eval_map[token]})
                else:
                    return Poly({(token,): 1})
        
        idx = 0
        poly = parse()
        return poly.to_list()
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是表达式的长度，$m$ 是多项式项的数量。解析和计算都需要遍历表达式。
- **空间复杂度**：$O(m)$，需要存储多项式的所有项。
