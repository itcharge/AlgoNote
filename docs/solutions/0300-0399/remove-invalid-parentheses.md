# [0301. 删除无效的括号](https://leetcode.cn/problems/remove-invalid-parentheses/)

- 标签：广度优先搜索、字符串、回溯
- 难度：困难

## 题目链接

- [0301. 删除无效的括号 - 力扣](https://leetcode.cn/problems/remove-invalid-parentheses/)

## 题目大意

**描述**：

给定一个由若干括号和字母组成的字符串 $s$，删除最小数量的无效括号，使得输入的字符串有效。

**要求**：

返回所有可能的结果。答案可以按任意顺序返回。

**说明**：

- $1 \le s.length \le 25$。
- $s$ 由小写英文字母以及括号 `'('` 和 `')'` 组成。
- $s$ 中至多含 $20$ 个括号。

**示例**：

- 示例 1：

```python
输入：s = "()())()"
输出：["(())()","()()()"]
```

- 示例 2：

```python
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]
```

## 解题思路

### 思路 1：回溯算法

这道题要求删除最小数量的无效括号，使得字符串有效。我们可以使用回溯算法来解决这个问题。

**1. 问题分析**

- 首先需要计算需要删除的最少左括号数量 $left\_remove$ 和右括号数量 $right\_remove$。
- 然后使用回溯算法尝试删除这些括号，生成所有可能的有效字符串。
- 为了避免重复结果，需要去重处理。

**2. 算法思路**

使用回溯算法来生成所有可能的有效字符串：

- 首先遍历字符串，计算需要删除的最少左括号和右括号数量。
- 使用回溯函数 $backtrack$，参数包括当前字符串 $current$、当前位置 $index$、剩余需要删除的左括号数量 $left\_count$、右括号数量 $right\_count$、当前左括号数量 $left\_open$、右括号数量 $right\_open$。
- 在回溯过程中，对于每个字符：
  - 如果是左括号，可以选择删除或保留。
  - 如果是右括号，可以选择删除或保留（但要保证左括号数量大于右括号数量）。
  - 如果是其他字符，直接保留。
- 当遍历完整个字符串且括号数量平衡时，将结果加入答案集合。

**3. 关键步骤**

1. 计算需要删除的最少括号数量：$left\_remove$ 和 $right\_remove$。
2. 使用回溯函数生成所有可能的有效字符串。
3. 对于每个位置，尝试删除或保留当前括号。
4. 使用集合去重，返回所有有效结果。

### 思路 1：代码

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 计算需要删除的最少左括号和右括号数量
        left_remove = 0  # 需要删除的左括号数量
        right_remove = 0  # 需要删除的右括号数量
        
        for char in s:
            if char == '(':
                left_remove += 1
            elif char == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1
        
        result = set()  # 使用集合去重
        
        def backtrack(current, index, left_count, right_count, left_open, right_open):
            # 如果遍历完整个字符串
            if index == len(s):
                # 如果括号数量平衡，加入结果
                if left_open == right_open:
                    result.add(current)
                return
            
            char = s[index]
            
            # 如果是左括号
            if char == '(':
                # 选择删除这个左括号
                if left_count > 0:
                    backtrack(current, index + 1, left_count - 1, right_count, left_open, right_open)
                # 选择保留这个左括号
                backtrack(current + char, index + 1, left_count, right_count, left_open + 1, right_open)
            
            # 如果是右括号
            elif char == ')':
                # 选择删除这个右括号
                if right_count > 0:
                    backtrack(current, index + 1, left_count, right_count - 1, left_open, right_open)
                # 选择保留这个右括号（但要保证左括号数量大于右括号数量）
                if left_open > right_open:
                    backtrack(current + char, index + 1, left_count, right_count, left_open, right_open + 1)
            
            # 如果是其他字符，直接保留
            else:
                backtrack(current + char, index + 1, left_count, right_count, left_open, right_open)
        
        # 开始回溯
        backtrack("", 0, left_remove, right_remove, 0, 0)
        
        return list(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^n)$，其中 $n$ 是字符串长度。在最坏情况下，每个括号都有两种选择（删除或保留），所以时间复杂度为 $O(2^n)$。
- **空间复杂度**：$O(n)$，递归栈的深度最多为 $n$，结果集合的空间复杂度也为 $O(n)$。
