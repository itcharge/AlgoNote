# [0866. 回文质数](https://leetcode.cn/problems/prime-palindrome/)

- 标签：数学、数论
- 难度：中等

## 题目链接

- [0866. 回文质数 - 力扣](https://leetcode.cn/problems/prime-palindrome/)

## 题目大意

**描述**：

给定一个整数 $n$。

**要求**：

返回大于或等于 $n$ 的最小 回文质数。

**说明**：

- 一个整数如果恰好有两个除数：1 和它本身，那么它是「质数」。注意，1 不是质数。
   - 例如，2、3、5、7、11 和 13 都是质数。
- 一个整数如果从左向右读和从右向左读是相同的，那么它是「回文数」。
   - 例如，101 和 12321 都是回文数。
- 测试用例保证答案总是存在，并且在 $[2, 2 \times 10^8]$ 范围内。
- $1 \le n \le 10^{8}$。

**示例**：

- 示例 1：

```python
输入：n = 6
输出：7
```

- 示例 2：

```python
输入：n = 8
输出：11
```

## 解题思路

### 思路 1:数学 + 枚举

关键观察:除了 11 之外,所有偶数位的回文数都能被 11 整除,因此不是质数。

所以我们只需要检查奇数位的回文数即可。

1. 编写判断质数的函数 `is_prime(x)`。
2. 编写判断回文数的函数 `is_palindrome(x)`。
3. 从 $n$ 开始枚举:
   - 如果当前数是偶数位且大于 11,直接跳到下一个奇数位的起始位置
   - 否则检查是否同时是回文数和质数
4. 返回第一个满足条件的数。

### 思路 1:代码

```python
class Solution:
    def primePalindrome(self, n: int) -> int:
        # 判断是否为质数
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            # 只需检查到 sqrt(x)
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True
        
        # 判断是否为回文数
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]
        
        # 特判
        if n == 1:
            return 2
        
        # 从 n 开始枚举
        x = n
        while True:
            # 如果是偶数位且大于 11,跳到下一个奇数位
            s = str(x)
            if len(s) % 2 == 0 and x > 11:
                # 跳到下一个奇数位的起始位置
                x = 10 ** len(s)
                continue
            
            # 检查是否同时是回文数和质数
            if is_palindrome(x) and is_prime(x):
                return x
            
            x += 1
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(N \sqrt{N})$,其中 $N$ 是答案的大小。需要枚举并检查每个数是否为质数。
- **空间复杂度**:$O(\log N)$,字符串转换需要的空间。
