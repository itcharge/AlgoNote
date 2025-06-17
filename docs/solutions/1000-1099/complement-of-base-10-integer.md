# [1009. 十进制整数的反码](https://leetcode.cn/problems/complement-of-base-10-integer/)

- 标签：位运算
- 难度：简单

## 题目链接

- [1009. 十进制整数的反码 - 力扣](https://leetcode.cn/problems/complement-of-base-10-integer/)

## 题目大意

**描述**：给定一个十进制数 $n$。

**要求**：返回其二进制表示的反码对应的十进制整数。

**说明**：

- $0 \le N < 10^9$。

**示例**：

- 示例 1：

```python
输入：5
输出：2
解释：5 的二进制表示为 "101"，其二进制反码为 "010"，也就是十进制中的 2 。
```

- 示例 2：

```python
输入：7
输出：0
解释：7 的二进制表示为 "111"，其二进制反码为 "000"，也就是十进制中的 0 。
```

## 解题思路

### 思路 1：模拟

1. 将十进制数 $n$ 转为二进制 $binary$。
2. 遍历二进制 $binary$ 的每一个数位 $digit$。
   1. 如果 $digit$ 为 $0$，则将其转为 $1$，存入答案 $res$ 中。
   2. 如果 $digit$ 为 $1$，则将其转为 $0$，存入答案 $res$ 中。
3. 返回答案 $res$。

### 思路 1：代码

```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = ""
        while n:
            binary += str(n % 2)
            n //= 2
        if binary == "":
            binary = "0"
        else:
            binary = binary[::-1]
        res = 0
        for digit in binary:
            if digit == '0':
                res = res * 2 + 1
            else:
                res = res * 2
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(len(n))$，其中 $len(n)$ 为 $n$ 对应二进制的长度。
- **空间复杂度**：$O(1)$。
