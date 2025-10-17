# [0030. 串联所有单词的子串](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/)

- 标签：哈希表、字符串、滑动窗口
- 难度：困难

## 题目链接

- [0030. 串联所有单词的子串 - 力扣](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/)

## 题目大意

**描述**：

给定一个字符串 $s$ 和一个字符串数组 $words$。$words$ 中所有字符串长度相同。

$s$ 中的「串联子串」是指一个包含 $words$ 中所有字符串以任意顺序排列连接起来的子串。
- 例如，如果 $words = ["ab","cd","ef"]$， 那么 `"abcdef"`， `"abefcd"`，`"cdabef"`， `"cdefab"`，`"efabcd"` 和 `"efcdab"` 都是串联子串。 `"acdbef"` 不是串联子串，因为他不是任何 $words$ 排列的连接。

**要求**：

返回所有串联子串在 $s$ 中的开始索引。你可以以任意顺序返回答案。

**说明**：

- $1 \le s.length \le 10^4$。
- $1 \le words.length \le 5000$。
- $1 <= words[i].length <= 30$。
- $words[i]$ 和 $s$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
输出顺序无关紧要。返回 [9,0] 也是可以的。
```

- 示例 2：

```python
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
所以我们返回一个空数组。
```

## 解题思路

### 思路 1：滑动窗口 + 哈希表

**核心思想**：

使用滑动窗口技术，结合哈希表来统计单词出现次数，通过固定窗口大小来检查所有可能的串联子串。

**算法步骤**：

1. **计算窗口大小**：串联子串的长度为 $word\_length \times word\_count$，其中 $word\_length$ 是每个单词的长度，$word\_count$ 是单词数组的长度。

2. **构建目标哈希表**：统计 $words$ 数组中每个单词的出现次数，存储在 $target\_count$ 中。

3. **滑动窗口检查**：从字符串 $s$ 的每个可能起始位置开始，使用滑动窗口：
   - 窗口大小为 $word\_length \times word\_count$。
   - 将窗口内的字符串按 $word\_length$ 分割成单词。
   - 统计这些单词的出现次数，与 $target\_count$ 比较。

4. **匹配判断**：如果当前窗口内的单词统计与目标统计完全匹配，则记录起始位置。

**关键点**：

- 滑动窗口的大小固定为所有单词的总长度。
- 使用哈希表快速比较单词出现次数。
- 需要处理字符串长度不足的情况。

### 思路 1：代码

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        找到所有串联子串的起始位置
        """
        if not s or not words or not words[0]:
            return []
        
        # 获取基本参数
        word_length = len(words[0])  # 每个单词的长度
        word_count = len(words)      # 单词数量
        total_length = word_length * word_count  # 串联子串的总长度
        
        # 如果字符串长度小于串联子串长度，直接返回空列表
        if len(s) < total_length:
            return []
        
        # 构建目标单词计数哈希表
        target_count = {}
        for word in words:
            target_count[word] = target_count.get(word, 0) + 1
        
        result = []
        
        # 遍历所有可能的起始位置
        for start in range(len(s) - total_length + 1):
            # 获取当前窗口的子串
            window = s[start:start + total_length]
            
            # 将窗口按单词长度分割
            window_words = []
            for i in range(0, total_length, word_length):
                word = window[i:i + word_length]
                window_words.append(word)
            
            # 统计当前窗口的单词出现次数
            current_count = {}
            for word in window_words:
                current_count[word] = current_count.get(word, 0) + 1
            
            # 检查是否匹配目标计数
            if current_count == target_count:
                result.append(start)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m \times k)$，其中 $n$ 是字符串 $s$ 的长度，$m$ 是单词数组的长度，$k$ 是每个单词的长度。需要检查 $O(n)$ 个起始位置，每个位置需要处理 $O(m)$ 个单词，每个单词长度为 $O(k)$。
- **空间复杂度**：$O(m \times k)$，用于存储目标单词计数哈希表和当前窗口单词计数哈希表。
