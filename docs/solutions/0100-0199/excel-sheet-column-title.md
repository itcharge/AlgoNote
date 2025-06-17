# [0168. Excel 表列名称](https://leetcode.cn/problems/excel-sheet-column-title/)

- 标签：数学、字符串
- 难度：简单

## 题目链接

- [0168. Excel 表列名称 - 力扣](https://leetcode.cn/problems/excel-sheet-column-title/)

## 题目大意

描述：给定一个正整数 columnNumber。

要求：返回它在 Excel 表中相对应的列名称。

1 -> A，2 -> B，3 -> C，…，26 -> Z，…，28 -> AB

## 解题思路

实质上就是 10 进制转 26 进制。不过映射范围是 1~26，而不是 0~25，如果将 columnNumber 直接对 26 取余，则结果为 0~25，而本题余数为 1~26。可以直接将 columnNumber = columnNumber - 1，这样就可以将范围变为 0~25 就更加容易判断了。

## 代码

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber:
            columnNumber -= 1
            s = chr(65 + columnNumber % 26) + s
            columnNumber //= 26
        return s
```

