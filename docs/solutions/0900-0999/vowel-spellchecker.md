# [0966. 元音拼写检查器](https://leetcode.cn/problems/vowel-spellchecker/)

- 标签：数组、哈希表、字符串
- 难度：中等

## 题目链接

- [0966. 元音拼写检查器 - 力扣](https://leetcode.cn/problems/vowel-spellchecker/)

## 题目大意

**描述**：

在给定单词列表 $wordlist$ 的情况下，我们希望实现一个拼写检查器，将查询单词转换为正确的单词。

对于给定的查询单词 $query$，拼写检查器将会处理两类拼写错误：

- 大小写：如果查询匹配单词列表中的某个单词（不区分大小写），则返回的正确单词与单词列表中的大小写相同。
   - 例如：`wordlist = ["yellow"]`, `query = "YellOw"`: `correct = "yellow"`
   - 例如：`wordlist = ["yellow"]`, `query = "yellow"`: `correct = "Yellow"`
   - 例如：`wordlist = ["yellow"]`, `query = "yellow"`: `correct = "yellow"`
- 元音错误：如果在将查询单词中的元音 (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`)  分别替换为任何元音后，能与单词列表中的单词匹配（不区分大小写），则返回的正确单词与单词列表中的匹配项大小写相同。
   - 例如：`wordlist = ["yellow"]`, `query = "yollow"`: `correct = "YellOw"`
   - 例如：`wordlist = ["yellow"]`, `query = "yeellow"`: `correct = ""` （无匹配项）
   - 例如：`wordlist = ["yellow"]`, `query = "yllw"`: `correct = ""` （无匹配项）

此外，拼写检查器还按照以下优先级规则操作：

- 当查询完全匹配单词列表中的某个单词（区分大小写）时，应返回相同的单词。
- 当查询匹配到大小写问题的单词时，您应该返回单词列表中的第一个这样的匹配项。
- 当查询匹配到元音错误的单词时，您应该返回单词列表中的第一个这样的匹配项。
- 如果该查询在单词列表中没有匹配项，则应返回空字符串。

给定一些查询 $queries$。

**要求**：

返回一个单词列表 $answer$，其中 $answer[i]$ 是由查询 $query = queries[i]$ 得到的正确单词。

**说明**：

- $1 \le wordlist.length, queries.length \le 5000$。
- $1 \le wordlist[i].length, queries[i].length \le 7$。
- $wordlist[i]$ 和 $queries[i]$ 只包含英文字母。

**示例**：

- 示例 1：

```python
输入：wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
输出：["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
```

- 示例 2：

```python
输入：wordlist = ["yellow"], queries = ["YellOw"]
输出：["yellow"]
```

## 解题思路

### 思路 1：哈希表

使用三个哈希表分别处理三种匹配情况：完全匹配、大小写匹配、元音匹配。

1. 建立三个哈希表：
   - $exact$：存储完全匹配的单词。
   - $lower$：存储小写形式的单词（用于大小写匹配）。
   - $vowel$：存储元音替换后的单词（用于元音匹配）。
2. 对于每个查询，按优先级依次查找：
   - 首先查找完全匹配。
   - 其次查找大小写匹配。
   - 最后查找元音匹配。
3. 如果都没有匹配，返回空字符串。

### 思路 1：代码

```python
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # 将元音替换为统一字符
        def devowel(word):
            return ''.join('*' if c in 'aeiouAEIOU' else c for c in word)
        
        # 三个哈希表
        exact = set(wordlist)  # 完全匹配
        lower = {}  # 大小写匹配
        vowel = {}  # 元音匹配
        
        for word in wordlist:
            lower_word = word.lower()
            vowel_word = devowel(lower_word)
            
            # 只保留第一个匹配的单词
            if lower_word not in lower:
                lower[lower_word] = word
            if vowel_word not in vowel:
                vowel[vowel_word] = word
        
        result = []
        for query in queries:
            # 1. 完全匹配
            if query in exact:
                result.append(query)
            # 2. 大小写匹配
            elif query.lower() in lower:
                result.append(lower[query.lower()])
            # 3. 元音匹配
            elif devowel(query.lower()) in vowel:
                result.append(vowel[devowel(query.lower())])
            # 4. 无匹配
            else:
                result.append("")
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m + q \times m)$，其中 $n$ 是单词列表的长度，$q$ 是查询列表的长度，$m$ 是单词的平均长度。
- **空间复杂度**：$O(n \times m)$，需要存储所有单词的不同形式。
