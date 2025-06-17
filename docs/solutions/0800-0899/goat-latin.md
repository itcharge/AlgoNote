# [0824. 山羊拉丁文](https://leetcode.cn/problems/goat-latin/)

- 标签：字符串
- 难度：简单

## 题目链接

- [0824. 山羊拉丁文 - 力扣](https://leetcode.cn/problems/goat-latin/)

## 题目大意

**描述**：给定一个由若干单词组成的句子 $sentence$，单词之间由空格分隔。每个单词仅由大写和小写字母组成。

**要求**：将句子转换为「山羊拉丁文（Goat Latin）」，并返回将 $sentence$ 转换为山羊拉丁文后的句子。

**说明**：

- 山羊拉丁文的规则如下：
  - 如果单词以元音开头（`a`，`e`，`i`，`o`，`u`），在单词后添加 `"ma"`。
    - 例如，单词 `"apple"` 变为 `"applema"`。

  - 如果单词以辅音字母开头（即，非元音字母），移除第一个字符并将它放到末尾，之后再添加 `"ma"`。
    - 例如，单词 `"goat"` 变为 `"oatgma"`。

  - 根据单词在句子中的索引，在单词最后添加与索引相同数量的字母 `a`，索引从 $1$ 开始。
    - 例如，在第一个单词后添加 `"a"` ，在第二个单词后添加 `"aa"`，以此类推。

- $1 \le sentence.length \le 150$。
- $sentence$ 由英文字母和空格组成。
- $sentence$ 不含前导或尾随空格。
- $sentence$ 中的所有单词由单个空格分隔。

**示例**：

- 示例 1：

```python
输入：sentence = "I speak Goat Latin"
输出："Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
```

- 示例 2：

```python
输入：sentence = "The quick brown fox jumped over the lazy dog"
输出："heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
```

## 解题思路

### 思路 1：模拟

1. 使用集合 $vowels$ 存储元音字符，然后将 $sentence$ 按照空格分隔成单词数组 $words$。
2. 遍历单词数组 $words$，对于当前单词 $word$，根据山羊拉丁文的规则，将其转为山羊拉丁文的单词，并存入答案数组 $res$ 中。
3. 遍历完之后将答案数组拼接为字符串并返回。

### 思路 1：代码

```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        words = sentence.split(' ')
        res = []
        for i in range(len(words)):
            word = words[i]
            ans = ""
            if word[0] in vowels:
                ans += word + "ma"
            else:
                ans += word[1:] + word[0] + "ma"
            ans += 'a' * (i + 1)
            res.append(ans)

        return " ".join(res)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

