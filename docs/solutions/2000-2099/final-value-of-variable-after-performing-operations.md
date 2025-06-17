# [2011. 执行操作后的变量值](https://leetcode.cn/problems/final-value-of-variable-after-performing-operations/)

- 标签：数组、字符串、模拟
- 难度：简单

## 题目链接

- [2011. 执行操作后的变量值 - 力扣](https://leetcode.cn/problems/final-value-of-variable-after-performing-operations/)

## 题目大意

存在一种支持 `4` 种操作和 `1` 个变量 `X` 的编程语言：

- `++X` 和 `x++` 使得变量 `X` 值加 `1`。
- `--X` 和 `X--` 使得变脸 `X ` 值减 `1`。

`X` 的初始值是 `0`。现在给定一个字符串数组 `operations`，这是由操作组成的一个列表。

要求：返回执行所有操作后，`X` 的最终值。

## 解题思路

思路很简单，初始答案 `res` 赋值为 `0`。

然后遍历操作列表 `operations`，判断每一个操作 `operation` 的符号。如果操作中含有 `+`，则让答案加 `1`，否则，则让答案减 `1`。最后输出答案。

## 代码

```python
def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0

        for opration in operations:
            res += 1 if '+' in opration else -1

        return res
```

