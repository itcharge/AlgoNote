# [0884. 两句话中的不常见单词](https://leetcode.cn/problems/uncommon-words-from-two-sentences/)

- 标签：哈希表、字符串
- 难度：简单

## 题目链接

- [0884. 两句话中的不常见单词 - 力扣](https://leetcode.cn/problems/uncommon-words-from-two-sentences/)

## 题目大意

**描述**：给定两个字符串 $s1$ 和 $s2$ ，分别表示两个句子。

**要求**：返回所有不常用单词的列表。返回列表中单词可以按任意顺序组织。

**说明**：

- **句子**：是一串由空格分隔的单词。
- **单词**：仅由小写字母组成的子字符串。
- **不常见单词**：如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
- $1 \le s1.length, s2.length \le 200$。
- $s1$ 和 $s2$ 由小写英文字母和空格组成。
- $s1$ 和 $s2$ 都不含前导或尾随空格。
- $s1$ 和 $s2$ 中的所有单词间均由单个空格分隔。

**示例**：

- 示例 1：

```python
输入：s1 = "this apple is sweet", s2 = "this apple is sour"
输出：["sweet","sour"]
```

- 示例 2：

```python
输入：s1 = "apple apple", s2 = "banana"
输出：["banana"]
```

## 解题思路

### 思路 1：哈希表

题目要求找出在其中一个句子中恰好出现一次，在另一个句子中却没有出现的单词，其实就是找出在两个句子中只出现过一次的单词，我们可以用哈希表统计两个句子中每个单词的出现频次，然后将出现频次为 $1$ 的单词就是不常见单词，将其加入答案数组即可。

具体步骤如下：

1.  遍历字符串 $s1$、$s2$，使用哈希表 $table$ 统计字符串 $s1$、$s2$ 各个单词的出现频次。
2. 遍历哈希表，找出出现频次为 $1$ 的单词，将其加入答案数组 $res$ 中。
3. 遍历完返回答案数组 $res$。

### 思路 1：代码

```python
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        table = dict()
        for word in s1.split(' '):
            if word not in table:
                table[word] = 1
            else:
                table[word] += 1
        
        for word in s2.split(' '):
            if word not in table:
                table[word] = 1
            else:
                table[word] += 1
       
        res = []
        for word in table:
            if table[word] == 1:
                res.append(word)
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n)$，其中 $m$、$n$ 分别为字符串 $s1$、$s2$ 的长度。
- **空间复杂度**：$O(m + n)$。
