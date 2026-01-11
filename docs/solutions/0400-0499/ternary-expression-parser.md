# [0439. 三元表达式解析器](https://leetcode.cn/problems/ternary-expression-parser/)

- 标签：栈、递归、字符串
- 难度：中等

## 题目链接

- [0439. 三元表达式解析器 - 力扣](https://leetcode.cn/problems/ternary-expression-parser/)

## 题目大意

**描述**：

给定一个由数字、`T`、`F`、`'?'` 和 `':'` 组成的字符串 $expression$，表示一个三元表达式，其中 `T` 为真，`F` 为假。表达式中的所有数字都是一位 数（即在 $[0,9]$ 范围内）。

三元表达式的格式为：`条件 ? 值1 : 值2`，如果条件为真，返回值 1，否则返回值 2。表达式可以嵌套。

**要求**：

返回表达式的计算结果。

**说明**：

- $5 \le expression.length \le 10^4$。
- $expression$ 由数字、`'T'`、`'F'`、`'?'` 和 `':'` 组成。
- 保证 $expression$ 是一个有效的三元表达式，且每个数字都是一位数。

**示例**：

- 示例 1：

```python
输入：expression = "T?2:3"
输出："2"
解释：条件为 T（真），返回 2。
```

- 示例 2：

```python
输入：expression = "F?1:T?4:5"
输出："4"
解释：条件为 F（假），计算 T?4:5，条件为 T（真），返回 4。
```

## 解题思路

### 思路 1：栈 + 递归

三元表达式的格式为：`条件 ? 值1 : 值2`，可以嵌套。需要从右向左解析，因为右边的表达式可能是嵌套的三元表达式。

**解题步骤**：

1. 使用栈来处理嵌套的三元表达式。
2. 从右向左遍历字符串：
   - 遇到数字或字母，压入栈。
   - 遇到 `'?'`，说明找到一个三元表达式的开始，此时栈顶应该是两个值（`值1` 和 `值2`）。
   - 继续向左找到条件（`'T'` 或 `'F'`），根据条件选择对应的值压入栈。
3. 最后栈中只剩一个元素，即为结果。

**关键点**：

- 从右向左遍历，遇到 `'?'` 时，栈顶两个元素分别是 `值1` 和 `值2`。
- 遇到 `':'` 时跳过。
- 条件字符在 `'?'` 的左边。

### 思路 1：代码

```python
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        n = len(expression)
        
        # 从右向左遍历
        i = n - 1
        while i >= 0:
            char = expression[i]
            
            if char == '?':
                # 栈顶两个元素是 值1 和 值2
                val1 = stack.pop()
                val2 = stack.pop()
                
                # 向左找条件
                i -= 1
                condition = expression[i]
                
                # 根据条件选择值
                if condition == 'T':
                    stack.append(val1)
                else:
                    stack.append(val2)
            elif char != ':':
                # 数字或字母，压入栈
                stack.append(char)
            
            i -= 1
        
        return stack[0]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是表达式的长度。每个字符最多被处理一次。
- **空间复杂度**：$O(n)$，栈的空间开销。
