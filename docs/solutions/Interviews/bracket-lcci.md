# [面试题 08.09. 括号](https://leetcode.cn/problems/bracket-lcci/)

- 标签：字符串、动态规划、回溯
- 难度：中等

## 题目链接

- [面试题 08.09. 括号 - 力扣](https://leetcode.cn/problems/bracket-lcci/)

## 题目大意

给定一个整数 `n`。

要求：生成所有有可能且有效的括号组合。

## 解题思路

通过回溯算法生成所有答案。为了生成的括号组合是有效的，回溯的时候，使用一个标记变量 `symbol` 来表示是否当前组合是否成对匹配。

如果在当前组合中增加一个 `(`，则 `symbol += 1`，如果增加一个 `)`，则 `symbol -= 1`。显然只有在 `symbol < n` 的时候，才能增加 `(`，在 `symbol > 0` 的时候，才能增加 `)`。

如果最终生成 `2 * n` 的括号组合，并且 `symbol == 0`，则说明当前组合是有效的，将其加入到最终答案数组中。

最终输出最终答案数组。

## 代码

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(parenthesis, symbol, index):
            if n * 2 == index:
                if symbol == 0:
                    parentheses.append(parenthesis)
            else:
                if symbol < n:
                    backtrack(parenthesis + '(', symbol + 1, index + 1)
                if symbol > 0:
                    backtrack(parenthesis + ')', symbol - 1, index + 1)

        parentheses = list()
        backtrack("", 0, 0)
        return parentheses
```

