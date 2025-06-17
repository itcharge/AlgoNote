# [LCR 182. 动态口令](https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

- 标签：数学、双指针、字符串
- 难度：简单

## 题目链接

- [LCR 182. 动态口令 - 力扣](https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

## 题目大意

给定一个字符串 `s` 和一个整数 `n`。

要求：将字符串 `s` 每个字符向左旋转 `n` 位。

- 左旋转：将字符串前面的若干字符转移到字符串的尾部。

## 解题思路

- 使用数组 `res` 存放答案。
- 先遍历 `[n, len(s) - 1]` 范围的字符，将其存入数组。
- 再遍历 `[0, n - 1]` 范围的字符，将其存入数组。
- 将数组转为字符串返回。

## 代码

```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return "".join(res)
```

