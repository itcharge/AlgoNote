# [0476. 数字的补数](https://leetcode.cn/problems/number-complement/)

- 标签：位运算
- 难度：简单

## 题目链接

- [0476. 数字的补数 - 力扣](https://leetcode.cn/problems/number-complement/)

## 题目大意

**描述**：

对整数的二进制表示取反（$0$ 变 $1$，$1$ 变 $0$）后，再转换为十进制表示，可以得到这个整数的补数。

- 例如，整数 $5$ 的二进制表示是 `"101"`，取反后得到 `"010"`，再转回十进制表示得到补数 $2$。

给定一个整数 $num$。

**要求**：

输出它的补数。

**说明**：

- $1 \le num \lt 2^{31}$。

- 注意：本题与 [1009. 十进制整数的反码](https://leetcode-cn.com/problems/complement-of-base-10-integer/) 相同。

**示例**：

- 示例 1：

```python
输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
```

- 示例 2：

```python
输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
```

## 解题思路

### 思路 1：

1. 将十进制数 $num$ 转为二进制 $binary$。
2. 遍历二进制 $binary$ 的每一个数位 $digit$。
   1. 如果 $digit$ 为 $0$，则将其转为 $1$，存入答案 $res$ 中。
   2. 如果 $digit$ 为 $1$，则将其转为 $0$，存入答案 $res$ 中。
3. 返回答案 $res$。

### 思路 1：代码

```python
class Solution:
    def findComplement(self, num: int) -> int:
        # 将 num 转为二进制字符串
        binary = ""
        while num:
            binary += str(num % 2)  # 不断取余，转换为二进制
            num //= 2
        # 如果 binary 为空，说明 num 为 0，补数为 1
        if binary == "":
            binary = "0"
        else:
            binary = binary[::-1]  # 翻转二进制字符串，得到正确的二进制表示
        
        # 将二进制字符串进行补数转换（0 变 1，1 变 0）
        res = 0
        for digit in binary:
            if digit == '0':
                res = res * 2 + 1  # 0 变为 1
            else:
                res = res * 2      # 1 变为 0
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log num)$，其中 $num$ 为给定的正整数。我们需要将 $num$ 转换为二进制表示，需要 $O(\log num)$ 时间，然后对二进制的每一位进行处理。
- **空间复杂度**：$O(\log num)$，其中 $num$ 为给定的正整数。我们需要 $O(\log num)$ 的空间来存储二进制字符串。
