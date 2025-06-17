# [0921. 使括号有效的最少添加](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/)

- 标签：栈、贪心、字符串
- 难度：中等

## 题目链接

- [0921. 使括号有效的最少添加 - 力扣](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/)

## 题目大意

**描述**：给定一个括号字符串 `s`，可以在字符串的任何位置插入一个括号。

**要求**：返回为使结果字符串 `s` 有效而必须添加的最少括号数。

**说明**：

- $1 \le s.length \le 1000$。
- `s` 只包含 `'('` 和 `')'` 字符。

只有满足下面几点之一，括号字符串才是有效的：

- 它是一个空字符串，或者
- 它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
- 它可以被写作 (A)，其中 A 是有效字符串。

例如，如果 `s = "()))"`，你可以插入一个开始括号为 `"(()))"` 或结束括号为 `"())))"`。

**示例**：

- 示例 1：

```python
输入：s = "())"
输出：1
```

## 解题思路

### 思路 1：贪心算法

为了最终添加的最少括号数，我们应该尽可能将当前能够匹配的括号先进行配对。则剩余的未完成配对的括号数量就是答案。

我们使用变量 `left_cnt` 来记录当前左括号的数量。使用 `res` 来记录添加的最少括号数量。

- 遍历字符串，判断当前字符。
- 如果当前字符为左括号 `(`，则令 `left_cnt` 加 `1`。
- 如果当前字符为右括号 `)`，则令 `left_cnt` 减 `1`。如果 `left_cnt` 减到 `-1`，说明当前有右括号不能完成匹配，则答案数量 `res` 加 `1`，并令 `left_cnt` 重新赋值为 `0`。
- 遍历完之后，令 `res` 加上剩余不匹配的 `left_cnt` 数量。
- 最后输出 `res`。

### 思路 1：贪心算法代码

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        left_cnt = 0
        for ch in s:
            if ch == '(':
                left_cnt += 1
            elif ch == ')':
                left_cnt -= 1
                if left_cnt == -1:
                    left_cnt = 0
                    res += 1
        res += left_cnt
        return res
```
