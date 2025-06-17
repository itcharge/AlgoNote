# [1047. 删除字符串中的所有相邻重复项](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/)

- 标签：栈、字符串
- 难度：简单

## 题目链接

- [1047. 删除字符串中的所有相邻重复项 - 力扣](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/)

## 题目大意

给定一个全部由小写字母组成的字符串 S，重复的删除相邻且相同的字母，直到相邻字母不再有相同的。

比如 "abbaca"。先删除相邻且相同的字母 "bb"，变为 "aaca"，再删除相邻且相同的字母 "aa"，变为 "ca"，无相邻且相同的字母，即 "ca" 为最终结果。

## 解题思路

跟括号匹配有点类似。我们可以利用「栈」来做这道题。遍历字符串，如果当前字符与栈顶字符相同，则将栈顶所有相同字符删除，否则就将当前字符入栈。

## 代码

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
```

