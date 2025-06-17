# [0166. 分数到小数](https://leetcode.cn/problems/fraction-to-recurring-decimal/)

- 标签：哈希表、数学、字符串
- 难度：中等

## 题目链接

- [0166. 分数到小数 - 力扣](https://leetcode.cn/problems/fraction-to-recurring-decimal/)

## 题目大意

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，要求以字符串的形式返回该分数对应小数结果。

- 如果小数部分为循环小数，则将循环的小数部分括在括号内。

## 解题思路

先处理特殊数据，例如 0、负数等。

然后利用整除运算，计算出分数的整数部分。在根据取余运算结果，判断是否含有小数部分。

因为小数部分可能会有循环部分，所以使用哈希表来判断是否出现了循环小数。哈希表所存键值为 数字：数字开始位置。

然后计算小数部分，每次将被除数 * 10 然后对除数进行整除，再对被除数进行取余操作，直到被除数变为 0，或者在字典中出现了循环小数为止。

## 代码

```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        if numerator ^ denominator < 0:
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        numerator %= denominator
        if numerator == 0:
            return ''.join(res)
        res.append('.')

        record = dict()
        while numerator:
            if numerator not in record:
                record[numerator] = len(res)
                numerator *= 10
                res.append(str(numerator // denominator))
                numerator %= denominator
            else:
                res.insert(record[numerator], '(')
                res.append(')')
                break
        return ''.join(res)
```

