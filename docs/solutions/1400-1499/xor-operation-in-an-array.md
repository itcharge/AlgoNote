# [1486. 数组异或操作](https://leetcode.cn/problems/xor-operation-in-an-array/)

- 标签：位运算、数学
- 难度：简单

## 题目链接

- [1486. 数组异或操作 - 力扣](https://leetcode.cn/problems/xor-operation-in-an-array/)

## 题目大意

给定两个整数 n、start。数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）。n 为数组长度。返回数组 nums 中所有元素按位异或（XOR）后得到的结果。

## 解题思路

### 1. 模拟

直接按照题目要求模拟即可。

### 2. 规律

- $x \oplus x = 0$；
- $x \oplus y = y \oplus x$（交换律）；
- $(x \oplus y) \oplus z = x \oplus (y \oplus z)$（结合律）；
- $x \oplus y \oplus y = x$（自反性）；
- $\forall i \in Z$，有 $4i \oplus (4i+1) \oplus (4i+2) \oplus (4i+3) = 0$；
- $\forall i \in Z$，有 $2i \oplus (2i+1) = 1$；
- $\forall i \in Z$，有 $2i \oplus 1 = 2i+1$。

本题中计算的是 $start \oplus (start + 2) \oplus (start + 4) \oplus (start + 6) \oplus … \oplus (start+(2*(n-1)))$。

可以看出，如果 start 为奇数，则 $start+2, start + 4, …, start + (2 \times(n - 1))$ 都为奇数。如果 start 为偶数，则 $start + 2, start + 4, …, start + (2 \times(n - 1))$ 都为偶数。则它们对应二进制的最低位相同，则我们可以将最低位提取处理单独处理。从而将公式转换一下。

令 $s = \frac{start}{2}$，则等式变为 $(s) \oplus (s+1) \oplus (s+2) \oplus (s+3) \oplus … \oplus (s+(n-1)) * 2 + e$，e 表示运算结果的最低位。

根据自反性，$(s) \oplus (s+1) \oplus (s+2) \oplus (s+3) \oplus … \oplus (s+(n-1)) = \\ (1 \oplus 2 \oplus … \oplus (s-1)) \oplus (1 \oplus 2 \oplus … \oplus (s-1) \oplus (s) \oplus (s+1) \oplus … \oplus (s+(n-1)))$

例如： $3 \oplus 4 \oplus 5 \oplus 6 \oplus 7 = (1 \oplus 2) \oplus (1 \oplus 2 \oplus 3 \oplus 4 \oplus 5 \oplus 6 \oplus7)$

就变为了计算前 n 项序列的异或值。假设我们定义一个函数 sumXor(x) 用于计算前 n 项数的异或结果，通过观察可得出：

$sumXor(x) = \begin{cases} \begin{array} \ x, & x = 4i, k \in Z \cr (x-1) \oplus x, & x = 4i+1, k \in Z \cr (x-2) \oplus (x-1) \oplus x, & x = 4i+2, k \in Z \cr (x-3) \oplus (x-2) \oplus (x-3) \oplus x, & x = 4i+3, k \in Z \end{array} \end{cases}$

继续化简得：

$sumXor(x) = \begin{cases} \begin{array} \ x, & x = 4i, k \in Z \cr 1, & x = 4i+1, k \in Z \cr x+1, & x = 4i+2, k \in Z \cr 0, & x = 4i+3, k \in Z \end{array} \end{cases}$

则最终结果为 $sumXor(s-1) \oplus sumXor(s+n-1) * 2 + e$。

下面还有最后一位 e 的计算。

- 如果 start 为偶数，则最后一位 e 为 0。
- 如果 start 为奇数，最后一位 e 跟 n 有关，如果 n 为奇数，则最后一位 e 为 1，如果 n 为偶数，则最后一位 e 为 0。

总结下来就是 `e = start & n & 1`。

## 代码

1. 模拟

```python
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= (start + i * 2)
        return ans
```

2. 规律

```python
class Solution:
    def sumXor(self, x):
        if x % 4 == 0:
            return x
        if x % 4 == 1:
            return 1
        if x % 4 == 2:
            return x + 1
        return 0
    def xorOperation(self, n: int, start: int) -> int:
        s = start >> 1
        e = n & start & 1
        ans = self.sumXor(s-1) ^ self.sumXor(s + n - 1)
        return ans << 1 | e
```

