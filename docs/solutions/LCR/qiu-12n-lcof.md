# [LCR 189. 设计机械累加器](https://leetcode.cn/problems/qiu-12n-lcof/)

- 标签：位运算、递归、脑筋急转弯
- 难度：中等

## 题目链接

- [LCR 189. 设计机械累加器 - 力扣](https://leetcode.cn/problems/qiu-12n-lcof/)

## 题目大意

给定一个整数 `n`。

要求：计算 `1 + 2 + ... + n`，并且不能使用乘除法、for、while、if、else、switch、case 等关键字及条件判断语句（A?B:C）。

## 解题思路

Python 中的逻辑运算最终返回的是最后一个非空值。比如 `3 and 2 and 'a'` 最终返回的是 `'a'`。利用这个特性可以递归求解。

## 代码

```python
class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n - 1)
```

