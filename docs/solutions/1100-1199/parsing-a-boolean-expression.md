# [1106. 解析布尔表达式](https://leetcode.cn/problems/parsing-a-boolean-expression/)

- 标签：栈、递归、字符串
- 难度：困难

## 题目链接

- [1106. 解析布尔表达式 - 力扣](https://leetcode.cn/problems/parsing-a-boolean-expression/)

## 题目大意

**描述**：给定一个以字符串形式表述的布尔表达式 $expression$，需要计算它的结果（$true$ 或 $false$）。

表达式可以包含以下内容：
- `'t'`：表示 $true$
- `'f'`：表示 $false$
- `'!(subExpr)'`：对内部表达式进行逻辑**非**（NOT）运算
- `'&(subExpr1, subExpr2, ...)'`：对内部表达式进行逻辑**与**（AND）运算
- `'|(subExpr1, subExpr2, ...)'`：对内部表达式进行逻辑**或**（OR）运算

**要求**：返回该布尔表达式的运算结果。题目保证表达式是有效的。

**说明**：

- $1 \le expression.length \le 2 \times 10^4$。
- $expression[i]$ 为 `'('`、`')'`、`'&'`、`'|'`、`'!'`、`'t'`、`'f'` 和 `','` 之一。

**示例**：

- 示例 1：

```python
输入：expression = "&(|(f))"
输出：false
解释：
首先，计算 |(f) --> f ，表达式变为 "&(f)" 。
接着，计算 &(f) --> f ，表达式变为 "f" 。
最后，返回 false 。
```

- 示例 2：

```python
输入：expression = "|(f,f,f,t)"
输出：true
解释：计算 (false OR false OR false OR true) ，结果为 true 。
```

## 解题思路

### 思路 1：栈 + 模拟

**拆解步骤**：

1. **遍历每个字符**，根据字符类型分别处理：

2. **遇到 `t`、`f`、运算符（`!`、`&`、`|`）或 `(`**：直接入栈，等待后续处理。

3. **遇到 `,`**：逗号只是分隔符，直接跳过。

4. **遇到 `)`**：说明一个子表达式结束了，开始计算：
   - 从栈中依次弹出元素，直到遇到 `(`，这些弹出的元素就是这个子表达式里的布尔值
   - 弹出 `(`
   - 再弹出一个元素，那就是运算符（`!`、`&` 或 `|`）
   - 根据运算符计算结果：
     - `!`：对第一个值取反
     - `&`：所有值做 AND（Python 的 `all()`）
     - `|`：所有值做 OR（Python 的 `any()`）
   - 把结果（`'t'` 或 `'f'`）压回栈中

5. **遍历结束后，栈中唯一剩下的就是最终结果**。

**用人话举个例子**：`expression = "&(|(f))"`

| 步骤 | 字符 | 操作 | 栈内容 |
|:---:|:----:|:----|:-------|
| 1 | `&` | 入栈 | `['&']` |
| 2 | `(` | 入栈 | `['&', '(']` |
| 3 | `\|` | 入栈 | `['&', '(', '\|']` |
| 4 | `(` | 入栈 | `['&', '(', '\|', '(']` |
| 5 | `f` | 入栈 | `['&', '(', '\|', '(', 'f']` |
| 6 | `)` | 弹出 `f`，遇到 `(`，弹出 `(`，弹出 `\|`，计算 `\|(f)=f`，压入 `f` | `['&', '(', 'f']` |
| 7 | `)` | 弹出 `f`，遇到 `(`，弹出 `(`，弹出 `&`，计算 `&(f)=f`，压入 `f` | `['f']` |

结果为 `false`。

### 思路 1：代码

```python
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch == ',':
                # 逗号只是分隔符，直接跳过
                continue
            elif ch == ')':
                # 遇到右括号，开始计算当前子表达式
                values = []

                # 弹出所有布尔值，直到遇到左括号
                while stack and stack[-1] != '(':
                    val = stack.pop()
                    values.append(True if val == 't' else False)

                # 弹出左括号
                stack.pop()

                # 弹出运算符
                operator = stack.pop()

                # 根据运算符计算
                if operator == '!':
                    result = not values[0]      # 非运算
                elif operator == '&':
                    result = all(values)        # 与运算：全真才真
                elif operator == '|':
                    result = any(values)        # 或运算：有真即真

                # 把结果压回栈中
                stack.append('t' if result else 'f')
            else:
                # 运算符、左括号、t、f 都直接入栈
                stack.append(ch)

        # 栈中只剩一个元素，就是最终结果
        return stack[0] == 't'
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。用人话说就是：每个字符最多被处理一次（入栈和出栈各一次），所以时间和字符串长度成正比。
- **空间复杂度**：$O(n)$。栈最多存储整个表达式的所有字符。
