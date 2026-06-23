# [1455. 检查单词是否为句中其他单词的前缀](https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

- 标签：字符串、双指针
- 难度：简单

## 题目链接

- [1455. 检查单词是否为句中其他单词的前缀 - 力扣](https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

## 题目大意

**描述**：给定一个字符串 $sentence$ 表示一个句子（由若干单词用空格分隔），和一个字符串 $searchWord$。

**要求**：返回 $searchWord$ 在句子中某个单词的前缀中第一次出现时的单词索引（从 $1$ 开始）。如果不存在，返回 $-1$。

**说明**：
- $1 \le sentence.length \le 100$。
- $1 \le searchWord.length \le 10$。

**示例**：

- 示例 1：

```python
输入：sentence = "i love eating burger", searchWord = "burg"
输出：4
解释："burg" 是 "burger" 的前缀，而 "burger" 是句子中第 4 个单词。
```

- 示例 2：

```python
输入：sentence = "this problem is an easy problem", searchWord = "pro"
输出：2
解释："pro" 是 "problem" 的前缀，而 "problem" 是句子中第 2 个也是第 6 个单词，但是应该返回最小下标 2 。
```

## 解题思路

### 思路 1：分割 + 遍历

#### 1. 核心思想

将句子按空格分割成单词列表，遍历每个单词检查是否以 $searchWord$ 开头。返回第一个匹配的单词的索引（$1$ 索引）。

#### 2. 具体步骤

**第 1 步**：用 `split()` 将 $sentence$ 分割成单词列表。

**第 2 步**：遍历单词列表，对每个单词使用 `startswith()` 或切片比较。

**第 3 步**：如果找到，返回 $i + 1$（$1$ 索引）。

**第 4 步**：遍历完成未找到，返回 $-1$。

#### 3. 举例说明

以 $sentence = "i love eating burger", searchWord = "burg"$ 为例：

分割后：$["i", "love", "eating", "burger"]$

- "i".startswith("burg") → False
- "love".startswith("burg") → False
- "eating".startswith("burg") → False
- "burger".startswith("burg") → True，索引 $4$

返回 $4$。

### 思路 1：代码

```python
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是单词数，$m$ 是 $searchWord$ 长度。
- **空间复杂度**：$O(n)$，存储分割后的单词列表。
