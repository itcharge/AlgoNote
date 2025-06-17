# [0409. 最长回文串](https://leetcode.cn/problems/longest-palindrome/)

- 标签：贪心、哈希表、字符串
- 难度：简单

## 题目链接

- [0409. 最长回文串 - 力扣](https://leetcode.cn/problems/longest-palindrome/)

## 题目大意

给定一个包含大写字母和小写字母的字符串 `s`。

要求：找到通过这些字母构造成的最长的回文串。

注意：

- 在构造过程中，请注意区分大小写。比如 `Aa` 不能当做一个回文字符串。
- 假设字符串的长度不会超过 `1010`。

## 解题思路

这道题目是通过给定字母构造回文串，并找到最长的回文串长度。那就要先看看回文串的特点。在回文串中，最多只有一个字母出现过奇数次，其余字符都出现过偶数次。且相同字母是中心对称的。

则我们可以用哈希表统计字符出现次数。对于每个字符，使用尽可能多的偶数次字符作为回文串的两侧，并记录下使用的字符个数，记录到答案中。再使用一个 `flag` 标记下是否有奇数次的字符，如果有的话，最终答案再加 1。最后输出答案。

## 代码

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        word_dict = dict()
        for ch in s:
            if ch in word_dict:
                word_dict[ch] += 1
            else:
                word_dict[ch] = 1

        ans = 0
        flag = False
        for value in word_dict.values():
            ans += value // 2 * 2
            if value % 2 == 1:
                flag = True

        if flag:
            ans += 1

        return ans
```

