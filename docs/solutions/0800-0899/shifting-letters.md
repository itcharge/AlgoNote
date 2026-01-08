# [0848. 字母移位](https://leetcode.cn/problems/shifting-letters/)

- 标签：数组、字符串、前缀和
- 难度：中等

## 题目链接

- [0848. 字母移位 - 力扣](https://leetcode.cn/problems/shifting-letters/)

## 题目大意

**描述**：

有一个由小写字母组成的字符串 $s$，和一个长度相同的整数数组 $shifts$。

我们将字母表中的下一个字母称为原字母的「移位 `shift()`」 （由于字母表是环绕的， `'z'` 将会变成 `'a'`）。

- 例如，`shift('a') = 'b'`, `shift('t') = 'u'`, 以及 `shift('z') = 'a'`。

对于每个 $shifts[i] = x$，我们会将 $s$ 中的前 $i + 1$ 个字母移位 $x$ 次。

**要求**：

返回「将所有这些移位都应用到 $s$ 后最终得到的字符串」。


**说明**：

- $1 \le s.length \le 10^{5}$。
- $s$ 由小写英文字母组成。
- $shifts.length == s.length$。
- $0 \le shifts[i] \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：s = "abc", shifts = [3,5,9]
输出："rpl"
解释： 
我们以 "abc" 开始。
将 S 中的第 1 个字母移位 3 次后，我们得到 "dbc"。
再将 S 中的前 2 个字母移位 5 次后，我们得到 "igc"。
最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 "rpl"。
```

- 示例 2：

```python
输入：
输出：
```

## 解题思路

### 思路 1:后缀和

根据题意,对于位置 $i$ 的字符,它需要移位的总次数为 $\sum_{j=i}^{n-1} shifts[j]$。

如果直接计算每个位置的移位次数,时间复杂度为 $O(n^2)$,会超时。我们可以使用后缀和来优化:

1. 从后向前遍历 $shifts$ 数组,计算后缀和 $total$。
2. 对于位置 $i$,其移位次数为 $total$。
3. 将字符 $s[i]$ 移位 $total \bmod 26$ 次(因为字母表是循环的)。
4. 更新 $total$ 为下一个位置的后缀和。

### 思路 1:代码

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        res = []
        total = 0  # 后缀和
        
        # 从后向前遍历
        for i in range(n - 1, -1, -1):
            total += shifts[i]
            # 计算移位后的字符
            # ord(s[i]) - ord('a') 得到字符相对于 'a' 的偏移量
            # 加上移位次数后对 26 取模,得到新的偏移量
            new_char = chr((ord(s[i]) - ord('a') + total) % 26 + ord('a'))
            res.append(new_char)
        
        # 因为是从后向前遍历,需要反转结果
        return ''.join(res[::-1])
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n)$,其中 $n$ 是字符串 $s$ 的长度。只需遍历一次数组。
- **空间复杂度**:$O(n)$,需要存储结果字符串。
