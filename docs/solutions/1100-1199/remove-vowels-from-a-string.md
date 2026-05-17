# [1119. 删去字符串中的元音](https://leetcode.cn/problems/remove-vowels-from-a-string/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1119. 删去字符串中的元音 - 力扣](https://leetcode.cn/problems/remove-vowels-from-a-string/)

## 题目大意

**描述**：给定一个字符串 $s$。

**要求**：删去其中的所有元音字母 `'a'`、`'e'`、`'i'`、`'o'`、`'u'`，返回剩下的字符组成的新字符串。

**说明**：

- $1 \le s.length \le 10^3$。
- $s$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "leetcodeisacommunityforcoders"
输出："ltcdscmmntyfrcdrs"
```

- 示例 2：

```python
输入：s = "aeiou"
输出：""
```

## 解题思路

### 思路 1：字符串遍历

**拆解步骤**：

1. 用一个集合存好所有元音字母，方便快速判断。
2. 遍历字符串中的每个字符。
3. 如果当前字符不是元音，就加入结果列表。
4. 把结果列表拼接成字符串返回。

**为什么用列表而不是直接字符串拼接？** Python 中字符串是不可变的，每次拼接都会创建新字符串，效率低。用列表收集字符最后一次性 `join` 效率更高。虽然不是这道题的关键（$n$ 只有 $10^3$），但这是好习惯。

### 思路 1：代码

```python
class Solution:
    def removeVowels(self, s: str) -> str:
        # 元音字母集合，用集合方便快速判断
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # 收集非元音字符
        result = []
        for ch in s:
            if ch not in vowels:
                result.append(ch)

        # 拼接成字符串返回
        return ''.join(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。用人话说就是：从头到尾遍历一次字符串，每个字符判断是否元音是常数时间。
- **空间复杂度**：$O(n)$。结果字符串的长度最多和原字符串一样长。
