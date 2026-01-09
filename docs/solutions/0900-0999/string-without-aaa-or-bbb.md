# [0984. 不含 AAA 或 BBB 的字符串](https://leetcode.cn/problems/string-without-aaa-or-bbb/)

- 标签：贪心、字符串
- 难度：中等

## 题目链接

- [0984. 不含 AAA 或 BBB 的字符串 - 力扣](https://leetcode.cn/problems/string-without-aaa-or-bbb/)

## 题目大意

**描述**：

给定两个整数 $a$ 和 $b$。

**要求**：

返回 任意 字符串 $s$，要求满足：

- $s$ 的长度为 $a + b$，且正好包含 $a$ 个 `'a'` 字母与 $b$ 个 `'b'` 字母；
- 子串 `'aaa'` 没有出现在 $s$ 中；
- 子串 `'bbb'` 没有出现在 $s$ 中。

**说明**：

- $0 \le a, b \le 10^{3}$。
- 对于给定的 $a$ 和 $b$，保证存在满足要求的 $s$。

**示例**：

- 示例 1：

```python
输入：a = 1, b = 2
输出："abb"
解释："abb", "bab" 和 "bba" 都是正确答案。
```

- 示例 2：

```python
输入：a = 4, b = 1
输出："aabaa"
```

## 解题思路

### 思路 1：贪心

使用贪心策略构造字符串：优先放置数量较多的字符，但要避免连续三个相同字符。

1. 每次选择剩余数量较多的字符。
2. 如果该字符已经连续出现两次，则必须放置另一个字符。
3. 否则，如果该字符数量较多，可以连续放置两个；如果数量相近，则只放置一个。
4. 重复上述过程，直到所有字符都放置完毕。

### 思路 1：代码

```python
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        
        while a > 0 or b > 0:
            # 判断是否需要写入 'a'
            write_a = False
            n = len(result)
            
            # 如果最后两个字符是 'bb'，必须写 'a'
            if n >= 2 and result[-1] == result[-2] == 'b':
                write_a = True
            # 如果最后两个字符是 'aa'，不能写 'a'
            elif n >= 2 and result[-1] == result[-2] == 'a':
                write_a = False
            # 否则，选择剩余数量较多的字符
            else:
                write_a = a >= b
            
            if write_a:
                result.append('a')
                a -= 1
            else:
                result.append('b')
                b -= 1
        
        return ''.join(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(a + b)$，需要构造长度为 $a + b$ 的字符串。
- **空间复杂度**：$O(1)$，不考虑结果字符串的空间。
