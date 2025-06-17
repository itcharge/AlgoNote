# [0557. 反转字符串中的单词 III](https://leetcode.cn/problems/reverse-words-in-a-string-iii/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [0557. 反转字符串中的单词 III - 力扣](https://leetcode.cn/problems/reverse-words-in-a-string-iii/)

## 题目大意

**描述**：给定一个字符串 `s`。

**要求**：将字符串中每个单词的字符顺序进行反装，同时仍保留空格和单词的初始顺序。

**说明**：

- $1 \le s.length \le 5 * 10^4$。
- `s` 包含可打印的 ASCII 字符。
- `s` 不包含任何开头或结尾空格。
- `s` 里至少有一个词。
- `s` 中的所有单词都用一个空格隔开。

**示例**：

- 示例 1：

```python
输入：s = "Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
```

- 示例 2：

```python
输入： s = "God Ding"
输出："doG gniD"
```

## 解题思路

### 思路 1：使用额外空间

因为 Python 的字符串是不可变的，所以在原字符串空间上进行切换顺序操作肯定是不可行的了。但我们可以利用切片方法。

1. 将字符串按空格进行分割，分割成一个个的单词。
2. 再将每个单词进行反转。
3. 最后将每个单词连接起来。

### 思路 1：代码

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。