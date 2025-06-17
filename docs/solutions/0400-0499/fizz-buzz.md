# [0412. Fizz Buzz](https://leetcode.cn/problems/fizz-buzz/)

- 标签：数学、字符串、模拟
- 难度：简单

## 题目链接

- [0412. Fizz Buzz - 力扣](https://leetcode.cn/problems/fizz-buzz/)

## 题目大意

给定一个整数 n，按照规则，输出 1~n 的字符串表示。

规则：

- 如果 i 是 3 的倍数，输出 "Fizz"；
- 如果 i 是 5 的倍数，输出 "Buzz"；
- 如果 i 是 3 和 5 的倍数，则输出 "FizzBuzz"。

## 解题思路

简单题，按照题目规则输出即可。

## 代码

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
```

