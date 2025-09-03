# [1859. 将句子排序](https://leetcode.cn/problems/sorting-the-sentence/)

- 标签：字符串、排序
- 难度：简单

## 题目链接

- [1859. 将句子排序 - 力扣](https://leetcode.cn/problems/sorting-the-sentence/)

## 题目大意

**描述**：给定一个句子 $s$，句子中包含的单词不超过 $9$ 个。并且句子 $s$ 中每个单词末尾添加了「从 $1$ 开始的单词位置索引」，并且将句子中所有单词打乱顺序。

举个例子，句子 `"This is a sentence"` 可以被打乱顺序得到 `"sentence4 a3 is2 This1"` 或者 `"is2 sentence4 This1 a3"` 。

**要求**：重新构造并得到原本顺序的句子。

**说明**：

- **一个句子**：指的是一个序列的单词用单个空格连接起来，且开头和结尾没有任何空格。每个单词都只包含小写或大写英文字母。
- $2 \le s.length \le 200$。
- $s$ 只包含小写和大写英文字母、空格以及从 $1$ 到 $9$ 的数字。
- $s$ 中单词数目为 $1$ 到 $9$ 个。
- $s$ 中的单词由单个空格分隔。
- $s$ 不包含任何前导或者后缀空格。

**示例**：

- 示例 1：

```python
输入：s = "is2 sentence4 This1 a3"
输出："This is a sentence"
解释：将 s 中的单词按照初始位置排序，得到 "This1 is2 a3 sentence4" ，然后删除数字。
```

- 示例 2：

```python
输入：s = "Myself2 Me1 I4 and3"
输出："Me Myself and I"
解释：将 s 中的单词按照初始位置排序，得到 "Me1 Myself2 and3 I4" ，然后删除数字。
```

## 解题思路

### 思路 1：模拟

1. 将句子 $s$ 按照空格分隔成数组 $s\_list$。
2. 遍历数组 $s\_list$ 中的单词：
   1. 从单词中分割出对应单词索引 $idx$ 和对应单词 $word$。
   2. 将单词 $word$ 存入答案数组 $res$ 对应位置 $idx - 1$ 上，即：$res[int(idx) - 1] = word$。
3. 将答案数组用空格拼接成句子字符串，并返回。

### 思路 1：代码

```python
class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        size = len(s_list)
        res = ["" for _ in range(size)]
        for sub in s_list:
            idx = ""
            word = ""
            for ch in sub:
                if '1' <= ch <= '9':
                    idx += ch
                else:
                    word += ch
            res[int(idx) - 1] = word

        return " ".join(res)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m)$，其中 $m$ 为给定句子 $s$ 的长度。
- **空间复杂度**：$O(m)$。

