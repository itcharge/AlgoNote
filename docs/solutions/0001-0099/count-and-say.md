# [0038. 外观数列](https://leetcode.cn/problems/count-and-say/)

- 标签：字符串
- 难度：中等

## 题目链接

- [0038. 外观数列 - 力扣](https://leetcode.cn/problems/count-and-say/)

## 题目大意

给定一个正整数 n，$(1 \le n \le 30)$，要求输出外观数列的第 n 项。

外观数列：整数序列，数字由 1 开始，每一项都是对前一项的描述

例如：

| 1.  |    1 | 由 1 开始           |
| --- | ---: | ------------------- |
| 2.  |   11 | 表示 1 个 1         |
| 3.  |   21 | 表示 2 个 1         |
| 4.  | 1211 | 表示 1 个 1，1 个 2 |



## 解题思路

模拟题目遍历求解。

将 ans 设为 "1"，每次遍历判断相邻且相同的数字有多少个，再将 ans 拼接上「数字个数 + 数字」。

## 代码

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for _ in range(1, n):
            s = ""
            start = 0
            for i in range(len(ans)):
                if ans[i] != ans[start]:
                    s += str(i-start) + ans[start]
                    start = i
            s += str(len(ans)-start) + ans[start]
            ans = s
        return ans
```

