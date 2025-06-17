# [0171. Excel 表列序号](https://leetcode.cn/problems/excel-sheet-column-number/)

- 标签：数学、字符串
- 难度：简单

## 题目链接

- [0171. Excel 表列序号 - 力扣](https://leetcode.cn/problems/excel-sheet-column-number/)

## 题目大意

给你一个字符串 `columnTitle` ，表示 Excel 表格中的列名称。

要求：返回该列名称对应的列序号。

## 解题思路

Excel 表的列名称由大写字母组成，共有 26 个，因此列名称的表示实质是 26 进制，需要将 26 进制转换成十进制。转换过程如下：

- 将每一位对应列名称转换成整数（注意列序号从 `1` 开始）。
- 将当前结果乘上进制数（`26`），然后累加上当前位上的整数。

最后输出答案。

## 代码

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            num = ord(ch) - ord('A') + 1
            ans = ans * 26 + num
        return ans
```

