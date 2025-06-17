# [1720. 解码异或后的数组](https://leetcode.cn/problems/decode-xored-array/)

- 标签：位运算、数组
- 难度：简单

## 题目链接

- [1720. 解码异或后的数组 - 力扣](https://leetcode.cn/problems/decode-xored-array/)

## 题目大意

n 个非负整数构成数组 arr，经过编码后变为长度为 n-1 的整数数组 encoded，其中 `encoded[i] = arr[i] XOR arr[i+1]`。例如 arr = [1, 0, 2, 1] 经过编码后变为 encoded = [1, 2, 3]。

现在给定编码后的数组 encoded 和原数组 arr 的第一个元素 arr[0]。要求返回原数组 arr。

## 解题思路

首先要了解异或的性质：

- 异或运算满足交换律和结合律。
  - 交换律：`a^b = b^a`
  - 结合律：`(a^b)^c = a^(b^c)`
- 任何整数和自身做异或运算结果都为 0，即 `x^x = 0`。
- 任何整数和 0 做异或运算结果都为其本身，即 `x^0 = 0`。

已知当 $1 \le i \le n$ 时，有 `encoded[i-1] = arr[i-1] XOR arr[i]`。两边同时「异或」上 arr[i-1]。得：

- `encoded[i-1] XOR arr[i-1] = arr[i-1] XOR arr[i] XOR arr[i-1]`
- `encoded[i-1] XOR arr[i-1] = arr[i] XOR 0`
- `encoded[i-1] XOR arr[i-1] = arr[i]`

所以就可以根据所得结论 `arr[i] = encoded[i-1] XOR arr[i-1]` 模拟得出原数组 arr。

## 代码

```python
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first
        for i in range(1, n):
            arr[i] = encoded[i-1] ^ arr[i-1]
        return arr
```

