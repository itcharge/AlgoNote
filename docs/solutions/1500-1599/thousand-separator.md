# [1556. 千位分隔数](https://leetcode.cn/problems/thousand-separator/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1556. 千位分隔数 - 力扣](https://leetcode.cn/problems/thousand-separator/)

## 题目大意

**描述**：给定一个整数 $n$。

**要求**：每隔三位田间点（即 `"."` 符号）作为千位分隔符，并将结果以字符串格式返回。

**说明**：

- $0 \le n \le 2^{31}$。

**示例**：

- 示例 1：

```python
输入：n = 987
输出："987"
```

- 示例 2：

```python
输入：n = 123456789
输出："123.456.789"
```

## 解题思路

### 思路 1：模拟

1. 使用字符串变量 $ans$ 用于存储答案，使用一个计数器 $idx$ 来记录当前位数的个数。
2. 将 $n$ 转为字符串 $s$ 后，从低位向高位遍历。
3. 将当前数字 $s[i]$ 存入 $ans$ 中，计数器加 $1$，当计数器为 $3$ 的整数倍并且当前数字位不是最高位时，将 `"."` 存入 $ans$ 中。
4. 遍历完成后，将 $ans$ 翻转后返回。

### 思路 1：代码

```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        ans = ""

        idx = 0
        for i in range(len(s) - 1, -1, -1):
            ans += s[i]
            idx += 1
            if idx % 3 == 0 and i != 0:
                ans += "."

        return ''.join(reversed(ans))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(\log n)$。

