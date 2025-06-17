# [0738. 单调递增的数字](https://leetcode.cn/problems/monotone-increasing-digits/)

- 标签：贪心、数学
- 难度：中等

## 题目链接

- [0738. 单调递增的数字 - 力扣](https://leetcode.cn/problems/monotone-increasing-digits/)

## 题目大意

给定一个非负整数 n，找出小于等于 n 的最大整数，同时该整数需要满足其各个位数上的数字是单调递增的。

## 解题思路

为了方便操作，我们先将整数 n 转为 list 数组，即 n_list。

题目要求这个整数尽可能的大，那么这个数从高位开始，就应该尽可能的保持不变。那么我们需要从高位到低位，找到第一个满足 `n_list[i - 1] > n_list[i]` 的位置，然后把 `n_list[i] - 1`，再把剩下的低位都变为 9。 

##  代码

```python
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n_list = list(str(n))
        size = len(n_list)
        start_i = size
        for i in range(size - 1, 0, -1):
            if n_list[i - 1] > n_list[i]:
                start_i = i
                n_list[i - 1] = chr(ord(n_list[i - 1]) - 1)

        for i in range(start_i, size, 1):
            n_list[i] = '9'
        res = int(''.join(n_list))
        return res
```

