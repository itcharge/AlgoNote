# [1858. 包含所有前缀的最长单词](https://leetcode.cn/problems/longest-word-with-all-prefixes/)

- 标签：深度优先搜索、字典树
- 难度：中等

## 题目链接

- [1858. 包含所有前缀的最长单词 - 力扣](https://leetcode.cn/problems/longest-word-with-all-prefixes/)

## 题目大意

给定一个字符串数组 `words`。

要求：找出 `words` 中所有前缀从都在 `words` 中的最长字符串。如果存在多个符合条件相同长度的字符串，则输出字典序中最小的字符串。如果不存在这样的字符串，返回 `' '`。

- 例如：令 `words = ["a", "app", "ap"]`。字符串 `"app"` 含前缀 `"ap"` 和 `"a"` ，都在 `words` 中。

## 解题思路

使用字典树存储所有单词，再将字典中单词按照长度从大到小、字典序从小到大排序。

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
            if not cur.isEnd:
                return False
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        tire_tree = Trie()
        for word in words:
            tire_tree.insert(word)
        words.sort(key=lambda x:(-len(x), x))
        for word in words:
            if tire_tree.search(word):
                return word
        return ''
```

