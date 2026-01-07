# [0809. 情感丰富的文字](https://leetcode.cn/problems/expressive-words/)

- 标签：数组、双指针、字符串
- 难度：中等

## 题目链接

- [0809. 情感丰富的文字 - 力扣](https://leetcode.cn/problems/expressive-words/)

## 题目大意

**描述**：

有时候人们会用重复写一些字母来表示额外的感受，比如 `"hello"` -> `"heeellooo"`, `"hi"` -> `"hiii"`。我们将相邻字母都相同的一串字符定义为相同字母组，例如：`"h"`, `"eee"`,` "ll"`, `"ooo"`。

对于一个给定的字符串 $S$ ，如果另一个单词能够通过将一些字母组扩张从而使其和 $S$ 相同，我们将这个单词定义为可扩张的（stretchy）。

扩张操作定义如下：选择一个字母组（包含字母 $c$ ），然后往其中添加相同的字母 $c$ 使其长度达到 3 或以上。

- 例如，以 `"hello"` 为例，我们可以对字母组 `"o"` 扩张得到 `"hellooo"`，但是无法以同样的方法得到 `"helloo"` 因为字母组 `"oo"` 长度小于 3。此外，我们可以进行另一种扩张 `"ll" -> "lllll"` 以获得 `"helllllooo"`。如果 ·，那么查询词 "hello" 是可扩张的，因为可以对它执行这两种扩张操作使得 `query = "hello"` -> `"hellooo"` -> `"helllllooo" = s`。

给定字符串 $S$ 和一组查询单词 $words$。

**要求**：

输出其中可扩张的单词数量。

**说明**：

- $1 \le s.length, words.length \le 10^{3}$。
- $1 \le words[i].length \le 10^{3}$。
- $s$ 和所有在 $words$ 中的单词都只由小写字母组成。

**示例**：

- 示例 1：

```python
输入： 
s = "heeellooo"
words = ["hello", "hi", "helo"]
输出：1
解释：
我们能通过扩张 "hello" 的 "e" 和 "o" 来得到 "heeellooo"。
我们不能通过扩张 "helo" 来得到 "heeellooo" 因为 "ll" 的长度小于 3 。
```

## 解题思路

### 思路 1：双指针

这道题要求判断一个单词是否可以通过扩张字母组得到目标字符串 $s$。

关键规则：

- 扩张操作只能将字母组扩张到长度 3 或以上。
- 如果原字母组长度已经是 3 或以上，可以继续扩张。
- 如果原字母组长度小于 3，不能扩张。

算法步骤：

1. 使用双指针分别遍历 $s$ 和 $word$。
2. 对于每个字母组，统计在 $s$ 和 $word$ 中的连续出现次数。
3. 判断是否可以扩张：
   - 如果字母不同，返回 $False$。
   - 如果 $s$ 中的次数小于 $word$ 中的次数，无法扩张，返回 $False$。
   - 如果 $s$ 中的次数大于 $word$ 中的次数，但 $s$ 中的次数小于 3，无法扩张，返回 $False$。
4. 如果所有字母组都满足条件，返回 $True$。

### 思路 1：代码

```python
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(word):
            """检查 word 是否可以扩张得到 s"""
            i, j = 0, 0
            n, m = len(s), len(word)
            
            while i < n and j < m:
                # 如果字母不同，无法扩张
                if s[i] != word[j]:
                    return False
                
                # 统计 s 中当前字母的连续出现次数
                ch = s[i]
                cnt_s = 0
                while i < n and s[i] == ch:
                    cnt_s += 1
                    i += 1
                
                # 统计 word 中当前字母的连续出现次数
                cnt_word = 0
                while j < m and word[j] == ch:
                    cnt_word += 1
                    j += 1
                
                # 判断是否可以扩张
                if cnt_s < cnt_word:
                    # s 中的次数少于 word，无法扩张
                    return False
                if cnt_s > cnt_word and cnt_s < 3:
                    # s 中的次数多于 word，但少于 3，无法扩张
                    return False
            
            # 检查是否都遍历完
            return i == n and j == m
        
        # 统计可扩张的单词数量
        count = 0
        for word in words:
            if check(word):
                count += 1
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是 $\text{words}$ 的长度，$m$ 是字符串 $s$ 的长度。需要对每个单词进行检查。
- **空间复杂度**：$O(1)$，只使用常数额外空间。
