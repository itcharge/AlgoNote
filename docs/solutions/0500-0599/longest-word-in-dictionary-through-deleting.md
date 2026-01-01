# [0524. 通过删除字母匹配到字典里最长单词](https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/)

- 标签：数组、双指针、字符串、排序
- 难度：中等

## 题目链接

- [0524. 通过删除字母匹配到字典里最长单词 - 力扣](https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/)

## 题目大意

**描述**：

给定一个字符串 $s$ 和一个字符串数组 $dictionary$。

**要求**：

找出并返回 $dictionary$ 中最长的字符串，该字符串可以通过删除 $s$ 中的某些字符得到。

如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。


**说明**：

- $1 \le s.length \le 10^{3}$。
- $1 \le dictionary.length \le 10^{3}$。
- $1 \le dictionary[i].length \le 10^{3}$。
- $s$ 和 $dictionary[i]$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
```

- 示例 2：

```python
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
```

## 解题思路

### 思路 1：双指针匹配 & 按要求排序

核心在于判断每个字典中的单词 $w$ 是否 $w$ 是 $s$ 子序列。

1. 对 $dictionary$ 按长度降序、字典序升序排序。
2. 对每个字符串用双指针扫是否为子序列，遇到第一个返回即可。

### 思路 1：代码

```python
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subseq(word, s):
            it = iter(s)
            return all(c in it for c in word)
        # 长度优先、字典序次之
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            if is_subseq(word, s):
                return word
        return ""
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(nm)$，$n$为字典总单词数，$m$为$s$长度。
- **空间复杂度**：$O(1)$。
