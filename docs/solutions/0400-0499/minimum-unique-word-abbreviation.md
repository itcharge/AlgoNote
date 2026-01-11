# [0411. 最短独占单词缩写](https://leetcode.cn/problems/minimum-unique-word-abbreviation/)

- 标签：位运算、数组、字符串、回溯
- 难度：困难

## 题目链接

- [0411. 最短独占单词缩写 - 力扣](https://leetcode.cn/problems/minimum-unique-word-abbreviation/)

## 题目大意

**描述**：

给定目标单词 $target$ 和字典 $dictionary$。

缩写规则：

- 你可以选择 $target$ 中任意数量的「不相邻」的子字符串（即这些子字符串在原串中不重叠且不相邻），将它们替换成它们的长度（十进制表示）。
- 其余字符保留原样。


例如 `"substitution"` 可以缩写为：

- `"s10n"`（替换 `"ubstitutio"` 长度为 10）
- `"sub4u4"`（替换 `"stit"` 和 `"tion"`，长度分别为 4 和 4，它们不相邻）
- `"12"`（替换整个字符串）
- `"su3i1u2on"`（替换 `"bst"`、`"t"`、`"ti"`，长度分别为 3、1、2，它们不相邻）
- `"substitution"`（不替换任何子串）

不允许替换两个相邻的子串，因为那样它们应该合并成一个更大的子串来替换。

- 例如 `"s55n"` 试图替换 `"ubsti"`（长度 5）和 `"tutio"`（长度 5），但这两个子串在原串中是相邻的（`"ubstitutio"` 是连续的），所以不允许，应该直接替换成 `"s10n"`。

**要求**：

在 $target$ 的所有合法缩写中，找出一个「长度最短」的缩写，并且这个缩写「不能」是 $dictionary$ 中任何其他字符串的缩写形式。

如果有多个最短长度的缩写，任意返回一个即可。

**说明**：

- $1 \le target.length \le 21$。
- $0 \le dictionary.length \le 1000$。
- $1 \le dictionary[i].length \le 100$。
- $target$ 和 $dictionary[i]$ 只包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：target = "apple", dictionary = ["blade"]
输出："a4"
解释："a4" 是最短的独占缩写，"blade" 无法匹配。
```

- 示例 2：

```python
输入：target = "apple", dictionary = ["plain","amber","blade"]
输出："1p3"
解释："1p3" 是最短的独占缩写。
```

## 解题思路

### 思路 1：回溯 + 剪枝

给定目标单词 $target$ 和字典 $dictionary$，需要找到最短的独占缩写，使得字典中的单词都不能匹配这个缩写。

**核心思路**：

- 枚举所有可能的缩写（保留不同位置的字符）。
- 对于每个缩写，检查是否与字典中的单词冲突。
- 使用位运算表示保留哪些字符：第 $i$ 位为 1 表示保留第 $i$ 个字符。
- 找到长度最短的不冲突缩写。

**解题步骤**：

1. 枚举所有可能的位掩码（$0$ 到 $2^n - 1$）。
2. 对于每个位掩码，生成对应的缩写。
3. 检查该缩写是否与字典中的单词冲突。
4. 记录最短的不冲突缩写。

**优化**：

- 按照保留字符数从少到多枚举（缩写长度从短到长）。
- 一旦找到不冲突的缩写，立即返回。

### 思路 1：代码

```python
class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)
        
        # 过滤掉长度不同的单词
        dictionary = [word for word in dictionary if len(word) == n]
        
        # 如果字典为空，返回最短缩写
        if not dictionary:
            return str(n)
        
        # 生成缩写
        def get_abbr(word, mask):
            abbr = []
            count = 0
            for i in range(len(word)):
                if mask & (1 << i):
                    if count > 0:
                        abbr.append(str(count))
                        count = 0
                    abbr.append(word[i])
                else:
                    count += 1
            if count > 0:
                abbr.append(str(count))
            return ''.join(abbr)
        
        # 检查缩写是否匹配单词
        def matches(abbr, word):
            i = j = 0
            while i < len(abbr) and j < len(word):
                if abbr[i].isdigit():
                    # 解析数字
                    if abbr[i] == '0':
                        return False
                    num = 0
                    while i < len(abbr) and abbr[i].isdigit():
                        num = num * 10 + int(abbr[i])
                        i += 1
                    j += num
                else:
                    if abbr[i] != word[j]:
                        return False
                    i += 1
                    j += 1
            return i == len(abbr) and j == len(word)
        
        # 按照保留字符数从少到多枚举
        min_len = float('inf')
        result = ""
        
        for mask in range(1 << n):
            abbr = get_abbr(target, mask)
            
            # 检查是否与字典中的单词冲突
            valid = True
            for word in dictionary:
                if matches(abbr, word):
                    valid = False
                    break
            
            if valid and len(abbr) < min_len:
                min_len = len(abbr)
                result = abbr
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^n \times m \times n)$，其中 $n$ 是目标单词长度，$m$ 是字典大小。需要枚举 $2^n$ 个缩写，每个缩写需要与 $m$ 个单词匹配。
- **空间复杂度**：$O(n)$，存储缩写字符串。
