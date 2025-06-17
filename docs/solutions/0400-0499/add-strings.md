# [0415. 字符串相加](https://leetcode.cn/problems/add-strings/)

- 标签：数学、字符串、模拟
- 难度：简单

## 题目链接

- [0415. 字符串相加 - 力扣](https://leetcode.cn/problems/add-strings/)

## 题目大意

**描述**：给定两个字符串形式的非负整数 `num1` 和`num2`。

**要求**：计算它们的和，并同样以字符串形式返回。

**说明**：

- $1 \le num1.length, num2.length \le 10^4$。
- $num1$ 和 $num2$ 都只包含数字 $0 \sim 9$。
- $num1$ 和 $num2$ 都不包含任何前导零。
- 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

**示例**：

- 示例 1：

```python
输入：num1 = "11", num2 = "123"
输出："134"
```

- 示例 2：

```python
输入：num1 = "456", num2 = "77"
输出："533"
```

## 解题思路

### 思路 1：双指针

需要用字符串的形式来模拟大数加法。

加法的计算方式是：从个位数开始，由低位到高位，按位相加，如果相加之后超过 `10`，就需要向前进位。

模拟加法的做法是：

1. 用一个数组存储按位相加后的结果，每一位对应一位数。
2. 然后分别使用一个指针变量，对两个数 `num1`、`num2` 字符串进行反向遍历，将相加后的各个位置上的结果保存在数组中，这样计算完成之后就得到了一个按位反向的结果。
3. 最后返回结果的时候将数组反向转为字符串即可。

注意需要考虑 `num1`、`num2` 不等长的情况，让短的那个字符串对应位置按 $0$ 计算即可。

### 思路 1：代码

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num1 位数
        digit1 = len(num1) - 1
        # num2 位数
        digit2 = len(num2) - 1

        # 进位
        carry = 0
        # sum 存储反向结果
        sum = []
        # 逆序相加
        while carry > 0 or digit1 >= 0 or digit2 >= 0:
            # 获取对应位数上的数字
            num1_d = int(num1[digit1]) if digit1 >= 0 else 0
            num2_d = int(num2[digit2]) if digit2 >= 0 else 0
            digit1 -= 1
            digit2 -= 1
            # 计算结果，存储，进位
            num = num1_d+num2_d+carry
            sum.append('%d'%(num%10))
            carry = num // 10
        # 返回计算结果
        return "".join(sum[::-1])
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(max(m + n))$。其中 $m$ 是字符串 $num1$ 的长度，$n$ 是字符串 $num2$ 的长度。
- **空间复杂度**：$O(max(m + n))$。