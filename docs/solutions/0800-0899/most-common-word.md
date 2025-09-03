# [0819. 最常见的单词](https://leetcode.cn/problems/most-common-word/)

- 标签：哈希表、字符串、计数
- 难度：简单

## 题目链接

- [0819. 最常见的单词 - 力扣](https://leetcode.cn/problems/most-common-word/)

## 题目大意

**描述**：给定一个字符串 $paragraph$ 表示段落，再给定搞一个禁用单词列表 $banned$。

**要求**：返回出现次数最多，同时不在禁用列表中的单词。

**说明**：

- 题目保证至少有一个词不在禁用列表中，而且答案唯一。
- 禁用列表 $banned$ 中的单词用小写字母表示，不含标点符号。
- 段落 $paragraph$ 只包含字母、空格和下列标点符号`!?',;.`
- 段落中的单词不区分大小写。
- $1 \le \text{段落长度} \le 1000$。
- $0 \le \text{禁用单词个数} \le 100$。
- $1 \le \text{禁用单词长度} \le 10$。
- 答案是唯一的，且都是小写字母（即使在 $paragraph$ 里是大写的，即使是一些特定的名词，答案都是小写的）。
- 不存在没有连字符或者带有连字符的单词。
- 单词里只包含字母，不会出现省略号或者其他标点符号。

**示例**：

- 示例 1：

```python
输入: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
输出: "ball"
解释: 
"hit" 出现了3次，但它是一个禁用的单词。
"ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。 
注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 "ball,"）， 
"hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
```

- 示例 2：

```python
输入：
paragraph = "a."
banned = []
输出："a"
```

## 解题思路

### 思路 1：哈希表

1. 将禁用词列表转为集合 $banned\_set$。
2. 遍历段落 $paragraph$，获取段落中的所有单词。
3. 判断当前单词是否在禁用词集合中，如果不在禁用词集合中，则使用哈希表对该单词进行计数。
4. 遍历完，找出哈希表中频率最大的单词，将该单词作为答案进行返回。

### 思路 1：代码

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        cnts = Counter()

        word = ""
        for ch in paragraph:
            if ch.isalpha():
                word += ch.lower()
            else:
                if word and word not in banned_set:
                    cnts[word] += 1
                word = ""
        if word and word not in banned_set:
            cnts[word] += 1

        max_cnt, ans = 0, ""
        for word, cnt in cnts.items():
            if cnt > max_cnt:
                max_cnt = cnt
                ans = word
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 为段落 $paragraph$ 的长度，$m$ 是禁用词 $banned$ 的长度。
- **空间复杂度**：$O(n + m)$。

