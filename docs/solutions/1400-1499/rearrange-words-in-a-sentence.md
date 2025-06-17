# [1451. 重新排列句子中的单词](https://leetcode.cn/problems/rearrange-words-in-a-sentence/)

- 标签：字符串、排序
- 难度：中等

## 题目链接

- [1451. 重新排列句子中的单词 - 力扣](https://leetcode.cn/problems/rearrange-words-in-a-sentence/)

## 题目大意

**描述**：「句子」是一个用空格分隔单词的字符串。给定一个满足下述格式的句子 $text$:

- 句子的首字母大写。
- $text$ 中的每个单词都用单个空格分隔。

**要求**：重新排列 $text$ 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。

请同样按上述格式返回新的句子。

**说明**：

- $text$ 以大写字母开头，然后包含若干小写字母以及单词间的单个空格。
- $1 \le text.length \le 10^5$。

**示例**：

- 示例 1：

```python
输入：text = "Leetcode is cool"
输出："Is cool leetcode"
解释：句子中共有 3 个单词，长度为 8 的 "Leetcode" ，长度为 2 的 "is" 以及长度为 4 的 "cool"。
输出需要按单词的长度升序排列，新句子中的第一个单词首字母需要大写。
```

- 示例 2：

```python
输入：text = "Keep calm and code on"
输出："On and keep calm code"
解释：输出的排序情况如下：
"On" 2 个字母。
"and" 3 个字母。
"keep" 4 个字母，因为存在长度相同的其他单词，所以它们之间需要保留在原句子中的相对顺序。
"calm" 4 个字母。
"code" 4 个字母。
```

## 解题思路

### 思路 1：模拟

1. 将 $text$ 按照 `" "` 进行分割为单词数组 $words$。
2. 将单词数组按照「单词长度」进行升序排序。
3. 将单词数组用 `" "` 连接起来，并将首字母转为大写字母，其他字母转为小写字母，将结果存入答案字符串 $ans$ 中。
4. 返回答案字符串 $ans$。

### 思路 1：代码

```Python
class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        words.sort(key=lambda word:len(word))
        ans = " ".join(words).capitalize()

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 为字符串 $text$ 的长度。
- **空间复杂度**：$O(n)$。

