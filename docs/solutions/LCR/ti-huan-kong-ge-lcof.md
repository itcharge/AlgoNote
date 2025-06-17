# [LCR 122. 路径加密](https://leetcode.cn/problems/ti-huan-kong-ge-lcof/)

- 标签：字符串
- 难度：简单

## 题目链接

- [LCR 122. 路径加密 - 力扣](https://leetcode.cn/problems/ti-huan-kong-ge-lcof/)

## 题目大意

给定一个字符串 `s`。

要求：将字符串 `s` 中的每个空格换成 `%20`。

## 解题思路

Python 的字符串是不可变类型，所以需要先用数组存储答案，再将其转为字符串返回。具体操作如下。

- 定义数组 `res`，遍历字符串 `s`。
  - 如果当前字符 `ch` 为空格，则将 ` %20` 加入到数组中。
  - 如果当前字符 `ch` 不为空格，则直接加入到数组中。
- 遍历完之后，通过 `join` 将其转为字符串返回。

## 代码

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for ch in s:
            if ch == ' ':
                res.append("%20")
            else:
                res.append(ch)
        return "".join(res)
```

