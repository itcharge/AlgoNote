# [0013. 罗马数字转整数](https://leetcode.cn/problems/roman-to-integer/)

- 标签：哈希表、数学、字符串
- 难度：简单

## 题目链接

- [0013. 罗马数字转整数 - 力扣](https://leetcode.cn/problems/roman-to-integer/)

## 题目大意

给定一个罗马数字对应的字符串，将其转换为整数。

罗马数字规则：

- I 代表数值 1，V 代表数值 5，X 代表数值 10，L 代表数值 50，C 代表数值 100，D 代表数值 500，M 代表数值 1000；
- 一般罗马数字较大数字在左边，较小数字在右边，此时值为两者之和，比如 XI = X + I = 10 + 1 = 11。
- 例外情况下，较小数字在左边，较大数字在右边，此时值为后者减前者之差，比如 IX = X - I = 10 - 1 = 9。

## 解题思路

用一个哈希表存储罗马数字与对应数值关系。遍历罗马数字对应的字符串，判断相邻两个数大小关系，并计算对应结果。

## 代码

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        nunbers = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        sum = 0
        pre_num = nunbers[s[0]]
        for i in range(1, len(s)):
            cur_num = nunbers[s[i]]
            if pre_num < cur_num:
                sum -= pre_num
            else:
                sum += pre_num
            pre_num = cur_num
        sum += pre_num
        return sum
```

