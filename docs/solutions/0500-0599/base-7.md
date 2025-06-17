# [0504. 七进制数](https://leetcode.cn/problems/base-7/)

- 标签：数学
- 难度：简单

## 题目链接

- [0504. 七进制数 - 力扣](https://leetcode.cn/problems/base-7/)

## 题目大意

**描述**：给定一个整数 $num$。

**要求**：将其转换为 $7$ 进制数，并以字符串形式输出。

**说明**：

- $-10^7 \le num \le 10^7$。

**示例**：

- 示例 1：

```python
输入: num = 100
输出: "202"
```

- 示例 2：

```python
输入: num = -7
输出: "-10"
```

## 解题思路

### 思路 1：模拟

1. $num$ 不断对 $7$ 取余整除。
2. 然后将取到的余数进行拼接成字符串即可。

### 思路 1：代码

```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            return "-" + self.convertToBase7(-num)
        ans = ""
        while num:
            ans = str(num % 7) + ans
            num //= 7
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log |n|)$。
- **空间复杂度**：$O(\log |n|)$。

