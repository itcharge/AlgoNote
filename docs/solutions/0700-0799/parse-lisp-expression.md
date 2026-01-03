# [0736. Lisp 语法解析](https://leetcode.cn/problems/parse-lisp-expression/)

- 标签：栈、递归、哈希表、字符串
- 难度：困难

## 题目链接

- [0736. Lisp 语法解析 - 力扣](https://leetcode.cn/problems/parse-lisp-expression/)

## 题目大意

**描述**：

给定一个类似 Lisp 语句的字符串表达式 $expression$。

表达式语法如下所示:

- 表达式可以为整数，let 表达式，add 表达式，mult 表达式，或赋值的变量。表达式的结果总是一个整数。
- (整数可以是正整数、负整数、0)
- **let** 表达式采用 `"(let v1 e1 v2 e2 ... vn en expr)"` 的形式，其中 let 总是以字符串 `"let"` 来表示，接下来会跟随一对或多对交替的变量和表达式，也就是说，第一个变量 v1 被分配为表达式 e1 的值，第二个变量 v2 被分配为表达式 e2 的值，依次类推；最终 let 表达式的值为 expr 表达式的值。
- **add** 表达式表示为 `"(add e1 e2)"`，其中 add 总是以字符串 `"add"` 来表示，该表达式总是包含两个表达式 e1、e2，最终结果是 e1 表达式的值与 e2 表达式的值之「和」。
- **mult** 表达式表示为 `"(mult e1 e2)"`，其中 mult 总是以字符串 `"mult"` 表示，该表达式总是包含两个表达式 e1、e2，最终结果是 e1 表达式的值与 e2 表达式的值之「积」。
- 在该题目中，变量名以小写字符开始，之后跟随 0 个或多个小写字符或数字。为了方便，`"add"`，`"let"`，`"mult"` 会被定义为 `"关键字"`，不会用作变量名。
- 最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。测试用例中每一个表达式都是合法的。有关作用域的更多详细信息，请参阅示例。

**要求**：

求出其计算结果。

**说明**：

- $1 \le expression.length \le 2000$。
- $exprssion$ 中不含前导和尾随空格。
- $expressoin$ 中的不同部分（token）之间用单个空格进行分隔。
- 答案和所有中间计算结果都符合 32-bit 整数范围。
- 测试用例中的表达式均为合法的且最终结果为整数。

**示例**：

- 示例 1：

```python
输入：expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
输出：14
解释：
计算表达式 (add x y), 在检查变量 x 值时，
在变量的上下文中由最内层作用域依次向外检查。
首先找到 x = 3, 所以此处的 x 值是 3 。
```

- 示例 2：

```python
输入：expression = "(let x 3 x 2 x)"
输出：2
解释：let 语句中的赋值运算按顺序处理即可。
```

## 解题思路

### 思路 1：递归 + 哈希表

这道题需要解析和计算 Lisp 表达式。可以使用递归来处理嵌套的表达式。

**解题步骤**：

1. 使用递归函数 `evaluate` 来计算表达式的值。
2. 使用哈希表（作用域）来存储变量的值。
3. 根据表达式的类型进行处理：
   - 如果是整数，直接返回其值。
   - 如果是变量，从作用域中查找其值。
   - 如果是 `let` 表达式，依次赋值变量，然后计算最后一个表达式。
   - 如果是 `add` 表达式，计算两个子表达式的和。
   - 如果是 `mult` 表达式，计算两个子表达式的积。

**实现细节**：
- 使用栈来解析表达式，处理括号嵌套。
- 每个 `let` 表达式创建新的作用域（复制父作用域）。
- 递归计算子表达式的值。

### 思路 1：代码

```python
class Solution:
    def evaluate(self, expression: str) -> int:
        def parse(expr):
            """解析表达式，返回 token 列表"""
            tokens = []
            i = 0
            while i < len(expr):
                if expr[i] in '()':
                    tokens.append(expr[i])
                    i += 1
                elif expr[i] == ' ':
                    i += 1
                else:
                    j = i
                    while j < len(expr) and expr[j] not in '() ':
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
            return tokens
        
        def evaluate_helper(tokens, index, scope):
            """递归计算表达式的值"""
            token = tokens[index]
            
            if token == '(':
                # 处理括号表达式
                index += 1
                op = tokens[index]
                index += 1
                
                if op == 'let':
                    # 创建新的作用域
                    new_scope = scope.copy()
                    
                    # 处理变量赋值
                    while True:
                        # 检查是否是最后一个表达式
                        if tokens[index] == ')':
                            # 没有最后的表达式，返回 0
                            return 0, index + 1
                        
                        # 先保存当前位置
                        saved_index = index
                        
                        # 尝试解析下一个表达式
                        value, next_index = evaluate_helper(tokens, index, new_scope)
                        
                        # 检查是否还有下一个 token
                        if tokens[next_index] == ')':
                            # 这是最后一个表达式
                            return value, next_index + 1
                        
                        # 这是一个变量名，读取其值
                        var_name = tokens[saved_index]
                        index = next_index
                        
                        # 计算变量的值
                        var_value, index = evaluate_helper(tokens, index, new_scope)
                        new_scope[var_name] = var_value
                
                elif op == 'add':
                    # 计算两个子表达式的和
                    val1, index = evaluate_helper(tokens, index, scope)
                    val2, index = evaluate_helper(tokens, index, scope)
                    index += 1  # 跳过 ')'
                    return val1 + val2, index
                
                elif op == 'mult':
                    # 计算两个子表达式的积
                    val1, index = evaluate_helper(tokens, index, scope)
                    val2, index = evaluate_helper(tokens, index, scope)
                    index += 1  # 跳过 ')'
                    return val1 * val2, index
            
            elif token.lstrip('-').isdigit():
                # 整数
                return int(token), index + 1
            
            else:
                # 变量
                return scope.get(token, 0), index + 1
        
        tokens = parse(expression)
        result, _ = evaluate_helper(tokens, 0, {})
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是表达式的长度。需要遍历表达式一次。
- **空间复杂度**：$O(n)$。递归栈和作用域的空间消耗。
