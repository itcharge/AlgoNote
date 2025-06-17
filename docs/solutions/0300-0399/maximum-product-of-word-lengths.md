# [0318. 最大单词长度乘积](https://leetcode.cn/problems/maximum-product-of-word-lengths/)

- 标签：位运算、数组、字符串
- 难度：中等

## 题目链接

- [0318. 最大单词长度乘积 - 力扣](https://leetcode.cn/problems/maximum-product-of-word-lengths/)

## 题目大意

给定一个字符串数组 `words`。字符串中只包含英语的小写字母。

要求：计算当两个字符串 `words[i]` 和 `words[j]` 不包含相同字符时，它们长度的乘积的最大值。如果没有不包含相同字符的一对字符串，返回 0。

## 解题思路

这道题的核心难点是判断任意两个字符串之间是否包含相同字符。最直接的做法是先遍历第一个字符串的每个字符，再遍历第二个字符串查看是否有相同字符。但是这样做的话，时间复杂度过高。考虑怎么样可以优化一下。

题目中说字符串中只包含英语的小写字母，也就是 `26` 种字符。一个 `32` 位的 `int` 整数每一个二进制位都可以表示一种字符的有无，那么我们就可以通过一个整数来表示一个字符串中所拥有的字符种类。延伸一下，我们可以用一个整数数组来表示一个字符串数组中，每个字符串所拥有的字符种类。

接下来事情就简单了，两重循环遍历整数数组，遇到两个字符串不包含相同字符的情况，就计算一下他们长度的乘积，并维护一个乘积最大值。最后输出最大值即可。

## 代码

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        size = len(words)
        arr = [0 for _ in range(size)]
        for i in range(size):
            word = words[i]
            len_word = len(word)
            for j in range(len_word):
                arr[i] |= 1 << (ord(word[j]) - ord('a'))
        ans = 0
        for i in range(size):
            for j in range(i + 1, size):
                if arr[i] & arr[j] == 0:
                    k = len(words[i]) * len(words[j])
                    ans = k if ans < k else ans
        return ans
```

