# [0720. 词典中最长的单词](https://leetcode.cn/problems/longest-word-in-dictionary/)

- 标签：字典树、数组、哈希表、字符串、排序
- 难度：中等

## 题目链接

- [0720. 词典中最长的单词 - 力扣](https://leetcode.cn/problems/longest-word-in-dictionary/)

## 题目大意

给出一个字符串数组 `words` 组成的一本英语词典。

要求：从中找出最长的一个单词，该单词是由 `words` 词典中其他单词逐步添加一个字母组成。如果其中有多个可行的答案，则返回答案中字典序最小的单词。如果无答案，则返回空字符串。

## 解题思路

使用字典树存储每一个单词。再在字典树中查找每一个单词，查找的时候判断是否有以当前单词为前缀的单词。如果有，则该单词可以由前缀构成的单词逐步添加字母获得。此时，如果该单词比答案单词更长，则维护更新答案单词。

最后输出答案单词。

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
            if ch not in cur.children or not cur.children[ch].isEnd:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd

class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)

        ans = ""
        for word in words:
            if trie_tree.search(word):
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word
        return ans
```

