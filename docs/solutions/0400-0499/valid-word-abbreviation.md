# [0408. 有效单词缩写](https://leetcode.cn/problems/valid-word-abbreviation/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [0408. 有效单词缩写 - 力扣](https://leetcode.cn/problems/valid-word-abbreviation/)

## 题目大意

**描述**：

给定一个非空字符串 $word$ 和一个缩写 $abbr$，判断缩写是否是该单词的有效缩写。

字符串的缩写规则：用数字代替连续的字符。

例如，单词 `"substitution"` 可以缩写为：

- `"s10n"` (`"s ubstitutio n"`)
- `"sub4u4"` (`"sub stit u tion"`)
- `"12"` (`"substitution"`)
- `"su3i1u2on"` (`"su bst i t u ti on"`)
- `"substitution"` (没有替换子字符串)

下列是不合法的缩写：

- `"s55n"` (`"s ubsti tutio n"`，两处缩写相邻)
- `"s010n"` (缩写存在前导零)
- `"s0ubstitution"` (缩写是一个空字符串)

**要求**：

判断 $abbr$ 是否是 $word$ 的有效缩写。

**说明**：

- $1 \le word.length \le 20$。
- $1 \le abbr.length \le 10$。
- $word$ 只包含小写英文字母。
- $abbr$ 只包含小写英文字母和数字。
- 数字不能有前导零。

**示例**：

- 示例 1：

```python
输入：word = "internationalization", abbr = "i12iz4n"
输出：true
解释：单词 "internationalization" 可以缩写为 "i12iz4n" ("i nternational iz atio n")。
```

- 示例 2：

```python
输入：word = "apple", abbr = "a2e"
输出：false
解释：单词 "apple" 无法缩写为 "a2e"。
```

## 解题思路

### 思路 1：双指针

判断缩写 $abbr$ 是否是单词 $word$ 的有效缩写。缩写规则是用数字代替连续的字符。

**解题步骤**：

1. 使用两个指针 $i$ 和 $j$ 分别指向 $word$ 和 $abbr$。
2. 遍历 $abbr$：
   - 如果当前字符是数字，解析完整的数字（可能是多位数），然后将 $i$ 向后移动相应位数。
   - 注意：数字不能有前导零（如 "01" 是非法的）。
   - 如果当前字符是字母，检查是否与 $word[i]$ 相同，相同则 $i$ 和 $j$ 都向后移动。
3. 最后检查两个指针是否都到达末尾。

**边界情况**：

- 数字有前导零：返回 `False`。
- 数字导致 $i$ 超出 $word$ 长度：返回 `False`。

### 思路 1：代码

```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # i 指向 word，j 指向 abbr
        
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # 检查前导零
                if abbr[j] == '0':
                    return False
                
                # 解析完整的数字
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                # 移动 i 指针
                i += num
            else:
                # 字母必须匹配
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        # 两个指针都应该到达末尾
        return i == len(word) and j == len(abbr)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n)$，其中 $m$ 和 $n$ 分别是 $word$ 和 $abbr$ 的长度。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
