# [0012. 整数转罗马数字](https://leetcode.cn/problems/integer-to-roman/)

- 标签：哈希表、数学、字符串
- 难度：中等

## 题目链接

- [0012. 整数转罗马数字 - 力扣](https://leetcode.cn/problems/integer-to-roman/)

## 题目大意

给定一个整数，将其转换为罗马数字。

罗马数字规则：

- I 代表数值 1，V 代表数值 5，X 代表数值 10，L 代表数值 50，C 代表数值 100，D 代表数值 500，M 代表数值 1000；
- 一般罗马数字较大数字在左边，较小数字在右边，此时值为两者之和，比如 XI = X + I = 10 + 1 = 11。
- 例外情况下，较小数字在左边，较大数字在右边，此时值为后者减前者之差，比如 IX = X - I = 10 - 1 = 9。

## 解题思路

根据规则，可以得出：

- I 代表数值 1，V 代表数值 5，X 代表数值 10，L 代表数值 50，C 代表数值 100，D 代表数值 500，M 代表数值 1000；
- CM 代表 900，CD 代表 400，XC 代表 90，XL 代表 40，IX 代表 9，IV 代表 4。

依次排序可得：

- 1000 : M、900 : CM、D : 500、400 : CD、100 : C、90 : XC、50 : L、40 : XL、10 : X、9 : IX、5 : V、4 : IV、1 : I。

使用贪心算法。每次尽量用最大的数对应的罗马字符来表示。先选择 1000，再选择 900，然后 500，等等。 

## 代码

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ""
        for key in roman_dict:
            if num // key != 0:
                res += roman_dict[key] * (num // key)
                num %= key
        return res
```

