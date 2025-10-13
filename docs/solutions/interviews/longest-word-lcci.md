# [面试题 17.15. 最长单词](https://leetcode.cn/problems/longest-word-lcci/)

- 标签：字典树、数组、哈希表、字符串
- 难度：中等

## 题目链接

- [面试题 17.15. 最长单词 - 力扣](https://leetcode.cn/problems/longest-word-lcci/)

## 题目大意

给定一组单词 `words`。

要求：找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。如果有多个长度相同的结果，返回其中字典序最小的一项，如果没有符合要求的单词则返回空字符串。

## 解题思路

先将所有单词按照长度从长到短排序，相同长度的字典序小的排在前面。然后将所有单词存入字典树中。

然后一重循环遍历所有单词 `word`，二重循环遍历单词中所有字符 `word[i]`。

如果当前遍历的字符为单词末尾，递归判断从 `i + 1` 位置开始，剩余部分是否可以切分为其他单词组合，如果可以切分，则返回当前单词 `word`。如果不可以切分，则返回空字符串 `""`。

## 代码

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd

    def splitToWord(self, remain):
        if not remain or remain == "":
            return True
        cur = self
        for i in range(len(remain)):
            ch = remain[i]
            if ch not in cur.children:
                return False
            if cur.children[ch].isEnd and self.splitToWord(remain[i + 1:]):
                return True
            cur = cur.children[ch]
        return False

    def dfs(self, words):
        for word in words:
            cur = self
            size = len(word)
            for i in range(size):
                ch = word[i]
                if i < size - 1 and cur.children[ch].isEnd and self.splitToWord(word[i+1:]):
                    return word
                cur = cur.children[ch]
        return ""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x))
        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)

        ans = trie_tree.dfs(words)
        return ans
```

