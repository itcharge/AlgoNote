# [0423. 从英文中重建数字](https://leetcode.cn/problems/reconstruct-original-digits-from-english/)

- 标签：哈希表、数学、字符串
- 难度：中等

## 题目链接

- [0423. 从英文中重建数字 - 力扣](https://leetcode.cn/problems/reconstruct-original-digits-from-english/)

## 题目大意

**描述**：

给定一个字符串 $s$，其中包含字母顺序打乱的用英文单词表示的若干数字（$0 \sim 9$）。

**要求**：

按升序返回原始的数字。

**说明**：

- $1 \le s.length \le 10^{5}$。
- $s[i]$ 为 `["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]` 这些字符之一。
- $s$ 保证是一个符合题目要求的字符串。

**示例**：

- 示例 1：

```python
输入：s = "owoztneoer"
输出："012"
```

- 示例 2：

```python
输入：s = "fviefuro"
输出："45"
```

## 解题思路

### 思路 1：哈希表统计 + 特征字符识别

这道题目的关键在于利用英文字母的特征来识别数字。

每个英文单词中都有一些独特字符可以帮助我们识别：

- `"zero"` 中的 `'z'` 是独一无二的
- `"two"` 中的 `'w'` 是独一无二的
- `"four"` 中的 `'u'` 是独一无二的
- `"six"` 中的 `'x'` 是独一无二的
- `"eight"` 中的 `'g'` 是独一无二的

利用这些特征字符，我们可以：

1. 先统计字符串 $s$ 中每个字符 $ch$ 的出现次数 $count[ch]$。
2. 识别出具有特征字符的数字：
   - $cnt[0]$ 的数量 = $count['z']$
   - $cnt[2]$ 的数量 = $count['w']$
   - $cnt[4]$ 的数量 = $count['u']$
   - $cnt[6]$ 的数量 = $count['x']$
   - $cnt[8]$ 的数量 = $count['g']$
3. 根据已有数字的出现次数，推断其他数字：
   - $cnt[1]$ 的数量 = $count['o'] - cnt[0] - cnt[2] - cnt[4]$（`'o'` 出现在 `"zero"`, `"one"`, `"two"`, `"four"` 中）
   - $cnt[3]$ 的数量 = $count['h'] - cnt[8]$（`'h'` 出现在 `"three"`, `"eight"` 中）
   - $cnt[5]$ 的数量 = $count['f'] - cnt[4]$（`'f'` 出现在 `"five"`, `"four"` 中）
   - $cnt[7]$ 的数量 = $count['s'] - cnt[6]$（`'s'` 出现在 `"seven"`, `"six"` 中）
   - $cnt[9]$ 的数量 = $count['i'] - cnt[5] - cnt[6] - cnt[8]$（`'i'` 出现在 `"nine"`, `"five"`, `"six"`, `å` 中）
4. 最后按照数字大小 $0 \sim 9$ 的顺序构造结果字符串。

### 思路 1：代码

```python
class Solution:
    def originalDigits(self, s: str) -> str:
        # 统计每个字符的出现次数
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        # cnt[i] 表示数字 i 的出现次数
        cnt = [0] * 10
        
        # 通过特征字符识别数字
        cnt[0] = count.get('z', 0)  # zero
        cnt[2] = count.get('w', 0)  # two
        cnt[4] = count.get('u', 0)  # four
        cnt[6] = count.get('x', 0)  # six
        cnt[8] = count.get('g', 0)  # eight
        
        # 根据已有数字推断其他数字
        cnt[1] = count.get('o', 0) - cnt[0] - cnt[2] - cnt[4]  # one (o 在 zero, one, two, four 中)
        cnt[3] = count.get('h', 0) - cnt[8]  # three (h 在 three, eight 中)
        cnt[5] = count.get('f', 0) - cnt[4]  # five (f 在 four, five 中)
        cnt[7] = count.get('s', 0) - cnt[6]  # seven (s 在 six, seven 中)
        cnt[9] = count.get('i', 0) - cnt[5] - cnt[6] - cnt[8]  # nine (i 在 five, six, eight, nine 中)
        
        # 构造结果字符串
        res = ""
        for i in range(10):
            res += str(i) * cnt[i]
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + 10)$。其中 $n$ 是字符串 $s$ 的长度。需要遍历字符串统计字符出现次数（$O(n)$），然后进行常数次计算（$O(10)$）。
- **空间复杂度**：$O(|\Sigma| + 10)$。其中 $|\Sigma|$ 是字符集大小，这里最多为 26 个字母。$O(10)$ 是用于存储每个数字出现次数的数组。
