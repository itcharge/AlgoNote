# [LCR 135. 报数](https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)

- 标签：数组、数学
- 难度：简单

## 题目链接

- [LCR 135. 报数 - 力扣](https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)

## 题目大意

给定一个数字 `n`。

要求：按顺序打印从 `1` 到最大 `n` 位的十进制数。

## 解题思路

直接枚举 $1 \sim 10^{n} - 1$，生成列表并返回。

## 代码

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]
```

