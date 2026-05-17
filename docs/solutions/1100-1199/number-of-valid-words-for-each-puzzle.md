# [1178. 猜字谜](https://leetcode.cn/problems/number-of-valid-words-for-each-puzzle/)

- 标签：位运算、字典树、数组、哈希表、字符串
- 难度：困难

## 题目链接

- [1178. 猜字谜 - 力扣](https://leetcode.cn/problems/number-of-valid-words-for-each-puzzle/)

## 题目大意

**描述**：给定一个单词列表 $words$ 和一个谜面列表 $puzzles$。一个单词 $word$ 能作为谜面 $puzzle$ 的谜底，必须同时满足两个条件：

1. 单词 $word$ 中包含谜面 $puzzle$ 的第一个字母。
2. 单词 $word$ 中的每个字母都在谜面 $puzzle$ 中出现过。

例如，谜面为 `"abcdefg"`，那么 `"faced"`、`"cabbage"` 都是有效谜底（所有字母都在谜面中，且包含首字母 `a`），而 `"beefed"`（不含 `a`）和 `"based"`（含 `s` 不在谜面中）都不是。

**要求**：返回一个数组 $answer$，$answer[i]$ 表示单词列表 $words$ 中能作为谜面 $puzzles[i]$ 谜底的单词数量。

**说明**：

- $1 \le words.length \le 10^5$。
- $4 \le words[i].length \le 50$。
- $1 \le puzzles.length \le 10^4$。
- $puzzles[i].length == 7$。
- $words[i][j]$、$puzzles[i][j]$ 都是小写英文字母。
- 每个 $puzzles[i]$ 所包含的字符都不重复。

**示例**：

```python
输入：
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
输出：[1,1,3,2,4,0]
```

## 解题思路

### 思路 1：位运算 + 哈希表 + 子集枚举

**为什么用二进制表示？** 小写字母一共 26 个，一个整数的二进制位有 32 位，足够用了。比如 `"aab"` 的二进制就是 `...0000011`（第 0 位和第 1 位是 1，表示包含 `a` 和 `b`）。这样判断一个单词的字母是否都在谜面里，只需要检查 `(word_mask & ~puzzle_mask) == 0`，一次位运算就搞定。

**拆解步骤**：

1. **预处理所有单词**：把每个单词转换成二进制表示（只关心有哪些字母，不关心出现几次），用哈希表统计每种二进制表示的单词数量。注意单词中可能有重复字母（如 `"aaaa"`），但二进制表示是一样的。

2. **对每个谜面**：
   - 把谜面也转成二进制表示
   - 枚举它的所有子集，但只考虑**包含首字母**的子集
   - 对于每个子集，从哈希表中取出对应的单词数量，累加起来

3. **返回累加结果**。

**子集枚举技巧**：给定一个集合的二进制表示 $mask$，枚举它的所有子集有一个经典写法：
```python
sub = mask
while sub:
    # 处理子集 sub
    sub = (sub - 1) & mask
```
如果想强制包含某个位，可以先把这个位或进去，再枚举剩余位的子集。

### 思路 1：代码

```python
from collections import Counter

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # 工具函数：把单词转成二进制表示（26 位，a 对应第 0 位）
        def word_to_bits(word):
            bits = 0
            for ch in word:
                bits |= 1 << (ord(ch) - ord('a'))
            return bits

        # 统计每种二进制表示对应多少个单词
        word_count = Counter(word_to_bits(word) for word in words)

        ans = []

        for puzzle in puzzles:
            # 谜面的二进制表示
            puzzle_bits = word_to_bits(puzzle)
            # 谜面首字母对应的位（必须包含）
            first_bit = 1 << (ord(puzzle[0]) - ord('a'))

            count = 0
            # 枚举谜面所有可能子集
            sub = puzzle_bits
            while sub:
                # 只考虑包含首字母的子集
                if sub & first_bit:
                    count += word_count[sub]
                # 枚举下一个子集（经典技巧）
                sub = (sub - 1) & puzzle_bits

            ans.append(count)

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n \times 2^7)$。用人话说就是：预处理 $m$ 个单词需要 $O(m)$ 时间；每个谜面最多有 $2^7 = 128$ 个子集（因为谜面固定只有 7 个字母），对 $n$ 个谜面就是 $O(n \times 128)$。总时间大约在百万级别，是可行的。
- **空间复杂度**：$O(m)$。哈希表最多存储 $m$ 种不同的单词二进制表示。
